import pytest

from app.models.user import UserRole


TASK_RBAC_MATRIX = [
    pytest.param(UserRole.admin, "list", 200, id="admin-list"),
    pytest.param(UserRole.manager, "list", 200, id="manager-list"),
    pytest.param(UserRole.member, "list", 200, id="member-list"),
    pytest.param(UserRole.admin, "read", 200, id="admin-read"),
    pytest.param(UserRole.manager, "read", 200, id="manager-read"),
    pytest.param(UserRole.member, "read", 200, id="member-read"),
    pytest.param(UserRole.admin, "create", 201, id="admin-create"),
    pytest.param(UserRole.manager, "create", 201, id="manager-create"),
    pytest.param(UserRole.member, "create", 201, id="member-create"),
    pytest.param(UserRole.admin, "update", 200, id="admin-update"),
    pytest.param(UserRole.manager, "update", 200, id="manager-update"),
    pytest.param(UserRole.member, "update", 200, id="member-update-own"),
    pytest.param(UserRole.admin, "archive", 200, id="admin-archive"),
    pytest.param(UserRole.manager, "archive", 200, id="manager-archive"),
    pytest.param(UserRole.member, "archive", 403, id="member-archive-denied"),
    pytest.param(UserRole.admin, "delete", 204, id="admin-delete"),
    pytest.param(UserRole.manager, "delete", 403, id="manager-delete-denied"),
    pytest.param(UserRole.member, "delete", 403, id="member-delete-denied"),
]


def create_project(client, headers, member_email):
    response = client.post(
        "/projects/",
        headers=headers,
        json={
            "name": "RBAC matrix project",
            "description": "Shared project for role/action checks",
            "member_emails": [member_email],
        },
    )
    assert response.status_code == 201, response.text
    return response.json()


def create_task(client, headers, project_id, title):
    response = client.post(
        "/tasks/",
        headers=headers,
        json={
            "title": title,
            "description": "Task for RBAC checks",
            "project_id": project_id,
        },
    )
    assert response.status_code == 201, response.text
    return response.json()


@pytest.mark.parametrize(
    ("role", "action", "expected_status"),
    TASK_RBAC_MATRIX,
)
def test_task_rbac_matrix(
    client,
    make_auth_user,
    role,
    action,
    expected_status,
):
    admin = make_auth_user(UserRole.admin)
    manager = make_auth_user(UserRole.manager)
    member = make_auth_user(UserRole.member)
    project = create_project(client, manager["headers"], member["email"])
    task = create_task(
        client,
        member["headers"],
        project["id"],
        "Task owned by the member",
    )
    actor = {
        UserRole.admin: admin,
        UserRole.manager: manager,
        UserRole.member: member,
    }[role]

    if action == "list":
        response = client.get(
            "/tasks/",
            headers=actor["headers"],
            params={"project_id": project["id"]},
        )
    elif action == "read":
        response = client.get(
            f"/tasks/{task['id']}",
            headers=actor["headers"],
        )
    elif action == "create":
        response = client.post(
            "/tasks/",
            headers=actor["headers"],
            json={
                "title": "Created in matrix test",
                "project_id": project["id"],
            },
        )
    elif action == "update":
        response = client.put(
            f"/tasks/{task['id']}",
            headers=actor["headers"],
            json={
                "title": "Updated by matrix actor",
                "status": "pending",
                "priority": "medium",
            },
        )
    elif action == "archive":
        response = client.post(
            f"/tasks/{task['id']}/archive",
            headers=actor["headers"],
        )
    else:
        response = client.delete(
            f"/tasks/{task['id']}",
            headers=actor["headers"],
        )

    assert response.status_code == expected_status, response.text


def test_member_cannot_update_another_members_task(
    client,
    make_auth_user,
):
    manager = make_auth_user(UserRole.manager)
    member = make_auth_user(UserRole.member)
    task_owner = make_auth_user(UserRole.member)
    project = client.post(
        "/projects/",
        headers=manager["headers"],
        json={
            "name": "Member ownership project",
            "member_emails": [member["email"], task_owner["email"]],
        },
    ).json()
    task = create_task(
        client,
        task_owner["headers"],
        project["id"],
        "Another member's task",
    )

    response = client.put(
        f"/tasks/{task['id']}",
        headers=member["headers"],
        json={"title": "Unauthorized update", "status": "pending"},
    )

    assert response.status_code == 403


def test_unrelated_manager_gets_forbidden_for_existing_task(
    client,
    make_auth_user,
):
    manager = make_auth_user(UserRole.manager)
    unrelated_manager = make_auth_user(UserRole.manager)
    project = client.post(
        "/projects/",
        headers=manager["headers"],
        json={"name": "Private manager project"},
    ).json()
    task = create_task(
        client,
        manager["headers"],
        project["id"],
        "Private task",
    )

    response = client.get(
        f"/tasks/{task['id']}",
        headers=unrelated_manager["headers"],
    )

    assert response.status_code == 403
