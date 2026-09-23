from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.task import Task, TaskStatus, TaskPriority
from app.models.project import Project
from app.models.user import User
from app.schemas.task import TaskCreate, TaskUpdate, TaskOut
from app.auth.dependencies import get_current_user

router = APIRouter(prefix="/tasks", tags=["Tasks"])


def _get_owned_project(project_id: int, db: Session, current_user: User) -> Project:
    project = db.query(Project).filter(Project.id == project_id).first()
    if project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    if project.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to access this project")
    return project


@router.post("/", response_model=TaskOut, status_code=status.HTTP_201_CREATED)
def create_task(payload: TaskCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    _get_owned_project(payload.project_id, db, current_user)

    task = Task(
        title=payload.title,
        description=payload.description,
        status=payload.status,
        priority=payload.priority,
        project_id=payload.project_id,
        created_by=current_user.id,
    )
    db.add(task)
    db.commit()
    db.refresh(task)
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
    query = db.query(Task).join(Project).filter(Project.owner_id == current_user.id)

    if status_filter is not None:
        query = query.filter(Task.status == status_filter)
    if priority is not None:
        query = query.filter(Task.priority == priority)
    if project_id is not None:
        query = query.filter(Task.project_id == project_id)
    if search is not None:
        query = query.filter(Task.title.ilike(f"%{search}%"))

    return query.offset(skip).limit(limit).all()


@router.get("/{task_id}", response_model=TaskOut)
def get_task(task_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    _get_owned_project(task.project_id, db, current_user)
    return task


@router.put("/{task_id}", response_model=TaskOut)
def update_task(
    task_id: int,
    payload: TaskUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    task = db.query(Task).filter(Task.id == task_id).first()
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    _get_owned_project(task.project_id, db, current_user)

    task.title = payload.title
    task.description = payload.description
    task.status = payload.status
    task.priority = payload.priority
    db.commit()
    db.refresh(task)
    return task


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    _get_owned_project(task.project_id, db, current_user)

    db.delete(task)
    db.commit()
    return None