from abc import ABC, abstractmethod
from sqlalchemy import func, or_
from app.models.project import Project
from app.models.user import User
from sqlalchemy.orm import Session

from app.models.task import Task, TaskPriority, TaskStatus
from app.schemas.task import TaskCreate, TaskUpdate


class TaskRepository(ABC):
    @abstractmethod
    def get_all(
        self,
        *,
        owner_id: int,
        is_admin: bool = False,
        status_filter: TaskStatus | None = None,
        priority: TaskPriority | None = None,
        project_id: int | None = None,
        search: str | None = None,
        skip: int = 0,
        limit: int = 20,
    ) -> list[Task]:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, task_id: int) -> Task | None:
        raise NotImplementedError

    @abstractmethod
    def get_deleted_by_id(self, task_id: int) -> Task | None:
        raise NotImplementedError

    @abstractmethod
    def get_deleted(self) -> list[Task]:
        raise NotImplementedError

    @abstractmethod
    def create(self, payload: TaskCreate, *, created_by: int) -> Task:
        raise NotImplementedError

    @abstractmethod
    def update(self, task: Task, payload: TaskUpdate) -> Task:
        raise NotImplementedError

    @abstractmethod
    def soft_delete(self, task: Task) -> None:
        raise NotImplementedError

    @abstractmethod
    def restore(self, task: Task) -> Task:
        raise NotImplementedError


class SQLAlchemyTaskRepository(TaskRepository):
    def __init__(self, db: Session):
        self.db = db

    def get_all(
        self,
        *,
        owner_id: int,
        is_admin: bool = False,
        status_filter: TaskStatus | None = None,
        priority: TaskPriority | None = None,
        project_id: int | None = None,
        search: str | None = None,
        skip: int = 0,
        limit: int = 20,
    ) -> list[Task]:
        query = self.db.query(Task).join(Task.project).filter(
            Task.deleted_at.is_(None)
        )

        if not is_admin:
            query = query.filter(
                or_(
                    Project.owner_id == owner_id,
                    Project.members.any(User.id == owner_id),
                )
            )

        if status_filter is not None:
            query = query.filter(Task.status == status_filter)
        if priority is not None:
            query = query.filter(Task.priority == priority)
        if project_id is not None:
            query = query.filter(Task.project_id == project_id)
        if search:
            query = query.filter(Task.title.ilike(f"%{search}%"))

        return query.offset(skip).limit(limit).all()

    def get_by_id(self, task_id: int) -> Task | None:
        return (
            self.db.query(Task)
            .filter(Task.id == task_id, Task.deleted_at.is_(None))
            .first()
        )

    def get_deleted_by_id(self, task_id: int) -> Task | None:
        return (
            self.db.query(Task)
            .filter(Task.id == task_id, Task.deleted_at.is_not(None))
            .first()
        )

    def get_deleted(self) -> list[Task]:
        return (
            self.db.query(Task)
            .filter(Task.deleted_at.is_not(None))
            .order_by(Task.deleted_at.desc(), Task.id.desc())
            .all()
        )

    def create(self, payload: TaskCreate, *, created_by: int) -> Task:
        task = Task(
            title=payload.title,
            description=payload.description,
            status=payload.status,
            priority=payload.priority,
            project_id=payload.project_id,
            created_by=created_by,
        )
        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)
        return task

    def update(self, task: Task, payload: TaskUpdate) -> Task:
        task.title = payload.title
        task.description = payload.description
        task.status = payload.status
        task.priority = payload.priority
        self.db.commit()
        self.db.refresh(task)
        return task

    def soft_delete(self, task: Task) -> None:
        task.deleted_at = func.now()
        self.db.commit()
        self.db.refresh(task)

    def restore(self, task: Task) -> Task:
        task.deleted_at = None
        self.db.commit()
        self.db.refresh(task)
        return task