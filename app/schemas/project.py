from pydantic import BaseModel, Field, field_validator
from datetime import datetime
from typing import Optional


class ProjectCreate(BaseModel):
    name: str = Field(..., min_length=1)
    description: Optional[str] = None
    member_emails: list[str] = Field(default_factory=list)
    
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

    class Config:
        from_attributes = True
        
class ProjectMemberAssign(BaseModel):
    emails: list[str]