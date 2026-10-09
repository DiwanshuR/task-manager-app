import logging

logger = logging.getLogger(__name__)

from typing import Annotated

from fastapi import APIRouter, Depends, Path, Query, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.task import Task, TaskStatus, TaskPriority
from app.models.project import Project
from app.models.user import User
from app.schemas.task import TaskCreate, TaskUpdate, TaskOut
from app.auth.dependencies import get_current_user

from app.repositories.task_repository import SQLAlchemyTaskRepository
from app.repositories.project_repository import SQLAlchemyProjectRepository
from app.services.task_service import TaskService
from app.schemas.error import API_ERROR_RESPONSES


from app.exceptions import (
    ProjectNotFoundError,
    TaskNotFoundError,
    UnauthorizedActionError,
)

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"],
    responses=API_ERROR_RESPONSES,
)

def _task_service(db: Session) -> TaskService:
    return TaskService(
        task_repository=SQLAlchemyTaskRepository(db),
        project_repository=SQLAlchemyProjectRepository(db),
    )
    
# removed _get_owned_project function and moved it to TaskService class in services/task_service.py for better separation of concerns and testability.



# ...existing code...

@router.post("/", response_model=TaskOut, status_code=status.HTTP_201_CREATED)
def create_task(
    payload: TaskCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    service = _task_service(db)
    task = service.create(
        payload,
        user_id=current_user.id,
        role=current_user.role,
    )

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
    project_id: int | None = Query(None, le=2_147_483_647),
    search: str | None = Query(None, description="Case-insensitive match on task title"),
    skip: int = Query(0, ge=0, le=2_147_483_647),
    limit: int = Query(20, ge=1, le=100),
):
    service = _task_service(db)

    return service.list(
        user_id=current_user.id,
        role=current_user.role,
        status_filter=status_filter,
        priority=priority,
        project_id=project_id,
        search=search,
        skip=skip,
        limit=limit,
    )


@router.get("/deleted", response_model=list[TaskOut])
def list_deleted_tasks(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    service = _task_service(db)
    return service.list_deleted(
        user_id=current_user.id,
        role=current_user.role,
    )


@router.get("/{task_id:int}", response_model=TaskOut)
def get_task(
    task_id: Annotated[int, Path(le=2_147_483_647)],
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    service = _task_service(db)
    return service.get(
        task_id,
        user_id=current_user.id,
        role=current_user.role,
    )


@router.put("/{task_id:int}", response_model=TaskOut)
def update_task(
    task_id: Annotated[int, Path(le=2_147_483_647)],
    payload: TaskUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    service = _task_service(db)
    return service.update(
        task_id,
        payload,
        user_id=current_user.id,
        role=current_user.role,
    )


@router.post(
    "/{task_id:int}/archive",
    response_model=TaskOut,
    status_code=status.HTTP_200_OK,
)
def archive_task(
    task_id: Annotated[int, Path(le=2_147_483_647)],
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    service = _task_service(db)
    return service.archive(
        task_id,
        user_id=current_user.id,
        role=current_user.role,
    )


@router.post(
    "/{task_id:int}/restore",
    response_model=TaskOut,
    status_code=status.HTTP_200_OK,
)
def restore_task(
    task_id: Annotated[int, Path(le=2_147_483_647)],
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    service = _task_service(db)
    task = service.restore(
        task_id,
        user_id=current_user.id,
        role=current_user.role,
    )
    logger.info("Task restored task_id=%s user_id=%s", task_id, current_user.id)
    return task


@router.delete("/{task_id:int}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(
    task_id: Annotated[int, Path(le=2_147_483_647)],
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    service = _task_service(db)
    service.delete(
        task_id,
        user_id=current_user.id,
        role=current_user.role,
    )

    logger.info(
        "Task deleted task_id=%s user_id=%s",
        task_id,
        current_user.id,
    )
    return None