from mutmut.mutation.trampoline import MutantDict
from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated

from app.models.task import TaskStatus
from app.services.task_rules import normalize_title

mutants_x_normalize_task_title__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_normalize_task_title__mutmut)
def normalize_task_title(title: str) -> str:
    """Use the existing pure title-validation rule."""
    return normalize_title(title)


def x_normalize_task_title__mutmut_orig(title: str) -> str:
    """Use the existing pure title-validation rule."""
    return normalize_title(title)


def x_normalize_task_title__mutmut_1(title: str) -> str:
    """Use the existing pure title-validation rule."""
    return normalize_title(None)


mutants_x_normalize_task_title__mutmut["_mutmut_orig"] = x_normalize_task_title__mutmut_orig  # type: ignore # mutmut generated
mutants_x_normalize_task_title__mutmut["x_normalize_task_title__mutmut_1"] = (
    x_normalize_task_title__mutmut_1  # type: ignore # mutmut generated
)
mutants_x_is_valid_task_status__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_is_valid_task_status__mutmut)
def is_valid_task_status(status: str) -> bool:
    """Return whether a status is supported by the task model."""
    # Compare enum values too, in case status is a TaskStatus member.
    status_value = getattr(status, "value", status)

    return status_value in {task_status.value for task_status in TaskStatus}


def x_is_valid_task_status__mutmut_orig(status: str) -> bool:
    """Return whether a status is supported by the task model."""
    # Compare enum values too, in case status is a TaskStatus member.
    status_value = getattr(status, "value", status)

    return status_value in {task_status.value for task_status in TaskStatus}


def x_is_valid_task_status__mutmut_1(status: str) -> bool:
    """Return whether a status is supported by the task model."""
    # Compare enum values too, in case status is a TaskStatus member.
    status_value = None

    return status_value in {task_status.value for task_status in TaskStatus}


def x_is_valid_task_status__mutmut_2(status: str) -> bool:
    """Return whether a status is supported by the task model."""
    # Compare enum values too, in case status is a TaskStatus member.
    status_value = getattr(None, "value", status)

    return status_value in {task_status.value for task_status in TaskStatus}


def x_is_valid_task_status__mutmut_3(status: str) -> bool:
    """Return whether a status is supported by the task model."""
    # Compare enum values too, in case status is a TaskStatus member.
    status_value = getattr(status, None, status)

    return status_value in {task_status.value for task_status in TaskStatus}


def x_is_valid_task_status__mutmut_4(status: str) -> bool:
    """Return whether a status is supported by the task model."""
    # Compare enum values too, in case status is a TaskStatus member.
    status_value = getattr(status, "value", None)

    return status_value in {task_status.value for task_status in TaskStatus}


def x_is_valid_task_status__mutmut_5(status: str) -> bool:
    """Return whether a status is supported by the task model."""
    # Compare enum values too, in case status is a TaskStatus member.
    status_value = getattr("value", status)

    return status_value in {task_status.value for task_status in TaskStatus}


def x_is_valid_task_status__mutmut_6(status: str) -> bool:
    """Return whether a status is supported by the task model."""
    # Compare enum values too, in case status is a TaskStatus member.
    status_value = getattr(status, status)

    return status_value in {task_status.value for task_status in TaskStatus}


def x_is_valid_task_status__mutmut_7(status: str) -> bool:
    """Return whether a status is supported by the task model."""
    # Compare enum values too, in case status is a TaskStatus member.
    status_value = status.value

    return status_value in {task_status.value for task_status in TaskStatus}


def x_is_valid_task_status__mutmut_8(status: str) -> bool:
    """Return whether a status is supported by the task model."""
    # Compare enum values too, in case status is a TaskStatus member.
    status_value = getattr(status, "XXvalueXX", status)

    return status_value in {task_status.value for task_status in TaskStatus}


def x_is_valid_task_status__mutmut_9(status: str) -> bool:
    """Return whether a status is supported by the task model."""
    # Compare enum values too, in case status is a TaskStatus member.
    status_value = getattr(status, "VALUE", status)

    return status_value in {task_status.value for task_status in TaskStatus}


def x_is_valid_task_status__mutmut_10(status: str) -> bool:
    """Return whether a status is supported by the task model."""
    # Compare enum values too, in case status is a TaskStatus member.
    status_value = getattr(status, "value", status)

    return status_value not in {task_status.value for task_status in TaskStatus}


mutants_x_is_valid_task_status__mutmut["_mutmut_orig"] = x_is_valid_task_status__mutmut_orig  # type: ignore # mutmut generated
mutants_x_is_valid_task_status__mutmut["x_is_valid_task_status__mutmut_1"] = (
    x_is_valid_task_status__mutmut_1  # type: ignore # mutmut generated
)
mutants_x_is_valid_task_status__mutmut["x_is_valid_task_status__mutmut_2"] = (
    x_is_valid_task_status__mutmut_2  # type: ignore # mutmut generated
)
mutants_x_is_valid_task_status__mutmut["x_is_valid_task_status__mutmut_3"] = (
    x_is_valid_task_status__mutmut_3  # type: ignore # mutmut generated
)
mutants_x_is_valid_task_status__mutmut["x_is_valid_task_status__mutmut_4"] = (
    x_is_valid_task_status__mutmut_4  # type: ignore # mutmut generated
)
mutants_x_is_valid_task_status__mutmut["x_is_valid_task_status__mutmut_5"] = (
    x_is_valid_task_status__mutmut_5  # type: ignore # mutmut generated
)
mutants_x_is_valid_task_status__mutmut["x_is_valid_task_status__mutmut_6"] = (
    x_is_valid_task_status__mutmut_6  # type: ignore # mutmut generated
)
mutants_x_is_valid_task_status__mutmut["x_is_valid_task_status__mutmut_7"] = (
    x_is_valid_task_status__mutmut_7  # type: ignore # mutmut generated
)
mutants_x_is_valid_task_status__mutmut["x_is_valid_task_status__mutmut_8"] = (
    x_is_valid_task_status__mutmut_8  # type: ignore # mutmut generated
)
mutants_x_is_valid_task_status__mutmut["x_is_valid_task_status__mutmut_9"] = (
    x_is_valid_task_status__mutmut_9  # type: ignore # mutmut generated
)
mutants_x_is_valid_task_status__mutmut["x_is_valid_task_status__mutmut_10"] = (
    x_is_valid_task_status__mutmut_10  # type: ignore # mutmut generated
)
