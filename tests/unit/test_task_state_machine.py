import pytest

from app.models.task import (
    TASK_STATUS_TRANSITIONS,
    TaskStatus,
    can_transition_task_status,
)


LEGAL_TRANSITIONS = [
    (current, target)
    for current, targets in TASK_STATUS_TRANSITIONS.items()
    for target in sorted(targets, key=lambda status: status.value)
]
ILLEGAL_TRANSITIONS = [
    (current, target)
    for current in TaskStatus
    for target in TaskStatus
    if current != target
    and target not in TASK_STATUS_TRANSITIONS[current]
]


@pytest.mark.parametrize(("current", "target"), LEGAL_TRANSITIONS)
def test_task_state_machine_allows_each_legal_transition(current, target):
    assert can_transition_task_status(current, target) is True


@pytest.mark.parametrize(("current", "target"), ILLEGAL_TRANSITIONS)
def test_task_state_machine_rejects_each_illegal_transition(current, target):
    assert can_transition_task_status(current, target) is False
