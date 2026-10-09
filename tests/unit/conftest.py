import pytest

from app.domain.entities import Task, User


@pytest.fixture
def make_user():
    """Return a factory so each test can make the user it needs."""
    def _make_user(*, user_id=1, role="member"):
        return User(id=user_id, role=role)

    return _make_user


@pytest.fixture
def make_task():
    """Return a factory so each test can make the task it needs."""
    def _make_task(
        *,
        owner_id=1,
        title="Test task",
        priority="medium",
        due_date=None,
    ):
        return Task(
            owner_id=owner_id,
            title=title,
            priority=priority,
            due_date=due_date,
        )

    return _make_task