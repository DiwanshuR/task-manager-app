import bcrypt
import hashlib
from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError
from app.config import settings
from typing import Callable

Clock = Callable[[], datetime]
_BCRYPT_SHA256_PREFIX = "bcrypt-sha256-v1$"


def _prehash_password(password: str) -> bytes:
    digest = hashlib.sha256(
        b"task-manager:bcrypt-sha256-v1:" + password.encode("utf-8")
    ).hexdigest()
    return digest.encode("ascii")

def _current_time(now: Clock | None) -> datetime:
    return now() if now is not None else datetime.now(timezone.utc)

def hash_password(plain_password: str) -> str:
    password_bytes = plain_password.encode("utf-8")
    if len(password_bytes) > 72 or b"\x00" in password_bytes:
        hashed_bytes = bcrypt.hashpw(_prehash_password(plain_password), bcrypt.gensalt())
        return _BCRYPT_SHA256_PREFIX + hashed_bytes.decode("utf-8")

    return bcrypt.hashpw(password_bytes, bcrypt.gensalt()).decode("utf-8")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    if not isinstance(plain_password, str) or not isinstance(hashed_password, str):
        return False

    try:
        if hashed_password.startswith(_BCRYPT_SHA256_PREFIX):
            password_bytes = _prehash_password(plain_password)
            hashed_password = hashed_password[len(_BCRYPT_SHA256_PREFIX) :]
        else:
            password_bytes = plain_password.encode("utf-8")

        return bcrypt.checkpw(
            password_bytes,
            hashed_password.encode("utf-8"),
        )
    except (ValueError, TypeError):
        # A malformed/corrupted hash should fail authentication, not crash.
        return False


def create_access_token(data: dict, now: Clock | None = None) -> str:
    payload = data.copy()
    payload["type"] = "access"
    payload["exp"] = _current_time(now) + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    return jwt.encode(
        payload,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )

def create_refresh_token(data: dict, now: Clock | None = None) -> str:
    payload = data.copy()
    payload["type"] = "refresh"
    payload["exp"] = _current_time(now) + timedelta(
        days=settings.REFRESH_TOKEN_EXPIRE_DAYS
    )

    return jwt.encode(
        payload,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM,
    )


def _decode_token(
    token: str,
    expected_type: str,
    now: Clock | None = None,
) -> dict | None:
    try:
        # Verify the signature and algorithm, but check exp ourselves below
        # so the test can supply a controlled clock.
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM],
            options={"verify_exp": False},
        )

        if payload.get("type") != expected_type:
            return None

        exp = payload.get("exp")
        if isinstance(exp, bool) or not isinstance(exp, (int, float)):
            return None

        if _current_time(now).timestamp() >= exp:
            return None

        return payload
    except (JWTError, ValueError, TypeError, OverflowError):
        # Malformed or invalid tokens should fail closed, not leak parsing errors.
        return None


def decode_access_token(token: str, now: Clock | None = None) -> dict | None:
    return _decode_token(token, "access", now)


def decode_refresh_token(token: str, now: Clock | None = None) -> dict | None:
    return _decode_token(token, "refresh", now)
