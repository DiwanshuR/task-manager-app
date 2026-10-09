from dataclasses import dataclass
from datetime import date


@dataclass
class User:
    id: int
    role: str = "member"


@dataclass
class Task:
    owner_id: int
    title: str
    priority: str = "medium"
    due_date: date | None = None