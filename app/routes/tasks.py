import logging

logger = logging.getLogger(__name__)

from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.task import Task, TaskStatus, TaskPriority
from app.models.project import Project
from app.models.user import User
from app.schemas.task import TaskCreate, TaskUpdate, TaskOut
from app.auth.dependencies import get_current_user

from app.repositories.task_repository import SQLAlchemyTaskRepository
from app.repositories.project_repository import SQLAlchemyProjectRepository

from app.exceptions import (
    ProjectNotFoundError,
    TaskNotFoundError,
    UnauthorizedActionError,
)

router = APIRouter(prefix="/tasks", tags=["Tasks"])


def _get_owned_project(project_id: int, db: Session, current_user: User) -> Project:
    # project = db.query(Project).filter(Project.id == project_id).first()
    project = SQLAlchemyProjectRepository(db).get_by_id(project_id)
    if project is None:
        # raise HTTPException(status_code=404, detail="Project not found")
        raise ProjectNotFoundError(project_id)
    if project.owner_id != current_user.id:
        # raise HTTPException(status_code=403, detail="Not authorized to access this project")
        raise UnauthorizedActionError(
            action="access",
            resource="project",
            resource_id=project_id,
        )
    return project


@router.post("/", response_model=TaskOut, status_code=status.HTTP_201_CREATED)
def create_task(payload: TaskCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    _get_owned_project(payload.project_id, db, current_user)

    repo = SQLAlchemyTaskRepository(db)
    
    # task = Task(
    #     title=payload.title,
    #     description=payload.description,
    #     status=payload.status,
    #     priority=payload.priority,
    #     project_id=payload.project_id,
    #     created_by=current_user.id,
    # )
    # db.add(task)
    # db.commit()
    # db.refresh(task)
    # return task
    # Just use the repository     
    task = repo.create(payload, created_by=current_user.id) 
    logger.info(
        "Task created task_id=%s project_id=%s user_id=%s",
        task.id,
        task.project_id,
        current_user.id,
    )
    return task


@router.get("/", response_model=list[TaskOut])
def list_tasks(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
    status_filter: TaskStatus | None = Query(None, alias="status"),
    priority: TaskPriority | None = None,
    project_id: int | None = None,
    search: str | None = Query(None, description="Case-insensitive match on task title"),
    skip: int = Query(0, ge=0),
    limit: int = Query(20, ge=1, le=100),
):
    repo = SQLAlchemyTaskRepository(db)
    
    return repo.get_all(
        owner_id=current_user.id,
        status_filter=status_filter,
        priority=priority,
        project_id=project_id,
        search=search,
        skip=skip,
        limit=limit
    )

@router.get("/{task_id}", response_model=TaskOut)
def get_task(task_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    repo = SQLAlchemyTaskRepository(db)
    task = repo.get_by_id(task_id)
    if task is None:
        # raise HTTPException(status_code=404, detail="Task not found")
        raise TaskNotFoundError(task_id)
    _get_owned_project(task.project_id, db, current_user)
    return task


@router.put("/{task_id}", response_model=TaskOut)
def update_task(
    task_id: int,
    payload: TaskUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    repo = SQLAlchemyTaskRepository(db)
    task = repo.get_by_id(task_id)
    if task is None:
        # raise HTTPException(status_code=404, detail="Task not found")
        raise TaskNotFoundError(task_id)
    _get_owned_project(task.project_id, db, current_user)

    return repo.update(task, payload)


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    repo = SQLAlchemyTaskRepository(db)
    task = repo.get_by_id(task_id)
    if task is None:
        # raise HTTPException(status_code=404, detail="Task not found")
        raise TaskNotFoundError(task_id)    # using custome exceptions 
    _get_owned_project(task.project_id, db, current_user)

    repo.delete(task)
    logger.info(
        "Task deleted task_id=%s user_id=%s",
        task.id,
        current_user.id,
    )
    return None