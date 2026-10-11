from app.models.user import UserRole
from app.repositories.user_repository import SQLAlchemyUserRepository


def test_update_changes_user_fields_and_preserves_omitted_fields(db_session):
    repository = SQLAlchemyUserRepository(db_session)
    user = repository.create(
        name="Original Name",
        email="original@example.com",
        password_hash="test-hash",
        role=UserRole.member,
    )

    updated = repository.update(
    user,
    name="Updated Name",
    email="updated@example.com",
    role=UserRole.admin,
    )

    assert updated.name == "Updated Name"
    assert updated.email == "updated@example.com"
    assert updated.role is UserRole.admin

    unchanged = repository.update(updated)
    assert unchanged.name == "Updated Name"
    assert unchanged.email == "updated@example.com"
    assert unchanged.role is UserRole.admin


def test_delete_removes_user_from_repository(db_session):
    repository = SQLAlchemyUserRepository(db_session)
    user = repository.create(
        name="User To Delete",
        email="delete@example.com",
        password_hash="test-hash",
        role=UserRole.member,
    )
    user_id = user.id

    repository.delete(user)

    assert repository.get_by_id(user_id) is None
    assert repository.get_by_email("delete@example.com") is None