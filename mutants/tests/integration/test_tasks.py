from app.models.user import UserRole


def create_project(client, headers):
    response = client.post(
        "/projects/",
        headers=headers,
        json={"name": "Task test project", "description": "For task tests"},
    )
    assert response.status_code == 201, response.text
    return response.json()


def create_task(client, headers, project_id, title, status="pending"):
    return client.post(
        "/tasks/",
        headers=headers,
        json={
            "title": title,
            "description": "Task for testing",
            "status": status,
            "priority": "medium",
            "project_id": project_id,
        },
    )


def test_task_list_requires_login(client):
    response = client.get("/tasks/")

    assert response.status_code == 401


def test_task_create_and_filter_by_status(client, create_user):
    manager = create_user("task-manager@example.com", role=UserRole.manager)
    project = create_project(client, manager["headers"])

    pending = create_task(
        client, manager["headers"], project["id"], "Pending task", "pending"
    )
    created = create_task(
        client, manager["headers"], project["id"], "Finished task"
    )

    assert pending.status_code == 201, pending.text
    assert created.status_code == 201, created.text

    task_id = created.json()["id"]
    for status in ("in_progress", "done"):
        done = client.put(
            f"/tasks/{task_id}",
            headers=manager["headers"],
            json={
                "title": "Finished task",
                "description": "Task for testing",
                "status": status,
                "priority": "medium",
            },
        )
        assert done.status_code == 200, done.text

    response = client.get(
        "/tasks/",
        headers=manager["headers"],
        params={"status": "pending", "project_id": project["id"]},
    )

    assert response.status_code == 200
    titles = [task["title"] for task in response.json()]
    assert "Pending task" in titles
    assert "Finished task" not in titles


def test_user_cannot_create_task_in_another_users_project(client, create_user):
    manager = create_user("task-project-owner@example.com", role=UserRole.manager)
    other_user = create_user("task-other-user@example.com")
    project = create_project(client, manager["headers"])

    response = create_task(
        client,
        other_user["headers"],
        project["id"],
        "Unauthorized task",
    )

    assert response.status_code == 403


def test_create_task_schema_rejects_archived_status(client, create_user):
    manager = create_user("task-archived-create@example.com", role=UserRole.manager)

    response = client.post(
        "/tasks/",
        headers=manager["headers"],
        json={"title": "Invalid initial status", "project_id": 1, "status": "archived"},
    )

    assert response.status_code == 422
    assert response.json()["error"]["code"] == "validation_error"


def test_task_update_rejects_unhashable_status_as_validation_error(
    client,
    create_user,
):
    manager = create_user("task-invalid-status@example.com", role=UserRole.manager)

    response = client.put(
        "/tasks/1",
        headers=manager["headers"],
        json={"title": "Malformed status", "status": {}, "priority": "medium"},
    )

    assert response.status_code == 422
    assert response.json()["error"]["code"] == "validation_error"


def test_oversized_database_ids_are_validation_errors(client, create_user):
    admin = create_user("task-oversized-id@example.com", role=UserRole.admin)
    oversized_id = 2_147_483_648

    task_response = client.post(
        f"/tasks/{oversized_id}/archive",
        headers=admin["headers"],
    )
    project_response = client.get(
        f"/projects/{oversized_id}",
        headers=admin["headers"],
    )

    assert task_response.status_code == 422
    assert task_response.json()["error"]["code"] == "validation_error"
    assert project_response.status_code == 422
    assert project_response.json()["error"]["code"] == "validation_error"


def test_put_deleted_collection_returns_method_not_allowed(client):
    response = client.put("/tasks/deleted")

    assert response.status_code == 405
    assert response.headers["allow"] == "GET"


def test_oversized_pagination_offset_is_a_validation_error(client, create_user):
    manager = create_user("task-oversized-offset@example.com", role=UserRole.manager)

    response = client.get(
        "/tasks/",
        headers=manager["headers"],
        params={"skip": 9_223_372_036_854_775_808},
    )

    assert response.status_code == 422
    assert response.json()["error"]["code"] == "validation_error"