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


@pytest.fixture
def db_session():
    engine = create_engine(
        "sqlite://",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    testing_session = sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine,
    )

    Base.metadata.create_all(bind=engine)
    session = testing_session()

    try:
        yield session
    finally:
        session.close()
        Base.metadata.drop_all(bind=engine)
        engine.dispose()


@pytest.fixture
def client(db_session):
    def override_get_db():
        yield db_session

    app.dependency_overrides[get_db] = override_get_db

    try:
        with TestClient(app) as test_client:
            yield test_client
    finally:
        app.dependency_overrides.clear()


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
            "headers": {"Authorization": f"Bearer {token}"},
        }

    return _create_user