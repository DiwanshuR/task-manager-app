from datetime import datetime, timedelta, timezone

from app.auth.security import (
    hash_password,
    verify_password,
    create_access_token,
    decode_access_token
)

import pytest
from jose import jwt
import json
import base64
from app.config import settings

# day 2 task 3 - hashing tests 
def test_hash_password_does_not_return_plaintext():
    password = "TestPassword123!"

    password_hash = hash_password(password)

    assert password_hash != password


def test_verify_password_accepts_the_correct_password():
    password = "TestPassword123!"
    password_hash = hash_password(password)

    assert verify_password(password, password_hash) is True


def test_verify_password_rejects_the_wrong_password():
    password_hash = hash_password("TestPassword123!")

    assert verify_password("WrongPassword123!", password_hash) is False
    

def test_hash_password_uses_a_different_salt_each_time():
    password = "TestPassword123!"

    first_hash = hash_password(password)
    second_hash = hash_password(password)

    assert first_hash != second_hash
    assert verify_password(password, first_hash) is True
    assert verify_password(password, second_hash) is True


def test_verify_password_rejects_corrupted_hash_without_raising():
    assert verify_password("TestPassword123!", "not-a-valid-bcrypt-hash") is False


# ------------------------------------------------------------------

# day 2 task 1 checking jwt expiration and security
def test_access_token_round_trips_claims():
    now = datetime(2030, 1, 1, tzinfo=timezone.utc)
    token = create_access_token(
        {"sub": "user-123", "role": "member"},
        now=lambda: now,
    )

    payload = decode_access_token(token, now=lambda: now)

    assert payload is not None
    assert payload["sub"] == "user-123"
    assert payload["role"] == "member"
    assert payload["type"] == "access"
    assert "exp" in payload


def test_access_token_is_valid_one_second_before_expiry(monkeypatch):
    now = datetime(2030, 1, 1, tzinfo=timezone.utc)
    monkeypatch.setattr(
        "app.auth.security.settings.ACCESS_TOKEN_EXPIRE_MINUTES",
        1,
    )
    token = create_access_token({"sub": "user-123"}, now=lambda: now)

    # JWT exp is represented as a whole Unix timestamp.
    exp = jwt.get_unverified_claims(token)["exp"]
    one_second_before_expiry = datetime.fromtimestamp(
        exp - 1,
        tz=timezone.utc,
    )

    assert decode_access_token(
        token,
        now=lambda: one_second_before_expiry,
    ) is not None


def test_access_token_is_rejected_exactly_at_expiry(monkeypatch):
    now = datetime(2030, 1, 1, tzinfo=timezone.utc)
    monkeypatch.setattr(
        "app.auth.security.settings.ACCESS_TOKEN_EXPIRE_MINUTES",
        1,
    )
    token = create_access_token({"sub": "user-123"}, now=lambda: now)

    exp = jwt.get_unverified_claims(token)["exp"]
    exactly_at_expiry = datetime.fromtimestamp(exp, tz=timezone.utc)

    assert decode_access_token(token, now=lambda: exactly_at_expiry) is None


def test_access_token_is_rejected_long_after_expiry(monkeypatch):
    now = datetime(2030, 1, 1, tzinfo=timezone.utc)
    monkeypatch.setattr(
        "app.auth.security.settings.ACCESS_TOKEN_EXPIRE_MINUTES",
        1,
    )
    token = create_access_token({"sub": "user-123"}, now=lambda: now)

    long_after_expiry = now + timedelta(days=30)

    assert decode_access_token(token, now=lambda: long_after_expiry) is None
    
    
# --------------------------------------------------------------------------------
    
# day 2 task 2 tests checking jwt security

def _encode_json_segment(value: dict) -> str:
    """Encode a JWT header or payload as an unpadded base64url segment."""
    raw = json.dumps(value, separators=(",", ":")).encode("utf-8")
    return base64.urlsafe_b64encode(raw).rstrip(b"=").decode("ascii")


def test_tampered_payload_is_rejected():
    now = datetime(2030, 1, 1, tzinfo=timezone.utc)
    token = create_access_token(
        {"sub": "user-123", "role": "member"},
        now=lambda: now,
    )

    header_segment, payload_segment, signature_segment = token.split(".")
    payload = jwt.get_unverified_claims(token)
    payload["role"] = "admin"

    tampered_token = ".".join(
        [
            header_segment,
            _encode_json_segment(payload),
            signature_segment,
        ]
    )

    assert decode_access_token(tampered_token, now=lambda: now) is None


def test_token_signed_with_different_secret_is_rejected():
    now = datetime(2030, 1, 1, tzinfo=timezone.utc)
    claims = {
        "sub": "user-123",
        "type": "access",
        "exp": int((now + timedelta(minutes=5)).timestamp()),
    }
    token = jwt.encode(
        claims,
        "a-different-test-secret",
        algorithm=settings.ALGORITHM,
    )

    assert decode_access_token(token, now=lambda: now) is None


def test_unsigned_alg_none_token_is_rejected():
    now = datetime(2030, 1, 1, tzinfo=timezone.utc)
    header = {"alg": "none", "typ": "JWT"}
    payload = {
        "sub": "user-123",
        "type": "access",
        "exp": int((now + timedelta(minutes=5)).timestamp()),
    }
    unsigned_token = (
        f"{_encode_json_segment(header)}."
        f"{_encode_json_segment(payload)}."
    )

    assert decode_access_token(unsigned_token, now=lambda: now) is None


@pytest.mark.parametrize("token", ["", "abc", "a.b", "a.b.c"])
def test_malformed_tokens_are_rejected_without_raising(token):
    now = datetime(2030, 1, 1, tzinfo=timezone.utc)

    assert decode_access_token(token, now=lambda: now) is None