from abc import ABC, abstractmethod

from sqlalchemy.orm import Session

from app.models.task import Task, TaskPriority, TaskStatus
from app.schemas.task import TaskCreate, TaskUpdate


class TaskRepository(ABC):
    @abstractmethod
    def get_all(
        self,
        *,
        owner_id: int,
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
    def create(self, payload: TaskCreate, *, created_by: int) -> Task:
        raise NotImplementedError

    @abstractmethod
    def update(self, task: Task, payload: TaskUpdate) -> Task:
        raise NotImplementedError

    @abstractmethod
    def delete(self, task: Task) -> None:
        raise NotImplementedError


class SQLAlchemyTaskRepository(TaskRepository):
    def __init__(self, db: Session):
        self.db = db

    def get_all(
        self,
        *,
        owner_id: int,
        status_filter: TaskStatus | None = None,
        priority: TaskPriority | None = None,
        project_id: int | None = None,
        search: str | None = None,
        skip: int = 0,
        limit: int = 20,
    ) -> list[Task]:
        query = (
            self.db.query(Task)
            .join(Task.project)
            .filter(Task.project.has(owner_id=owner_id))
        )

        if status_filter is not None:
            query = query.filter(Task.status == status_filter)
        if priority is not None:
            query = query.filter(Task.priority == priority)
        if project_id is not None:
            query = query.filter(Task.project_id == project_id)
        if search is not None:
            query = query.filter(Task.title.ilike(f"%{search}%"))

        return query.offset(skip).limit(limit).all()

    def get_by_id(self, task_id: int) -> Task | None:
        return self.db.query(Task).filter(Task.id == task_id).first()

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

    def delete(self, task: Task) -> None:
        self.db.delete(task)
        self.db.commit()