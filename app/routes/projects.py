from typing import Annotated

from fastapi import APIRouter, Depends, Path, status
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.database import get_db
from app.models.project import Project
from app.models.user import User
from app.schemas.project import ProjectCreate, ProjectUpdate, ProjectOut, ProjectMemberAssign
from app.auth.dependencies import get_current_user
from app.auth.dependencies import require_roles
from app.models.user import UserRole
from app.repositories.project_repository import SQLAlchemyProjectRepository
from app.exceptions import (
    NotFoundError,
    PermissionDeniedError,
    ProjectNotFoundError,
    UnauthorizedActionError,
)
from app.schemas.error import API_ERROR_RESPONSES

router = APIRouter(
    prefix="/projects",
    tags=["Projects"],
    responses=API_ERROR_RESPONSES,
)


@router.post("/", response_model=ProjectOut, status_code=status.HTTP_201_CREATED)
def create_project(
    payload: ProjectCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(
        require_roles(UserRole.admin, UserRole.manager)
    ),
):
    # Normalize and de-duplicate email addresses.
    emails = {
        email.strip().casefold()
        for email in payload.member_emails
        if email.strip()
    }

    members = []
    if emails:
        members = (
            db.query(User)
            .filter(func.lower(User.email).in_(emails))
            .all()
        )

        found_emails = {user.email.casefold() for user in members}
        missing_emails = sorted(emails - found_emails)

        if missing_emails:
            raise NotFoundError(
                f"Users not found: {', '.join(missing_emails)}",
                details={"emails": missing_emails},
            )

    repo = SQLAlchemyProjectRepository(db)
    return repo.create(
        payload,
        owner_id=current_user.id,
        members=members,
    )

@router.post("/{project_id:int}/members", response_model=ProjectOut)
def assign_project_members(
    project_id: Annotated[int, Path(le=2_147_483_647)],
    payload: ProjectMemberAssign,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    repo = SQLAlchemyProjectRepository(db)
    project = repo.get_by_id(project_id)

    if project is None:
        raise ProjectNotFoundError(project_id)

    is_admin = current_user.role == UserRole.admin
    is_owner_manager = (
        current_user.role == UserRole.manager
        and project.owner_id == current_user.id
    )

    if not is_admin and not is_owner_manager:
        raise PermissionDeniedError(
            "Only the project manager or an admin can assign members",
            details={"project_id": project_id},
        )

    emails = {
        email.strip().casefold()
        for email in payload.emails
        if email.strip()
    }

    users = (
        db.query(User)
        .filter(func.lower(User.email).in_(emails))
        .all()
        if emails
        else []
    )

    found_emails = {user.email.casefold() for user in users}
    missing_emails = sorted(emails - found_emails)

    if missing_emails:
        raise NotFoundError(
            f"Users not found: {', '.join(missing_emails)}",
            details={"emails": missing_emails},
        )

    existing_ids = {member.id for member in project.members}
    project.members.extend(
        user for user in users if user.id not in existing_ids
    )

    db.commit()
    db.refresh(project)
    return project

@router.get("/", response_model=list[ProjectOut])
def list_projects(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    repo = SQLAlchemyProjectRepository(db)
    return repo.get_visible_to_user(current_user)

@router.get("/{project_id:int}", response_model=ProjectOut)
def get_project(
    project_id: Annotated[int, Path(le=2_147_483_647)],
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    repo = SQLAlchemyProjectRepository(db)
    project = repo.get_by_id(project_id)

    if project is None:
        raise ProjectNotFoundError(project_id)

    is_admin = current_user.role == UserRole.admin
    is_owner = project.owner_id == current_user.id
    is_member = any(member.id == current_user.id for member in project.members)

    if not (is_admin or is_owner or is_member):
        raise UnauthorizedActionError(
            action="access",
            resource="project",
            resource_id=project_id,
        )

    return project


@router.put("/{project_id:int}", response_model=ProjectOut)
def update_project(
    project_id: Annotated[int, Path(le=2_147_483_647)],
    payload: ProjectUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    repo = SQLAlchemyProjectRepository(db)
    project = repo.get_by_id(project_id)
    
    if project is None:
        raise ProjectNotFoundError(project_id)
    if project.owner_id != current_user.id and current_user.role != UserRole.admin:
        raise UnauthorizedActionError(
            action="modify",
            resource="project",
            resource_id=project_id,
        )

    return repo.update(project, payload)


@router.delete("/{project_id:int}", status_code=status.HTTP_204_NO_CONTENT)
def delete_project(
    project_id: Annotated[int, Path(le=2_147_483_647)],
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    repo = SQLAlchemyProjectRepository(db)
    project = repo.get_by_id(project_id)
    if project is None:
        raise ProjectNotFoundError(project_id)
    if project.owner_id != current_user.id:
        raise UnauthorizedActionError(
            action="delete",
            resource="project",
            resource_id=project_id,
        )

    repo.delete(project)
    return None