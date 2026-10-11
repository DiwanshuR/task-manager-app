from typing import Annotated

from email_validator import EmailNotValidError, validate_email
from pydantic import AfterValidator, BaseModel, Field, field_serializer
from datetime import datetime
from app.models.user import UserRole
from app.schemas.datetime import as_utc


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_x__validate_email_address__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x__validate_email_address__mutmut)
def _validate_email_address(value: str) -> str:
    try:
        return validate_email(
            value,
            test_environment=True,
            check_deliverability=False,
        ).normalized
    except EmailNotValidError as exc:
        raise ValueError(str(exc)) from exc


def x__validate_email_address__mutmut_orig(value: str) -> str:
    try:
        return validate_email(
            value,
            test_environment=True,
            check_deliverability=False,
        ).normalized
    except EmailNotValidError as exc:
        raise ValueError(str(exc)) from exc


def x__validate_email_address__mutmut_1(value: str) -> str:
    try:
        return validate_email(
            None,
            test_environment=True,
            check_deliverability=False,
        ).normalized
    except EmailNotValidError as exc:
        raise ValueError(str(exc)) from exc


def x__validate_email_address__mutmut_2(value: str) -> str:
    try:
        return validate_email(
            value,
            test_environment=None,
            check_deliverability=False,
        ).normalized
    except EmailNotValidError as exc:
        raise ValueError(str(exc)) from exc


def x__validate_email_address__mutmut_3(value: str) -> str:
    try:
        return validate_email(
            value,
            test_environment=True,
            check_deliverability=None,
        ).normalized
    except EmailNotValidError as exc:
        raise ValueError(str(exc)) from exc


def x__validate_email_address__mutmut_4(value: str) -> str:
    try:
        return validate_email(
            test_environment=True,
            check_deliverability=False,
        ).normalized
    except EmailNotValidError as exc:
        raise ValueError(str(exc)) from exc


def x__validate_email_address__mutmut_5(value: str) -> str:
    try:
        return validate_email(
            value,
            check_deliverability=False,
        ).normalized
    except EmailNotValidError as exc:
        raise ValueError(str(exc)) from exc


def x__validate_email_address__mutmut_6(value: str) -> str:
    try:
        return validate_email(
            value,
            test_environment=True,
            ).normalized
    except EmailNotValidError as exc:
        raise ValueError(str(exc)) from exc


def x__validate_email_address__mutmut_7(value: str) -> str:
    try:
        return validate_email(
            value,
            test_environment=False,
            check_deliverability=False,
        ).normalized
    except EmailNotValidError as exc:
        raise ValueError(str(exc)) from exc


def x__validate_email_address__mutmut_8(value: str) -> str:
    try:
        return validate_email(
            value,
            test_environment=True,
            check_deliverability=True,
        ).normalized
    except EmailNotValidError as exc:
        raise ValueError(str(exc)) from exc


def x__validate_email_address__mutmut_9(value: str) -> str:
    try:
        return validate_email(
            value,
            test_environment=True,
            check_deliverability=False,
        ).normalized
    except EmailNotValidError as exc:
        raise ValueError(None) from exc


def x__validate_email_address__mutmut_10(value: str) -> str:
    try:
        return validate_email(
            value,
            test_environment=True,
            check_deliverability=False,
        ).normalized
    except EmailNotValidError as exc:
        raise ValueError(str(None)) from exc

mutants_x__validate_email_address__mutmut['_mutmut_orig'] = x__validate_email_address__mutmut_orig # type: ignore # mutmut generated
mutants_x__validate_email_address__mutmut['x__validate_email_address__mutmut_1'] = x__validate_email_address__mutmut_1 # type: ignore # mutmut generated
mutants_x__validate_email_address__mutmut['x__validate_email_address__mutmut_2'] = x__validate_email_address__mutmut_2 # type: ignore # mutmut generated
mutants_x__validate_email_address__mutmut['x__validate_email_address__mutmut_3'] = x__validate_email_address__mutmut_3 # type: ignore # mutmut generated
mutants_x__validate_email_address__mutmut['x__validate_email_address__mutmut_4'] = x__validate_email_address__mutmut_4 # type: ignore # mutmut generated
mutants_x__validate_email_address__mutmut['x__validate_email_address__mutmut_5'] = x__validate_email_address__mutmut_5 # type: ignore # mutmut generated
mutants_x__validate_email_address__mutmut['x__validate_email_address__mutmut_6'] = x__validate_email_address__mutmut_6 # type: ignore # mutmut generated
mutants_x__validate_email_address__mutmut['x__validate_email_address__mutmut_7'] = x__validate_email_address__mutmut_7 # type: ignore # mutmut generated
mutants_x__validate_email_address__mutmut['x__validate_email_address__mutmut_8'] = x__validate_email_address__mutmut_8 # type: ignore # mutmut generated
mutants_x__validate_email_address__mutmut['x__validate_email_address__mutmut_9'] = x__validate_email_address__mutmut_9 # type: ignore # mutmut generated
mutants_x__validate_email_address__mutmut['x__validate_email_address__mutmut_10'] = x__validate_email_address__mutmut_10 # type: ignore # mutmut generated


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