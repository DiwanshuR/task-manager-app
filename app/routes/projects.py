from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.project import Project
from app.models.user import User
from app.schemas.project import ProjectCreate, ProjectUpdate, ProjectOut
from app.auth.dependencies import get_current_user
from app.auth.dependencies import require_roles
from app.models.user import UserRole
from app.repositories.project_repository import SQLAlchemyProjectRepository
from app.exceptions import ProjectNotFoundError, UnauthorizedActionError

router = APIRouter(prefix="/projects", tags=["Projects"])


@router.post("/", response_model=ProjectOut, status_code=status.HTTP_201_CREATED)
def create_project(
    payload: ProjectCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(
        require_roles(UserRole.admin, UserRole.manager)
    ),
):
    # project = Project(name=payload.name, description=payload.description, owner_id=current_user.id)
    # db.add(project)
    # db.commit()
    # db.refresh(project)
    # return project
    repo = SQLAlchemyProjectRepository(db)  # we used repository directly now
    return repo.create(payload, owner_id=current_user.id)


@router.get("/", response_model=list[ProjectOut])
def list_projects(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    repo = SQLAlchemyProjectRepository(db)
    return repo.get_all(owner_id=current_user.id)

@router.get("/{project_id}", response_model=ProjectOut)
def get_project(project_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    repo = SQLAlchemyProjectRepository(db)
    project = repo.get_by_id(project_id)
    if project is None:
        # raise HTTPException(status_code=404, detail="Project not found")
        raise ProjectNotFoundError(project_id)
    
    if project.owner_id != current_user.id and current_user.role != UserRole.admin:
        # raise HTTPException(status_code=403, detail="Not authorized to access this project")
        raise UnauthorizedActionError(
            action="access",
            resource="project",
            resource_id=project_id,
        )
    return project


@router.put("/{project_id}", response_model=ProjectOut)
def update_project(
    project_id: int,
    payload: ProjectUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    repo = SQLAlchemyProjectRepository(db)
    project = repo.get_by_id(project_id)
    
    if project is None:
        # raise HTTPException(status_code=404, detail="Project not found")
        raise ProjectNotFoundError(project_id)
    if project.owner_id != current_user.id and current_user.role != UserRole.admin:
        # raise HTTPException(status_code=403, detail="Not authorized to modify this project")
        raise UnauthorizedActionError(
            action="modify",
            resource="project",
            resource_id=project_id,
        )

    return repo.update(project, payload)


@router.delete("/{project_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_project(project_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    repo = SQLAlchemyProjectRepository(db)
    project = repo.get_by_id(project_id)
    if project is None:
        raise ProjectNotFoundError(project_id)
    if project.owner_id != current_user.id:
        # raise HTTPException(status_code=403, detail="Not authorized to delete this project")
        raise UnauthorizedActionError(
            action="delete",
            resource="project",
            resource_id=project_id,
        )

    repo.delete(project)
    return None