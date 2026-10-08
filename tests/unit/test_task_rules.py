from datetime import date, timedelta

import pytest

from app.services.task_rules import (
    can_edit_task,
    days_until_due,
    normalize_title,
    validate_priority,
    is_task_overdue
)


@pytest.mark.parametrize(
    "length",
    [1, 100],
)
def test_normalize_title_accepts_boundary_lengths(length):
    title = "T" * length

    assert normalize_title(title) == title


@pytest.mark.parametrize(
    "title",
    ["", "   ", "T" * 101],
)
def test_normalize_title_rejects_blank_or_too_long_titles(title):
    with pytest.raises(ValueError):
        normalize_title(title)


def test_normalize_title_trims_surrounding_whitespace():
    assert normalize_title("  Write tests  ") == "Write tests"


@pytest.mark.parametrize(
    "priority",
    ["low", "medium", "high"],
)
def test_validate_priority_accepts_supported_values(priority):
    assert validate_priority(priority) == priority


@pytest.mark.parametrize(
    "priority",
    ["", "urgent"],
)
def test_validate_priority_rejects_unsupported_values(priority):
    with pytest.raises(ValueError):
        validate_priority(priority)


def test_task_owner_can_edit_task(make_user, make_task):
    user = make_user(user_id=10)
    task = make_task(owner_id=10)

    assert can_edit_task(user, task) is True


@pytest.mark.parametrize(
    "role",
    ["manager", "admin"],
)
def test_privileged_user_can_edit_another_users_task(
    make_user,
    make_task,
    role,
):
    user = make_user(user_id=20, role=role)
    task = make_task(owner_id=10)

    assert can_edit_task(user, task) is True


def test_other_member_cannot_edit_task(make_user, make_task):
    user = make_user(user_id=20, role="member")
    task = make_task(owner_id=10)

    assert can_edit_task(user, task) is False


@pytest.mark.parametrize(
    ("offset", "expected_days"),
    [
        (-2, -2),
        (0, 0),
        (3, 3),
    ],
)
def test_days_until_due_handles_past_today_and_future_dates(
    offset,
    expected_days,
):
    today = date(2026, 1, 10)
    due_date = today + timedelta(days=offset)

    assert days_until_due(due_date, today) == expected_days
    

@pytest.mark.parametrize(
    ("due_date", "today", "expected"),
    [
        (date(2030, 1, 9), date(2030, 1, 10), True),
        (date(2030, 1, 10), date(2030, 1, 10), False),
        (date(2030, 1, 11), date(2030, 1, 10), False),
    ],
)
def test_is_task_overdue(due_date, today, expected):
    assert is_task_overdue(due_date, today) is expected