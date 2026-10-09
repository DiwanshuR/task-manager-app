import logging
from pathlib import Path

from logging import FileHandler

import pytest

from app.models.user import UserRole

# 2. Write a test asserting the response contains no traceback, no RuntimeError, no file paths — and a second test asserting the traceback was written to the log (use pytest's caplog fixture).
def test_unhandled_error_response_does_not_leak_traceback_or_paths(client):
    response = client.get("/__boom")

    assert response.status_code == 500
    assert response.json() == {
        "error": {
            "code": "internal_error",
            "message": "An unexpected error occurred. Please try again later.",
            "details": None,
        }
    }
    for secret in (
        "Traceback",
        "RuntimeError",
        str(Path(__file__).resolve().parents[2]),
        str(Path(__file__).resolve()),
    ):
        assert secret not in response.text


def test_deliberate_error_endpoint_is_excluded_from_openapi(client):
    response = client.get("/openapi.json")

    assert response.status_code == 200
    assert "/__boom" not in response.json()["paths"]


def test_unhandled_error_traceback_is_written_to_log(
    client,
    caplog,
    monkeypatch,
):
    root_logger = logging.getLogger()
    for handler in root_logger.handlers:
        if isinstance(handler, FileHandler):
            monkeypatch.setattr(handler, "emit", lambda record: None)

    with caplog.at_level(logging.ERROR, logger="app.main"):
        response = client.get("/__boom")

    assert response.status_code == 500
    error_records = [
        record
        for record in caplog.records
        if record.name == "app.main" and record.exc_info is not None
    ]
    assert len(error_records) == 1
    assert "Traceback (most recent call last)" in caplog.text
    assert (
        "RuntimeError: Intentional exception-handler test failure"
        in caplog.text
    )

# task 3. Write one parametrized test proving 401 / 403 / 404 / 409 / 422 / 500 all return the identical envelope shape.
@pytest.mark.parametrize(
    ("error_case", "expected_status", "expected_code"),
    [
        ("unauthenticated", 401, "authentication_error"),
        ("permission_denied", 403, "permission_denied"),
        ("not_found", 404, "task_not_found"),
        ("conflict", 409, "invalid_task_transition"),
        ("validation", 422, "validation_error"),
        ("internal", 500, "internal_error"),
    ],
)
def test_api_errors_share_the_same_envelope(
    client,
    make_auth_user,
    error_case,
    expected_status,
    expected_code,
):
    if error_case == "unauthenticated":
        response = client.get("/tasks/")
    elif error_case == "permission_denied":
        member = make_auth_user(UserRole.member)
        response = client.post(
            "/projects/",
            headers=member["headers"],
            json={"name": "Member-created project"},
        )
    elif error_case == "not_found":
        manager = make_auth_user(UserRole.manager)
        response = client.get(
            "/tasks/999999",
            headers=manager["headers"],
        )
    elif error_case == "conflict":
        manager = make_auth_user(UserRole.manager)
        project_response = client.post(
            "/projects/",
            headers=manager["headers"],
            json={"name": "Conflict test project"},
        )
        assert project_response.status_code == 201, project_response.text
        task_response = client.post(
            "/tasks/",
            headers=manager["headers"],
            json={
                "title": "Conflict test task",
                "project_id": project_response.json()["id"],
            },
        )
        assert task_response.status_code == 201, task_response.text
        response = client.put(
            f"/tasks/{task_response.json()['id']}",
            headers=manager["headers"],
            json={
                "title": "Conflict test task",
                "status": "done",
                "priority": "medium",
            },
        )
    elif error_case == "validation":
        response = client.post("/auth/register", json={})
    else:
        response = client.get("/__boom")

    assert response.status_code == expected_status, response.text
    assert set(response.json()) == {"error"}
    error = response.json()["error"]
    assert set(error) == {"code", "message", "details"}
    assert error["code"] == expected_code
    assert isinstance(error["message"], str)
    assert error["message"]
