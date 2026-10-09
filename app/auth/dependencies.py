from fastapi import Depends, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.database import get_db
from app.auth.security import decode_access_token
from app.models.user import User
from typing import Callable
from app.models.user import UserRole, User
from app.repositories.user_repository import SQLAlchemyUserRepository
from app.exceptions import AuthenticationError, PermissionDeniedError

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")


def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
) -> User:
    payload = decode_access_token(token)
    if payload is None:
        raise AuthenticationError(
            "Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    user_id = payload.get("sub")
    if user_id is None:
        raise AuthenticationError(
            "Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    
    repo = SQLAlchemyUserRepository(db)
    user = repo.get_by_id(int(user_id))
    if user is None:
        raise AuthenticationError(
            "Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return user


def require_roles(*allowed_roles: UserRole) -> Callable:
    def role_checker(
        current_user: User = Depends(get_current_user),
    ) -> User:
        if current_user.role not in allowed_roles:
            raise PermissionDeniedError(
                "You do not have permission to perform this action",
            )

        return current_user

    return role_checker