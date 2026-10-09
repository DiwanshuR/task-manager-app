from pydantic import BaseModel, Field, field_serializer, field_validator
from datetime import datetime
from typing import Literal, Optional
from app.models.task import Task, TaskStatus, TaskPriority
from app.schemas.datetime import as_utc


class TaskCreate(BaseModel):
    title: str = Field(..., min_length=1)
    description: Optional[str] = None
    status: Literal[TaskStatus.pending] = TaskStatus.pending
    priority: TaskPriority = TaskPriority.medium
    project_id: int = Field(..., le=2_147_483_647)
    
    @field_validator("title")
    @classmethod
    def title_must_contain_non_whitespace(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("Task title cannot be empty")
        return value

class TaskUpdate(BaseModel):
    title: str = Field(..., min_length=1)
    description: Optional[str] = None
    status: TaskStatus = TaskStatus.pending
    priority: TaskPriority = TaskPriority.medium
    
    @field_validator("title")
    @classmethod
    def title_must_contain_non_whitespace(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("Task title cannot be empty")
        return value

    @field_validator("status", mode="before")
    @classmethod
    def status_must_be_valid(cls, value: object) -> object:
        if not Task.is_valid_status(value):
            raise ValueError(
                "Status must be pending, in_progress, or done"
            )
        return value


class TaskOut(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    status: TaskStatus
    priority: TaskPriority
    project_id: int
    created_by: int
    created_at: datetime
    updated_at: datetime

    @field_serializer("created_at", "updated_at")
    def serialize_timestamps(self, value: datetime) -> datetime:
        return as_utc(value)

    class Config:
        from_attributes = True