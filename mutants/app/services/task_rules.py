from datetime import date

from app.domain.entities import Task, User


MIN_TITLE_LENGTH = 1
MAX_TITLE_LENGTH = 100
VALID_PRIORITIES = {"low", "medium", "high"}
PRIVILEGED_ROLES = {"admin", "manager"}


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_normalize_title__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_normalize_title__mutmut)
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


def x_normalize_title__mutmut_orig(title: str) -> str:
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


def x_normalize_title__mutmut_1(title: str) -> str:
    """Trim a title and reject it if it is blank or too long."""
    if isinstance(title, str):
        raise ValueError("Title must be text")

    normalized = title.strip()

    if not MIN_TITLE_LENGTH <= len(normalized) <= MAX_TITLE_LENGTH:
        raise ValueError(
            f"Title must be between {MIN_TITLE_LENGTH} "
            f"and {MAX_TITLE_LENGTH} characters"
        )

    return normalized


def x_normalize_title__mutmut_2(title: str) -> str:
    """Trim a title and reject it if it is blank or too long."""
    if not isinstance(title, str):
        raise ValueError(None)

    normalized = title.strip()

    if not MIN_TITLE_LENGTH <= len(normalized) <= MAX_TITLE_LENGTH:
        raise ValueError(
            f"Title must be between {MIN_TITLE_LENGTH} "
            f"and {MAX_TITLE_LENGTH} characters"
        )

    return normalized


def x_normalize_title__mutmut_3(title: str) -> str:
    """Trim a title and reject it if it is blank or too long."""
    if not isinstance(title, str):
        raise ValueError("XXTitle must be textXX")

    normalized = title.strip()

    if not MIN_TITLE_LENGTH <= len(normalized) <= MAX_TITLE_LENGTH:
        raise ValueError(
            f"Title must be between {MIN_TITLE_LENGTH} "
            f"and {MAX_TITLE_LENGTH} characters"
        )

    return normalized


def x_normalize_title__mutmut_4(title: str) -> str:
    """Trim a title and reject it if it is blank or too long."""
    if not isinstance(title, str):
        raise ValueError("title must be text")

    normalized = title.strip()

    if not MIN_TITLE_LENGTH <= len(normalized) <= MAX_TITLE_LENGTH:
        raise ValueError(
            f"Title must be between {MIN_TITLE_LENGTH} "
            f"and {MAX_TITLE_LENGTH} characters"
        )

    return normalized


def x_normalize_title__mutmut_5(title: str) -> str:
    """Trim a title and reject it if it is blank or too long."""
    if not isinstance(title, str):
        raise ValueError("TITLE MUST BE TEXT")

    normalized = title.strip()

    if not MIN_TITLE_LENGTH <= len(normalized) <= MAX_TITLE_LENGTH:
        raise ValueError(
            f"Title must be between {MIN_TITLE_LENGTH} "
            f"and {MAX_TITLE_LENGTH} characters"
        )

    return normalized


def x_normalize_title__mutmut_6(title: str) -> str:
    """Trim a title and reject it if it is blank or too long."""
    if not isinstance(title, str):
        raise ValueError("Title must be text")

    normalized = None

    if not MIN_TITLE_LENGTH <= len(normalized) <= MAX_TITLE_LENGTH:
        raise ValueError(
            f"Title must be between {MIN_TITLE_LENGTH} "
            f"and {MAX_TITLE_LENGTH} characters"
        )

    return normalized


def x_normalize_title__mutmut_7(title: str) -> str:
    """Trim a title and reject it if it is blank or too long."""
    if not isinstance(title, str):
        raise ValueError("Title must be text")

    normalized = title.strip()

    if MIN_TITLE_LENGTH <= len(normalized) <= MAX_TITLE_LENGTH:
        raise ValueError(
            f"Title must be between {MIN_TITLE_LENGTH} "
            f"and {MAX_TITLE_LENGTH} characters"
        )

    return normalized


def x_normalize_title__mutmut_8(title: str) -> str:
    """Trim a title and reject it if it is blank or too long."""
    if not isinstance(title, str):
        raise ValueError("Title must be text")

    normalized = title.strip()

    if not MIN_TITLE_LENGTH < len(normalized) <= MAX_TITLE_LENGTH:
        raise ValueError(
            f"Title must be between {MIN_TITLE_LENGTH} "
            f"and {MAX_TITLE_LENGTH} characters"
        )

    return normalized


def x_normalize_title__mutmut_9(title: str) -> str:
    """Trim a title and reject it if it is blank or too long."""
    if not isinstance(title, str):
        raise ValueError("Title must be text")

    normalized = title.strip()

    if not MIN_TITLE_LENGTH <= len(normalized) < MAX_TITLE_LENGTH:
        raise ValueError(
            f"Title must be between {MIN_TITLE_LENGTH} "
            f"and {MAX_TITLE_LENGTH} characters"
        )

    return normalized


def x_normalize_title__mutmut_10(title: str) -> str:
    """Trim a title and reject it if it is blank or too long."""
    if not isinstance(title, str):
        raise ValueError("Title must be text")

    normalized = title.strip()

    if not MIN_TITLE_LENGTH <= len(normalized) <= MAX_TITLE_LENGTH:
        raise ValueError(
            None
        )

    return normalized

mutants_x_normalize_title__mutmut['_mutmut_orig'] = x_normalize_title__mutmut_orig # type: ignore # mutmut generated
mutants_x_normalize_title__mutmut['x_normalize_title__mutmut_1'] = x_normalize_title__mutmut_1 # type: ignore # mutmut generated
mutants_x_normalize_title__mutmut['x_normalize_title__mutmut_2'] = x_normalize_title__mutmut_2 # type: ignore # mutmut generated
mutants_x_normalize_title__mutmut['x_normalize_title__mutmut_3'] = x_normalize_title__mutmut_3 # type: ignore # mutmut generated
mutants_x_normalize_title__mutmut['x_normalize_title__mutmut_4'] = x_normalize_title__mutmut_4 # type: ignore # mutmut generated
mutants_x_normalize_title__mutmut['x_normalize_title__mutmut_5'] = x_normalize_title__mutmut_5 # type: ignore # mutmut generated
mutants_x_normalize_title__mutmut['x_normalize_title__mutmut_6'] = x_normalize_title__mutmut_6 # type: ignore # mutmut generated
mutants_x_normalize_title__mutmut['x_normalize_title__mutmut_7'] = x_normalize_title__mutmut_7 # type: ignore # mutmut generated
mutants_x_normalize_title__mutmut['x_normalize_title__mutmut_8'] = x_normalize_title__mutmut_8 # type: ignore # mutmut generated
mutants_x_normalize_title__mutmut['x_normalize_title__mutmut_9'] = x_normalize_title__mutmut_9 # type: ignore # mutmut generated
mutants_x_normalize_title__mutmut['x_normalize_title__mutmut_10'] = x_normalize_title__mutmut_10 # type: ignore # mutmut generated
mutants_x_validate_priority__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_validate_priority__mutmut)
def validate_priority(priority: str) -> str:
    """Return a valid priority, or raise ValueError."""
    if priority not in VALID_PRIORITIES:
        raise ValueError("Priority must be low, medium, or high")

    return priority


def x_validate_priority__mutmut_orig(priority: str) -> str:
    """Return a valid priority, or raise ValueError."""
    if priority not in VALID_PRIORITIES:
        raise ValueError("Priority must be low, medium, or high")

    return priority


def x_validate_priority__mutmut_1(priority: str) -> str:
    """Return a valid priority, or raise ValueError."""
    if priority in VALID_PRIORITIES:
        raise ValueError("Priority must be low, medium, or high")

    return priority


def x_validate_priority__mutmut_2(priority: str) -> str:
    """Return a valid priority, or raise ValueError."""
    if priority not in VALID_PRIORITIES:
        raise ValueError(None)

    return priority


def x_validate_priority__mutmut_3(priority: str) -> str:
    """Return a valid priority, or raise ValueError."""
    if priority not in VALID_PRIORITIES:
        raise ValueError("XXPriority must be low, medium, or highXX")

    return priority


def x_validate_priority__mutmut_4(priority: str) -> str:
    """Return a valid priority, or raise ValueError."""
    if priority not in VALID_PRIORITIES:
        raise ValueError("priority must be low, medium, or high")

    return priority


def x_validate_priority__mutmut_5(priority: str) -> str:
    """Return a valid priority, or raise ValueError."""
    if priority not in VALID_PRIORITIES:
        raise ValueError("PRIORITY MUST BE LOW, MEDIUM, OR HIGH")

    return priority

mutants_x_validate_priority__mutmut['_mutmut_orig'] = x_validate_priority__mutmut_orig # type: ignore # mutmut generated
mutants_x_validate_priority__mutmut['x_validate_priority__mutmut_1'] = x_validate_priority__mutmut_1 # type: ignore # mutmut generated
mutants_x_validate_priority__mutmut['x_validate_priority__mutmut_2'] = x_validate_priority__mutmut_2 # type: ignore # mutmut generated
mutants_x_validate_priority__mutmut['x_validate_priority__mutmut_3'] = x_validate_priority__mutmut_3 # type: ignore # mutmut generated
mutants_x_validate_priority__mutmut['x_validate_priority__mutmut_4'] = x_validate_priority__mutmut_4 # type: ignore # mutmut generated
mutants_x_validate_priority__mutmut['x_validate_priority__mutmut_5'] = x_validate_priority__mutmut_5 # type: ignore # mutmut generated
mutants_x_can_edit_task__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_can_edit_task__mutmut)
def can_edit_task(user: User, task: Task) -> bool:
    """Managers/admins and the task owner may edit the task."""
    return user.role in PRIVILEGED_ROLES or user.id == task.owner_id


def x_can_edit_task__mutmut_orig(user: User, task: Task) -> bool:
    """Managers/admins and the task owner may edit the task."""
    return user.role in PRIVILEGED_ROLES or user.id == task.owner_id


def x_can_edit_task__mutmut_1(user: User, task: Task) -> bool:
    """Managers/admins and the task owner may edit the task."""
    return user.role in PRIVILEGED_ROLES and user.id == task.owner_id


def x_can_edit_task__mutmut_2(user: User, task: Task) -> bool:
    """Managers/admins and the task owner may edit the task."""
    return user.role not in PRIVILEGED_ROLES or user.id == task.owner_id


def x_can_edit_task__mutmut_3(user: User, task: Task) -> bool:
    """Managers/admins and the task owner may edit the task."""
    return user.role in PRIVILEGED_ROLES or user.id != task.owner_id

mutants_x_can_edit_task__mutmut['_mutmut_orig'] = x_can_edit_task__mutmut_orig # type: ignore # mutmut generated
mutants_x_can_edit_task__mutmut['x_can_edit_task__mutmut_1'] = x_can_edit_task__mutmut_1 # type: ignore # mutmut generated
mutants_x_can_edit_task__mutmut['x_can_edit_task__mutmut_2'] = x_can_edit_task__mutmut_2 # type: ignore # mutmut generated
mutants_x_can_edit_task__mutmut['x_can_edit_task__mutmut_3'] = x_can_edit_task__mutmut_3 # type: ignore # mutmut generated
mutants_x_days_until_due__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_days_until_due__mutmut)
def days_until_due(due_date: date, today: date) -> int:
    """Return days until due; negative means the task is overdue."""
    return (due_date - today).days


def x_days_until_due__mutmut_orig(due_date: date, today: date) -> int:
    """Return days until due; negative means the task is overdue."""
    return (due_date - today).days


def x_days_until_due__mutmut_1(due_date: date, today: date) -> int:
    """Return days until due; negative means the task is overdue."""
    return (due_date + today).days

mutants_x_days_until_due__mutmut['_mutmut_orig'] = x_days_until_due__mutmut_orig # type: ignore # mutmut generated
mutants_x_days_until_due__mutmut['x_days_until_due__mutmut_1'] = x_days_until_due__mutmut_1 # type: ignore # mutmut generated
mutants_x_is_task_overdue__mutmut: MutantDict = {}  # type: ignore

@_mutmut_mutated(mutants_x_is_task_overdue__mutmut)
def is_task_overdue(due_date: date, today: date) -> bool:
    """A task is overdue when its due date is earlier than today."""
    return due_date < today

def x_is_task_overdue__mutmut_orig(due_date: date, today: date) -> bool:
    """A task is overdue when its due date is earlier than today."""
    return due_date < today

def x_is_task_overdue__mutmut_1(due_date: date, today: date) -> bool:
    """A task is overdue when its due date is earlier than today."""
    return due_date <= today

mutants_x_is_task_overdue__mutmut['_mutmut_orig'] = x_is_task_overdue__mutmut_orig # type: ignore # mutmut generated
mutants_x_is_task_overdue__mutmut['x_is_task_overdue__mutmut_1'] = x_is_task_overdue__mutmut_1 # type: ignore # mutmut generated