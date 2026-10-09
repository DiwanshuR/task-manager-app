from pydantic import BaseModel, Field, field_validator
from datetime import datetime
from typing import Optional
from app.models.task import Task, TaskStatus, TaskPriority


class TaskCreate(BaseModel):
    title: str = Field(..., min_length=1)
    description: Optional[str] = None
    status: TaskStatus = TaskStatus.pending
    priority: TaskPriority = TaskPriority.medium
    project_id: int
    
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
        if getattr(value, "value", value) != TaskStatus.pending.value:
            raise ValueError("New tasks must start as pending")
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

    class Config:
        from_attributes = True