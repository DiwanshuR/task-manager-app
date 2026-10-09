from __future__ import annotations

from app.exceptions import (
    ArchivedTaskError,
    ProjectNotFoundError,
    TaskStateConflictError,
    TaskNotFoundError,
    UnauthorizedActionError,
)
from app.models.task import (
    Task,
    TaskPriority,
    TaskStatus,
    can_transition_task_status,
)
from app.repositories.project_repository import ProjectRepository
from app.repositories.task_repository import TaskRepository
from app.schemas.task import TaskCreate, TaskUpdate


class TaskService:
    """Task use cases, independent of HTTP and database implementations."""

    def __init__(
        self,
        task_repository: TaskRepository,
        project_repository: ProjectRepository,
    ):
        self.task_repository = task_repository
        self.project_repository = project_repository

    def _require_project_access(
        self,
        project_id: int,
        user_id: int,
        role: str,
    ) -> None:
        project = self.project_repository.get_by_id(project_id)

        if project is None:
            raise ProjectNotFoundError(project_id)

        role_value = getattr(role, "value", role)
        is_admin = role_value == "admin"
        is_owner = project.owner_id == user_id
        is_member = any(member.id == user_id for member in project.members)

        if not (is_admin or is_owner or is_member):
            raise UnauthorizedActionError(
                action="access",
                resource="project",
                resource_id=project_id,
            )

    def create(self, payload: TaskCreate, *, user_id: int, role: str):
        self._require_project_access(payload.project_id, user_id, role)
        return self.task_repository.create(payload, created_by=user_id)

    def list(
        self,
        *,
        user_id: int,
        role: str,
        status_filter: TaskStatus | None = None,
        priority: TaskPriority | None = None,
        project_id: int | None = None,
        search: str | None = None,
        skip: int = 0,
        limit: int = 20,
    ):
        role_value = getattr(role, "value", role)

        return self.task_repository.get_all(
            owner_id=user_id,
            is_admin=(role_value == "admin"),
            status_filter=status_filter,
            priority=priority,
            project_id=project_id,
            search=search,
            skip=skip,
            limit=limit,
        )

    def get(self, task_id: int, *, user_id: int, role: str):
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_project_access(task.project_id, user_id, role)
        return task

    def update(
        self,
        task_id: int,
        payload: TaskUpdate,
        *,
        user_id: int,
        role: str,
    ):
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_task_update_access(
            task,
            user_id=user_id,
            role=role,
        )

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        if payload.status != task.status:
            if payload.status == TaskStatus.archived or not can_transition_task_status(
                task.status,
                payload.status,
            ):
                raise TaskStateConflictError(
                    task.status.value,
                    payload.status.value,
                )

        return self.task_repository.update(task, payload)

    def _require_task_update_access(
        self,
        task: Task,
        *,
        user_id: int,
        role: str,
    ) -> None:
        self._require_project_access(task.project_id, user_id, role)

        role_value = getattr(role, "value", role)
        if role_value == "admin" or role_value == "manager":
            return

        if role_value == "member" and task.created_by == user_id:
            return

        raise UnauthorizedActionError(
            action="update",
            resource="task",
            resource_id=task.id,
        )

    def archive(self, task_id: int, *, user_id: int, role: str):
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        role_value = getattr(role, "value", role)
        if role_value not in {"admin", "manager"}:
            raise UnauthorizedActionError(
                action="archive",
                resource="task",
                resource_id=task_id,
            )

        self._require_project_access(task.project_id, user_id, role)

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        if not can_transition_task_status(task.status, TaskStatus.archived):
            raise TaskStateConflictError(
                task.status.value,
                TaskStatus.archived.value,
            )

        payload = TaskUpdate(
            title=task.title,
            description=task.description,
            status=TaskStatus.archived,
            priority=task.priority,
        )
        return self.task_repository.update(task, payload)

    def delete(self, task_id: int, *, user_id: int, role: str) -> None:
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_project_access(task.project_id, user_id, role)

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        role_value = getattr(role, "value", role)
        if role_value != "admin":
            raise UnauthorizedActionError(
                action="delete",
                resource="task",
                resource_id=task_id,
            )

        self.task_repository.soft_delete(task)

    def list_deleted(self, *, user_id: int, role: str) -> list[Task]:
        role_value = getattr(role, "value", role)
        if role_value != "admin":
            raise UnauthorizedActionError(
                action="view deleted",
                resource="tasks",
            )

        return self.task_repository.get_deleted()

    def restore(self, task_id: int, *, user_id: int, role: str) -> Task:
        role_value = getattr(role, "value", role)
        if role_value != "admin":
            raise UnauthorizedActionError(
                action="restore",
                resource="task",
                resource_id=task_id,
            )

        task = self.task_repository.get_deleted_by_id(task_id)
        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_project_access(task.project_id, user_id, role)
        return self.task_repository.restore(task)