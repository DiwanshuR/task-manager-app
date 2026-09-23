from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class ProjectCreate(BaseModel):
    name: str = Field(..., min_length=1)
    description: Optional[str] = None


class ProjectUpdate(BaseModel):
    name: str = Field(..., min_length=1)
    description: Optional[str] = None


class ProjectOut(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    owner_id: int
    created_at: datetime

    class Config:
        from_attributes = True