import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.database import Base, get_db
from app.main import app
from app.models.project import Project  # Register model tables with Base.
from app.models.task import Task
from app.models.user import User, UserRole
import uuid

from app.auth.security import create_access_token

# Thias fixture provides a database session that is rolled back after each test, ensuring isolation.
@pytest.fixture
def db_session():
    engine = create_engine(
        "sqlite://",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )

    # Register all ORM tables and create them for this test's database.
    Base.metadata.create_all(bind=engine)

    connection = engine.connect()
    outer_transaction = connection.begin()

    testing_session = sessionmaker(
        bind=connection,
        autocommit=False,
        autoflush=False,
        join_transaction_mode="create_savepoint",
    )
    session = testing_session()

    try:
        yield session
    finally:
        session.close()

        # Undo all changes, including commits made by repositories.
        outer_transaction.rollback()

        connection.close()
        Base.metadata.drop_all(bind=engine)
        engine.dispose()

# This fixture provides a TestClient that uses the db_session fixture to override the get_db dependency.
@pytest.fixture
def client(db_session):
    def override_get_db():
        yield db_session

    previous_overrides = app.dependency_overrides.copy()
    app.dependency_overrides[get_db] = override_get_db

    test_client = TestClient(app, raise_server_exceptions=False)
    try:
        yield test_client
    finally:
        test_client.close()
        app.dependency_overrides.clear()
        app.dependency_overrides.update(previous_overrides)


@pytest.fixture
def create_user(client, db_session):
    def _create_user(email, role=UserRole.member):
        registration = client.post(
            "/auth/register",
            json={
                "name": "Test User",
                "email": email,
                "password": "TestPassword123!",
            },
        )
        assert registration.status_code == 201, registration.text

        if role != UserRole.member:
            user = db_session.query(User).filter(User.email == email).first()
            user.role = role
            db_session.commit()

        login = client.post(
            "/auth/login",
            data={
                "username": email,
                "password": "TestPassword123!",
            },
        )
        assert login.status_code == 200, login.text

        token = login.json()["access_token"]
        return {
            "email": email,
            "headers": {"Authorization": "Bearer " + token},
        }

    return _create_user


# Our access token identifuees the user with sub, your get_current_user loads the user record and gets the role from database. This fixture avoids having to create a user and log in for every test that needs a project.
# What we doing here and why is we creating a user and directly minting(i.e creating) a JWT for that user? Because we want to test the API endpoints that require authentication without going through the full registration and login process for each test. By creating a user and generating a JWT token, we can simulate an authenticated user and test the endpoints that require authentication. This approach saves time and simplifies the testing process, allowing us to focus on testing the functionality of the endpoints rather than the authentication flow.
@pytest.fixture(
    params=[UserRole.admin, UserRole.manager, UserRole.member],
    ids=["admin", "manager", "member"],
)
def role(request):
    """Run a test once for each application role."""
    return request.param



@pytest.fixture
def make_auth_user(db_session):
    """Create a database-backed test user and mint an access token directly."""
    def _make_auth_user(role: UserRole):
        user = User(
            name=f"Test {role.value}",
            email=f"{role.value}-{uuid.uuid4().hex}@example.com",
            password_hash="unused-by-token-auth-tests",
            role=role,
        )
        db_session.add(user)
        db_session.flush()  # Assign user.id without committing the test transaction.

        token = create_access_token({"sub": str(user.id)})
        return {
            "id": user.id,
            "email": user.email,
            "headers": {"Authorization": "Bearer " + token},
        }

    return _make_auth_user


@pytest.fixture
def auth_header(make_auth_user):
    """Return a helper that mints a token for a user with the requested role."""
    def _make_auth_header(role: UserRole):
        return make_auth_user(role)["headers"]

    return _make_auth_header