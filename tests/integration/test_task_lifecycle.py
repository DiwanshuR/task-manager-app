import pytest

from app.models.task import TASK_STATUS_TRANSITIONS, TaskStatus
from app.models.project import Project
from app.models.task import Task
from app.models.user import User
from app.models.user import UserRole


STATUS_TRANSITION_MATRIX = [
    pytest.param(
        current,
        target,
        target in TASK_STATUS_TRANSITIONS[current],
        id=f"{current.value}-to-{target.value}",
    )
    for current in TaskStatus
    for target in TaskStatus
    if current != target
]


def create_shared_project(client, manager, member):
    response = client.post(
        "/projects/",
        headers=manager["headers"],
        json={
            "name": "Lifecycle project",
            "member_emails": [member["email"]],
        },
    )
    assert response.status_code == 201, response.text
    return response.json()


def create_task(client, headers, project_id, title="Lifecycle task"):
    response = client.post(
        "/tasks/",
        headers=headers,
        json={"title": title, "project_id": project_id},
    )
    assert response.status_code == 201, response.text
    return response.json()


def update_status(client, headers, task_id, status):
    return client.put(
        f"/tasks/{task_id}",
        headers=headers,
        json={
            "title": "Lifecycle task",
            "status": status.value,
            "priority": "medium",
        },
    )


def advance_to_status(client, headers, task_id, current_status):
    if current_status in {TaskStatus.in_progress, TaskStatus.done}:
        response = update_status(client, headers, task_id, TaskStatus.in_progress)
        assert response.status_code == 200, response.text

    if current_status == TaskStatus.done:
        response = update_status(client, headers, task_id, TaskStatus.done)
        assert response.status_code == 200, response.text

    if current_status == TaskStatus.archived:
        response = client.post(
            f"/tasks/{task_id}/archive",
            headers=headers,
        )
        assert response.status_code == 200, response.text


def test_member_login_create_progress_complete_and_reread(
    client,
    create_user,
    make_auth_user,
):
    manager = make_auth_user(UserRole.manager)
    member = create_user("journey-member@example.com")
    project = create_shared_project(client, manager, member)

    created = create_task(
        client,
        member["headers"],
        project["id"],
        title="Complete a report",
    )
    task_id = created["id"]
    assert created["status"] == TaskStatus.pending.value

    in_progress = client.put(
        f"/tasks/{task_id}",
        headers=member["headers"],
        json={
            "title": "Complete a report",
            "status": TaskStatus.in_progress.value,
            "priority": "medium",
        },
    )
    assert in_progress.status_code == 200, in_progress.text
    assert in_progress.json()["status"] == TaskStatus.in_progress.value

    done = client.put(
        f"/tasks/{task_id}",
        headers=member["headers"],
        json={
            "title": "Complete a report",
            "status": TaskStatus.done.value,
            "priority": "medium",
        },
    )
    assert done.status_code == 200, done.text

    reread = client.get(f"/tasks/{task_id}", headers=member["headers"])
    assert reread.status_code == 200, reread.text
    assert reread.json()["status"] == TaskStatus.done.value


def test_member_cannot_archive_task(client, make_auth_user):
    manager = make_auth_user(UserRole.manager)
    member = make_auth_user(UserRole.member)
    project = create_shared_project(client, manager, member)
    task = create_task(client, member["headers"], project["id"])

    response = client.post(
        f"/tasks/{task['id']}/archive",
        headers=member["headers"],
    )

    assert response.status_code == 403
    reread = client.get(
        f"/tasks/{task['id']}",
        headers=member["headers"],
    )
    assert reread.status_code == 200
    assert reread.json()["status"] == TaskStatus.pending.value


def test_manager_archive_is_terminal_for_member_manager_and_admin(
    client,
    make_auth_user,
):
    manager = make_auth_user(UserRole.manager)
    member = make_auth_user(UserRole.member)
    admin = make_auth_user(UserRole.admin)
    project = create_shared_project(client, manager, member)
    task = create_task(client, member["headers"], project["id"])

    archived = client.post(
        f"/tasks/{task['id']}/archive",
        headers=manager["headers"],
    )
    assert archived.status_code == 200, archived.text
    assert archived.json()["status"] == TaskStatus.archived.value

    for actor in (member, manager, admin):
        reread = client.get(
            f"/tasks/{task['id']}",
            headers=actor["headers"],
        )
        assert reread.status_code == 200
        assert reread.json()["status"] == TaskStatus.archived.value

        update = client.put(
            f"/tasks/{task['id']}",
            headers=actor["headers"],
            json={
                "title": "Must remain archived",
                "status": TaskStatus.archived.value,
                "priority": "high",
            },
        )
        assert update.status_code == 409

        delete = client.delete(
            f"/tasks/{task['id']}",
            headers=actor["headers"],
        )
        assert delete.status_code == 409


def test_admin_delete_means_owner_gets_not_found(
    client,
    make_auth_user,
    db_session,
):
    manager = make_auth_user(UserRole.manager)
    member = make_auth_user(UserRole.member)
    admin = make_auth_user(UserRole.admin)
    project = create_shared_project(client, manager, member)
    task = create_task(client, member["headers"], project["id"])

    deleted = client.delete(
        f"/tasks/{task['id']}",
        headers=admin["headers"],
    )
    assert deleted.status_code == 204

    reread = client.get(
        f"/tasks/{task['id']}",
        headers=member["headers"],
    )
    assert reread.status_code == 404

    visible_tasks = client.get(
        f"/tasks/?project_id={project['id']}",
        headers=member["headers"],
    )
    assert visible_tasks.status_code == 200, visible_tasks.text
    assert all(item["id"] != task["id"] for item in visible_tasks.json())

    retained = db_session.query(Task).filter(Task.id == task["id"]).one()
    assert retained.deleted_at is not None

    deleted_list = client.get(
        "/tasks/deleted",
        headers=admin["headers"],
    )
    assert deleted_list.status_code == 200, deleted_list.text
    assert [item["id"] for item in deleted_list.json()] == [task["id"]]

    manager_deleted_list = client.get(
        "/tasks/deleted",
        headers=manager["headers"],
    )
    assert manager_deleted_list.status_code == 403
    manager_restore = client.post(
        f"/tasks/{task['id']}/restore",
        headers=manager["headers"],
    )
    assert manager_restore.status_code == 403

    restored = client.post(
        f"/tasks/{task['id']}/restore",
        headers=admin["headers"],
    )
    assert restored.status_code == 200, restored.text

    retained = db_session.query(Task).filter(Task.id == task["id"]).one()
    assert retained.deleted_at is None
    reread_after_restore = client.get(
        f"/tasks/{task['id']}",
        headers=member["headers"],
    )
    assert reread_after_restore.status_code == 200, reread_after_restore.text

    restore_again = client.post(
        f"/tasks/{task['id']}/restore",
        headers=admin["headers"],
    )
    assert restore_again.status_code == 404


@pytest.mark.parametrize(
    ("current_status", "target_status", "is_legal"),
    STATUS_TRANSITION_MATRIX,
)
def test_task_api_enforces_every_status_transition(
    client,
    make_auth_user,
    current_status,
    target_status,
    is_legal,
):
    manager = make_auth_user(UserRole.manager)
    project = client.post(
        "/projects/",
        headers=manager["headers"],
        json={"name": "Transition matrix project"},
    ).json()
    task = create_task(client, manager["headers"], project["id"])
    task_id = task["id"]
    advance_to_status(client, manager["headers"], task_id, current_status)

    if target_status == TaskStatus.archived:
        response = client.post(
            f"/tasks/{task_id}/archive",
            headers=manager["headers"],
        )
    else:
        response = update_status(
            client,
            manager["headers"],
            task_id,
            target_status,
        )

    assert response.status_code == (200 if is_legal else 409), response.text
    reread = client.get(
        f"/tasks/{task_id}",
        headers=manager["headers"],
    )
    assert reread.status_code == 200
    expected_status = target_status if is_legal else current_status
    assert reread.json()["status"] == expected_status.value


def test_existing_inaccessible_task_is_forbidden_but_missing_task_is_not_found(
    client,
    make_auth_user,
):
    manager = make_auth_user(UserRole.manager)
    outsider = make_auth_user(UserRole.member)
    project = client.post(
        "/projects/",
        headers=manager["headers"],
        json={"name": "Private lifecycle project"},
    ).json()
    task = create_task(client, manager["headers"], project["id"])

    forbidden = client.get(
        f"/tasks/{task['id']}",
        headers=outsider["headers"],
    )
    missing = client.get(
        "/tasks/999999",
        headers=outsider["headers"],
    )

    assert forbidden.status_code == 403
    assert missing.status_code == 404


def test_task_count_matches_only_the_rows_seeded_for_this_test(db_session):
    assert db_session.query(Task).count() == 0

    owner = User(
        name="Seed owner",
        email="seed-owner@example.com",
        password_hash="not-used",
        role=UserRole.manager,
    )
    db_session.add(owner)
    db_session.flush()

    project = Project(name="Seeded project", owner_id=owner.id)
    db_session.add(project)
    db_session.flush()
    db_session.add_all(
        [
            Task(title="Seeded task 1", project_id=project.id, created_by=owner.id),
            Task(title="Seeded task 2", project_id=project.id, created_by=owner.id),
        ]
    )
    db_session.commit()

    assert db_session.query(Task).count() == 2
