import bcrypt
import hashlib
from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError
from app.config import settings
from typing import Callable

Clock = Callable[[], datetime]
_BCRYPT_SHA256_PREFIX = "bcrypt-sha256-v1$"


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x__prehash_password__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__prehash_password__mutmut)
def _prehash_password(password: str) -> bytes:
    digest = hashlib.sha256(
        b"task-manager:bcrypt-sha256-v1:" + password.encode("utf-8")
    ).hexdigest()
    return digest.encode("ascii")


def x__prehash_password__mutmut_orig(password: str) -> bytes:
    digest = hashlib.sha256(
        b"task-manager:bcrypt-sha256-v1:" + password.encode("utf-8")
    ).hexdigest()
    return digest.encode("ascii")


def x__prehash_password__mutmut_1(password: str) -> bytes:
    digest = None
    return digest.encode("ascii")


def x__prehash_password__mutmut_2(password: str) -> bytes:
    digest = hashlib.sha256(
        None
    ).hexdigest()
    return digest.encode("ascii")


def x__prehash_password__mutmut_3(password: str) -> bytes:
    digest = hashlib.sha256(
        b"task-manager:bcrypt-sha256-v1:" - password.encode("utf-8")
    ).hexdigest()
    return digest.encode("ascii")


def x__prehash_password__mutmut_4(password: str) -> bytes:
    digest = hashlib.sha256(
        b"XXtask-manager:bcrypt-sha256-v1:XX" + password.encode("utf-8")
    ).hexdigest()
    return digest.encode("ascii")


def x__prehash_password__mutmut_5(password: str) -> bytes:
    digest = hashlib.sha256(
        b"TASK-MANAGER:BCRYPT-SHA256-V1:" + password.encode("utf-8")
    ).hexdigest()
    return digest.encode("ascii")


def x__prehash_password__mutmut_6(password: str) -> bytes:
    digest = hashlib.sha256(
        b"task-manager:bcrypt-sha256-v1:" + password.encode(None)
    ).hexdigest()
    return digest.encode("ascii")


def x__prehash_password__mutmut_7(password: str) -> bytes:
    digest = hashlib.sha256(
        b"task-manager:bcrypt-sha256-v1:" + password.encode("XXutf-8XX")
    ).hexdigest()
    return digest.encode("ascii")


def x__prehash_password__mutmut_8(password: str) -> bytes:
    digest = hashlib.sha256(
        b"task-manager:bcrypt-sha256-v1:" + password.encode("UTF-8")
    ).hexdigest()
    return digest.encode("ascii")


def x__prehash_password__mutmut_9(password: str) -> bytes:
    digest = hashlib.sha256(
        b"task-manager:bcrypt-sha256-v1:" + password.encode("utf-8")
    ).hexdigest()
    return digest.encode(None)


def x__prehash_password__mutmut_10(password: str) -> bytes:
    digest = hashlib.sha256(
        b"task-manager:bcrypt-sha256-v1:" + password.encode("utf-8")
    ).hexdigest()
    return digest.encode("XXasciiXX")


def x__prehash_password__mutmut_11(password: str) -> bytes:
    digest = hashlib.sha256(
        b"task-manager:bcrypt-sha256-v1:" + password.encode("utf-8")
    ).hexdigest()
    return digest.encode("ASCII")

mutants_x__prehash_password__mutmut['_mutmut_orig'] = x__prehash_password__mutmut_orig # type: ignore # mutmut generated
mutants_x__prehash_password__mutmut['x__prehash_password__mutmut_1'] = x__prehash_password__mutmut_1 # type: ignore # mutmut generated
mutants_x__prehash_password__mutmut['x__prehash_password__mutmut_2'] = x__prehash_password__mutmut_2 # type: ignore # mutmut generated
mutants_x__prehash_password__mutmut['x__prehash_password__mutmut_3'] = x__prehash_password__mutmut_3 # type: ignore # mutmut generated
mutants_x__prehash_password__mutmut['x__prehash_password__mutmut_4'] = x__prehash_password__mutmut_4 # type: ignore # mutmut generated
mutants_x__prehash_password__mutmut['x__prehash_password__mutmut_5'] = x__prehash_password__mutmut_5 # type: ignore # mutmut generated
mutants_x__prehash_password__mutmut['x__prehash_password__mutmut_6'] = x__prehash_password__mutmut_6 # type: ignore # mutmut generated
mutants_x__prehash_password__mutmut['x__prehash_password__mutmut_7'] = x__prehash_password__mutmut_7 # type: ignore # mutmut generated
mutants_x__prehash_password__mutmut['x__prehash_password__mutmut_8'] = x__prehash_password__mutmut_8 # type: ignore # mutmut generated
mutants_x__prehash_password__mutmut['x__prehash_password__mutmut_9'] = x__prehash_password__mutmut_9 # type: ignore # mutmut generated
mutants_x__prehash_password__mutmut['x__prehash_password__mutmut_10'] = x__prehash_password__mutmut_10 # type: ignore # mutmut generated
mutants_x__prehash_password__mutmut['x__prehash_password__mutmut_11'] = x__prehash_password__mutmut_11 # type: ignore # mutmut generated
mutants_x__current_time__mutmut: MutantDict = {}  # type: ignore

@_mutmut_mutated(mutants_x__current_time__mutmut)
def _current_time(now: Clock | None) -> datetime:
    return now() if now is not None else datetime.now(timezone.utc)

def x__current_time__mutmut_orig(now: Clock | None) -> datetime:
    return now() if now is not None else datetime.now(timezone.utc)

def x__current_time__mutmut_1(now: Clock | None) -> datetime:
    return now() if (now is not None) and False else datetime.now(timezone.utc)

def x__current_time__mutmut_2(now: Clock | None) -> datetime:
    return now() if (now is not None) or True else datetime.now(timezone.utc)

def x__current_time__mutmut_3(now: Clock | None) -> datetime:
    return now() if now is None else datetime.now(timezone.utc)

def x__current_time__mutmut_4(now: Clock | None) -> datetime:
    return now() if now is not None else datetime.now(None)

mutants_x__current_time__mutmut['_mutmut_orig'] = x__current_time__mutmut_orig # type: ignore # mutmut generated
mutants_x__current_time__mutmut['x__current_time__mutmut_1'] = x__current_time__mutmut_1 # type: ignore # mutmut generated
mutants_x__current_time__mutmut['x__current_time__mutmut_2'] = x__current_time__mutmut_2 # type: ignore # mutmut generated
mutants_x__current_time__mutmut['x__current_time__mutmut_3'] = x__current_time__mutmut_3 # type: ignore # mutmut generated
mutants_x__current_time__mutmut['x__current_time__mutmut_4'] = x__current_time__mutmut_4 # type: ignore # mutmut generated
mutants_x_hash_password__mutmut: MutantDict = {}  # type: ignore

@_mutmut_mutated(mutants_x_hash_password__mutmut)
def hash_password(plain_password: str) -> str:
    password_bytes = plain_password.encode("utf-8")
    if len(password_bytes) > 72 or b"\x00" in password_bytes:
        hashed_bytes = bcrypt.hashpw(_prehash_password(plain_password), bcrypt.gensalt())
        return _BCRYPT_SHA256_PREFIX + hashed_bytes.decode("utf-8")

    return bcrypt.hashpw(password_bytes, bcrypt.gensalt()).decode("utf-8")

def x_hash_password__mutmut_orig(plain_password: str) -> str:
    password_bytes = plain_password.encode("utf-8")
    if len(password_bytes) > 72 or b"\x00" in password_bytes:
        hashed_bytes = bcrypt.hashpw(_prehash_password(plain_password), bcrypt.gensalt())
        return _BCRYPT_SHA256_PREFIX + hashed_bytes.decode("utf-8")

    return bcrypt.hashpw(password_bytes, bcrypt.gensalt()).decode("utf-8")

def x_hash_password__mutmut_1(plain_password: str) -> str:
    password_bytes = None
    if len(password_bytes) > 72 or b"\x00" in password_bytes:
        hashed_bytes = bcrypt.hashpw(_prehash_password(plain_password), bcrypt.gensalt())
        return _BCRYPT_SHA256_PREFIX + hashed_bytes.decode("utf-8")

    return bcrypt.hashpw(password_bytes, bcrypt.gensalt()).decode("utf-8")

def x_hash_password__mutmut_2(plain_password: str) -> str:
    password_bytes = plain_password.encode(None)
    if len(password_bytes) > 72 or b"\x00" in password_bytes:
        hashed_bytes = bcrypt.hashpw(_prehash_password(plain_password), bcrypt.gensalt())
        return _BCRYPT_SHA256_PREFIX + hashed_bytes.decode("utf-8")

    return bcrypt.hashpw(password_bytes, bcrypt.gensalt()).decode("utf-8")

def x_hash_password__mutmut_3(plain_password: str) -> str:
    password_bytes = plain_password.encode("XXutf-8XX")
    if len(password_bytes) > 72 or b"\x00" in password_bytes:
        hashed_bytes = bcrypt.hashpw(_prehash_password(plain_password), bcrypt.gensalt())
        return _BCRYPT_SHA256_PREFIX + hashed_bytes.decode("utf-8")

    return bcrypt.hashpw(password_bytes, bcrypt.gensalt()).decode("utf-8")

def x_hash_password__mutmut_4(plain_password: str) -> str:
    password_bytes = plain_password.encode("UTF-8")
    if len(password_bytes) > 72 or b"\x00" in password_bytes:
        hashed_bytes = bcrypt.hashpw(_prehash_password(plain_password), bcrypt.gensalt())
        return _BCRYPT_SHA256_PREFIX + hashed_bytes.decode("utf-8")

    return bcrypt.hashpw(password_bytes, bcrypt.gensalt()).decode("utf-8")

def x_hash_password__mutmut_5(plain_password: str) -> str:
    password_bytes = plain_password.encode("utf-8")
    if len(password_bytes) > 72 and b"\x00" in password_bytes:
        hashed_bytes = bcrypt.hashpw(_prehash_password(plain_password), bcrypt.gensalt())
        return _BCRYPT_SHA256_PREFIX + hashed_bytes.decode("utf-8")

    return bcrypt.hashpw(password_bytes, bcrypt.gensalt()).decode("utf-8")

def x_hash_password__mutmut_6(plain_password: str) -> str:
    password_bytes = plain_password.encode("utf-8")
    if len(password_bytes) >= 72 or b"\x00" in password_bytes:
        hashed_bytes = bcrypt.hashpw(_prehash_password(plain_password), bcrypt.gensalt())
        return _BCRYPT_SHA256_PREFIX + hashed_bytes.decode("utf-8")

    return bcrypt.hashpw(password_bytes, bcrypt.gensalt()).decode("utf-8")

def x_hash_password__mutmut_7(plain_password: str) -> str:
    password_bytes = plain_password.encode("utf-8")
    if len(password_bytes) > 73 or b"\x00" in password_bytes:
        hashed_bytes = bcrypt.hashpw(_prehash_password(plain_password), bcrypt.gensalt())
        return _BCRYPT_SHA256_PREFIX + hashed_bytes.decode("utf-8")

    return bcrypt.hashpw(password_bytes, bcrypt.gensalt()).decode("utf-8")

def x_hash_password__mutmut_8(plain_password: str) -> str:
    password_bytes = plain_password.encode("utf-8")
    if len(password_bytes) > 72 or b"XX\x00XX" in password_bytes:
        hashed_bytes = bcrypt.hashpw(_prehash_password(plain_password), bcrypt.gensalt())
        return _BCRYPT_SHA256_PREFIX + hashed_bytes.decode("utf-8")

    return bcrypt.hashpw(password_bytes, bcrypt.gensalt()).decode("utf-8")

def x_hash_password__mutmut_9(plain_password: str) -> str:
    password_bytes = plain_password.encode("utf-8")
    if len(password_bytes) > 72 or b"\x00" not in password_bytes:
        hashed_bytes = bcrypt.hashpw(_prehash_password(plain_password), bcrypt.gensalt())
        return _BCRYPT_SHA256_PREFIX + hashed_bytes.decode("utf-8")

    return bcrypt.hashpw(password_bytes, bcrypt.gensalt()).decode("utf-8")

def x_hash_password__mutmut_10(plain_password: str) -> str:
    password_bytes = plain_password.encode("utf-8")
    if len(password_bytes) > 72 or b"\x00" in password_bytes:
        hashed_bytes = None
        return _BCRYPT_SHA256_PREFIX + hashed_bytes.decode("utf-8")

    return bcrypt.hashpw(password_bytes, bcrypt.gensalt()).decode("utf-8")

def x_hash_password__mutmut_11(plain_password: str) -> str:
    password_bytes = plain_password.encode("utf-8")
    if len(password_bytes) > 72 or b"\x00" in password_bytes:
        hashed_bytes = bcrypt.hashpw(None, bcrypt.gensalt())
        return _BCRYPT_SHA256_PREFIX + hashed_bytes.decode("utf-8")

    return bcrypt.hashpw(password_bytes, bcrypt.gensalt()).decode("utf-8")

def x_hash_password__mutmut_12(plain_password: str) -> str:
    password_bytes = plain_password.encode("utf-8")
    if len(password_bytes) > 72 or b"\x00" in password_bytes:
        hashed_bytes = bcrypt.hashpw(_prehash_password(plain_password), None)
        return _BCRYPT_SHA256_PREFIX + hashed_bytes.decode("utf-8")

    return bcrypt.hashpw(password_bytes, bcrypt.gensalt()).decode("utf-8")

def x_hash_password__mutmut_13(plain_password: str) -> str:
    password_bytes = plain_password.encode("utf-8")
    if len(password_bytes) > 72 or b"\x00" in password_bytes:
        hashed_bytes = bcrypt.hashpw(bcrypt.gensalt())
        return _BCRYPT_SHA256_PREFIX + hashed_bytes.decode("utf-8")

    return bcrypt.hashpw(password_bytes, bcrypt.gensalt()).decode("utf-8")

def x_hash_password__mutmut_14(plain_password: str) -> str:
    password_bytes = plain_password.encode("utf-8")
    if len(password_bytes) > 72 or b"\x00" in password_bytes:
        hashed_bytes = bcrypt.hashpw(_prehash_password(plain_password), )
        return _BCRYPT_SHA256_PREFIX + hashed_bytes.decode("utf-8")

    return bcrypt.hashpw(password_bytes, bcrypt.gensalt()).decode("utf-8")

def x_hash_password__mutmut_15(plain_password: str) -> str:
    password_bytes = plain_password.encode("utf-8")
    if len(password_bytes) > 72 or b"\x00" in password_bytes:
        hashed_bytes = bcrypt.hashpw(_prehash_password(None), bcrypt.gensalt())
        return _BCRYPT_SHA256_PREFIX + hashed_bytes.decode("utf-8")

    return bcrypt.hashpw(password_bytes, bcrypt.gensalt()).decode("utf-8")

def x_hash_password__mutmut_16(plain_password: str) -> str:
    password_bytes = plain_password.encode("utf-8")
    if len(password_bytes) > 72 or b"\x00" in password_bytes:
        hashed_bytes = bcrypt.hashpw(_prehash_password(plain_password), bcrypt.gensalt())
        return _BCRYPT_SHA256_PREFIX - hashed_bytes.decode("utf-8")

    return bcrypt.hashpw(password_bytes, bcrypt.gensalt()).decode("utf-8")

def x_hash_password__mutmut_17(plain_password: str) -> str:
    password_bytes = plain_password.encode("utf-8")
    if len(password_bytes) > 72 or b"\x00" in password_bytes:
        hashed_bytes = bcrypt.hashpw(_prehash_password(plain_password), bcrypt.gensalt())
        return _BCRYPT_SHA256_PREFIX + hashed_bytes.decode(None)

    return bcrypt.hashpw(password_bytes, bcrypt.gensalt()).decode("utf-8")

def x_hash_password__mutmut_18(plain_password: str) -> str:
    password_bytes = plain_password.encode("utf-8")
    if len(password_bytes) > 72 or b"\x00" in password_bytes:
        hashed_bytes = bcrypt.hashpw(_prehash_password(plain_password), bcrypt.gensalt())
        return _BCRYPT_SHA256_PREFIX + hashed_bytes.decode("XXutf-8XX")

    return bcrypt.hashpw(password_bytes, bcrypt.gensalt()).decode("utf-8")

def x_hash_password__mutmut_19(plain_password: str) -> str:
    password_bytes = plain_password.encode("utf-8")
    if len(password_bytes) > 72 or b"\x00" in password_bytes:
        hashed_bytes = bcrypt.hashpw(_prehash_password(plain_password), bcrypt.gensalt())
        return _BCRYPT_SHA256_PREFIX + hashed_bytes.decode("UTF-8")

    return bcrypt.hashpw(password_bytes, bcrypt.gensalt()).decode("utf-8")

def x_hash_password__mutmut_20(plain_password: str) -> str:
    password_bytes = plain_password.encode("utf-8")
    if len(password_bytes) > 72 or b"\x00" in password_bytes:
        hashed_bytes = bcrypt.hashpw(_prehash_password(plain_password), bcrypt.gensalt())
        return _BCRYPT_SHA256_PREFIX + hashed_bytes.decode("utf-8")

    return bcrypt.hashpw(password_bytes, bcrypt.gensalt()).decode(None)

def x_hash_password__mutmut_21(plain_password: str) -> str:
    password_bytes = plain_password.encode("utf-8")
    if len(password_bytes) > 72 or b"\x00" in password_bytes:
        hashed_bytes = bcrypt.hashpw(_prehash_password(plain_password), bcrypt.gensalt())
        return _BCRYPT_SHA256_PREFIX + hashed_bytes.decode("utf-8")

    return bcrypt.hashpw(None, bcrypt.gensalt()).decode("utf-8")

def x_hash_password__mutmut_22(plain_password: str) -> str:
    password_bytes = plain_password.encode("utf-8")
    if len(password_bytes) > 72 or b"\x00" in password_bytes:
        hashed_bytes = bcrypt.hashpw(_prehash_password(plain_password), bcrypt.gensalt())
        return _BCRYPT_SHA256_PREFIX + hashed_bytes.decode("utf-8")

    return bcrypt.hashpw(password_bytes, None).decode("utf-8")

def x_hash_password__mutmut_23(plain_password: str) -> str:
    password_bytes = plain_password.encode("utf-8")
    if len(password_bytes) > 72 or b"\x00" in password_bytes:
        hashed_bytes = bcrypt.hashpw(_prehash_password(plain_password), bcrypt.gensalt())
        return _BCRYPT_SHA256_PREFIX + hashed_bytes.decode("utf-8")

    return bcrypt.hashpw(bcrypt.gensalt()).decode("utf-8")

def x_hash_password__mutmut_24(plain_password: str) -> str:
    password_bytes = plain_password.encode("utf-8")
    if len(password_bytes) > 72 or b"\x00" in password_bytes:
        hashed_bytes = bcrypt.hashpw(_prehash_password(plain_password), bcrypt.gensalt())
        return _BCRYPT_SHA256_PREFIX + hashed_bytes.decode("utf-8")

    return bcrypt.hashpw(password_bytes, ).decode("utf-8")

def x_hash_password__mutmut_25(plain_password: str) -> str:
    password_bytes = plain_password.encode("utf-8")
    if len(password_bytes) > 72 or b"\x00" in password_bytes:
        hashed_bytes = bcrypt.hashpw(_prehash_password(plain_password), bcrypt.gensalt())
        return _BCRYPT_SHA256_PREFIX + hashed_bytes.decode("utf-8")

    return bcrypt.hashpw(password_bytes, bcrypt.gensalt()).decode("XXutf-8XX")

def x_hash_password__mutmut_26(plain_password: str) -> str:
    password_bytes = plain_password.encode("utf-8")
    if len(password_bytes) > 72 or b"\x00" in password_bytes:
        hashed_bytes = bcrypt.hashpw(_prehash_password(plain_password), bcrypt.gensalt())
        return _BCRYPT_SHA256_PREFIX + hashed_bytes.decode("utf-8")

    return bcrypt.hashpw(password_bytes, bcrypt.gensalt()).decode("UTF-8")

mutants_x_hash_password__mutmut['_mutmut_orig'] = x_hash_password__mutmut_orig # type: ignore # mutmut generated
mutants_x_hash_password__mutmut['x_hash_password__mutmut_1'] = x_hash_password__mutmut_1 # type: ignore # mutmut generated
mutants_x_hash_password__mutmut['x_hash_password__mutmut_2'] = x_hash_password__mutmut_2 # type: ignore # mutmut generated
mutants_x_hash_password__mutmut['x_hash_password__mutmut_3'] = x_hash_password__mutmut_3 # type: ignore # mutmut generated
mutants_x_hash_password__mutmut['x_hash_password__mutmut_4'] = x_hash_password__mutmut_4 # type: ignore # mutmut generated
mutants_x_hash_password__mutmut['x_hash_password__mutmut_5'] = x_hash_password__mutmut_5 # type: ignore # mutmut generated
mutants_x_hash_password__mutmut['x_hash_password__mutmut_6'] = x_hash_password__mutmut_6 # type: ignore # mutmut generated
mutants_x_hash_password__mutmut['x_hash_password__mutmut_7'] = x_hash_password__mutmut_7 # type: ignore # mutmut generated
mutants_x_hash_password__mutmut['x_hash_password__mutmut_8'] = x_hash_password__mutmut_8 # type: ignore # mutmut generated
mutants_x_hash_password__mutmut['x_hash_password__mutmut_9'] = x_hash_password__mutmut_9 # type: ignore # mutmut generated
mutants_x_hash_password__mutmut['x_hash_password__mutmut_10'] = x_hash_password__mutmut_10 # type: ignore # mutmut generated
mutants_x_hash_password__mutmut['x_hash_password__mutmut_11'] = x_hash_password__mutmut_11 # type: ignore # mutmut generated
mutants_x_hash_password__mutmut['x_hash_password__mutmut_12'] = x_hash_password__mutmut_12 # type: ignore # mutmut generated
mutants_x_hash_password__mutmut['x_hash_password__mutmut_13'] = x_hash_password__mutmut_13 # type: ignore # mutmut generated
mutants_x_hash_password__mutmut['x_hash_password__mutmut_14'] = x_hash_password__mutmut_14 # type: ignore # mutmut generated
mutants_x_hash_password__mutmut['x_hash_password__mutmut_15'] = x_hash_password__mutmut_15 # type: ignore # mutmut generated
mutants_x_hash_password__mutmut['x_hash_password__mutmut_16'] = x_hash_password__mutmut_16 # type: ignore # mutmut generated
mutants_x_hash_password__mutmut['x_hash_password__mutmut_17'] = x_hash_password__mutmut_17 # type: ignore # mutmut generated
mutants_x_hash_password__mutmut['x_hash_password__mutmut_18'] = x_hash_password__mutmut_18 # type: ignore # mutmut generated
mutants_x_hash_password__mutmut['x_hash_password__mutmut_19'] = x_hash_password__mutmut_19 # type: ignore # mutmut generated
mutants_x_hash_password__mutmut['x_hash_password__mutmut_20'] = x_hash_password__mutmut_20 # type: ignore # mutmut generated
mutants_x_hash_password__mutmut['x_hash_password__mutmut_21'] = x_hash_password__mutmut_21 # type: ignore # mutmut generated
mutants_x_hash_password__mutmut['x_hash_password__mutmut_22'] = x_hash_password__mutmut_22 # type: ignore # mutmut generated
mutants_x_hash_password__mutmut['x_hash_password__mutmut_23'] = x_hash_password__mutmut_23 # type: ignore # mutmut generated
mutants_x_hash_password__mutmut['x_hash_password__mutmut_24'] = x_hash_password__mutmut_24 # type: ignore # mutmut generated
mutants_x_hash_password__mutmut['x_hash_password__mutmut_25'] = x_hash_password__mutmut_25 # type: ignore # mutmut generated
mutants_x_hash_password__mutmut['x_hash_password__mutmut_26'] = x_hash_password__mutmut_26 # type: ignore # mutmut generated
mutants_x_verify_password__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_verify_password__mutmut)
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


def x_verify_password__mutmut_orig(plain_password: str, hashed_password: str) -> bool:
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


def x_verify_password__mutmut_1(plain_password: str, hashed_password: str) -> bool:
    if not isinstance(plain_password, str) and not isinstance(hashed_password, str):
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


def x_verify_password__mutmut_2(plain_password: str, hashed_password: str) -> bool:
    if isinstance(plain_password, str) or not isinstance(hashed_password, str):
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


def x_verify_password__mutmut_3(plain_password: str, hashed_password: str) -> bool:
    if not isinstance(plain_password, str) or isinstance(hashed_password, str):
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


def x_verify_password__mutmut_4(plain_password: str, hashed_password: str) -> bool:
    if not isinstance(plain_password, str) or not isinstance(hashed_password, str):
        return True

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


def x_verify_password__mutmut_5(plain_password: str, hashed_password: str) -> bool:
    if not isinstance(plain_password, str) or not isinstance(hashed_password, str):
        return False

    try:
        if hashed_password.startswith(None):
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


def x_verify_password__mutmut_6(plain_password: str, hashed_password: str) -> bool:
    if not isinstance(plain_password, str) or not isinstance(hashed_password, str):
        return False

    try:
        if hashed_password.startswith(_BCRYPT_SHA256_PREFIX):
            password_bytes = None
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


def x_verify_password__mutmut_7(plain_password: str, hashed_password: str) -> bool:
    if not isinstance(plain_password, str) or not isinstance(hashed_password, str):
        return False

    try:
        if hashed_password.startswith(_BCRYPT_SHA256_PREFIX):
            password_bytes = _prehash_password(None)
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


def x_verify_password__mutmut_8(plain_password: str, hashed_password: str) -> bool:
    if not isinstance(plain_password, str) or not isinstance(hashed_password, str):
        return False

    try:
        if hashed_password.startswith(_BCRYPT_SHA256_PREFIX):
            password_bytes = _prehash_password(plain_password)
            hashed_password = None
        else:
            password_bytes = plain_password.encode("utf-8")

        return bcrypt.checkpw(
            password_bytes,
            hashed_password.encode("utf-8"),
        )
    except (ValueError, TypeError):
        # A malformed/corrupted hash should fail authentication, not crash.
        return False


def x_verify_password__mutmut_9(plain_password: str, hashed_password: str) -> bool:
    if not isinstance(plain_password, str) or not isinstance(hashed_password, str):
        return False

    try:
        if hashed_password.startswith(_BCRYPT_SHA256_PREFIX):
            password_bytes = _prehash_password(plain_password)
            hashed_password = hashed_password[len(_BCRYPT_SHA256_PREFIX) :]
        else:
            password_bytes = None

        return bcrypt.checkpw(
            password_bytes,
            hashed_password.encode("utf-8"),
        )
    except (ValueError, TypeError):
        # A malformed/corrupted hash should fail authentication, not crash.
        return False


def x_verify_password__mutmut_10(plain_password: str, hashed_password: str) -> bool:
    if not isinstance(plain_password, str) or not isinstance(hashed_password, str):
        return False

    try:
        if hashed_password.startswith(_BCRYPT_SHA256_PREFIX):
            password_bytes = _prehash_password(plain_password)
            hashed_password = hashed_password[len(_BCRYPT_SHA256_PREFIX) :]
        else:
            password_bytes = plain_password.encode(None)

        return bcrypt.checkpw(
            password_bytes,
            hashed_password.encode("utf-8"),
        )
    except (ValueError, TypeError):
        # A malformed/corrupted hash should fail authentication, not crash.
        return False


def x_verify_password__mutmut_11(plain_password: str, hashed_password: str) -> bool:
    if not isinstance(plain_password, str) or not isinstance(hashed_password, str):
        return False

    try:
        if hashed_password.startswith(_BCRYPT_SHA256_PREFIX):
            password_bytes = _prehash_password(plain_password)
            hashed_password = hashed_password[len(_BCRYPT_SHA256_PREFIX) :]
        else:
            password_bytes = plain_password.encode("XXutf-8XX")

        return bcrypt.checkpw(
            password_bytes,
            hashed_password.encode("utf-8"),
        )
    except (ValueError, TypeError):
        # A malformed/corrupted hash should fail authentication, not crash.
        return False


def x_verify_password__mutmut_12(plain_password: str, hashed_password: str) -> bool:
    if not isinstance(plain_password, str) or not isinstance(hashed_password, str):
        return False

    try:
        if hashed_password.startswith(_BCRYPT_SHA256_PREFIX):
            password_bytes = _prehash_password(plain_password)
            hashed_password = hashed_password[len(_BCRYPT_SHA256_PREFIX) :]
        else:
            password_bytes = plain_password.encode("UTF-8")

        return bcrypt.checkpw(
            password_bytes,
            hashed_password.encode("utf-8"),
        )
    except (ValueError, TypeError):
        # A malformed/corrupted hash should fail authentication, not crash.
        return False


def x_verify_password__mutmut_13(plain_password: str, hashed_password: str) -> bool:
    if not isinstance(plain_password, str) or not isinstance(hashed_password, str):
        return False

    try:
        if hashed_password.startswith(_BCRYPT_SHA256_PREFIX):
            password_bytes = _prehash_password(plain_password)
            hashed_password = hashed_password[len(_BCRYPT_SHA256_PREFIX) :]
        else:
            password_bytes = plain_password.encode("utf-8")

        return bcrypt.checkpw(
            None,
            hashed_password.encode("utf-8"),
        )
    except (ValueError, TypeError):
        # A malformed/corrupted hash should fail authentication, not crash.
        return False


def x_verify_password__mutmut_14(plain_password: str, hashed_password: str) -> bool:
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
            None,
        )
    except (ValueError, TypeError):
        # A malformed/corrupted hash should fail authentication, not crash.
        return False


def x_verify_password__mutmut_15(plain_password: str, hashed_password: str) -> bool:
    if not isinstance(plain_password, str) or not isinstance(hashed_password, str):
        return False

    try:
        if hashed_password.startswith(_BCRYPT_SHA256_PREFIX):
            password_bytes = _prehash_password(plain_password)
            hashed_password = hashed_password[len(_BCRYPT_SHA256_PREFIX) :]
        else:
            password_bytes = plain_password.encode("utf-8")

        return bcrypt.checkpw(
            hashed_password.encode("utf-8"),
        )
    except (ValueError, TypeError):
        # A malformed/corrupted hash should fail authentication, not crash.
        return False


def x_verify_password__mutmut_16(plain_password: str, hashed_password: str) -> bool:
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
            )
    except (ValueError, TypeError):
        # A malformed/corrupted hash should fail authentication, not crash.
        return False


def x_verify_password__mutmut_17(plain_password: str, hashed_password: str) -> bool:
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
            hashed_password.encode(None),
        )
    except (ValueError, TypeError):
        # A malformed/corrupted hash should fail authentication, not crash.
        return False


def x_verify_password__mutmut_18(plain_password: str, hashed_password: str) -> bool:
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
            hashed_password.encode("XXutf-8XX"),
        )
    except (ValueError, TypeError):
        # A malformed/corrupted hash should fail authentication, not crash.
        return False


def x_verify_password__mutmut_19(plain_password: str, hashed_password: str) -> bool:
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
            hashed_password.encode("UTF-8"),
        )
    except (ValueError, TypeError):
        # A malformed/corrupted hash should fail authentication, not crash.
        return False


def x_verify_password__mutmut_20(plain_password: str, hashed_password: str) -> bool:
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
        return True

mutants_x_verify_password__mutmut['_mutmut_orig'] = x_verify_password__mutmut_orig # type: ignore # mutmut generated
mutants_x_verify_password__mutmut['x_verify_password__mutmut_1'] = x_verify_password__mutmut_1 # type: ignore # mutmut generated
mutants_x_verify_password__mutmut['x_verify_password__mutmut_2'] = x_verify_password__mutmut_2 # type: ignore # mutmut generated
mutants_x_verify_password__mutmut['x_verify_password__mutmut_3'] = x_verify_password__mutmut_3 # type: ignore # mutmut generated
mutants_x_verify_password__mutmut['x_verify_password__mutmut_4'] = x_verify_password__mutmut_4 # type: ignore # mutmut generated
mutants_x_verify_password__mutmut['x_verify_password__mutmut_5'] = x_verify_password__mutmut_5 # type: ignore # mutmut generated
mutants_x_verify_password__mutmut['x_verify_password__mutmut_6'] = x_verify_password__mutmut_6 # type: ignore # mutmut generated
mutants_x_verify_password__mutmut['x_verify_password__mutmut_7'] = x_verify_password__mutmut_7 # type: ignore # mutmut generated
mutants_x_verify_password__mutmut['x_verify_password__mutmut_8'] = x_verify_password__mutmut_8 # type: ignore # mutmut generated
mutants_x_verify_password__mutmut['x_verify_password__mutmut_9'] = x_verify_password__mutmut_9 # type: ignore # mutmut generated
mutants_x_verify_password__mutmut['x_verify_password__mutmut_10'] = x_verify_password__mutmut_10 # type: ignore # mutmut generated
mutants_x_verify_password__mutmut['x_verify_password__mutmut_11'] = x_verify_password__mutmut_11 # type: ignore # mutmut generated
mutants_x_verify_password__mutmut['x_verify_password__mutmut_12'] = x_verify_password__mutmut_12 # type: ignore # mutmut generated
mutants_x_verify_password__mutmut['x_verify_password__mutmut_13'] = x_verify_password__mutmut_13 # type: ignore # mutmut generated
mutants_x_verify_password__mutmut['x_verify_password__mutmut_14'] = x_verify_password__mutmut_14 # type: ignore # mutmut generated
mutants_x_verify_password__mutmut['x_verify_password__mutmut_15'] = x_verify_password__mutmut_15 # type: ignore # mutmut generated
mutants_x_verify_password__mutmut['x_verify_password__mutmut_16'] = x_verify_password__mutmut_16 # type: ignore # mutmut generated
mutants_x_verify_password__mutmut['x_verify_password__mutmut_17'] = x_verify_password__mutmut_17 # type: ignore # mutmut generated
mutants_x_verify_password__mutmut['x_verify_password__mutmut_18'] = x_verify_password__mutmut_18 # type: ignore # mutmut generated
mutants_x_verify_password__mutmut['x_verify_password__mutmut_19'] = x_verify_password__mutmut_19 # type: ignore # mutmut generated
mutants_x_verify_password__mutmut['x_verify_password__mutmut_20'] = x_verify_password__mutmut_20 # type: ignore # mutmut generated
mutants_x_create_access_token__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_create_access_token__mutmut)
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


def x_create_access_token__mutmut_orig(data: dict, now: Clock | None = None) -> str:
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


def x_create_access_token__mutmut_1(data: dict, now: Clock | None = None) -> str:
    payload = None
    payload["type"] = "access"
    payload["exp"] = _current_time(now) + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    return jwt.encode(
        payload,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )


def x_create_access_token__mutmut_2(data: dict, now: Clock | None = None) -> str:
    payload = data.copy()
    payload["type"] = None
    payload["exp"] = _current_time(now) + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    return jwt.encode(
        payload,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )


def x_create_access_token__mutmut_3(data: dict, now: Clock | None = None) -> str:
    payload = data.copy()
    payload["XXtypeXX"] = "access"
    payload["exp"] = _current_time(now) + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    return jwt.encode(
        payload,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )


def x_create_access_token__mutmut_4(data: dict, now: Clock | None = None) -> str:
    payload = data.copy()
    payload["TYPE"] = "access"
    payload["exp"] = _current_time(now) + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    return jwt.encode(
        payload,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )


def x_create_access_token__mutmut_5(data: dict, now: Clock | None = None) -> str:
    payload = data.copy()
    payload["type"] = "XXaccessXX"
    payload["exp"] = _current_time(now) + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    return jwt.encode(
        payload,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )


def x_create_access_token__mutmut_6(data: dict, now: Clock | None = None) -> str:
    payload = data.copy()
    payload["type"] = "ACCESS"
    payload["exp"] = _current_time(now) + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    return jwt.encode(
        payload,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )


def x_create_access_token__mutmut_7(data: dict, now: Clock | None = None) -> str:
    payload = data.copy()
    payload["type"] = "access"
    payload["exp"] = None
    return jwt.encode(
        payload,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )


def x_create_access_token__mutmut_8(data: dict, now: Clock | None = None) -> str:
    payload = data.copy()
    payload["type"] = "access"
    payload["XXexpXX"] = _current_time(now) + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    return jwt.encode(
        payload,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )


def x_create_access_token__mutmut_9(data: dict, now: Clock | None = None) -> str:
    payload = data.copy()
    payload["type"] = "access"
    payload["EXP"] = _current_time(now) + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    return jwt.encode(
        payload,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )


def x_create_access_token__mutmut_10(data: dict, now: Clock | None = None) -> str:
    payload = data.copy()
    payload["type"] = "access"
    payload["exp"] = _current_time(now) - timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    return jwt.encode(
        payload,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )


def x_create_access_token__mutmut_11(data: dict, now: Clock | None = None) -> str:
    payload = data.copy()
    payload["type"] = "access"
    payload["exp"] = _current_time(None) + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    return jwt.encode(
        payload,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )


def x_create_access_token__mutmut_12(data: dict, now: Clock | None = None) -> str:
    payload = data.copy()
    payload["type"] = "access"
    payload["exp"] = _current_time(now) + timedelta(
        minutes=None
    )
    return jwt.encode(
        payload,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )


def x_create_access_token__mutmut_13(data: dict, now: Clock | None = None) -> str:
    payload = data.copy()
    payload["type"] = "access"
    payload["exp"] = _current_time(now) + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    return jwt.encode(
        None,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )


def x_create_access_token__mutmut_14(data: dict, now: Clock | None = None) -> str:
    payload = data.copy()
    payload["type"] = "access"
    payload["exp"] = _current_time(now) + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    return jwt.encode(
        payload,
        None,
        algorithm=settings.ALGORITHM
    )


def x_create_access_token__mutmut_15(data: dict, now: Clock | None = None) -> str:
    payload = data.copy()
    payload["type"] = "access"
    payload["exp"] = _current_time(now) + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    return jwt.encode(
        payload,
        settings.SECRET_KEY,
        algorithm=None
    )


def x_create_access_token__mutmut_16(data: dict, now: Clock | None = None) -> str:
    payload = data.copy()
    payload["type"] = "access"
    payload["exp"] = _current_time(now) + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    return jwt.encode(
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )


def x_create_access_token__mutmut_17(data: dict, now: Clock | None = None) -> str:
    payload = data.copy()
    payload["type"] = "access"
    payload["exp"] = _current_time(now) + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    return jwt.encode(
        payload,
        algorithm=settings.ALGORITHM
    )


def x_create_access_token__mutmut_18(data: dict, now: Clock | None = None) -> str:
    payload = data.copy()
    payload["type"] = "access"
    payload["exp"] = _current_time(now) + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    return jwt.encode(
        payload,
        settings.SECRET_KEY,
        )

mutants_x_create_access_token__mutmut['_mutmut_orig'] = x_create_access_token__mutmut_orig # type: ignore # mutmut generated
mutants_x_create_access_token__mutmut['x_create_access_token__mutmut_1'] = x_create_access_token__mutmut_1 # type: ignore # mutmut generated
mutants_x_create_access_token__mutmut['x_create_access_token__mutmut_2'] = x_create_access_token__mutmut_2 # type: ignore # mutmut generated
mutants_x_create_access_token__mutmut['x_create_access_token__mutmut_3'] = x_create_access_token__mutmut_3 # type: ignore # mutmut generated
mutants_x_create_access_token__mutmut['x_create_access_token__mutmut_4'] = x_create_access_token__mutmut_4 # type: ignore # mutmut generated
mutants_x_create_access_token__mutmut['x_create_access_token__mutmut_5'] = x_create_access_token__mutmut_5 # type: ignore # mutmut generated
mutants_x_create_access_token__mutmut['x_create_access_token__mutmut_6'] = x_create_access_token__mutmut_6 # type: ignore # mutmut generated
mutants_x_create_access_token__mutmut['x_create_access_token__mutmut_7'] = x_create_access_token__mutmut_7 # type: ignore # mutmut generated
mutants_x_create_access_token__mutmut['x_create_access_token__mutmut_8'] = x_create_access_token__mutmut_8 # type: ignore # mutmut generated
mutants_x_create_access_token__mutmut['x_create_access_token__mutmut_9'] = x_create_access_token__mutmut_9 # type: ignore # mutmut generated
mutants_x_create_access_token__mutmut['x_create_access_token__mutmut_10'] = x_create_access_token__mutmut_10 # type: ignore # mutmut generated
mutants_x_create_access_token__mutmut['x_create_access_token__mutmut_11'] = x_create_access_token__mutmut_11 # type: ignore # mutmut generated
mutants_x_create_access_token__mutmut['x_create_access_token__mutmut_12'] = x_create_access_token__mutmut_12 # type: ignore # mutmut generated
mutants_x_create_access_token__mutmut['x_create_access_token__mutmut_13'] = x_create_access_token__mutmut_13 # type: ignore # mutmut generated
mutants_x_create_access_token__mutmut['x_create_access_token__mutmut_14'] = x_create_access_token__mutmut_14 # type: ignore # mutmut generated
mutants_x_create_access_token__mutmut['x_create_access_token__mutmut_15'] = x_create_access_token__mutmut_15 # type: ignore # mutmut generated
mutants_x_create_access_token__mutmut['x_create_access_token__mutmut_16'] = x_create_access_token__mutmut_16 # type: ignore # mutmut generated
mutants_x_create_access_token__mutmut['x_create_access_token__mutmut_17'] = x_create_access_token__mutmut_17 # type: ignore # mutmut generated
mutants_x_create_access_token__mutmut['x_create_access_token__mutmut_18'] = x_create_access_token__mutmut_18 # type: ignore # mutmut generated
mutants_x_create_refresh_token__mutmut: MutantDict = {}  # type: ignore

@_mutmut_mutated(mutants_x_create_refresh_token__mutmut)
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

def x_create_refresh_token__mutmut_orig(data: dict, now: Clock | None = None) -> str:
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

def x_create_refresh_token__mutmut_1(data: dict, now: Clock | None = None) -> str:
    payload = None
    payload["type"] = "refresh"
    payload["exp"] = _current_time(now) + timedelta(
        days=settings.REFRESH_TOKEN_EXPIRE_DAYS
    )

    return jwt.encode(
        payload,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM,
    )

def x_create_refresh_token__mutmut_2(data: dict, now: Clock | None = None) -> str:
    payload = data.copy()
    payload["type"] = None
    payload["exp"] = _current_time(now) + timedelta(
        days=settings.REFRESH_TOKEN_EXPIRE_DAYS
    )

    return jwt.encode(
        payload,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM,
    )

def x_create_refresh_token__mutmut_3(data: dict, now: Clock | None = None) -> str:
    payload = data.copy()
    payload["XXtypeXX"] = "refresh"
    payload["exp"] = _current_time(now) + timedelta(
        days=settings.REFRESH_TOKEN_EXPIRE_DAYS
    )

    return jwt.encode(
        payload,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM,
    )

def x_create_refresh_token__mutmut_4(data: dict, now: Clock | None = None) -> str:
    payload = data.copy()
    payload["TYPE"] = "refresh"
    payload["exp"] = _current_time(now) + timedelta(
        days=settings.REFRESH_TOKEN_EXPIRE_DAYS
    )

    return jwt.encode(
        payload,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM,
    )

def x_create_refresh_token__mutmut_5(data: dict, now: Clock | None = None) -> str:
    payload = data.copy()
    payload["type"] = "XXrefreshXX"
    payload["exp"] = _current_time(now) + timedelta(
        days=settings.REFRESH_TOKEN_EXPIRE_DAYS
    )

    return jwt.encode(
        payload,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM,
    )

def x_create_refresh_token__mutmut_6(data: dict, now: Clock | None = None) -> str:
    payload = data.copy()
    payload["type"] = "REFRESH"
    payload["exp"] = _current_time(now) + timedelta(
        days=settings.REFRESH_TOKEN_EXPIRE_DAYS
    )

    return jwt.encode(
        payload,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM,
    )

def x_create_refresh_token__mutmut_7(data: dict, now: Clock | None = None) -> str:
    payload = data.copy()
    payload["type"] = "refresh"
    payload["exp"] = None

    return jwt.encode(
        payload,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM,
    )

def x_create_refresh_token__mutmut_8(data: dict, now: Clock | None = None) -> str:
    payload = data.copy()
    payload["type"] = "refresh"
    payload["XXexpXX"] = _current_time(now) + timedelta(
        days=settings.REFRESH_TOKEN_EXPIRE_DAYS
    )

    return jwt.encode(
        payload,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM,
    )

def x_create_refresh_token__mutmut_9(data: dict, now: Clock | None = None) -> str:
    payload = data.copy()
    payload["type"] = "refresh"
    payload["EXP"] = _current_time(now) + timedelta(
        days=settings.REFRESH_TOKEN_EXPIRE_DAYS
    )

    return jwt.encode(
        payload,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM,
    )

def x_create_refresh_token__mutmut_10(data: dict, now: Clock | None = None) -> str:
    payload = data.copy()
    payload["type"] = "refresh"
    payload["exp"] = _current_time(now) - timedelta(
        days=settings.REFRESH_TOKEN_EXPIRE_DAYS
    )

    return jwt.encode(
        payload,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM,
    )

def x_create_refresh_token__mutmut_11(data: dict, now: Clock | None = None) -> str:
    payload = data.copy()
    payload["type"] = "refresh"
    payload["exp"] = _current_time(None) + timedelta(
        days=settings.REFRESH_TOKEN_EXPIRE_DAYS
    )

    return jwt.encode(
        payload,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM,
    )

def x_create_refresh_token__mutmut_12(data: dict, now: Clock | None = None) -> str:
    payload = data.copy()
    payload["type"] = "refresh"
    payload["exp"] = _current_time(now) + timedelta(
        days=None
    )

    return jwt.encode(
        payload,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM,
    )

def x_create_refresh_token__mutmut_13(data: dict, now: Clock | None = None) -> str:
    payload = data.copy()
    payload["type"] = "refresh"
    payload["exp"] = _current_time(now) + timedelta(
        days=settings.REFRESH_TOKEN_EXPIRE_DAYS
    )

    return jwt.encode(
        None,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM,
    )

def x_create_refresh_token__mutmut_14(data: dict, now: Clock | None = None) -> str:
    payload = data.copy()
    payload["type"] = "refresh"
    payload["exp"] = _current_time(now) + timedelta(
        days=settings.REFRESH_TOKEN_EXPIRE_DAYS
    )

    return jwt.encode(
        payload,
        None,
        algorithm=settings.ALGORITHM,
    )

def x_create_refresh_token__mutmut_15(data: dict, now: Clock | None = None) -> str:
    payload = data.copy()
    payload["type"] = "refresh"
    payload["exp"] = _current_time(now) + timedelta(
        days=settings.REFRESH_TOKEN_EXPIRE_DAYS
    )

    return jwt.encode(
        payload,
        settings.SECRET_KEY,
        algorithm=None,
    )

def x_create_refresh_token__mutmut_16(data: dict, now: Clock | None = None) -> str:
    payload = data.copy()
    payload["type"] = "refresh"
    payload["exp"] = _current_time(now) + timedelta(
        days=settings.REFRESH_TOKEN_EXPIRE_DAYS
    )

    return jwt.encode(
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM,
    )

def x_create_refresh_token__mutmut_17(data: dict, now: Clock | None = None) -> str:
    payload = data.copy()
    payload["type"] = "refresh"
    payload["exp"] = _current_time(now) + timedelta(
        days=settings.REFRESH_TOKEN_EXPIRE_DAYS
    )

    return jwt.encode(
        payload,
        algorithm=settings.ALGORITHM,
    )

def x_create_refresh_token__mutmut_18(data: dict, now: Clock | None = None) -> str:
    payload = data.copy()
    payload["type"] = "refresh"
    payload["exp"] = _current_time(now) + timedelta(
        days=settings.REFRESH_TOKEN_EXPIRE_DAYS
    )

    return jwt.encode(
        payload,
        settings.SECRET_KEY,
        )

mutants_x_create_refresh_token__mutmut['_mutmut_orig'] = x_create_refresh_token__mutmut_orig # type: ignore # mutmut generated
mutants_x_create_refresh_token__mutmut['x_create_refresh_token__mutmut_1'] = x_create_refresh_token__mutmut_1 # type: ignore # mutmut generated
mutants_x_create_refresh_token__mutmut['x_create_refresh_token__mutmut_2'] = x_create_refresh_token__mutmut_2 # type: ignore # mutmut generated
mutants_x_create_refresh_token__mutmut['x_create_refresh_token__mutmut_3'] = x_create_refresh_token__mutmut_3 # type: ignore # mutmut generated
mutants_x_create_refresh_token__mutmut['x_create_refresh_token__mutmut_4'] = x_create_refresh_token__mutmut_4 # type: ignore # mutmut generated
mutants_x_create_refresh_token__mutmut['x_create_refresh_token__mutmut_5'] = x_create_refresh_token__mutmut_5 # type: ignore # mutmut generated
mutants_x_create_refresh_token__mutmut['x_create_refresh_token__mutmut_6'] = x_create_refresh_token__mutmut_6 # type: ignore # mutmut generated
mutants_x_create_refresh_token__mutmut['x_create_refresh_token__mutmut_7'] = x_create_refresh_token__mutmut_7 # type: ignore # mutmut generated
mutants_x_create_refresh_token__mutmut['x_create_refresh_token__mutmut_8'] = x_create_refresh_token__mutmut_8 # type: ignore # mutmut generated
mutants_x_create_refresh_token__mutmut['x_create_refresh_token__mutmut_9'] = x_create_refresh_token__mutmut_9 # type: ignore # mutmut generated
mutants_x_create_refresh_token__mutmut['x_create_refresh_token__mutmut_10'] = x_create_refresh_token__mutmut_10 # type: ignore # mutmut generated
mutants_x_create_refresh_token__mutmut['x_create_refresh_token__mutmut_11'] = x_create_refresh_token__mutmut_11 # type: ignore # mutmut generated
mutants_x_create_refresh_token__mutmut['x_create_refresh_token__mutmut_12'] = x_create_refresh_token__mutmut_12 # type: ignore # mutmut generated
mutants_x_create_refresh_token__mutmut['x_create_refresh_token__mutmut_13'] = x_create_refresh_token__mutmut_13 # type: ignore # mutmut generated
mutants_x_create_refresh_token__mutmut['x_create_refresh_token__mutmut_14'] = x_create_refresh_token__mutmut_14 # type: ignore # mutmut generated
mutants_x_create_refresh_token__mutmut['x_create_refresh_token__mutmut_15'] = x_create_refresh_token__mutmut_15 # type: ignore # mutmut generated
mutants_x_create_refresh_token__mutmut['x_create_refresh_token__mutmut_16'] = x_create_refresh_token__mutmut_16 # type: ignore # mutmut generated
mutants_x_create_refresh_token__mutmut['x_create_refresh_token__mutmut_17'] = x_create_refresh_token__mutmut_17 # type: ignore # mutmut generated
mutants_x_create_refresh_token__mutmut['x_create_refresh_token__mutmut_18'] = x_create_refresh_token__mutmut_18 # type: ignore # mutmut generated
mutants_x__decode_token__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__decode_token__mutmut)
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


def x__decode_token__mutmut_orig(
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


def x__decode_token__mutmut_1(
    token: str,
    expected_type: str,
    now: Clock | None = None,
) -> dict | None:
    try:
        # Verify the signature and algorithm, but check exp ourselves below
        # so the test can supply a controlled clock.
        payload = None

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


def x__decode_token__mutmut_2(
    token: str,
    expected_type: str,
    now: Clock | None = None,
) -> dict | None:
    try:
        # Verify the signature and algorithm, but check exp ourselves below
        # so the test can supply a controlled clock.
        payload = jwt.decode(
            None,
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


def x__decode_token__mutmut_3(
    token: str,
    expected_type: str,
    now: Clock | None = None,
) -> dict | None:
    try:
        # Verify the signature and algorithm, but check exp ourselves below
        # so the test can supply a controlled clock.
        payload = jwt.decode(
            token,
            None,
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


def x__decode_token__mutmut_4(
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
            algorithms=None,
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


def x__decode_token__mutmut_5(
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
            options=None,
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


def x__decode_token__mutmut_6(
    token: str,
    expected_type: str,
    now: Clock | None = None,
) -> dict | None:
    try:
        # Verify the signature and algorithm, but check exp ourselves below
        # so the test can supply a controlled clock.
        payload = jwt.decode(
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


def x__decode_token__mutmut_7(
    token: str,
    expected_type: str,
    now: Clock | None = None,
) -> dict | None:
    try:
        # Verify the signature and algorithm, but check exp ourselves below
        # so the test can supply a controlled clock.
        payload = jwt.decode(
            token,
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


def x__decode_token__mutmut_8(
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


def x__decode_token__mutmut_9(
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


def x__decode_token__mutmut_10(
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
            options={"XXverify_expXX": False},
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


def x__decode_token__mutmut_11(
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
            options={"VERIFY_EXP": False},
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


def x__decode_token__mutmut_12(
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
            options={"verify_exp": True},
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


def x__decode_token__mutmut_13(
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

        if payload.get(None) != expected_type:
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


def x__decode_token__mutmut_14(
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

        if payload.get("XXtypeXX") != expected_type:
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


def x__decode_token__mutmut_15(
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

        if payload.get("TYPE") != expected_type:
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


def x__decode_token__mutmut_16(
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

        if payload.get("type") == expected_type:
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


def x__decode_token__mutmut_17(
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

        exp = None
        if isinstance(exp, bool) or not isinstance(exp, (int, float)):
            return None

        if _current_time(now).timestamp() >= exp:
            return None

        return payload
    except (JWTError, ValueError, TypeError, OverflowError):
        # Malformed or invalid tokens should fail closed, not leak parsing errors.
        return None


def x__decode_token__mutmut_18(
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

        exp = payload.get(None)
        if isinstance(exp, bool) or not isinstance(exp, (int, float)):
            return None

        if _current_time(now).timestamp() >= exp:
            return None

        return payload
    except (JWTError, ValueError, TypeError, OverflowError):
        # Malformed or invalid tokens should fail closed, not leak parsing errors.
        return None


def x__decode_token__mutmut_19(
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

        exp = payload.get("XXexpXX")
        if isinstance(exp, bool) or not isinstance(exp, (int, float)):
            return None

        if _current_time(now).timestamp() >= exp:
            return None

        return payload
    except (JWTError, ValueError, TypeError, OverflowError):
        # Malformed or invalid tokens should fail closed, not leak parsing errors.
        return None


def x__decode_token__mutmut_20(
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

        exp = payload.get("EXP")
        if isinstance(exp, bool) or not isinstance(exp, (int, float)):
            return None

        if _current_time(now).timestamp() >= exp:
            return None

        return payload
    except (JWTError, ValueError, TypeError, OverflowError):
        # Malformed or invalid tokens should fail closed, not leak parsing errors.
        return None


def x__decode_token__mutmut_21(
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
        if isinstance(exp, bool) and not isinstance(exp, (int, float)):
            return None

        if _current_time(now).timestamp() >= exp:
            return None

        return payload
    except (JWTError, ValueError, TypeError, OverflowError):
        # Malformed or invalid tokens should fail closed, not leak parsing errors.
        return None


def x__decode_token__mutmut_22(
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
        if isinstance(exp, bool) or isinstance(exp, (int, float)):
            return None

        if _current_time(now).timestamp() >= exp:
            return None

        return payload
    except (JWTError, ValueError, TypeError, OverflowError):
        # Malformed or invalid tokens should fail closed, not leak parsing errors.
        return None


def x__decode_token__mutmut_23(
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

        if _current_time(None).timestamp() >= exp:
            return None

        return payload
    except (JWTError, ValueError, TypeError, OverflowError):
        # Malformed or invalid tokens should fail closed, not leak parsing errors.
        return None


def x__decode_token__mutmut_24(
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

        if _current_time(now).timestamp() > exp:
            return None

        return payload
    except (JWTError, ValueError, TypeError, OverflowError):
        # Malformed or invalid tokens should fail closed, not leak parsing errors.
        return None

mutants_x__decode_token__mutmut['_mutmut_orig'] = x__decode_token__mutmut_orig # type: ignore # mutmut generated
mutants_x__decode_token__mutmut['x__decode_token__mutmut_1'] = x__decode_token__mutmut_1 # type: ignore # mutmut generated
mutants_x__decode_token__mutmut['x__decode_token__mutmut_2'] = x__decode_token__mutmut_2 # type: ignore # mutmut generated
mutants_x__decode_token__mutmut['x__decode_token__mutmut_3'] = x__decode_token__mutmut_3 # type: ignore # mutmut generated
mutants_x__decode_token__mutmut['x__decode_token__mutmut_4'] = x__decode_token__mutmut_4 # type: ignore # mutmut generated
mutants_x__decode_token__mutmut['x__decode_token__mutmut_5'] = x__decode_token__mutmut_5 # type: ignore # mutmut generated
mutants_x__decode_token__mutmut['x__decode_token__mutmut_6'] = x__decode_token__mutmut_6 # type: ignore # mutmut generated
mutants_x__decode_token__mutmut['x__decode_token__mutmut_7'] = x__decode_token__mutmut_7 # type: ignore # mutmut generated
mutants_x__decode_token__mutmut['x__decode_token__mutmut_8'] = x__decode_token__mutmut_8 # type: ignore # mutmut generated
mutants_x__decode_token__mutmut['x__decode_token__mutmut_9'] = x__decode_token__mutmut_9 # type: ignore # mutmut generated
mutants_x__decode_token__mutmut['x__decode_token__mutmut_10'] = x__decode_token__mutmut_10 # type: ignore # mutmut generated
mutants_x__decode_token__mutmut['x__decode_token__mutmut_11'] = x__decode_token__mutmut_11 # type: ignore # mutmut generated
mutants_x__decode_token__mutmut['x__decode_token__mutmut_12'] = x__decode_token__mutmut_12 # type: ignore # mutmut generated
mutants_x__decode_token__mutmut['x__decode_token__mutmut_13'] = x__decode_token__mutmut_13 # type: ignore # mutmut generated
mutants_x__decode_token__mutmut['x__decode_token__mutmut_14'] = x__decode_token__mutmut_14 # type: ignore # mutmut generated
mutants_x__decode_token__mutmut['x__decode_token__mutmut_15'] = x__decode_token__mutmut_15 # type: ignore # mutmut generated
mutants_x__decode_token__mutmut['x__decode_token__mutmut_16'] = x__decode_token__mutmut_16 # type: ignore # mutmut generated
mutants_x__decode_token__mutmut['x__decode_token__mutmut_17'] = x__decode_token__mutmut_17 # type: ignore # mutmut generated
mutants_x__decode_token__mutmut['x__decode_token__mutmut_18'] = x__decode_token__mutmut_18 # type: ignore # mutmut generated
mutants_x__decode_token__mutmut['x__decode_token__mutmut_19'] = x__decode_token__mutmut_19 # type: ignore # mutmut generated
mutants_x__decode_token__mutmut['x__decode_token__mutmut_20'] = x__decode_token__mutmut_20 # type: ignore # mutmut generated
mutants_x__decode_token__mutmut['x__decode_token__mutmut_21'] = x__decode_token__mutmut_21 # type: ignore # mutmut generated
mutants_x__decode_token__mutmut['x__decode_token__mutmut_22'] = x__decode_token__mutmut_22 # type: ignore # mutmut generated
mutants_x__decode_token__mutmut['x__decode_token__mutmut_23'] = x__decode_token__mutmut_23 # type: ignore # mutmut generated
mutants_x__decode_token__mutmut['x__decode_token__mutmut_24'] = x__decode_token__mutmut_24 # type: ignore # mutmut generated
mutants_x_decode_access_token__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_decode_access_token__mutmut)
def decode_access_token(token: str, now: Clock | None = None) -> dict | None:
    return _decode_token(token, "access", now)


def x_decode_access_token__mutmut_orig(token: str, now: Clock | None = None) -> dict | None:
    return _decode_token(token, "access", now)


def x_decode_access_token__mutmut_1(token: str, now: Clock | None = None) -> dict | None:
    return _decode_token(None, "access", now)


def x_decode_access_token__mutmut_2(token: str, now: Clock | None = None) -> dict | None:
    return _decode_token(token, None, now)


def x_decode_access_token__mutmut_3(token: str, now: Clock | None = None) -> dict | None:
    return _decode_token(token, "access", None)


def x_decode_access_token__mutmut_4(token: str, now: Clock | None = None) -> dict | None:
    return _decode_token("access", now)


def x_decode_access_token__mutmut_5(token: str, now: Clock | None = None) -> dict | None:
    return _decode_token(token, now)


def x_decode_access_token__mutmut_6(token: str, now: Clock | None = None) -> dict | None:
    return _decode_token(token, "access", )


def x_decode_access_token__mutmut_7(token: str, now: Clock | None = None) -> dict | None:
    return _decode_token(token, "XXaccessXX", now)


def x_decode_access_token__mutmut_8(token: str, now: Clock | None = None) -> dict | None:
    return _decode_token(token, "ACCESS", now)

mutants_x_decode_access_token__mutmut['_mutmut_orig'] = x_decode_access_token__mutmut_orig # type: ignore # mutmut generated
mutants_x_decode_access_token__mutmut['x_decode_access_token__mutmut_1'] = x_decode_access_token__mutmut_1 # type: ignore # mutmut generated
mutants_x_decode_access_token__mutmut['x_decode_access_token__mutmut_2'] = x_decode_access_token__mutmut_2 # type: ignore # mutmut generated
mutants_x_decode_access_token__mutmut['x_decode_access_token__mutmut_3'] = x_decode_access_token__mutmut_3 # type: ignore # mutmut generated
mutants_x_decode_access_token__mutmut['x_decode_access_token__mutmut_4'] = x_decode_access_token__mutmut_4 # type: ignore # mutmut generated
mutants_x_decode_access_token__mutmut['x_decode_access_token__mutmut_5'] = x_decode_access_token__mutmut_5 # type: ignore # mutmut generated
mutants_x_decode_access_token__mutmut['x_decode_access_token__mutmut_6'] = x_decode_access_token__mutmut_6 # type: ignore # mutmut generated
mutants_x_decode_access_token__mutmut['x_decode_access_token__mutmut_7'] = x_decode_access_token__mutmut_7 # type: ignore # mutmut generated
mutants_x_decode_access_token__mutmut['x_decode_access_token__mutmut_8'] = x_decode_access_token__mutmut_8 # type: ignore # mutmut generated
mutants_x_decode_refresh_token__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_decode_refresh_token__mutmut)
def decode_refresh_token(token: str, now: Clock | None = None) -> dict | None:
    return _decode_token(token, "refresh", now)


def x_decode_refresh_token__mutmut_orig(token: str, now: Clock | None = None) -> dict | None:
    return _decode_token(token, "refresh", now)


def x_decode_refresh_token__mutmut_1(token: str, now: Clock | None = None) -> dict | None:
    return _decode_token(None, "refresh", now)


def x_decode_refresh_token__mutmut_2(token: str, now: Clock | None = None) -> dict | None:
    return _decode_token(token, None, now)


def x_decode_refresh_token__mutmut_3(token: str, now: Clock | None = None) -> dict | None:
    return _decode_token(token, "refresh", None)


def x_decode_refresh_token__mutmut_4(token: str, now: Clock | None = None) -> dict | None:
    return _decode_token("refresh", now)


def x_decode_refresh_token__mutmut_5(token: str, now: Clock | None = None) -> dict | None:
    return _decode_token(token, now)


def x_decode_refresh_token__mutmut_6(token: str, now: Clock | None = None) -> dict | None:
    return _decode_token(token, "refresh", )


def x_decode_refresh_token__mutmut_7(token: str, now: Clock | None = None) -> dict | None:
    return _decode_token(token, "XXrefreshXX", now)


def x_decode_refresh_token__mutmut_8(token: str, now: Clock | None = None) -> dict | None:
    return _decode_token(token, "REFRESH", now)

mutants_x_decode_refresh_token__mutmut['_mutmut_orig'] = x_decode_refresh_token__mutmut_orig # type: ignore # mutmut generated
mutants_x_decode_refresh_token__mutmut['x_decode_refresh_token__mutmut_1'] = x_decode_refresh_token__mutmut_1 # type: ignore # mutmut generated
mutants_x_decode_refresh_token__mutmut['x_decode_refresh_token__mutmut_2'] = x_decode_refresh_token__mutmut_2 # type: ignore # mutmut generated
mutants_x_decode_refresh_token__mutmut['x_decode_refresh_token__mutmut_3'] = x_decode_refresh_token__mutmut_3 # type: ignore # mutmut generated
mutants_x_decode_refresh_token__mutmut['x_decode_refresh_token__mutmut_4'] = x_decode_refresh_token__mutmut_4 # type: ignore # mutmut generated
mutants_x_decode_refresh_token__mutmut['x_decode_refresh_token__mutmut_5'] = x_decode_refresh_token__mutmut_5 # type: ignore # mutmut generated
mutants_x_decode_refresh_token__mutmut['x_decode_refresh_token__mutmut_6'] = x_decode_refresh_token__mutmut_6 # type: ignore # mutmut generated
mutants_x_decode_refresh_token__mutmut['x_decode_refresh_token__mutmut_7'] = x_decode_refresh_token__mutmut_7 # type: ignore # mutmut generated
mutants_x_decode_refresh_token__mutmut['x_decode_refresh_token__mutmut_8'] = x_decode_refresh_token__mutmut_8 # type: ignore # mutmut generated
