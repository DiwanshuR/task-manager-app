from app.services.task_rules import normalize_title
from app.models.task import TaskStatus


def normalize_task_title(title: str) -> str:
    """Use the existing pure title-validation rule."""
    return normalize_title(title)


def is_valid_task_status(status: str) -> bool:
    """Return whether a status is supported by the task model."""
    # Compare enum values too, in case status is a TaskStatus member.
    status_value = getattr(status, "value", status)

    return status_value in {task_status.value for task_status in TaskStatus}