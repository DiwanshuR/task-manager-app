import enum
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Enum as SQLEnum
from sqlalchemy.orm import relationship, validates
from sqlalchemy.sql import func
from app.database import Base


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict



class TaskStatus(str, enum.Enum):
    pending = "pending"
    in_progress = "in_progress"
    done = "done"
    archived = "archived"


TASK_STATUS_TRANSITIONS = {
    TaskStatus.pending: frozenset({TaskStatus.in_progress, TaskStatus.archived}),
    TaskStatus.in_progress: frozenset({TaskStatus.done, TaskStatus.archived}),
    TaskStatus.done: frozenset({TaskStatus.archived}),
    TaskStatus.archived: frozenset(),
}
mutants_x_can_transition_task_status__mutmut: MutantDict = {}  # type: ignore


@_mutmut_mutated(mutants_x_can_transition_task_status__mutmut)
def can_transition_task_status(
    current: TaskStatus,
    target: TaskStatus,
) -> bool:
    return target in TASK_STATUS_TRANSITIONS[current]


def x_can_transition_task_status__mutmut_orig(
    current: TaskStatus,
    target: TaskStatus,
) -> bool:
    return target in TASK_STATUS_TRANSITIONS[current]


def x_can_transition_task_status__mutmut_1(
    current: TaskStatus,
    target: TaskStatus,
) -> bool:
    return target not in TASK_STATUS_TRANSITIONS[current]

mutants_x_can_transition_task_status__mutmut['_mutmut_orig'] = x_can_transition_task_status__mutmut_orig # type: ignore # mutmut generated
mutants_x_can_transition_task_status__mutmut['x_can_transition_task_status__mutmut_1'] = x_can_transition_task_status__mutmut_1 # type: ignore # mutmut generated


class TaskPriority(str, enum.Enum):
    low = "low"
    medium = "medium"
    high = "high"
mutants_xǁTaskǁis_valid_status__mutmut: MutantDict = {}  # type: ignore
mutants_xǁTaskǁ__eq____mutmut: MutantDict = {}  # type: ignore


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(String(1000), nullable=True)
    status = Column(SQLEnum(TaskStatus), nullable=False, default=TaskStatus.pending)
    priority = Column(SQLEnum(TaskPriority), nullable=False, default=TaskPriority.medium)
    project_id = Column(Integer, ForeignKey("projects.id"), nullable=False)
    created_by = Column(Integer, ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    deleted_at = Column(DateTime(timezone=True), nullable=True)

    project = relationship("Project", back_populates="tasks")
    
    @validates("title")
    def validate_title(self, key: str, value: str) -> str:
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Task title cannot be empty")
        return value.strip()

    @staticmethod
    @_mutmut_mutated(mutants_xǁTaskǁis_valid_status__mutmut)
    def is_valid_status(status: object) -> bool:
        if isinstance(status, TaskStatus):
            status = status.value

        return isinstance(status, str) and status in {
            task_status.value for task_status in TaskStatus
        }

    @staticmethod
    def xǁTaskǁis_valid_status__mutmut_orig(status: object) -> bool:
        if isinstance(status, TaskStatus):
            status = status.value

        return isinstance(status, str) and status in {
            task_status.value for task_status in TaskStatus
        }

    @staticmethod
    def xǁTaskǁis_valid_status__mutmut_1(status: object) -> bool:
        if isinstance(status, TaskStatus):
            status = None

        return isinstance(status, str) and status in {
            task_status.value for task_status in TaskStatus
        }

    @staticmethod
    def xǁTaskǁis_valid_status__mutmut_2(status: object) -> bool:
        if isinstance(status, TaskStatus):
            status = status.value

        return isinstance(status, str) or status in {
            task_status.value for task_status in TaskStatus
        }

    @staticmethod
    def xǁTaskǁis_valid_status__mutmut_3(status: object) -> bool:
        if isinstance(status, TaskStatus):
            status = status.value

        return isinstance(status, str) and status not in {
            task_status.value for task_status in TaskStatus
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Task":
        return cls(**data)

    def __repr__(self) -> str:
        return (
            f"Task(id={self.id!r}, title={self.title!r}, "
            f"status={self.status!r}, project_id={self.project_id!r})"
        )

    @_mutmut_mutated(mutants_xǁTaskǁ__eq____mutmut)
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Task):
            return NotImplemented

        return (
            self.id,
            self.title,
            self.description,
            self.status,
            self.priority,
            self.project_id,
            self.created_by,
        ) == (
            other.id,
            other.title,
            other.description,
            other.status,
            other.priority,
            other.project_id,
            other.created_by,
        )
        

    def xǁTaskǁ__eq____mutmut_orig(self, other: object) -> bool:
        if not isinstance(other, Task):
            return NotImplemented

        return (
            self.id,
            self.title,
            self.description,
            self.status,
            self.priority,
            self.project_id,
            self.created_by,
        ) == (
            other.id,
            other.title,
            other.description,
            other.status,
            other.priority,
            other.project_id,
            other.created_by,
        )
        

    def xǁTaskǁ__eq____mutmut_1(self, other: object) -> bool:
        if isinstance(other, Task):
            return NotImplemented

        return (
            self.id,
            self.title,
            self.description,
            self.status,
            self.priority,
            self.project_id,
            self.created_by,
        ) == (
            other.id,
            other.title,
            other.description,
            other.status,
            other.priority,
            other.project_id,
            other.created_by,
        )
        

    def xǁTaskǁ__eq____mutmut_2(self, other: object) -> bool:
        if not isinstance(other, Task):
            return NotImplemented

        return (
            self.id,
            self.title,
            self.description,
            self.status,
            self.priority,
            self.project_id,
            self.created_by,
        ) != (
            other.id,
            other.title,
            other.description,
            other.status,
            other.priority,
            other.project_id,
            other.created_by,
        )
        

mutants_xǁTaskǁis_valid_status__mutmut['_mutmut_orig'] = Task.xǁTaskǁis_valid_status__mutmut_orig # type: ignore # mutmut generated
mutants_xǁTaskǁis_valid_status__mutmut['xǁTaskǁis_valid_status__mutmut_1'] = Task.xǁTaskǁis_valid_status__mutmut_1 # type: ignore # mutmut generated
mutants_xǁTaskǁis_valid_status__mutmut['xǁTaskǁis_valid_status__mutmut_2'] = Task.xǁTaskǁis_valid_status__mutmut_2 # type: ignore # mutmut generated
mutants_xǁTaskǁis_valid_status__mutmut['xǁTaskǁis_valid_status__mutmut_3'] = Task.xǁTaskǁis_valid_status__mutmut_3 # type: ignore # mutmut generated

mutants_xǁTaskǁ__eq____mutmut['_mutmut_orig'] = Task.xǁTaskǁ__eq____mutmut_orig # type: ignore # mutmut generated
mutants_xǁTaskǁ__eq____mutmut['xǁTaskǁ__eq____mutmut_1'] = Task.xǁTaskǁ__eq____mutmut_1 # type: ignore # mutmut generated
mutants_xǁTaskǁ__eq____mutmut['xǁTaskǁ__eq____mutmut_2'] = Task.xǁTaskǁ__eq____mutmut_2 # type: ignore # mutmut generated