from pydantic import BaseModel, Field, field_serializer, field_validator
from datetime import datetime
from typing import Optional
from app.schemas.datetime import as_utc
from app.schemas.user import EmailAddress


class ProjectCreate(BaseModel):
    name: str = Field(..., min_length=1)
    description: Optional[str] = None
    member_emails: list[EmailAddress] = Field(default_factory=list)
    
    @field_validator("name")
    @classmethod
    def name_must_contain_non_whitespace(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("Project name cannot be empty")
        return value

class ProjectUpdate(BaseModel):
    name: str = Field(..., min_length=1)
    description: Optional[str] = None
    @field_validator("name")
    @classmethod
    def name_must_contain_non_whitespace(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("Project name cannot be empty")
        return value

class ProjectOut(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    owner_id: int
    created_at: datetime

    @field_serializer("created_at")
    def serialize_created_at(self, value: datetime) -> datetime:
        return as_utc(value)

    class Config:
        from_attributes = True
        
class ProjectMemberAssign(BaseModel):
    emails: list[EmailAddress]