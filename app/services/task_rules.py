from datetime import date

from app.domain.entities import Task, User


MIN_TITLE_LENGTH = 1
MAX_TITLE_LENGTH = 100
VALID_PRIORITIES = {"low", "medium", "high"}
PRIVILEGED_ROLES = {"admin", "manager"}


def normalize_title(title: str) -> str:
    """Trim a title and reject it if it is blank or too long."""
    if not isinstance(title, str):
        raise ValueError("Title must be text")

    normalized = title.strip()

    if not MIN_TITLE_LENGTH <= len(normalized) <= MAX_TITLE_LENGTH:
        raise ValueError(
            f"Title must be between {MIN_TITLE_LENGTH} "
            f"and {MAX_TITLE_LENGTH} characters"
        )

    return normalized


def validate_priority(priority: str) -> str:
    """Return a valid priority, or raise ValueError."""
    if priority not in VALID_PRIORITIES:
        raise ValueError("Priority must be low, medium, or high")

    return priority


def can_edit_task(user: User, task: Task) -> bool:
    """Managers/admins and the task owner may edit the task."""
    return user.role in PRIVILEGED_ROLES or user.id == task.owner_id


def days_until_due(due_date: date, today: date) -> int:
    """Return days until due; negative means the task is overdue."""
    return (due_date - today).days

def is_task_overdue(due_date: date, today: date) -> bool:
    """A task is overdue when its due date is earlier than today."""
    return due_date < today