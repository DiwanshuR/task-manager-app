from datetime import datetime, timezone

import pytest

from app.exceptions import (
    ProjectNotFoundError,
    TaskNotFoundError,
    UnauthorizedActionError,
)
from app.models.project import Project
from app.models.task import Task
from app.repositories.project_repository import ProjectRepository
from app.repositories.task_repository import TaskRepository
from app.schemas.task import TaskCreate, TaskUpdate
from app.services.task_service import TaskService


class FakeProjectRepository(ProjectRepository):
    def __init__(self, projects=()):
        self.projects = {project.id: project for project in projects}

    def get_all(self, *, owner_id: int):
        return [
            project
            for project in self.projects.values()
            if project.owner_id == owner_id
        ]

    def get_by_id(self, project_id: int):
        return self.projects.get(project_id)

    def create(self, payload, *, owner_id: int):
        raise NotImplementedError

    def update(self, project, payload):
        raise NotImplementedError

    def delete(self, project):
        raise NotImplementedError


class FakeTaskRepository(TaskRepository):
    def __init__(self):
        self.tasks = {}
        self.next_id = 1
        self.last_list_arguments = None

    def get_all(
        self,
        *,
        owner_id: int,
        is_admin: bool = False,
        status_filter=None,
        priority=None,
        project_id=None,
        search=None,
        skip=0,
        limit=20,
    ):
        self.last_list_arguments = {
            "owner_id": owner_id,
            "is_admin": is_admin,
            "status_filter": status_filter,
            "priority": priority,
            "project_id": project_id,
            "search": search,
            "skip": skip,
            "limit": limit,
        }
        visible_tasks = [
            task for task in self.tasks.values() if task.deleted_at is None
        ]
        return visible_tasks[skip : skip + limit]

    def get_by_id(self, task_id: int):
        task = self.tasks.get(task_id)
        return task if task is not None and task.deleted_at is None else None

    def get_deleted_by_id(self, task_id: int):
        task = self.tasks.get(task_id)
        return task if task is not None and task.deleted_at is not None else None

    def get_deleted(self):
        return [task for task in self.tasks.values() if task.deleted_at is not None]

    def create(self, payload: TaskCreate, *, created_by: int):
        task = Task(
            title=payload.title,
            description=payload.description,
            status=payload.status,
            priority=payload.priority,
            project_id=payload.project_id,
            created_by=created_by,
        )
        task.id = self.next_id
        self.next_id += 1
        self.tasks[task.id] = task
        return task

    def update(self, task: Task, payload: TaskUpdate):
        update_data = payload.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(task, field, value)
        return task

    def soft_delete(self, task: Task):
        task.deleted_at = datetime.now(timezone.utc)

    def restore(self, task: Task):
        task.deleted_at = None
        return task


def make_service():
    project = Project(
        id=1,
        name="Demo project",
        owner_id=10,
        members=[],
    )
    projects = FakeProjectRepository([project])
    tasks = FakeTaskRepository()
    return TaskService(tasks, projects), tasks


def test_create_task_uses_fake_repository_and_records_creator():
    service, task_repository = make_service()
    payload = TaskCreate(title="Test task", project_id=1)

    task = service.create(payload, user_id=10, role="member")

    assert task.id == 1
    assert task.title == "Test task"
    assert task.created_by == 10
    assert task_repository.get_by_id(task.id) is task


def test_create_task_rejects_user_without_project_access():
    service, task_repository = make_service()
    payload = TaskCreate(title="Test task", project_id=1)

    with pytest.raises(UnauthorizedActionError):
        service.create(payload, user_id=99, role="member")

    assert task_repository.tasks == {}


def test_create_task_rejects_missing_project():
    service, task_repository = make_service()
    payload = TaskCreate(title="Test task", project_id=999)

    with pytest.raises(ProjectNotFoundError):
        service.create(payload, user_id=10, role="member")

    assert task_repository.tasks == {}


def test_list_tasks_passes_filters_to_repository():
    service, task_repository = make_service()

    service.list(
        user_id=10,
        role="member",
        project_id=1,
        search="report",
        skip=2,
        limit=5,
    )

    assert task_repository.last_list_arguments == {
        "owner_id": 10,
        "is_admin": False,
        "status_filter": None,
        "priority": None,
        "project_id": 1,
        "search": "report",
        "skip": 2,
        "limit": 5,
    }


def test_get_rejects_missing_task():
    service, _ = make_service()

    with pytest.raises(TaskNotFoundError):
        service.get(999, user_id=10, role="member")


def test_update_task_changes_task_through_repository():
    service, _ = make_service()
    created = service.create(
        TaskCreate(title="Old title", project_id=1),
        user_id=10,
        role="member",
    )

    updated = service.update(
        created.id,
        TaskUpdate(title="New title"),
        user_id=10,
        role="member",
    )

    assert updated.title == "New title"


def test_delete_task_soft_deletes_task_through_repository():
    service, task_repository = make_service()
    created = service.create(
        TaskCreate(title="Delete me", project_id=1),
        user_id=10,
        role="member",
    )

    service.delete(
        created.id,
        user_id=99,
        role="admin",
    )

    assert task_repository.get_by_id(created.id) is None
    assert task_repository.tasks[created.id] is created
    assert created.deleted_at is not None