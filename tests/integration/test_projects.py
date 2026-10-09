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