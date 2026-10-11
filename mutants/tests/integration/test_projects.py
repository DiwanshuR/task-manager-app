from app.models.user import UserRole


def create_project(client, headers, name="Test project"):
    return client.post(
        "/projects/",
        headers=headers,
        json={"name": name, "description": "Project for testing"},
    )


def test_member_cannot_create_project(client, create_user):
    member = create_user("member@example.com")

    response = create_project(client, member["headers"])

    assert response.status_code == 403


def test_manager_can_create_and_list_project(client, create_user):
    manager = create_user("manager@example.com", role=UserRole.manager)

    created = create_project(client, manager["headers"])
    assert created.status_code == 201, created.text

    listed = client.get("/projects/", headers=manager["headers"])
    assert listed.status_code == 200
    assert any(project["name"] == "Test project" for project in listed.json())


def test_project_owner_can_update_project(client, create_user):
    manager = create_user("owner@example.com", role=UserRole.manager)
    created = create_project(client, manager["headers"])
    project_id = created.json()["id"]

    response = client.put(
        f"/projects/{project_id}",
        headers=manager["headers"],
        json={"name": "Updated project", "description": "Updated description"},
    )

    assert response.status_code == 200, response.text
    assert response.json()["name"] == "Updated project"


def test_other_user_cannot_view_project(client, create_user):
    manager = create_user("project-owner@example.com", role=UserRole.manager)
    other_user = create_user("other-user@example.com")

    created = create_project(client, manager["headers"])
    project_id = created.json()["id"]

    response = client.get(
        f"/projects/{project_id}",
        headers=other_user["headers"],
    )

    assert response.status_code == 403
    
    
# This test written after coverage check as projects routes was at least covered top 3 files, but not fully covered. This test ensures that a manager can add a member during project creation and that the member can view the project afterward.
def test_manager_can_add_member_during_project_creation(
    client,
    create_user,
):
    manager = create_user("project-manager@example.com", role=UserRole.manager)
    member = create_user("assigned-member@example.com")

    response = client.post(
        "/projects/",
        headers=manager["headers"],
        json={
            "name": "Shared project",
            "member_emails": [member["email"]],
        },
    )
    assert response.status_code == 201, response.text

    project_id = response.json()["id"]
    member_view = client.get(
        f"/projects/{project_id}",
        headers=member["headers"],
    )
    assert member_view.status_code == 200, member_view.text
    assert member_view.json()["name"] == "Shared project"
    
    
def test_project_owner_can_assign_member(client, create_user):
    manager = create_user("assignment-owner@example.com", role=UserRole.manager)
    member = create_user("new-member@example.com")

    created = create_project(client, manager["headers"])
    assert created.status_code == 201, created.text
    project_id = created.json()["id"]

    assigned = client.post(
        f"/projects/{project_id}/members",
        headers=manager["headers"],
        json={"emails": [member["email"]]},
    )
    assert assigned.status_code == 200, assigned.text

    member_view = client.get(
        f"/projects/{project_id}",
        headers=member["headers"],
    )
    assert member_view.status_code == 200, member_view.text
    assert member_view.json()["name"] == "Test project"