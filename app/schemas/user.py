from typing import Annotated

from email_validator import EmailNotValidError, validate_email
from pydantic import AfterValidator, BaseModel, Field, field_serializer
from datetime import datetime
from app.models.user import UserRole
from app.schemas.datetime import as_utc


def _validate_email_address(value: str) -> str:
    try:
        return validate_email(
            value,
            test_environment=True,
            check_deliverability=False,
        ).normalized
    except EmailNotValidError as exc:
        raise ValueError(str(exc)) from exc


EmailAddress = Annotated[
    str,
    Field(json_schema_extra={"format": "email"}),
    AfterValidator(_validate_email_address),
]


class UserCreate(BaseModel):
    name: str = Field(..., min_length=1)
    email: EmailAddress
    password: str = Field(
        ...,
        min_length=6,
        max_length=1024,
        description="Plain password, hashed before storage",
    )


class UserLogin(BaseModel):
    email: EmailAddress
    password: str


class UserOut(BaseModel):
    id: int
    name: str
    email: EmailAddress
    role : UserRole
    created_at: datetime

    @field_serializer("created_at")
    def serialize_created_at(self, value: datetime) -> datetime:
        return as_utc(value)

    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"