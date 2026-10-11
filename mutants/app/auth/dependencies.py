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


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x_get_current_user__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_get_current_user__mutmut)
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


def x_get_current_user__mutmut_orig(
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


def x_get_current_user__mutmut_1(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
) -> User:
    payload = None
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


def x_get_current_user__mutmut_2(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
) -> User:
    payload = decode_access_token(None)
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


def x_get_current_user__mutmut_3(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
) -> User:
    payload = decode_access_token(token)
    if payload is not None:
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


def x_get_current_user__mutmut_4(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
) -> User:
    payload = decode_access_token(token)
    if payload is None:
        raise AuthenticationError(
            None,
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


def x_get_current_user__mutmut_5(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
) -> User:
    payload = decode_access_token(token)
    if payload is None:
        raise AuthenticationError(
            "Could not validate credentials",
            headers=None,
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


def x_get_current_user__mutmut_6(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
) -> User:
    payload = decode_access_token(token)
    if payload is None:
        raise AuthenticationError(
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


def x_get_current_user__mutmut_7(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
) -> User:
    payload = decode_access_token(token)
    if payload is None:
        raise AuthenticationError(
            "Could not validate credentials",
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


def x_get_current_user__mutmut_8(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
) -> User:
    payload = decode_access_token(token)
    if payload is None:
        raise AuthenticationError(
            "XXCould not validate credentialsXX",
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


def x_get_current_user__mutmut_9(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
) -> User:
    payload = decode_access_token(token)
    if payload is None:
        raise AuthenticationError(
            "could not validate credentials",
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


def x_get_current_user__mutmut_10(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
) -> User:
    payload = decode_access_token(token)
    if payload is None:
        raise AuthenticationError(
            "COULD NOT VALIDATE CREDENTIALS",
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


def x_get_current_user__mutmut_11(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
) -> User:
    payload = decode_access_token(token)
    if payload is None:
        raise AuthenticationError(
            "Could not validate credentials",
            headers={"XXWWW-AuthenticateXX": "Bearer"},
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


def x_get_current_user__mutmut_12(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
) -> User:
    payload = decode_access_token(token)
    if payload is None:
        raise AuthenticationError(
            "Could not validate credentials",
            headers={"www-authenticate": "Bearer"},
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


def x_get_current_user__mutmut_13(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
) -> User:
    payload = decode_access_token(token)
    if payload is None:
        raise AuthenticationError(
            "Could not validate credentials",
            headers={"WWW-AUTHENTICATE": "Bearer"},
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


def x_get_current_user__mutmut_14(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
) -> User:
    payload = decode_access_token(token)
    if payload is None:
        raise AuthenticationError(
            "Could not validate credentials",
            headers={"WWW-Authenticate": "XXBearerXX"},
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


def x_get_current_user__mutmut_15(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
) -> User:
    payload = decode_access_token(token)
    if payload is None:
        raise AuthenticationError(
            "Could not validate credentials",
            headers={"WWW-Authenticate": "bearer"},
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


def x_get_current_user__mutmut_16(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
) -> User:
    payload = decode_access_token(token)
    if payload is None:
        raise AuthenticationError(
            "Could not validate credentials",
            headers={"WWW-Authenticate": "BEARER"},
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


def x_get_current_user__mutmut_17(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
) -> User:
    payload = decode_access_token(token)
    if payload is None:
        raise AuthenticationError(
            "Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    user_id = None
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


def x_get_current_user__mutmut_18(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
) -> User:
    payload = decode_access_token(token)
    if payload is None:
        raise AuthenticationError(
            "Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    user_id = payload.get(None)
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


def x_get_current_user__mutmut_19(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
) -> User:
    payload = decode_access_token(token)
    if payload is None:
        raise AuthenticationError(
            "Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    user_id = payload.get("XXsubXX")
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


def x_get_current_user__mutmut_20(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
) -> User:
    payload = decode_access_token(token)
    if payload is None:
        raise AuthenticationError(
            "Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    user_id = payload.get("SUB")
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


def x_get_current_user__mutmut_21(
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
    if user_id is not None:
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


def x_get_current_user__mutmut_22(
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
            None,
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


def x_get_current_user__mutmut_23(
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
            headers=None,
        )
    
    
    repo = SQLAlchemyUserRepository(db)
    user = repo.get_by_id(int(user_id))
    if user is None:
        raise AuthenticationError(
            "Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return user


def x_get_current_user__mutmut_24(
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


def x_get_current_user__mutmut_25(
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
            )
    
    
    repo = SQLAlchemyUserRepository(db)
    user = repo.get_by_id(int(user_id))
    if user is None:
        raise AuthenticationError(
            "Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return user


def x_get_current_user__mutmut_26(
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
            "XXCould not validate credentialsXX",
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


def x_get_current_user__mutmut_27(
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
            "could not validate credentials",
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


def x_get_current_user__mutmut_28(
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
            "COULD NOT VALIDATE CREDENTIALS",
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


def x_get_current_user__mutmut_29(
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
            headers={"XXWWW-AuthenticateXX": "Bearer"},
        )
    
    
    repo = SQLAlchemyUserRepository(db)
    user = repo.get_by_id(int(user_id))
    if user is None:
        raise AuthenticationError(
            "Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return user


def x_get_current_user__mutmut_30(
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
            headers={"www-authenticate": "Bearer"},
        )
    
    
    repo = SQLAlchemyUserRepository(db)
    user = repo.get_by_id(int(user_id))
    if user is None:
        raise AuthenticationError(
            "Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return user


def x_get_current_user__mutmut_31(
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
            headers={"WWW-AUTHENTICATE": "Bearer"},
        )
    
    
    repo = SQLAlchemyUserRepository(db)
    user = repo.get_by_id(int(user_id))
    if user is None:
        raise AuthenticationError(
            "Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return user


def x_get_current_user__mutmut_32(
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
            headers={"WWW-Authenticate": "XXBearerXX"},
        )
    
    
    repo = SQLAlchemyUserRepository(db)
    user = repo.get_by_id(int(user_id))
    if user is None:
        raise AuthenticationError(
            "Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return user


def x_get_current_user__mutmut_33(
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
            headers={"WWW-Authenticate": "bearer"},
        )
    
    
    repo = SQLAlchemyUserRepository(db)
    user = repo.get_by_id(int(user_id))
    if user is None:
        raise AuthenticationError(
            "Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return user


def x_get_current_user__mutmut_34(
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
            headers={"WWW-Authenticate": "BEARER"},
        )
    
    
    repo = SQLAlchemyUserRepository(db)
    user = repo.get_by_id(int(user_id))
    if user is None:
        raise AuthenticationError(
            "Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return user


def x_get_current_user__mutmut_35(
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
    
    
    repo = None
    user = repo.get_by_id(int(user_id))
    if user is None:
        raise AuthenticationError(
            "Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return user


def x_get_current_user__mutmut_36(
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
    
    
    repo = SQLAlchemyUserRepository(None)
    user = repo.get_by_id(int(user_id))
    if user is None:
        raise AuthenticationError(
            "Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return user


def x_get_current_user__mutmut_37(
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
    user = None
    if user is None:
        raise AuthenticationError(
            "Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return user


def x_get_current_user__mutmut_38(
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
    user = repo.get_by_id(None)
    if user is None:
        raise AuthenticationError(
            "Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return user


def x_get_current_user__mutmut_39(
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
    user = repo.get_by_id(int(None))
    if user is None:
        raise AuthenticationError(
            "Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return user


def x_get_current_user__mutmut_40(
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
    if user is not None:
        raise AuthenticationError(
            "Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return user


def x_get_current_user__mutmut_41(
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
            None,
            headers={"WWW-Authenticate": "Bearer"},
        )

    return user


def x_get_current_user__mutmut_42(
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
            headers=None,
        )

    return user


def x_get_current_user__mutmut_43(
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
            headers={"WWW-Authenticate": "Bearer"},
        )

    return user


def x_get_current_user__mutmut_44(
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
            )

    return user


def x_get_current_user__mutmut_45(
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
            "XXCould not validate credentialsXX",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return user


def x_get_current_user__mutmut_46(
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
            "could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return user


def x_get_current_user__mutmut_47(
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
            "COULD NOT VALIDATE CREDENTIALS",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return user


def x_get_current_user__mutmut_48(
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
            headers={"XXWWW-AuthenticateXX": "Bearer"},
        )

    return user


def x_get_current_user__mutmut_49(
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
            headers={"www-authenticate": "Bearer"},
        )

    return user


def x_get_current_user__mutmut_50(
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
            headers={"WWW-AUTHENTICATE": "Bearer"},
        )

    return user


def x_get_current_user__mutmut_51(
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
            headers={"WWW-Authenticate": "XXBearerXX"},
        )

    return user


def x_get_current_user__mutmut_52(
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
            headers={"WWW-Authenticate": "bearer"},
        )

    return user


def x_get_current_user__mutmut_53(
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
            headers={"WWW-Authenticate": "BEARER"},
        )

    return user

mutants_x_get_current_user__mutmut['_mutmut_orig'] = x_get_current_user__mutmut_orig # type: ignore # mutmut generated
mutants_x_get_current_user__mutmut['x_get_current_user__mutmut_1'] = x_get_current_user__mutmut_1 # type: ignore # mutmut generated
mutants_x_get_current_user__mutmut['x_get_current_user__mutmut_2'] = x_get_current_user__mutmut_2 # type: ignore # mutmut generated
mutants_x_get_current_user__mutmut['x_get_current_user__mutmut_3'] = x_get_current_user__mutmut_3 # type: ignore # mutmut generated
mutants_x_get_current_user__mutmut['x_get_current_user__mutmut_4'] = x_get_current_user__mutmut_4 # type: ignore # mutmut generated
mutants_x_get_current_user__mutmut['x_get_current_user__mutmut_5'] = x_get_current_user__mutmut_5 # type: ignore # mutmut generated
mutants_x_get_current_user__mutmut['x_get_current_user__mutmut_6'] = x_get_current_user__mutmut_6 # type: ignore # mutmut generated
mutants_x_get_current_user__mutmut['x_get_current_user__mutmut_7'] = x_get_current_user__mutmut_7 # type: ignore # mutmut generated
mutants_x_get_current_user__mutmut['x_get_current_user__mutmut_8'] = x_get_current_user__mutmut_8 # type: ignore # mutmut generated
mutants_x_get_current_user__mutmut['x_get_current_user__mutmut_9'] = x_get_current_user__mutmut_9 # type: ignore # mutmut generated
mutants_x_get_current_user__mutmut['x_get_current_user__mutmut_10'] = x_get_current_user__mutmut_10 # type: ignore # mutmut generated
mutants_x_get_current_user__mutmut['x_get_current_user__mutmut_11'] = x_get_current_user__mutmut_11 # type: ignore # mutmut generated
mutants_x_get_current_user__mutmut['x_get_current_user__mutmut_12'] = x_get_current_user__mutmut_12 # type: ignore # mutmut generated
mutants_x_get_current_user__mutmut['x_get_current_user__mutmut_13'] = x_get_current_user__mutmut_13 # type: ignore # mutmut generated
mutants_x_get_current_user__mutmut['x_get_current_user__mutmut_14'] = x_get_current_user__mutmut_14 # type: ignore # mutmut generated
mutants_x_get_current_user__mutmut['x_get_current_user__mutmut_15'] = x_get_current_user__mutmut_15 # type: ignore # mutmut generated
mutants_x_get_current_user__mutmut['x_get_current_user__mutmut_16'] = x_get_current_user__mutmut_16 # type: ignore # mutmut generated
mutants_x_get_current_user__mutmut['x_get_current_user__mutmut_17'] = x_get_current_user__mutmut_17 # type: ignore # mutmut generated
mutants_x_get_current_user__mutmut['x_get_current_user__mutmut_18'] = x_get_current_user__mutmut_18 # type: ignore # mutmut generated
mutants_x_get_current_user__mutmut['x_get_current_user__mutmut_19'] = x_get_current_user__mutmut_19 # type: ignore # mutmut generated
mutants_x_get_current_user__mutmut['x_get_current_user__mutmut_20'] = x_get_current_user__mutmut_20 # type: ignore # mutmut generated
mutants_x_get_current_user__mutmut['x_get_current_user__mutmut_21'] = x_get_current_user__mutmut_21 # type: ignore # mutmut generated
mutants_x_get_current_user__mutmut['x_get_current_user__mutmut_22'] = x_get_current_user__mutmut_22 # type: ignore # mutmut generated
mutants_x_get_current_user__mutmut['x_get_current_user__mutmut_23'] = x_get_current_user__mutmut_23 # type: ignore # mutmut generated
mutants_x_get_current_user__mutmut['x_get_current_user__mutmut_24'] = x_get_current_user__mutmut_24 # type: ignore # mutmut generated
mutants_x_get_current_user__mutmut['x_get_current_user__mutmut_25'] = x_get_current_user__mutmut_25 # type: ignore # mutmut generated
mutants_x_get_current_user__mutmut['x_get_current_user__mutmut_26'] = x_get_current_user__mutmut_26 # type: ignore # mutmut generated
mutants_x_get_current_user__mutmut['x_get_current_user__mutmut_27'] = x_get_current_user__mutmut_27 # type: ignore # mutmut generated
mutants_x_get_current_user__mutmut['x_get_current_user__mutmut_28'] = x_get_current_user__mutmut_28 # type: ignore # mutmut generated
mutants_x_get_current_user__mutmut['x_get_current_user__mutmut_29'] = x_get_current_user__mutmut_29 # type: ignore # mutmut generated
mutants_x_get_current_user__mutmut['x_get_current_user__mutmut_30'] = x_get_current_user__mutmut_30 # type: ignore # mutmut generated
mutants_x_get_current_user__mutmut['x_get_current_user__mutmut_31'] = x_get_current_user__mutmut_31 # type: ignore # mutmut generated
mutants_x_get_current_user__mutmut['x_get_current_user__mutmut_32'] = x_get_current_user__mutmut_32 # type: ignore # mutmut generated
mutants_x_get_current_user__mutmut['x_get_current_user__mutmut_33'] = x_get_current_user__mutmut_33 # type: ignore # mutmut generated
mutants_x_get_current_user__mutmut['x_get_current_user__mutmut_34'] = x_get_current_user__mutmut_34 # type: ignore # mutmut generated
mutants_x_get_current_user__mutmut['x_get_current_user__mutmut_35'] = x_get_current_user__mutmut_35 # type: ignore # mutmut generated
mutants_x_get_current_user__mutmut['x_get_current_user__mutmut_36'] = x_get_current_user__mutmut_36 # type: ignore # mutmut generated
mutants_x_get_current_user__mutmut['x_get_current_user__mutmut_37'] = x_get_current_user__mutmut_37 # type: ignore # mutmut generated
mutants_x_get_current_user__mutmut['x_get_current_user__mutmut_38'] = x_get_current_user__mutmut_38 # type: ignore # mutmut generated
mutants_x_get_current_user__mutmut['x_get_current_user__mutmut_39'] = x_get_current_user__mutmut_39 # type: ignore # mutmut generated
mutants_x_get_current_user__mutmut['x_get_current_user__mutmut_40'] = x_get_current_user__mutmut_40 # type: ignore # mutmut generated
mutants_x_get_current_user__mutmut['x_get_current_user__mutmut_41'] = x_get_current_user__mutmut_41 # type: ignore # mutmut generated
mutants_x_get_current_user__mutmut['x_get_current_user__mutmut_42'] = x_get_current_user__mutmut_42 # type: ignore # mutmut generated
mutants_x_get_current_user__mutmut['x_get_current_user__mutmut_43'] = x_get_current_user__mutmut_43 # type: ignore # mutmut generated
mutants_x_get_current_user__mutmut['x_get_current_user__mutmut_44'] = x_get_current_user__mutmut_44 # type: ignore # mutmut generated
mutants_x_get_current_user__mutmut['x_get_current_user__mutmut_45'] = x_get_current_user__mutmut_45 # type: ignore # mutmut generated
mutants_x_get_current_user__mutmut['x_get_current_user__mutmut_46'] = x_get_current_user__mutmut_46 # type: ignore # mutmut generated
mutants_x_get_current_user__mutmut['x_get_current_user__mutmut_47'] = x_get_current_user__mutmut_47 # type: ignore # mutmut generated
mutants_x_get_current_user__mutmut['x_get_current_user__mutmut_48'] = x_get_current_user__mutmut_48 # type: ignore # mutmut generated
mutants_x_get_current_user__mutmut['x_get_current_user__mutmut_49'] = x_get_current_user__mutmut_49 # type: ignore # mutmut generated
mutants_x_get_current_user__mutmut['x_get_current_user__mutmut_50'] = x_get_current_user__mutmut_50 # type: ignore # mutmut generated
mutants_x_get_current_user__mutmut['x_get_current_user__mutmut_51'] = x_get_current_user__mutmut_51 # type: ignore # mutmut generated
mutants_x_get_current_user__mutmut['x_get_current_user__mutmut_52'] = x_get_current_user__mutmut_52 # type: ignore # mutmut generated
mutants_x_get_current_user__mutmut['x_get_current_user__mutmut_53'] = x_get_current_user__mutmut_53 # type: ignore # mutmut generated
mutants_x_require_roles__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_require_roles__mutmut)
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


def x_require_roles__mutmut_orig(*allowed_roles: UserRole) -> Callable:
    def role_checker(
        current_user: User = Depends(get_current_user),
    ) -> User:
        if current_user.role not in allowed_roles:
            raise PermissionDeniedError(
                "You do not have permission to perform this action",
            )

        return current_user

    return role_checker


def x_require_roles__mutmut_1(*allowed_roles: UserRole) -> Callable:
    def role_checker(
        current_user: User = Depends(get_current_user),
    ) -> User:
        if current_user.role in allowed_roles:
            raise PermissionDeniedError(
                "You do not have permission to perform this action",
            )

        return current_user

    return role_checker


def x_require_roles__mutmut_2(*allowed_roles: UserRole) -> Callable:
    def role_checker(
        current_user: User = Depends(get_current_user),
    ) -> User:
        if current_user.role not in allowed_roles:
            raise PermissionDeniedError(
                None,
            )

        return current_user

    return role_checker


def x_require_roles__mutmut_3(*allowed_roles: UserRole) -> Callable:
    def role_checker(
        current_user: User = Depends(get_current_user),
    ) -> User:
        if current_user.role not in allowed_roles:
            raise PermissionDeniedError(
                "XXYou do not have permission to perform this actionXX",
            )

        return current_user

    return role_checker


def x_require_roles__mutmut_4(*allowed_roles: UserRole) -> Callable:
    def role_checker(
        current_user: User = Depends(get_current_user),
    ) -> User:
        if current_user.role not in allowed_roles:
            raise PermissionDeniedError(
                "you do not have permission to perform this action",
            )

        return current_user

    return role_checker


def x_require_roles__mutmut_5(*allowed_roles: UserRole) -> Callable:
    def role_checker(
        current_user: User = Depends(get_current_user),
    ) -> User:
        if current_user.role not in allowed_roles:
            raise PermissionDeniedError(
                "YOU DO NOT HAVE PERMISSION TO PERFORM THIS ACTION",
            )

        return current_user

    return role_checker

mutants_x_require_roles__mutmut['_mutmut_orig'] = x_require_roles__mutmut_orig # type: ignore # mutmut generated
mutants_x_require_roles__mutmut['x_require_roles__mutmut_1'] = x_require_roles__mutmut_1 # type: ignore # mutmut generated
mutants_x_require_roles__mutmut['x_require_roles__mutmut_2'] = x_require_roles__mutmut_2 # type: ignore # mutmut generated
mutants_x_require_roles__mutmut['x_require_roles__mutmut_3'] = x_require_roles__mutmut_3 # type: ignore # mutmut generated
mutants_x_require_roles__mutmut['x_require_roles__mutmut_4'] = x_require_roles__mutmut_4 # type: ignore # mutmut generated
mutants_x_require_roles__mutmut['x_require_roles__mutmut_5'] = x_require_roles__mutmut_5 # type: ignore # mutmut generated