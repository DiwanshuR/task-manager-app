import logging

logger = logging.getLogger(__name__)

from typing import Annotated

from fastapi import APIRouter, Depends, Path, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.user import User
from app.schemas.user import UserCreate, UserOut, Token
from app.auth.security import create_refresh_token, hash_password, verify_password, create_access_token, decode_refresh_token
from app.auth.dependencies import get_current_user
from app.models.user import UserRole
from app.auth.dependencies import require_roles
from app.repositories.user_repository import SQLAlchemyUserRepository
from app.exceptions import AuthenticationError, ConflictError
from app.schemas.error import API_ERROR_RESPONSES

router = APIRouter(
    prefix="/auth",
    tags=["Auth"],
    responses=API_ERROR_RESPONSES,
)


@router.post("/register", response_model=UserOut, status_code=status.HTTP_201_CREATED)
def register(payload: UserCreate, db: Session = Depends(get_db)):
    repo = SQLAlchemyUserRepository(db)
    existing = repo.get_by_email(payload.email)
    if existing:
        raise ConflictError(
            "Email is already registered",
            details={"field": "email"},
        )

    new_user = repo.create(
        name=payload.name,
        email=payload.email,
        password_hash=hash_password(payload.password),
        role=UserRole.member,
    )
    
    return new_user


@router.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    repo = SQLAlchemyUserRepository(db)
    user = repo.get_by_email(form_data.username)

    # Same error message whether the email doesn't exist or the password
    # is wrong -- telling an attacker which is which leaks which emails
    # are real accounts.
    if not user or not verify_password(form_data.password, user.password_hash):
        logger.warning("Login Failed")
        raise AuthenticationError(
            "Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = create_access_token(data={"sub": str(user.id)})
    refresh_token = create_refresh_token(data={"sub": str(user.id)})
    
    logger.info("Login succeeded user_id=%s", user.id)
    
    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer",
    }


@router.get("/current-user", response_model=UserOut)
def current_user(user: User = Depends(get_current_user)):
    return user

@router.delete("/users/{user_id:int}")
def delete_user(
    user_id: Annotated[int, Path(le=2_147_483_647)],
    current_user: User = Depends(require_roles(UserRole.admin)),
):
    # Only an admin reaches this code
    ...
    
@router.post("/refresh")
def refresh_access_token(refresh_token: str):
    payload = decode_refresh_token(refresh_token)

    if payload is None:
        raise AuthenticationError(
            "Invalid or expired refresh token",
            headers={"WWW-Authenticate": "Bearer"},
        )

    user_id = payload.get("sub")

    if not user_id:
        raise AuthenticationError(
            "Invalid refresh token",
            headers={"WWW-Authenticate": "Bearer"},
        )

    new_access_token = create_access_token({"sub": user_id})

    return {
        "access_token": new_access_token,
        "token_type": "bearer",
    }