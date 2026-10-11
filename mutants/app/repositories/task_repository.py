from abc import ABC, abstractmethod

from mutmut.mutation.trampoline import MutantDict
from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated
from sqlalchemy import func, or_
from sqlalchemy.orm import Session

from app.models.project import Project
from app.models.task import Task, TaskPriority, TaskStatus
from app.models.user import User
from app.schemas.task import TaskCreate, TaskUpdate


class TaskRepository(ABC):
    @abstractmethod
    def get_all(
        self,
        *,
        owner_id: int,
        is_admin: bool = False,
        status_filter: TaskStatus | None = None,
        priority: TaskPriority | None = None,
        project_id: int | None = None,
        search: str | None = None,
        skip: int = 0,
        limit: int = 20,
    ) -> list[Task]:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, task_id: int) -> Task | None:
        raise NotImplementedError

    @abstractmethod
    def get_deleted_by_id(self, task_id: int) -> Task | None:
        raise NotImplementedError

    @abstractmethod
    def get_deleted(self) -> list[Task]:
        raise NotImplementedError

    @abstractmethod
    def create(self, payload: TaskCreate, *, created_by: int) -> Task:
        raise NotImplementedError

    @abstractmethod
    def update(self, task: Task, payload: TaskUpdate) -> Task:
        raise NotImplementedError

    @abstractmethod
    def soft_delete(self, task: Task) -> None:
        raise NotImplementedError

    @abstractmethod
    def restore(self, task: Task) -> Task:
        raise NotImplementedError


mutants_xǁSQLAlchemyTaskRepositoryǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁSQLAlchemyTaskRepositoryǁget_all__mutmut: MutantDict = {}  # type: ignore
mutants_xǁSQLAlchemyTaskRepositoryǁget_by_id__mutmut: MutantDict = {}  # type: ignore
mutants_xǁSQLAlchemyTaskRepositoryǁget_deleted_by_id__mutmut: MutantDict = {}  # type: ignore
mutants_xǁSQLAlchemyTaskRepositoryǁget_deleted__mutmut: MutantDict = {}  # type: ignore
mutants_xǁSQLAlchemyTaskRepositoryǁcreate__mutmut: MutantDict = {}  # type: ignore
mutants_xǁSQLAlchemyTaskRepositoryǁupdate__mutmut: MutantDict = {}  # type: ignore
mutants_xǁSQLAlchemyTaskRepositoryǁsoft_delete__mutmut: MutantDict = {}  # type: ignore
mutants_xǁSQLAlchemyTaskRepositoryǁrestore__mutmut: MutantDict = {}  # type: ignore


class SQLAlchemyTaskRepository(TaskRepository):
    @_mutmut_mutated(mutants_xǁSQLAlchemyTaskRepositoryǁ__init____mutmut)
    def __init__(self, db: Session):
        self.db = db

    def xǁSQLAlchemyTaskRepositoryǁ__init____mutmut_orig(self, db: Session):
        self.db = db

    def xǁSQLAlchemyTaskRepositoryǁ__init____mutmut_1(self, db: Session):
        self.db = None

    @_mutmut_mutated(mutants_xǁSQLAlchemyTaskRepositoryǁget_all__mutmut)
    def get_all(
        self,
        *,
        owner_id: int,
        is_admin: bool = False,
        status_filter: TaskStatus | None = None,
        priority: TaskPriority | None = None,
        project_id: int | None = None,
        search: str | None = None,
        skip: int = 0,
        limit: int = 20,
    ) -> list[Task]:
        query = self.db.query(Task).join(Task.project).filter(Task.deleted_at.is_(None))

        if not is_admin:
            query = query.filter(
                or_(
                    Project.owner_id == owner_id,
                    Project.members.any(User.id == owner_id),
                )
            )

        if status_filter is not None:
            query = query.filter(Task.status == status_filter)
        if priority is not None:
            query = query.filter(Task.priority == priority)
        if project_id is not None:
            query = query.filter(Task.project_id == project_id)
        if search:
            query = query.filter(Task.title.ilike(f"%{search}%"))

        return query.offset(skip).limit(limit).all()

    def xǁSQLAlchemyTaskRepositoryǁget_all__mutmut_orig(
        self,
        *,
        owner_id: int,
        is_admin: bool = False,
        status_filter: TaskStatus | None = None,
        priority: TaskPriority | None = None,
        project_id: int | None = None,
        search: str | None = None,
        skip: int = 0,
        limit: int = 20,
    ) -> list[Task]:
        query = self.db.query(Task).join(Task.project).filter(Task.deleted_at.is_(None))

        if not is_admin:
            query = query.filter(
                or_(
                    Project.owner_id == owner_id,
                    Project.members.any(User.id == owner_id),
                )
            )

        if status_filter is not None:
            query = query.filter(Task.status == status_filter)
        if priority is not None:
            query = query.filter(Task.priority == priority)
        if project_id is not None:
            query = query.filter(Task.project_id == project_id)
        if search:
            query = query.filter(Task.title.ilike(f"%{search}%"))

        return query.offset(skip).limit(limit).all()

    def xǁSQLAlchemyTaskRepositoryǁget_all__mutmut_1(
        self,
        *,
        owner_id: int,
        is_admin: bool = True,
        status_filter: TaskStatus | None = None,
        priority: TaskPriority | None = None,
        project_id: int | None = None,
        search: str | None = None,
        skip: int = 0,
        limit: int = 20,
    ) -> list[Task]:
        query = self.db.query(Task).join(Task.project).filter(Task.deleted_at.is_(None))

        if not is_admin:
            query = query.filter(
                or_(
                    Project.owner_id == owner_id,
                    Project.members.any(User.id == owner_id),
                )
            )

        if status_filter is not None:
            query = query.filter(Task.status == status_filter)
        if priority is not None:
            query = query.filter(Task.priority == priority)
        if project_id is not None:
            query = query.filter(Task.project_id == project_id)
        if search:
            query = query.filter(Task.title.ilike(f"%{search}%"))

        return query.offset(skip).limit(limit).all()

    def xǁSQLAlchemyTaskRepositoryǁget_all__mutmut_2(
        self,
        *,
        owner_id: int,
        is_admin: bool = False,
        status_filter: TaskStatus | None = None,
        priority: TaskPriority | None = None,
        project_id: int | None = None,
        search: str | None = None,
        skip: int = 1,
        limit: int = 20,
    ) -> list[Task]:
        query = self.db.query(Task).join(Task.project).filter(Task.deleted_at.is_(None))

        if not is_admin:
            query = query.filter(
                or_(
                    Project.owner_id == owner_id,
                    Project.members.any(User.id == owner_id),
                )
            )

        if status_filter is not None:
            query = query.filter(Task.status == status_filter)
        if priority is not None:
            query = query.filter(Task.priority == priority)
        if project_id is not None:
            query = query.filter(Task.project_id == project_id)
        if search:
            query = query.filter(Task.title.ilike(f"%{search}%"))

        return query.offset(skip).limit(limit).all()

    def xǁSQLAlchemyTaskRepositoryǁget_all__mutmut_3(
        self,
        *,
        owner_id: int,
        is_admin: bool = False,
        status_filter: TaskStatus | None = None,
        priority: TaskPriority | None = None,
        project_id: int | None = None,
        search: str | None = None,
        skip: int = 0,
        limit: int = 21,
    ) -> list[Task]:
        query = self.db.query(Task).join(Task.project).filter(Task.deleted_at.is_(None))

        if not is_admin:
            query = query.filter(
                or_(
                    Project.owner_id == owner_id,
                    Project.members.any(User.id == owner_id),
                )
            )

        if status_filter is not None:
            query = query.filter(Task.status == status_filter)
        if priority is not None:
            query = query.filter(Task.priority == priority)
        if project_id is not None:
            query = query.filter(Task.project_id == project_id)
        if search:
            query = query.filter(Task.title.ilike(f"%{search}%"))

        return query.offset(skip).limit(limit).all()

    def xǁSQLAlchemyTaskRepositoryǁget_all__mutmut_4(
        self,
        *,
        owner_id: int,
        is_admin: bool = False,
        status_filter: TaskStatus | None = None,
        priority: TaskPriority | None = None,
        project_id: int | None = None,
        search: str | None = None,
        skip: int = 0,
        limit: int = 20,
    ) -> list[Task]:
        query = None

        if not is_admin:
            query = query.filter(
                or_(
                    Project.owner_id == owner_id,
                    Project.members.any(User.id == owner_id),
                )
            )

        if status_filter is not None:
            query = query.filter(Task.status == status_filter)
        if priority is not None:
            query = query.filter(Task.priority == priority)
        if project_id is not None:
            query = query.filter(Task.project_id == project_id)
        if search:
            query = query.filter(Task.title.ilike(f"%{search}%"))

        return query.offset(skip).limit(limit).all()

    def xǁSQLAlchemyTaskRepositoryǁget_all__mutmut_5(
        self,
        *,
        owner_id: int,
        is_admin: bool = False,
        status_filter: TaskStatus | None = None,
        priority: TaskPriority | None = None,
        project_id: int | None = None,
        search: str | None = None,
        skip: int = 0,
        limit: int = 20,
    ) -> list[Task]:
        query = self.db.query(Task).join(Task.project).filter(None)

        if not is_admin:
            query = query.filter(
                or_(
                    Project.owner_id == owner_id,
                    Project.members.any(User.id == owner_id),
                )
            )

        if status_filter is not None:
            query = query.filter(Task.status == status_filter)
        if priority is not None:
            query = query.filter(Task.priority == priority)
        if project_id is not None:
            query = query.filter(Task.project_id == project_id)
        if search:
            query = query.filter(Task.title.ilike(f"%{search}%"))

        return query.offset(skip).limit(limit).all()

    def xǁSQLAlchemyTaskRepositoryǁget_all__mutmut_6(
        self,
        *,
        owner_id: int,
        is_admin: bool = False,
        status_filter: TaskStatus | None = None,
        priority: TaskPriority | None = None,
        project_id: int | None = None,
        search: str | None = None,
        skip: int = 0,
        limit: int = 20,
    ) -> list[Task]:
        query = self.db.query(Task).join(None).filter(Task.deleted_at.is_(None))

        if not is_admin:
            query = query.filter(
                or_(
                    Project.owner_id == owner_id,
                    Project.members.any(User.id == owner_id),
                )
            )

        if status_filter is not None:
            query = query.filter(Task.status == status_filter)
        if priority is not None:
            query = query.filter(Task.priority == priority)
        if project_id is not None:
            query = query.filter(Task.project_id == project_id)
        if search:
            query = query.filter(Task.title.ilike(f"%{search}%"))

        return query.offset(skip).limit(limit).all()

    def xǁSQLAlchemyTaskRepositoryǁget_all__mutmut_7(
        self,
        *,
        owner_id: int,
        is_admin: bool = False,
        status_filter: TaskStatus | None = None,
        priority: TaskPriority | None = None,
        project_id: int | None = None,
        search: str | None = None,
        skip: int = 0,
        limit: int = 20,
    ) -> list[Task]:
        query = self.db.query(None).join(Task.project).filter(Task.deleted_at.is_(None))

        if not is_admin:
            query = query.filter(
                or_(
                    Project.owner_id == owner_id,
                    Project.members.any(User.id == owner_id),
                )
            )

        if status_filter is not None:
            query = query.filter(Task.status == status_filter)
        if priority is not None:
            query = query.filter(Task.priority == priority)
        if project_id is not None:
            query = query.filter(Task.project_id == project_id)
        if search:
            query = query.filter(Task.title.ilike(f"%{search}%"))

        return query.offset(skip).limit(limit).all()

    def xǁSQLAlchemyTaskRepositoryǁget_all__mutmut_8(
        self,
        *,
        owner_id: int,
        is_admin: bool = False,
        status_filter: TaskStatus | None = None,
        priority: TaskPriority | None = None,
        project_id: int | None = None,
        search: str | None = None,
        skip: int = 0,
        limit: int = 20,
    ) -> list[Task]:
        query = self.db.query(Task).join(Task.project).filter(Task.deleted_at.is_(None))

        if is_admin:
            query = query.filter(
                or_(
                    Project.owner_id == owner_id,
                    Project.members.any(User.id == owner_id),
                )
            )

        if status_filter is not None:
            query = query.filter(Task.status == status_filter)
        if priority is not None:
            query = query.filter(Task.priority == priority)
        if project_id is not None:
            query = query.filter(Task.project_id == project_id)
        if search:
            query = query.filter(Task.title.ilike(f"%{search}%"))

        return query.offset(skip).limit(limit).all()

    def xǁSQLAlchemyTaskRepositoryǁget_all__mutmut_9(
        self,
        *,
        owner_id: int,
        is_admin: bool = False,
        status_filter: TaskStatus | None = None,
        priority: TaskPriority | None = None,
        project_id: int | None = None,
        search: str | None = None,
        skip: int = 0,
        limit: int = 20,
    ) -> list[Task]:
        query = self.db.query(Task).join(Task.project).filter(Task.deleted_at.is_(None))

        if not is_admin:
            query = None

        if status_filter is not None:
            query = query.filter(Task.status == status_filter)
        if priority is not None:
            query = query.filter(Task.priority == priority)
        if project_id is not None:
            query = query.filter(Task.project_id == project_id)
        if search:
            query = query.filter(Task.title.ilike(f"%{search}%"))

        return query.offset(skip).limit(limit).all()

    def xǁSQLAlchemyTaskRepositoryǁget_all__mutmut_10(
        self,
        *,
        owner_id: int,
        is_admin: bool = False,
        status_filter: TaskStatus | None = None,
        priority: TaskPriority | None = None,
        project_id: int | None = None,
        search: str | None = None,
        skip: int = 0,
        limit: int = 20,
    ) -> list[Task]:
        query = self.db.query(Task).join(Task.project).filter(Task.deleted_at.is_(None))

        if not is_admin:
            query = query.filter(None)

        if status_filter is not None:
            query = query.filter(Task.status == status_filter)
        if priority is not None:
            query = query.filter(Task.priority == priority)
        if project_id is not None:
            query = query.filter(Task.project_id == project_id)
        if search:
            query = query.filter(Task.title.ilike(f"%{search}%"))

        return query.offset(skip).limit(limit).all()

    def xǁSQLAlchemyTaskRepositoryǁget_all__mutmut_11(
        self,
        *,
        owner_id: int,
        is_admin: bool = False,
        status_filter: TaskStatus | None = None,
        priority: TaskPriority | None = None,
        project_id: int | None = None,
        search: str | None = None,
        skip: int = 0,
        limit: int = 20,
    ) -> list[Task]:
        query = self.db.query(Task).join(Task.project).filter(Task.deleted_at.is_(None))

        if not is_admin:
            query = query.filter(
                or_(
                    None,
                    Project.members.any(User.id == owner_id),
                )
            )

        if status_filter is not None:
            query = query.filter(Task.status == status_filter)
        if priority is not None:
            query = query.filter(Task.priority == priority)
        if project_id is not None:
            query = query.filter(Task.project_id == project_id)
        if search:
            query = query.filter(Task.title.ilike(f"%{search}%"))

        return query.offset(skip).limit(limit).all()

    def xǁSQLAlchemyTaskRepositoryǁget_all__mutmut_12(
        self,
        *,
        owner_id: int,
        is_admin: bool = False,
        status_filter: TaskStatus | None = None,
        priority: TaskPriority | None = None,
        project_id: int | None = None,
        search: str | None = None,
        skip: int = 0,
        limit: int = 20,
    ) -> list[Task]:
        query = self.db.query(Task).join(Task.project).filter(Task.deleted_at.is_(None))

        if not is_admin:
            query = query.filter(
                or_(
                    Project.owner_id == owner_id,
                    None,
                )
            )

        if status_filter is not None:
            query = query.filter(Task.status == status_filter)
        if priority is not None:
            query = query.filter(Task.priority == priority)
        if project_id is not None:
            query = query.filter(Task.project_id == project_id)
        if search:
            query = query.filter(Task.title.ilike(f"%{search}%"))

        return query.offset(skip).limit(limit).all()

    def xǁSQLAlchemyTaskRepositoryǁget_all__mutmut_13(
        self,
        *,
        owner_id: int,
        is_admin: bool = False,
        status_filter: TaskStatus | None = None,
        priority: TaskPriority | None = None,
        project_id: int | None = None,
        search: str | None = None,
        skip: int = 0,
        limit: int = 20,
    ) -> list[Task]:
        query = self.db.query(Task).join(Task.project).filter(Task.deleted_at.is_(None))

        if not is_admin:
            query = query.filter(
                or_(
                    Project.members.any(User.id == owner_id),
                )
            )

        if status_filter is not None:
            query = query.filter(Task.status == status_filter)
        if priority is not None:
            query = query.filter(Task.priority == priority)
        if project_id is not None:
            query = query.filter(Task.project_id == project_id)
        if search:
            query = query.filter(Task.title.ilike(f"%{search}%"))

        return query.offset(skip).limit(limit).all()

    def xǁSQLAlchemyTaskRepositoryǁget_all__mutmut_14(
        self,
        *,
        owner_id: int,
        is_admin: bool = False,
        status_filter: TaskStatus | None = None,
        priority: TaskPriority | None = None,
        project_id: int | None = None,
        search: str | None = None,
        skip: int = 0,
        limit: int = 20,
    ) -> list[Task]:
        query = self.db.query(Task).join(Task.project).filter(Task.deleted_at.is_(None))

        if not is_admin:
            query = query.filter(
                or_(
                    Project.owner_id == owner_id,
                )
            )

        if status_filter is not None:
            query = query.filter(Task.status == status_filter)
        if priority is not None:
            query = query.filter(Task.priority == priority)
        if project_id is not None:
            query = query.filter(Task.project_id == project_id)
        if search:
            query = query.filter(Task.title.ilike(f"%{search}%"))

        return query.offset(skip).limit(limit).all()

    def xǁSQLAlchemyTaskRepositoryǁget_all__mutmut_15(
        self,
        *,
        owner_id: int,
        is_admin: bool = False,
        status_filter: TaskStatus | None = None,
        priority: TaskPriority | None = None,
        project_id: int | None = None,
        search: str | None = None,
        skip: int = 0,
        limit: int = 20,
    ) -> list[Task]:
        query = self.db.query(Task).join(Task.project).filter(Task.deleted_at.is_(None))

        if not is_admin:
            query = query.filter(
                or_(
                    Project.owner_id != owner_id,
                    Project.members.any(User.id == owner_id),
                )
            )

        if status_filter is not None:
            query = query.filter(Task.status == status_filter)
        if priority is not None:
            query = query.filter(Task.priority == priority)
        if project_id is not None:
            query = query.filter(Task.project_id == project_id)
        if search:
            query = query.filter(Task.title.ilike(f"%{search}%"))

        return query.offset(skip).limit(limit).all()

    def xǁSQLAlchemyTaskRepositoryǁget_all__mutmut_16(
        self,
        *,
        owner_id: int,
        is_admin: bool = False,
        status_filter: TaskStatus | None = None,
        priority: TaskPriority | None = None,
        project_id: int | None = None,
        search: str | None = None,
        skip: int = 0,
        limit: int = 20,
    ) -> list[Task]:
        query = self.db.query(Task).join(Task.project).filter(Task.deleted_at.is_(None))

        if not is_admin:
            query = query.filter(
                or_(
                    Project.owner_id == owner_id,
                    Project.members.any(None),
                )
            )

        if status_filter is not None:
            query = query.filter(Task.status == status_filter)
        if priority is not None:
            query = query.filter(Task.priority == priority)
        if project_id is not None:
            query = query.filter(Task.project_id == project_id)
        if search:
            query = query.filter(Task.title.ilike(f"%{search}%"))

        return query.offset(skip).limit(limit).all()

    def xǁSQLAlchemyTaskRepositoryǁget_all__mutmut_17(
        self,
        *,
        owner_id: int,
        is_admin: bool = False,
        status_filter: TaskStatus | None = None,
        priority: TaskPriority | None = None,
        project_id: int | None = None,
        search: str | None = None,
        skip: int = 0,
        limit: int = 20,
    ) -> list[Task]:
        query = self.db.query(Task).join(Task.project).filter(Task.deleted_at.is_(None))

        if not is_admin:
            query = query.filter(
                or_(
                    Project.owner_id == owner_id,
                    Project.members.any(User.id != owner_id),
                )
            )

        if status_filter is not None:
            query = query.filter(Task.status == status_filter)
        if priority is not None:
            query = query.filter(Task.priority == priority)
        if project_id is not None:
            query = query.filter(Task.project_id == project_id)
        if search:
            query = query.filter(Task.title.ilike(f"%{search}%"))

        return query.offset(skip).limit(limit).all()

    def xǁSQLAlchemyTaskRepositoryǁget_all__mutmut_18(
        self,
        *,
        owner_id: int,
        is_admin: bool = False,
        status_filter: TaskStatus | None = None,
        priority: TaskPriority | None = None,
        project_id: int | None = None,
        search: str | None = None,
        skip: int = 0,
        limit: int = 20,
    ) -> list[Task]:
        query = self.db.query(Task).join(Task.project).filter(Task.deleted_at.is_(None))

        if not is_admin:
            query = query.filter(
                or_(
                    Project.owner_id == owner_id,
                    Project.members.any(User.id == owner_id),
                )
            )

        if status_filter is None:
            query = query.filter(Task.status == status_filter)
        if priority is not None:
            query = query.filter(Task.priority == priority)
        if project_id is not None:
            query = query.filter(Task.project_id == project_id)
        if search:
            query = query.filter(Task.title.ilike(f"%{search}%"))

        return query.offset(skip).limit(limit).all()

    def xǁSQLAlchemyTaskRepositoryǁget_all__mutmut_19(
        self,
        *,
        owner_id: int,
        is_admin: bool = False,
        status_filter: TaskStatus | None = None,
        priority: TaskPriority | None = None,
        project_id: int | None = None,
        search: str | None = None,
        skip: int = 0,
        limit: int = 20,
    ) -> list[Task]:
        query = self.db.query(Task).join(Task.project).filter(Task.deleted_at.is_(None))

        if not is_admin:
            query = query.filter(
                or_(
                    Project.owner_id == owner_id,
                    Project.members.any(User.id == owner_id),
                )
            )

        if status_filter is not None:
            query = None
        if priority is not None:
            query = query.filter(Task.priority == priority)
        if project_id is not None:
            query = query.filter(Task.project_id == project_id)
        if search:
            query = query.filter(Task.title.ilike(f"%{search}%"))

        return query.offset(skip).limit(limit).all()

    def xǁSQLAlchemyTaskRepositoryǁget_all__mutmut_20(
        self,
        *,
        owner_id: int,
        is_admin: bool = False,
        status_filter: TaskStatus | None = None,
        priority: TaskPriority | None = None,
        project_id: int | None = None,
        search: str | None = None,
        skip: int = 0,
        limit: int = 20,
    ) -> list[Task]:
        query = self.db.query(Task).join(Task.project).filter(Task.deleted_at.is_(None))

        if not is_admin:
            query = query.filter(
                or_(
                    Project.owner_id == owner_id,
                    Project.members.any(User.id == owner_id),
                )
            )

        if status_filter is not None:
            query = query.filter(None)
        if priority is not None:
            query = query.filter(Task.priority == priority)
        if project_id is not None:
            query = query.filter(Task.project_id == project_id)
        if search:
            query = query.filter(Task.title.ilike(f"%{search}%"))

        return query.offset(skip).limit(limit).all()

    def xǁSQLAlchemyTaskRepositoryǁget_all__mutmut_21(
        self,
        *,
        owner_id: int,
        is_admin: bool = False,
        status_filter: TaskStatus | None = None,
        priority: TaskPriority | None = None,
        project_id: int | None = None,
        search: str | None = None,
        skip: int = 0,
        limit: int = 20,
    ) -> list[Task]:
        query = self.db.query(Task).join(Task.project).filter(Task.deleted_at.is_(None))

        if not is_admin:
            query = query.filter(
                or_(
                    Project.owner_id == owner_id,
                    Project.members.any(User.id == owner_id),
                )
            )

        if status_filter is not None:
            query = query.filter(Task.status != status_filter)
        if priority is not None:
            query = query.filter(Task.priority == priority)
        if project_id is not None:
            query = query.filter(Task.project_id == project_id)
        if search:
            query = query.filter(Task.title.ilike(f"%{search}%"))

        return query.offset(skip).limit(limit).all()

    def xǁSQLAlchemyTaskRepositoryǁget_all__mutmut_22(
        self,
        *,
        owner_id: int,
        is_admin: bool = False,
        status_filter: TaskStatus | None = None,
        priority: TaskPriority | None = None,
        project_id: int | None = None,
        search: str | None = None,
        skip: int = 0,
        limit: int = 20,
    ) -> list[Task]:
        query = self.db.query(Task).join(Task.project).filter(Task.deleted_at.is_(None))

        if not is_admin:
            query = query.filter(
                or_(
                    Project.owner_id == owner_id,
                    Project.members.any(User.id == owner_id),
                )
            )

        if status_filter is not None:
            query = query.filter(Task.status == status_filter)
        if priority is None:
            query = query.filter(Task.priority == priority)
        if project_id is not None:
            query = query.filter(Task.project_id == project_id)
        if search:
            query = query.filter(Task.title.ilike(f"%{search}%"))

        return query.offset(skip).limit(limit).all()

    def xǁSQLAlchemyTaskRepositoryǁget_all__mutmut_23(
        self,
        *,
        owner_id: int,
        is_admin: bool = False,
        status_filter: TaskStatus | None = None,
        priority: TaskPriority | None = None,
        project_id: int | None = None,
        search: str | None = None,
        skip: int = 0,
        limit: int = 20,
    ) -> list[Task]:
        query = self.db.query(Task).join(Task.project).filter(Task.deleted_at.is_(None))

        if not is_admin:
            query = query.filter(
                or_(
                    Project.owner_id == owner_id,
                    Project.members.any(User.id == owner_id),
                )
            )

        if status_filter is not None:
            query = query.filter(Task.status == status_filter)
        if priority is not None:
            query = None
        if project_id is not None:
            query = query.filter(Task.project_id == project_id)
        if search:
            query = query.filter(Task.title.ilike(f"%{search}%"))

        return query.offset(skip).limit(limit).all()

    def xǁSQLAlchemyTaskRepositoryǁget_all__mutmut_24(
        self,
        *,
        owner_id: int,
        is_admin: bool = False,
        status_filter: TaskStatus | None = None,
        priority: TaskPriority | None = None,
        project_id: int | None = None,
        search: str | None = None,
        skip: int = 0,
        limit: int = 20,
    ) -> list[Task]:
        query = self.db.query(Task).join(Task.project).filter(Task.deleted_at.is_(None))

        if not is_admin:
            query = query.filter(
                or_(
                    Project.owner_id == owner_id,
                    Project.members.any(User.id == owner_id),
                )
            )

        if status_filter is not None:
            query = query.filter(Task.status == status_filter)
        if priority is not None:
            query = query.filter(None)
        if project_id is not None:
            query = query.filter(Task.project_id == project_id)
        if search:
            query = query.filter(Task.title.ilike(f"%{search}%"))

        return query.offset(skip).limit(limit).all()

    def xǁSQLAlchemyTaskRepositoryǁget_all__mutmut_25(
        self,
        *,
        owner_id: int,
        is_admin: bool = False,
        status_filter: TaskStatus | None = None,
        priority: TaskPriority | None = None,
        project_id: int | None = None,
        search: str | None = None,
        skip: int = 0,
        limit: int = 20,
    ) -> list[Task]:
        query = self.db.query(Task).join(Task.project).filter(Task.deleted_at.is_(None))

        if not is_admin:
            query = query.filter(
                or_(
                    Project.owner_id == owner_id,
                    Project.members.any(User.id == owner_id),
                )
            )

        if status_filter is not None:
            query = query.filter(Task.status == status_filter)
        if priority is not None:
            query = query.filter(Task.priority != priority)
        if project_id is not None:
            query = query.filter(Task.project_id == project_id)
        if search:
            query = query.filter(Task.title.ilike(f"%{search}%"))

        return query.offset(skip).limit(limit).all()

    def xǁSQLAlchemyTaskRepositoryǁget_all__mutmut_26(
        self,
        *,
        owner_id: int,
        is_admin: bool = False,
        status_filter: TaskStatus | None = None,
        priority: TaskPriority | None = None,
        project_id: int | None = None,
        search: str | None = None,
        skip: int = 0,
        limit: int = 20,
    ) -> list[Task]:
        query = self.db.query(Task).join(Task.project).filter(Task.deleted_at.is_(None))

        if not is_admin:
            query = query.filter(
                or_(
                    Project.owner_id == owner_id,
                    Project.members.any(User.id == owner_id),
                )
            )

        if status_filter is not None:
            query = query.filter(Task.status == status_filter)
        if priority is not None:
            query = query.filter(Task.priority == priority)
        if project_id is None:
            query = query.filter(Task.project_id == project_id)
        if search:
            query = query.filter(Task.title.ilike(f"%{search}%"))

        return query.offset(skip).limit(limit).all()

    def xǁSQLAlchemyTaskRepositoryǁget_all__mutmut_27(
        self,
        *,
        owner_id: int,
        is_admin: bool = False,
        status_filter: TaskStatus | None = None,
        priority: TaskPriority | None = None,
        project_id: int | None = None,
        search: str | None = None,
        skip: int = 0,
        limit: int = 20,
    ) -> list[Task]:
        query = self.db.query(Task).join(Task.project).filter(Task.deleted_at.is_(None))

        if not is_admin:
            query = query.filter(
                or_(
                    Project.owner_id == owner_id,
                    Project.members.any(User.id == owner_id),
                )
            )

        if status_filter is not None:
            query = query.filter(Task.status == status_filter)
        if priority is not None:
            query = query.filter(Task.priority == priority)
        if project_id is not None:
            query = None
        if search:
            query = query.filter(Task.title.ilike(f"%{search}%"))

        return query.offset(skip).limit(limit).all()

    def xǁSQLAlchemyTaskRepositoryǁget_all__mutmut_28(
        self,
        *,
        owner_id: int,
        is_admin: bool = False,
        status_filter: TaskStatus | None = None,
        priority: TaskPriority | None = None,
        project_id: int | None = None,
        search: str | None = None,
        skip: int = 0,
        limit: int = 20,
    ) -> list[Task]:
        query = self.db.query(Task).join(Task.project).filter(Task.deleted_at.is_(None))

        if not is_admin:
            query = query.filter(
                or_(
                    Project.owner_id == owner_id,
                    Project.members.any(User.id == owner_id),
                )
            )

        if status_filter is not None:
            query = query.filter(Task.status == status_filter)
        if priority is not None:
            query = query.filter(Task.priority == priority)
        if project_id is not None:
            query = query.filter(None)
        if search:
            query = query.filter(Task.title.ilike(f"%{search}%"))

        return query.offset(skip).limit(limit).all()

    def xǁSQLAlchemyTaskRepositoryǁget_all__mutmut_29(
        self,
        *,
        owner_id: int,
        is_admin: bool = False,
        status_filter: TaskStatus | None = None,
        priority: TaskPriority | None = None,
        project_id: int | None = None,
        search: str | None = None,
        skip: int = 0,
        limit: int = 20,
    ) -> list[Task]:
        query = self.db.query(Task).join(Task.project).filter(Task.deleted_at.is_(None))

        if not is_admin:
            query = query.filter(
                or_(
                    Project.owner_id == owner_id,
                    Project.members.any(User.id == owner_id),
                )
            )

        if status_filter is not None:
            query = query.filter(Task.status == status_filter)
        if priority is not None:
            query = query.filter(Task.priority == priority)
        if project_id is not None:
            query = query.filter(Task.project_id != project_id)
        if search:
            query = query.filter(Task.title.ilike(f"%{search}%"))

        return query.offset(skip).limit(limit).all()

    def xǁSQLAlchemyTaskRepositoryǁget_all__mutmut_30(
        self,
        *,
        owner_id: int,
        is_admin: bool = False,
        status_filter: TaskStatus | None = None,
        priority: TaskPriority | None = None,
        project_id: int | None = None,
        search: str | None = None,
        skip: int = 0,
        limit: int = 20,
    ) -> list[Task]:
        query = self.db.query(Task).join(Task.project).filter(Task.deleted_at.is_(None))

        if not is_admin:
            query = query.filter(
                or_(
                    Project.owner_id == owner_id,
                    Project.members.any(User.id == owner_id),
                )
            )

        if status_filter is not None:
            query = query.filter(Task.status == status_filter)
        if priority is not None:
            query = query.filter(Task.priority == priority)
        if project_id is not None:
            query = query.filter(Task.project_id == project_id)
        if search:
            query = None

        return query.offset(skip).limit(limit).all()

    def xǁSQLAlchemyTaskRepositoryǁget_all__mutmut_31(
        self,
        *,
        owner_id: int,
        is_admin: bool = False,
        status_filter: TaskStatus | None = None,
        priority: TaskPriority | None = None,
        project_id: int | None = None,
        search: str | None = None,
        skip: int = 0,
        limit: int = 20,
    ) -> list[Task]:
        query = self.db.query(Task).join(Task.project).filter(Task.deleted_at.is_(None))

        if not is_admin:
            query = query.filter(
                or_(
                    Project.owner_id == owner_id,
                    Project.members.any(User.id == owner_id),
                )
            )

        if status_filter is not None:
            query = query.filter(Task.status == status_filter)
        if priority is not None:
            query = query.filter(Task.priority == priority)
        if project_id is not None:
            query = query.filter(Task.project_id == project_id)
        if search:
            query = query.filter(None)

        return query.offset(skip).limit(limit).all()

    def xǁSQLAlchemyTaskRepositoryǁget_all__mutmut_32(
        self,
        *,
        owner_id: int,
        is_admin: bool = False,
        status_filter: TaskStatus | None = None,
        priority: TaskPriority | None = None,
        project_id: int | None = None,
        search: str | None = None,
        skip: int = 0,
        limit: int = 20,
    ) -> list[Task]:
        query = self.db.query(Task).join(Task.project).filter(Task.deleted_at.is_(None))

        if not is_admin:
            query = query.filter(
                or_(
                    Project.owner_id == owner_id,
                    Project.members.any(User.id == owner_id),
                )
            )

        if status_filter is not None:
            query = query.filter(Task.status == status_filter)
        if priority is not None:
            query = query.filter(Task.priority == priority)
        if project_id is not None:
            query = query.filter(Task.project_id == project_id)
        if search:
            query = query.filter(Task.title.ilike(None))

        return query.offset(skip).limit(limit).all()

    def xǁSQLAlchemyTaskRepositoryǁget_all__mutmut_33(
        self,
        *,
        owner_id: int,
        is_admin: bool = False,
        status_filter: TaskStatus | None = None,
        priority: TaskPriority | None = None,
        project_id: int | None = None,
        search: str | None = None,
        skip: int = 0,
        limit: int = 20,
    ) -> list[Task]:
        query = self.db.query(Task).join(Task.project).filter(Task.deleted_at.is_(None))

        if not is_admin:
            query = query.filter(
                or_(
                    Project.owner_id == owner_id,
                    Project.members.any(User.id == owner_id),
                )
            )

        if status_filter is not None:
            query = query.filter(Task.status == status_filter)
        if priority is not None:
            query = query.filter(Task.priority == priority)
        if project_id is not None:
            query = query.filter(Task.project_id == project_id)
        if search:
            query = query.filter(Task.title.ilike(f"%{search}%"))

        return query.offset(skip).limit(None).all()

    def xǁSQLAlchemyTaskRepositoryǁget_all__mutmut_34(
        self,
        *,
        owner_id: int,
        is_admin: bool = False,
        status_filter: TaskStatus | None = None,
        priority: TaskPriority | None = None,
        project_id: int | None = None,
        search: str | None = None,
        skip: int = 0,
        limit: int = 20,
    ) -> list[Task]:
        query = self.db.query(Task).join(Task.project).filter(Task.deleted_at.is_(None))

        if not is_admin:
            query = query.filter(
                or_(
                    Project.owner_id == owner_id,
                    Project.members.any(User.id == owner_id),
                )
            )

        if status_filter is not None:
            query = query.filter(Task.status == status_filter)
        if priority is not None:
            query = query.filter(Task.priority == priority)
        if project_id is not None:
            query = query.filter(Task.project_id == project_id)
        if search:
            query = query.filter(Task.title.ilike(f"%{search}%"))

        return query.offset(None).limit(limit).all()

    @_mutmut_mutated(mutants_xǁSQLAlchemyTaskRepositoryǁget_by_id__mutmut)
    def get_by_id(self, task_id: int) -> Task | None:
        return self.db.query(Task).filter(Task.id == task_id, Task.deleted_at.is_(None)).first()

    def xǁSQLAlchemyTaskRepositoryǁget_by_id__mutmut_orig(self, task_id: int) -> Task | None:
        return self.db.query(Task).filter(Task.id == task_id, Task.deleted_at.is_(None)).first()

    def xǁSQLAlchemyTaskRepositoryǁget_by_id__mutmut_1(self, task_id: int) -> Task | None:
        return self.db.query(Task).filter(None, Task.deleted_at.is_(None)).first()

    def xǁSQLAlchemyTaskRepositoryǁget_by_id__mutmut_2(self, task_id: int) -> Task | None:
        return self.db.query(Task).filter(Task.id == task_id, None).first()

    def xǁSQLAlchemyTaskRepositoryǁget_by_id__mutmut_3(self, task_id: int) -> Task | None:
        return self.db.query(Task).filter(Task.deleted_at.is_(None)).first()

    def xǁSQLAlchemyTaskRepositoryǁget_by_id__mutmut_4(self, task_id: int) -> Task | None:
        return (
            self.db.query(Task)
            .filter(
                Task.id == task_id,
            )
            .first()
        )

    def xǁSQLAlchemyTaskRepositoryǁget_by_id__mutmut_5(self, task_id: int) -> Task | None:
        return self.db.query(None).filter(Task.id == task_id, Task.deleted_at.is_(None)).first()

    def xǁSQLAlchemyTaskRepositoryǁget_by_id__mutmut_6(self, task_id: int) -> Task | None:
        return self.db.query(Task).filter(Task.id != task_id, Task.deleted_at.is_(None)).first()

    @_mutmut_mutated(mutants_xǁSQLAlchemyTaskRepositoryǁget_deleted_by_id__mutmut)
    def get_deleted_by_id(self, task_id: int) -> Task | None:
        return self.db.query(Task).filter(Task.id == task_id, Task.deleted_at.is_not(None)).first()

    def xǁSQLAlchemyTaskRepositoryǁget_deleted_by_id__mutmut_orig(
        self, task_id: int
    ) -> Task | None:
        return self.db.query(Task).filter(Task.id == task_id, Task.deleted_at.is_not(None)).first()

    def xǁSQLAlchemyTaskRepositoryǁget_deleted_by_id__mutmut_1(self, task_id: int) -> Task | None:
        return self.db.query(Task).filter(None, Task.deleted_at.is_not(None)).first()

    def xǁSQLAlchemyTaskRepositoryǁget_deleted_by_id__mutmut_2(self, task_id: int) -> Task | None:
        return self.db.query(Task).filter(Task.id == task_id, None).first()

    def xǁSQLAlchemyTaskRepositoryǁget_deleted_by_id__mutmut_3(self, task_id: int) -> Task | None:
        return self.db.query(Task).filter(Task.deleted_at.is_not(None)).first()

    def xǁSQLAlchemyTaskRepositoryǁget_deleted_by_id__mutmut_4(self, task_id: int) -> Task | None:
        return (
            self.db.query(Task)
            .filter(
                Task.id == task_id,
            )
            .first()
        )

    def xǁSQLAlchemyTaskRepositoryǁget_deleted_by_id__mutmut_5(self, task_id: int) -> Task | None:
        return self.db.query(None).filter(Task.id == task_id, Task.deleted_at.is_not(None)).first()

    def xǁSQLAlchemyTaskRepositoryǁget_deleted_by_id__mutmut_6(self, task_id: int) -> Task | None:
        return self.db.query(Task).filter(Task.id != task_id, Task.deleted_at.is_not(None)).first()

    @_mutmut_mutated(mutants_xǁSQLAlchemyTaskRepositoryǁget_deleted__mutmut)
    def get_deleted(self) -> list[Task]:
        return (
            self.db.query(Task)
            .filter(Task.deleted_at.is_not(None))
            .order_by(Task.deleted_at.desc(), Task.id.desc())
            .all()
        )

    def xǁSQLAlchemyTaskRepositoryǁget_deleted__mutmut_orig(self) -> list[Task]:
        return (
            self.db.query(Task)
            .filter(Task.deleted_at.is_not(None))
            .order_by(Task.deleted_at.desc(), Task.id.desc())
            .all()
        )

    def xǁSQLAlchemyTaskRepositoryǁget_deleted__mutmut_1(self) -> list[Task]:
        return (
            self.db.query(Task)
            .filter(Task.deleted_at.is_not(None))
            .order_by(None, Task.id.desc())
            .all()
        )

    def xǁSQLAlchemyTaskRepositoryǁget_deleted__mutmut_2(self) -> list[Task]:
        return (
            self.db.query(Task)
            .filter(Task.deleted_at.is_not(None))
            .order_by(Task.deleted_at.desc(), None)
            .all()
        )

    def xǁSQLAlchemyTaskRepositoryǁget_deleted__mutmut_3(self) -> list[Task]:
        return (
            self.db.query(Task).filter(Task.deleted_at.is_not(None)).order_by(Task.id.desc()).all()
        )

    def xǁSQLAlchemyTaskRepositoryǁget_deleted__mutmut_4(self) -> list[Task]:
        return (
            self.db.query(Task)
            .filter(Task.deleted_at.is_not(None))
            .order_by(
                Task.deleted_at.desc(),
            )
            .all()
        )

    def xǁSQLAlchemyTaskRepositoryǁget_deleted__mutmut_5(self) -> list[Task]:
        return (
            self.db.query(Task).filter(None).order_by(Task.deleted_at.desc(), Task.id.desc()).all()
        )

    def xǁSQLAlchemyTaskRepositoryǁget_deleted__mutmut_6(self) -> list[Task]:
        return (
            self.db.query(None)
            .filter(Task.deleted_at.is_not(None))
            .order_by(Task.deleted_at.desc(), Task.id.desc())
            .all()
        )

    @_mutmut_mutated(mutants_xǁSQLAlchemyTaskRepositoryǁcreate__mutmut)
    def create(self, payload: TaskCreate, *, created_by: int) -> Task:
        task = Task(
            title=payload.title,
            description=payload.description,
            status=payload.status,
            priority=payload.priority,
            project_id=payload.project_id,
            created_by=created_by,
        )
        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)
        return task

    def xǁSQLAlchemyTaskRepositoryǁcreate__mutmut_orig(
        self, payload: TaskCreate, *, created_by: int
    ) -> Task:
        task = Task(
            title=payload.title,
            description=payload.description,
            status=payload.status,
            priority=payload.priority,
            project_id=payload.project_id,
            created_by=created_by,
        )
        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)
        return task

    def xǁSQLAlchemyTaskRepositoryǁcreate__mutmut_1(
        self, payload: TaskCreate, *, created_by: int
    ) -> Task:
        task = None
        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)
        return task

    def xǁSQLAlchemyTaskRepositoryǁcreate__mutmut_2(
        self, payload: TaskCreate, *, created_by: int
    ) -> Task:
        task = Task(
            title=None,
            description=payload.description,
            status=payload.status,
            priority=payload.priority,
            project_id=payload.project_id,
            created_by=created_by,
        )
        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)
        return task

    def xǁSQLAlchemyTaskRepositoryǁcreate__mutmut_3(
        self, payload: TaskCreate, *, created_by: int
    ) -> Task:
        task = Task(
            title=payload.title,
            description=None,
            status=payload.status,
            priority=payload.priority,
            project_id=payload.project_id,
            created_by=created_by,
        )
        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)
        return task

    def xǁSQLAlchemyTaskRepositoryǁcreate__mutmut_4(
        self, payload: TaskCreate, *, created_by: int
    ) -> Task:
        task = Task(
            title=payload.title,
            description=payload.description,
            status=None,
            priority=payload.priority,
            project_id=payload.project_id,
            created_by=created_by,
        )
        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)
        return task

    def xǁSQLAlchemyTaskRepositoryǁcreate__mutmut_5(
        self, payload: TaskCreate, *, created_by: int
    ) -> Task:
        task = Task(
            title=payload.title,
            description=payload.description,
            status=payload.status,
            priority=None,
            project_id=payload.project_id,
            created_by=created_by,
        )
        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)
        return task

    def xǁSQLAlchemyTaskRepositoryǁcreate__mutmut_6(
        self, payload: TaskCreate, *, created_by: int
    ) -> Task:
        task = Task(
            title=payload.title,
            description=payload.description,
            status=payload.status,
            priority=payload.priority,
            project_id=None,
            created_by=created_by,
        )
        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)
        return task

    def xǁSQLAlchemyTaskRepositoryǁcreate__mutmut_7(
        self, payload: TaskCreate, *, created_by: int
    ) -> Task:
        task = Task(
            title=payload.title,
            description=payload.description,
            status=payload.status,
            priority=payload.priority,
            project_id=payload.project_id,
            created_by=None,
        )
        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)
        return task

    def xǁSQLAlchemyTaskRepositoryǁcreate__mutmut_8(
        self, payload: TaskCreate, *, created_by: int
    ) -> Task:
        task = Task(
            description=payload.description,
            status=payload.status,
            priority=payload.priority,
            project_id=payload.project_id,
            created_by=created_by,
        )
        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)
        return task

    def xǁSQLAlchemyTaskRepositoryǁcreate__mutmut_9(
        self, payload: TaskCreate, *, created_by: int
    ) -> Task:
        task = Task(
            title=payload.title,
            status=payload.status,
            priority=payload.priority,
            project_id=payload.project_id,
            created_by=created_by,
        )
        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)
        return task

    def xǁSQLAlchemyTaskRepositoryǁcreate__mutmut_10(
        self, payload: TaskCreate, *, created_by: int
    ) -> Task:
        task = Task(
            title=payload.title,
            description=payload.description,
            priority=payload.priority,
            project_id=payload.project_id,
            created_by=created_by,
        )
        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)
        return task

    def xǁSQLAlchemyTaskRepositoryǁcreate__mutmut_11(
        self, payload: TaskCreate, *, created_by: int
    ) -> Task:
        task = Task(
            title=payload.title,
            description=payload.description,
            status=payload.status,
            project_id=payload.project_id,
            created_by=created_by,
        )
        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)
        return task

    def xǁSQLAlchemyTaskRepositoryǁcreate__mutmut_12(
        self, payload: TaskCreate, *, created_by: int
    ) -> Task:
        task = Task(
            title=payload.title,
            description=payload.description,
            status=payload.status,
            priority=payload.priority,
            created_by=created_by,
        )
        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)
        return task

    def xǁSQLAlchemyTaskRepositoryǁcreate__mutmut_13(
        self, payload: TaskCreate, *, created_by: int
    ) -> Task:
        task = Task(
            title=payload.title,
            description=payload.description,
            status=payload.status,
            priority=payload.priority,
            project_id=payload.project_id,
        )
        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)
        return task

    def xǁSQLAlchemyTaskRepositoryǁcreate__mutmut_14(
        self, payload: TaskCreate, *, created_by: int
    ) -> Task:
        task = Task(
            title=payload.title,
            description=payload.description,
            status=payload.status,
            priority=payload.priority,
            project_id=payload.project_id,
            created_by=created_by,
        )
        self.db.add(None)
        self.db.commit()
        self.db.refresh(task)
        return task

    def xǁSQLAlchemyTaskRepositoryǁcreate__mutmut_15(
        self, payload: TaskCreate, *, created_by: int
    ) -> Task:
        task = Task(
            title=payload.title,
            description=payload.description,
            status=payload.status,
            priority=payload.priority,
            project_id=payload.project_id,
            created_by=created_by,
        )
        self.db.add(task)
        self.db.commit()
        self.db.refresh(None)
        return task

    @_mutmut_mutated(mutants_xǁSQLAlchemyTaskRepositoryǁupdate__mutmut)
    def update(self, task: Task, payload: TaskUpdate) -> Task:
        task.title = payload.title
        task.description = payload.description
        task.status = payload.status
        task.priority = payload.priority
        self.db.commit()
        self.db.refresh(task)
        return task

    def xǁSQLAlchemyTaskRepositoryǁupdate__mutmut_orig(
        self, task: Task, payload: TaskUpdate
    ) -> Task:
        task.title = payload.title
        task.description = payload.description
        task.status = payload.status
        task.priority = payload.priority
        self.db.commit()
        self.db.refresh(task)
        return task

    def xǁSQLAlchemyTaskRepositoryǁupdate__mutmut_1(self, task: Task, payload: TaskUpdate) -> Task:
        task.title = None
        task.description = payload.description
        task.status = payload.status
        task.priority = payload.priority
        self.db.commit()
        self.db.refresh(task)
        return task

    def xǁSQLAlchemyTaskRepositoryǁupdate__mutmut_2(self, task: Task, payload: TaskUpdate) -> Task:
        task.title = payload.title
        task.description = None
        task.status = payload.status
        task.priority = payload.priority
        self.db.commit()
        self.db.refresh(task)
        return task

    def xǁSQLAlchemyTaskRepositoryǁupdate__mutmut_3(self, task: Task, payload: TaskUpdate) -> Task:
        task.title = payload.title
        task.description = payload.description
        task.status = None
        task.priority = payload.priority
        self.db.commit()
        self.db.refresh(task)
        return task

    def xǁSQLAlchemyTaskRepositoryǁupdate__mutmut_4(self, task: Task, payload: TaskUpdate) -> Task:
        task.title = payload.title
        task.description = payload.description
        task.status = payload.status
        task.priority = None
        self.db.commit()
        self.db.refresh(task)
        return task

    def xǁSQLAlchemyTaskRepositoryǁupdate__mutmut_5(self, task: Task, payload: TaskUpdate) -> Task:
        task.title = payload.title
        task.description = payload.description
        task.status = payload.status
        task.priority = payload.priority
        self.db.commit()
        self.db.refresh(None)
        return task

    @_mutmut_mutated(mutants_xǁSQLAlchemyTaskRepositoryǁsoft_delete__mutmut)
    def soft_delete(self, task: Task) -> None:
        task.deleted_at = func.now()
        self.db.commit()
        self.db.refresh(task)

    def xǁSQLAlchemyTaskRepositoryǁsoft_delete__mutmut_orig(self, task: Task) -> None:
        task.deleted_at = func.now()
        self.db.commit()
        self.db.refresh(task)

    def xǁSQLAlchemyTaskRepositoryǁsoft_delete__mutmut_1(self, task: Task) -> None:
        task.deleted_at = None
        self.db.commit()
        self.db.refresh(task)

    def xǁSQLAlchemyTaskRepositoryǁsoft_delete__mutmut_2(self, task: Task) -> None:
        task.deleted_at = func.now()
        self.db.commit()
        self.db.refresh(None)

    @_mutmut_mutated(mutants_xǁSQLAlchemyTaskRepositoryǁrestore__mutmut)
    def restore(self, task: Task) -> Task:
        task.deleted_at = None
        self.db.commit()
        self.db.refresh(task)
        return task

    def xǁSQLAlchemyTaskRepositoryǁrestore__mutmut_orig(self, task: Task) -> Task:
        task.deleted_at = None
        self.db.commit()
        self.db.refresh(task)
        return task

    def xǁSQLAlchemyTaskRepositoryǁrestore__mutmut_1(self, task: Task) -> Task:
        task.deleted_at = ""
        self.db.commit()
        self.db.refresh(task)
        return task

    def xǁSQLAlchemyTaskRepositoryǁrestore__mutmut_2(self, task: Task) -> Task:
        task.deleted_at = None
        self.db.commit()
        self.db.refresh(None)
        return task


mutants_xǁSQLAlchemyTaskRepositoryǁ__init____mutmut["_mutmut_orig"] = (
    SQLAlchemyTaskRepository.xǁSQLAlchemyTaskRepositoryǁ__init____mutmut_orig
)  # type: ignore # mutmut generated
mutants_xǁSQLAlchemyTaskRepositoryǁ__init____mutmut[
    "xǁSQLAlchemyTaskRepositoryǁ__init____mutmut_1"
] = SQLAlchemyTaskRepository.xǁSQLAlchemyTaskRepositoryǁ__init____mutmut_1  # type: ignore # mutmut generated

mutants_xǁSQLAlchemyTaskRepositoryǁget_all__mutmut["_mutmut_orig"] = (
    SQLAlchemyTaskRepository.xǁSQLAlchemyTaskRepositoryǁget_all__mutmut_orig
)  # type: ignore # mutmut generated
mutants_xǁSQLAlchemyTaskRepositoryǁget_all__mutmut[
    "xǁSQLAlchemyTaskRepositoryǁget_all__mutmut_1"
] = SQLAlchemyTaskRepository.xǁSQLAlchemyTaskRepositoryǁget_all__mutmut_1  # type: ignore # mutmut generated
mutants_xǁSQLAlchemyTaskRepositoryǁget_all__mutmut[
    "xǁSQLAlchemyTaskRepositoryǁget_all__mutmut_2"
] = SQLAlchemyTaskRepository.xǁSQLAlchemyTaskRepositoryǁget_all__mutmut_2  # type: ignore # mutmut generated
mutants_xǁSQLAlchemyTaskRepositoryǁget_all__mutmut[
    "xǁSQLAlchemyTaskRepositoryǁget_all__mutmut_3"
] = SQLAlchemyTaskRepository.xǁSQLAlchemyTaskRepositoryǁget_all__mutmut_3  # type: ignore # mutmut generated
mutants_xǁSQLAlchemyTaskRepositoryǁget_all__mutmut[
    "xǁSQLAlchemyTaskRepositoryǁget_all__mutmut_4"
] = SQLAlchemyTaskRepository.xǁSQLAlchemyTaskRepositoryǁget_all__mutmut_4  # type: ignore # mutmut generated
mutants_xǁSQLAlchemyTaskRepositoryǁget_all__mutmut[
    "xǁSQLAlchemyTaskRepositoryǁget_all__mutmut_5"
] = SQLAlchemyTaskRepository.xǁSQLAlchemyTaskRepositoryǁget_all__mutmut_5  # type: ignore # mutmut generated
mutants_xǁSQLAlchemyTaskRepositoryǁget_all__mutmut[
    "xǁSQLAlchemyTaskRepositoryǁget_all__mutmut_6"
] = SQLAlchemyTaskRepository.xǁSQLAlchemyTaskRepositoryǁget_all__mutmut_6  # type: ignore # mutmut generated
mutants_xǁSQLAlchemyTaskRepositoryǁget_all__mutmut[
    "xǁSQLAlchemyTaskRepositoryǁget_all__mutmut_7"
] = SQLAlchemyTaskRepository.xǁSQLAlchemyTaskRepositoryǁget_all__mutmut_7  # type: ignore # mutmut generated
mutants_xǁSQLAlchemyTaskRepositoryǁget_all__mutmut[
    "xǁSQLAlchemyTaskRepositoryǁget_all__mutmut_8"
] = SQLAlchemyTaskRepository.xǁSQLAlchemyTaskRepositoryǁget_all__mutmut_8  # type: ignore # mutmut generated
mutants_xǁSQLAlchemyTaskRepositoryǁget_all__mutmut[
    "xǁSQLAlchemyTaskRepositoryǁget_all__mutmut_9"
] = SQLAlchemyTaskRepository.xǁSQLAlchemyTaskRepositoryǁget_all__mutmut_9  # type: ignore # mutmut generated
mutants_xǁSQLAlchemyTaskRepositoryǁget_all__mutmut[
    "xǁSQLAlchemyTaskRepositoryǁget_all__mutmut_10"
] = SQLAlchemyTaskRepository.xǁSQLAlchemyTaskRepositoryǁget_all__mutmut_10  # type: ignore # mutmut generated
mutants_xǁSQLAlchemyTaskRepositoryǁget_all__mutmut[
    "xǁSQLAlchemyTaskRepositoryǁget_all__mutmut_11"
] = SQLAlchemyTaskRepository.xǁSQLAlchemyTaskRepositoryǁget_all__mutmut_11  # type: ignore # mutmut generated
mutants_xǁSQLAlchemyTaskRepositoryǁget_all__mutmut[
    "xǁSQLAlchemyTaskRepositoryǁget_all__mutmut_12"
] = SQLAlchemyTaskRepository.xǁSQLAlchemyTaskRepositoryǁget_all__mutmut_12  # type: ignore # mutmut generated
mutants_xǁSQLAlchemyTaskRepositoryǁget_all__mutmut[
    "xǁSQLAlchemyTaskRepositoryǁget_all__mutmut_13"
] = SQLAlchemyTaskRepository.xǁSQLAlchemyTaskRepositoryǁget_all__mutmut_13  # type: ignore # mutmut generated
mutants_xǁSQLAlchemyTaskRepositoryǁget_all__mutmut[
    "xǁSQLAlchemyTaskRepositoryǁget_all__mutmut_14"
] = SQLAlchemyTaskRepository.xǁSQLAlchemyTaskRepositoryǁget_all__mutmut_14  # type: ignore # mutmut generated
mutants_xǁSQLAlchemyTaskRepositoryǁget_all__mutmut[
    "xǁSQLAlchemyTaskRepositoryǁget_all__mutmut_15"
] = SQLAlchemyTaskRepository.xǁSQLAlchemyTaskRepositoryǁget_all__mutmut_15  # type: ignore # mutmut generated
mutants_xǁSQLAlchemyTaskRepositoryǁget_all__mutmut[
    "xǁSQLAlchemyTaskRepositoryǁget_all__mutmut_16"
] = SQLAlchemyTaskRepository.xǁSQLAlchemyTaskRepositoryǁget_all__mutmut_16  # type: ignore # mutmut generated
mutants_xǁSQLAlchemyTaskRepositoryǁget_all__mutmut[
    "xǁSQLAlchemyTaskRepositoryǁget_all__mutmut_17"
] = SQLAlchemyTaskRepository.xǁSQLAlchemyTaskRepositoryǁget_all__mutmut_17  # type: ignore # mutmut generated
mutants_xǁSQLAlchemyTaskRepositoryǁget_all__mutmut[
    "xǁSQLAlchemyTaskRepositoryǁget_all__mutmut_18"
] = SQLAlchemyTaskRepository.xǁSQLAlchemyTaskRepositoryǁget_all__mutmut_18  # type: ignore # mutmut generated
mutants_xǁSQLAlchemyTaskRepositoryǁget_all__mutmut[
    "xǁSQLAlchemyTaskRepositoryǁget_all__mutmut_19"
] = SQLAlchemyTaskRepository.xǁSQLAlchemyTaskRepositoryǁget_all__mutmut_19  # type: ignore # mutmut generated
mutants_xǁSQLAlchemyTaskRepositoryǁget_all__mutmut[
    "xǁSQLAlchemyTaskRepositoryǁget_all__mutmut_20"
] = SQLAlchemyTaskRepository.xǁSQLAlchemyTaskRepositoryǁget_all__mutmut_20  # type: ignore # mutmut generated
mutants_xǁSQLAlchemyTaskRepositoryǁget_all__mutmut[
    "xǁSQLAlchemyTaskRepositoryǁget_all__mutmut_21"
] = SQLAlchemyTaskRepository.xǁSQLAlchemyTaskRepositoryǁget_all__mutmut_21  # type: ignore # mutmut generated
mutants_xǁSQLAlchemyTaskRepositoryǁget_all__mutmut[
    "xǁSQLAlchemyTaskRepositoryǁget_all__mutmut_22"
] = SQLAlchemyTaskRepository.xǁSQLAlchemyTaskRepositoryǁget_all__mutmut_22  # type: ignore # mutmut generated
mutants_xǁSQLAlchemyTaskRepositoryǁget_all__mutmut[
    "xǁSQLAlchemyTaskRepositoryǁget_all__mutmut_23"
] = SQLAlchemyTaskRepository.xǁSQLAlchemyTaskRepositoryǁget_all__mutmut_23  # type: ignore # mutmut generated
mutants_xǁSQLAlchemyTaskRepositoryǁget_all__mutmut[
    "xǁSQLAlchemyTaskRepositoryǁget_all__mutmut_24"
] = SQLAlchemyTaskRepository.xǁSQLAlchemyTaskRepositoryǁget_all__mutmut_24  # type: ignore # mutmut generated
mutants_xǁSQLAlchemyTaskRepositoryǁget_all__mutmut[
    "xǁSQLAlchemyTaskRepositoryǁget_all__mutmut_25"
] = SQLAlchemyTaskRepository.xǁSQLAlchemyTaskRepositoryǁget_all__mutmut_25  # type: ignore # mutmut generated
mutants_xǁSQLAlchemyTaskRepositoryǁget_all__mutmut[
    "xǁSQLAlchemyTaskRepositoryǁget_all__mutmut_26"
] = SQLAlchemyTaskRepository.xǁSQLAlchemyTaskRepositoryǁget_all__mutmut_26  # type: ignore # mutmut generated
mutants_xǁSQLAlchemyTaskRepositoryǁget_all__mutmut[
    "xǁSQLAlchemyTaskRepositoryǁget_all__mutmut_27"
] = SQLAlchemyTaskRepository.xǁSQLAlchemyTaskRepositoryǁget_all__mutmut_27  # type: ignore # mutmut generated
mutants_xǁSQLAlchemyTaskRepositoryǁget_all__mutmut[
    "xǁSQLAlchemyTaskRepositoryǁget_all__mutmut_28"
] = SQLAlchemyTaskRepository.xǁSQLAlchemyTaskRepositoryǁget_all__mutmut_28  # type: ignore # mutmut generated
mutants_xǁSQLAlchemyTaskRepositoryǁget_all__mutmut[
    "xǁSQLAlchemyTaskRepositoryǁget_all__mutmut_29"
] = SQLAlchemyTaskRepository.xǁSQLAlchemyTaskRepositoryǁget_all__mutmut_29  # type: ignore # mutmut generated
mutants_xǁSQLAlchemyTaskRepositoryǁget_all__mutmut[
    "xǁSQLAlchemyTaskRepositoryǁget_all__mutmut_30"
] = SQLAlchemyTaskRepository.xǁSQLAlchemyTaskRepositoryǁget_all__mutmut_30  # type: ignore # mutmut generated
mutants_xǁSQLAlchemyTaskRepositoryǁget_all__mutmut[
    "xǁSQLAlchemyTaskRepositoryǁget_all__mutmut_31"
] = SQLAlchemyTaskRepository.xǁSQLAlchemyTaskRepositoryǁget_all__mutmut_31  # type: ignore # mutmut generated
mutants_xǁSQLAlchemyTaskRepositoryǁget_all__mutmut[
    "xǁSQLAlchemyTaskRepositoryǁget_all__mutmut_32"
] = SQLAlchemyTaskRepository.xǁSQLAlchemyTaskRepositoryǁget_all__mutmut_32  # type: ignore # mutmut generated
mutants_xǁSQLAlchemyTaskRepositoryǁget_all__mutmut[
    "xǁSQLAlchemyTaskRepositoryǁget_all__mutmut_33"
] = SQLAlchemyTaskRepository.xǁSQLAlchemyTaskRepositoryǁget_all__mutmut_33  # type: ignore # mutmut generated
mutants_xǁSQLAlchemyTaskRepositoryǁget_all__mutmut[
    "xǁSQLAlchemyTaskRepositoryǁget_all__mutmut_34"
] = SQLAlchemyTaskRepository.xǁSQLAlchemyTaskRepositoryǁget_all__mutmut_34  # type: ignore # mutmut generated

mutants_xǁSQLAlchemyTaskRepositoryǁget_by_id__mutmut["_mutmut_orig"] = (
    SQLAlchemyTaskRepository.xǁSQLAlchemyTaskRepositoryǁget_by_id__mutmut_orig
)  # type: ignore # mutmut generated
mutants_xǁSQLAlchemyTaskRepositoryǁget_by_id__mutmut[
    "xǁSQLAlchemyTaskRepositoryǁget_by_id__mutmut_1"
] = SQLAlchemyTaskRepository.xǁSQLAlchemyTaskRepositoryǁget_by_id__mutmut_1  # type: ignore # mutmut generated
mutants_xǁSQLAlchemyTaskRepositoryǁget_by_id__mutmut[
    "xǁSQLAlchemyTaskRepositoryǁget_by_id__mutmut_2"
] = SQLAlchemyTaskRepository.xǁSQLAlchemyTaskRepositoryǁget_by_id__mutmut_2  # type: ignore # mutmut generated
mutants_xǁSQLAlchemyTaskRepositoryǁget_by_id__mutmut[
    "xǁSQLAlchemyTaskRepositoryǁget_by_id__mutmut_3"
] = SQLAlchemyTaskRepository.xǁSQLAlchemyTaskRepositoryǁget_by_id__mutmut_3  # type: ignore # mutmut generated
mutants_xǁSQLAlchemyTaskRepositoryǁget_by_id__mutmut[
    "xǁSQLAlchemyTaskRepositoryǁget_by_id__mutmut_4"
] = SQLAlchemyTaskRepository.xǁSQLAlchemyTaskRepositoryǁget_by_id__mutmut_4  # type: ignore # mutmut generated
mutants_xǁSQLAlchemyTaskRepositoryǁget_by_id__mutmut[
    "xǁSQLAlchemyTaskRepositoryǁget_by_id__mutmut_5"
] = SQLAlchemyTaskRepository.xǁSQLAlchemyTaskRepositoryǁget_by_id__mutmut_5  # type: ignore # mutmut generated
mutants_xǁSQLAlchemyTaskRepositoryǁget_by_id__mutmut[
    "xǁSQLAlchemyTaskRepositoryǁget_by_id__mutmut_6"
] = SQLAlchemyTaskRepository.xǁSQLAlchemyTaskRepositoryǁget_by_id__mutmut_6  # type: ignore # mutmut generated

mutants_xǁSQLAlchemyTaskRepositoryǁget_deleted_by_id__mutmut["_mutmut_orig"] = (
    SQLAlchemyTaskRepository.xǁSQLAlchemyTaskRepositoryǁget_deleted_by_id__mutmut_orig
)  # type: ignore # mutmut generated
mutants_xǁSQLAlchemyTaskRepositoryǁget_deleted_by_id__mutmut[
    "xǁSQLAlchemyTaskRepositoryǁget_deleted_by_id__mutmut_1"
] = SQLAlchemyTaskRepository.xǁSQLAlchemyTaskRepositoryǁget_deleted_by_id__mutmut_1  # type: ignore # mutmut generated
mutants_xǁSQLAlchemyTaskRepositoryǁget_deleted_by_id__mutmut[
    "xǁSQLAlchemyTaskRepositoryǁget_deleted_by_id__mutmut_2"
] = SQLAlchemyTaskRepository.xǁSQLAlchemyTaskRepositoryǁget_deleted_by_id__mutmut_2  # type: ignore # mutmut generated
mutants_xǁSQLAlchemyTaskRepositoryǁget_deleted_by_id__mutmut[
    "xǁSQLAlchemyTaskRepositoryǁget_deleted_by_id__mutmut_3"
] = SQLAlchemyTaskRepository.xǁSQLAlchemyTaskRepositoryǁget_deleted_by_id__mutmut_3  # type: ignore # mutmut generated
mutants_xǁSQLAlchemyTaskRepositoryǁget_deleted_by_id__mutmut[
    "xǁSQLAlchemyTaskRepositoryǁget_deleted_by_id__mutmut_4"
] = SQLAlchemyTaskRepository.xǁSQLAlchemyTaskRepositoryǁget_deleted_by_id__mutmut_4  # type: ignore # mutmut generated
mutants_xǁSQLAlchemyTaskRepositoryǁget_deleted_by_id__mutmut[
    "xǁSQLAlchemyTaskRepositoryǁget_deleted_by_id__mutmut_5"
] = SQLAlchemyTaskRepository.xǁSQLAlchemyTaskRepositoryǁget_deleted_by_id__mutmut_5  # type: ignore # mutmut generated
mutants_xǁSQLAlchemyTaskRepositoryǁget_deleted_by_id__mutmut[
    "xǁSQLAlchemyTaskRepositoryǁget_deleted_by_id__mutmut_6"
] = SQLAlchemyTaskRepository.xǁSQLAlchemyTaskRepositoryǁget_deleted_by_id__mutmut_6  # type: ignore # mutmut generated

mutants_xǁSQLAlchemyTaskRepositoryǁget_deleted__mutmut["_mutmut_orig"] = (
    SQLAlchemyTaskRepository.xǁSQLAlchemyTaskRepositoryǁget_deleted__mutmut_orig
)  # type: ignore # mutmut generated
mutants_xǁSQLAlchemyTaskRepositoryǁget_deleted__mutmut[
    "xǁSQLAlchemyTaskRepositoryǁget_deleted__mutmut_1"
] = SQLAlchemyTaskRepository.xǁSQLAlchemyTaskRepositoryǁget_deleted__mutmut_1  # type: ignore # mutmut generated
mutants_xǁSQLAlchemyTaskRepositoryǁget_deleted__mutmut[
    "xǁSQLAlchemyTaskRepositoryǁget_deleted__mutmut_2"
] = SQLAlchemyTaskRepository.xǁSQLAlchemyTaskRepositoryǁget_deleted__mutmut_2  # type: ignore # mutmut generated
mutants_xǁSQLAlchemyTaskRepositoryǁget_deleted__mutmut[
    "xǁSQLAlchemyTaskRepositoryǁget_deleted__mutmut_3"
] = SQLAlchemyTaskRepository.xǁSQLAlchemyTaskRepositoryǁget_deleted__mutmut_3  # type: ignore # mutmut generated
mutants_xǁSQLAlchemyTaskRepositoryǁget_deleted__mutmut[
    "xǁSQLAlchemyTaskRepositoryǁget_deleted__mutmut_4"
] = SQLAlchemyTaskRepository.xǁSQLAlchemyTaskRepositoryǁget_deleted__mutmut_4  # type: ignore # mutmut generated
mutants_xǁSQLAlchemyTaskRepositoryǁget_deleted__mutmut[
    "xǁSQLAlchemyTaskRepositoryǁget_deleted__mutmut_5"
] = SQLAlchemyTaskRepository.xǁSQLAlchemyTaskRepositoryǁget_deleted__mutmut_5  # type: ignore # mutmut generated
mutants_xǁSQLAlchemyTaskRepositoryǁget_deleted__mutmut[
    "xǁSQLAlchemyTaskRepositoryǁget_deleted__mutmut_6"
] = SQLAlchemyTaskRepository.xǁSQLAlchemyTaskRepositoryǁget_deleted__mutmut_6  # type: ignore # mutmut generated

mutants_xǁSQLAlchemyTaskRepositoryǁcreate__mutmut["_mutmut_orig"] = (
    SQLAlchemyTaskRepository.xǁSQLAlchemyTaskRepositoryǁcreate__mutmut_orig
)  # type: ignore # mutmut generated
mutants_xǁSQLAlchemyTaskRepositoryǁcreate__mutmut["xǁSQLAlchemyTaskRepositoryǁcreate__mutmut_1"] = (
    SQLAlchemyTaskRepository.xǁSQLAlchemyTaskRepositoryǁcreate__mutmut_1
)  # type: ignore # mutmut generated
mutants_xǁSQLAlchemyTaskRepositoryǁcreate__mutmut["xǁSQLAlchemyTaskRepositoryǁcreate__mutmut_2"] = (
    SQLAlchemyTaskRepository.xǁSQLAlchemyTaskRepositoryǁcreate__mutmut_2
)  # type: ignore # mutmut generated
mutants_xǁSQLAlchemyTaskRepositoryǁcreate__mutmut["xǁSQLAlchemyTaskRepositoryǁcreate__mutmut_3"] = (
    SQLAlchemyTaskRepository.xǁSQLAlchemyTaskRepositoryǁcreate__mutmut_3
)  # type: ignore # mutmut generated
mutants_xǁSQLAlchemyTaskRepositoryǁcreate__mutmut["xǁSQLAlchemyTaskRepositoryǁcreate__mutmut_4"] = (
    SQLAlchemyTaskRepository.xǁSQLAlchemyTaskRepositoryǁcreate__mutmut_4
)  # type: ignore # mutmut generated
mutants_xǁSQLAlchemyTaskRepositoryǁcreate__mutmut["xǁSQLAlchemyTaskRepositoryǁcreate__mutmut_5"] = (
    SQLAlchemyTaskRepository.xǁSQLAlchemyTaskRepositoryǁcreate__mutmut_5
)  # type: ignore # mutmut generated
mutants_xǁSQLAlchemyTaskRepositoryǁcreate__mutmut["xǁSQLAlchemyTaskRepositoryǁcreate__mutmut_6"] = (
    SQLAlchemyTaskRepository.xǁSQLAlchemyTaskRepositoryǁcreate__mutmut_6
)  # type: ignore # mutmut generated
mutants_xǁSQLAlchemyTaskRepositoryǁcreate__mutmut["xǁSQLAlchemyTaskRepositoryǁcreate__mutmut_7"] = (
    SQLAlchemyTaskRepository.xǁSQLAlchemyTaskRepositoryǁcreate__mutmut_7
)  # type: ignore # mutmut generated
mutants_xǁSQLAlchemyTaskRepositoryǁcreate__mutmut["xǁSQLAlchemyTaskRepositoryǁcreate__mutmut_8"] = (
    SQLAlchemyTaskRepository.xǁSQLAlchemyTaskRepositoryǁcreate__mutmut_8
)  # type: ignore # mutmut generated
mutants_xǁSQLAlchemyTaskRepositoryǁcreate__mutmut["xǁSQLAlchemyTaskRepositoryǁcreate__mutmut_9"] = (
    SQLAlchemyTaskRepository.xǁSQLAlchemyTaskRepositoryǁcreate__mutmut_9
)  # type: ignore # mutmut generated
mutants_xǁSQLAlchemyTaskRepositoryǁcreate__mutmut[
    "xǁSQLAlchemyTaskRepositoryǁcreate__mutmut_10"
] = SQLAlchemyTaskRepository.xǁSQLAlchemyTaskRepositoryǁcreate__mutmut_10  # type: ignore # mutmut generated
mutants_xǁSQLAlchemyTaskRepositoryǁcreate__mutmut[
    "xǁSQLAlchemyTaskRepositoryǁcreate__mutmut_11"
] = SQLAlchemyTaskRepository.xǁSQLAlchemyTaskRepositoryǁcreate__mutmut_11  # type: ignore # mutmut generated
mutants_xǁSQLAlchemyTaskRepositoryǁcreate__mutmut[
    "xǁSQLAlchemyTaskRepositoryǁcreate__mutmut_12"
] = SQLAlchemyTaskRepository.xǁSQLAlchemyTaskRepositoryǁcreate__mutmut_12  # type: ignore # mutmut generated
mutants_xǁSQLAlchemyTaskRepositoryǁcreate__mutmut[
    "xǁSQLAlchemyTaskRepositoryǁcreate__mutmut_13"
] = SQLAlchemyTaskRepository.xǁSQLAlchemyTaskRepositoryǁcreate__mutmut_13  # type: ignore # mutmut generated
mutants_xǁSQLAlchemyTaskRepositoryǁcreate__mutmut[
    "xǁSQLAlchemyTaskRepositoryǁcreate__mutmut_14"
] = SQLAlchemyTaskRepository.xǁSQLAlchemyTaskRepositoryǁcreate__mutmut_14  # type: ignore # mutmut generated
mutants_xǁSQLAlchemyTaskRepositoryǁcreate__mutmut[
    "xǁSQLAlchemyTaskRepositoryǁcreate__mutmut_15"
] = SQLAlchemyTaskRepository.xǁSQLAlchemyTaskRepositoryǁcreate__mutmut_15  # type: ignore # mutmut generated

mutants_xǁSQLAlchemyTaskRepositoryǁupdate__mutmut["_mutmut_orig"] = (
    SQLAlchemyTaskRepository.xǁSQLAlchemyTaskRepositoryǁupdate__mutmut_orig
)  # type: ignore # mutmut generated
mutants_xǁSQLAlchemyTaskRepositoryǁupdate__mutmut["xǁSQLAlchemyTaskRepositoryǁupdate__mutmut_1"] = (
    SQLAlchemyTaskRepository.xǁSQLAlchemyTaskRepositoryǁupdate__mutmut_1
)  # type: ignore # mutmut generated
mutants_xǁSQLAlchemyTaskRepositoryǁupdate__mutmut["xǁSQLAlchemyTaskRepositoryǁupdate__mutmut_2"] = (
    SQLAlchemyTaskRepository.xǁSQLAlchemyTaskRepositoryǁupdate__mutmut_2
)  # type: ignore # mutmut generated
mutants_xǁSQLAlchemyTaskRepositoryǁupdate__mutmut["xǁSQLAlchemyTaskRepositoryǁupdate__mutmut_3"] = (
    SQLAlchemyTaskRepository.xǁSQLAlchemyTaskRepositoryǁupdate__mutmut_3
)  # type: ignore # mutmut generated
mutants_xǁSQLAlchemyTaskRepositoryǁupdate__mutmut["xǁSQLAlchemyTaskRepositoryǁupdate__mutmut_4"] = (
    SQLAlchemyTaskRepository.xǁSQLAlchemyTaskRepositoryǁupdate__mutmut_4
)  # type: ignore # mutmut generated
mutants_xǁSQLAlchemyTaskRepositoryǁupdate__mutmut["xǁSQLAlchemyTaskRepositoryǁupdate__mutmut_5"] = (
    SQLAlchemyTaskRepository.xǁSQLAlchemyTaskRepositoryǁupdate__mutmut_5
)  # type: ignore # mutmut generated

mutants_xǁSQLAlchemyTaskRepositoryǁsoft_delete__mutmut["_mutmut_orig"] = (
    SQLAlchemyTaskRepository.xǁSQLAlchemyTaskRepositoryǁsoft_delete__mutmut_orig
)  # type: ignore # mutmut generated
mutants_xǁSQLAlchemyTaskRepositoryǁsoft_delete__mutmut[
    "xǁSQLAlchemyTaskRepositoryǁsoft_delete__mutmut_1"
] = SQLAlchemyTaskRepository.xǁSQLAlchemyTaskRepositoryǁsoft_delete__mutmut_1  # type: ignore # mutmut generated
mutants_xǁSQLAlchemyTaskRepositoryǁsoft_delete__mutmut[
    "xǁSQLAlchemyTaskRepositoryǁsoft_delete__mutmut_2"
] = SQLAlchemyTaskRepository.xǁSQLAlchemyTaskRepositoryǁsoft_delete__mutmut_2  # type: ignore # mutmut generated

mutants_xǁSQLAlchemyTaskRepositoryǁrestore__mutmut["_mutmut_orig"] = (
    SQLAlchemyTaskRepository.xǁSQLAlchemyTaskRepositoryǁrestore__mutmut_orig
)  # type: ignore # mutmut generated
mutants_xǁSQLAlchemyTaskRepositoryǁrestore__mutmut[
    "xǁSQLAlchemyTaskRepositoryǁrestore__mutmut_1"
] = SQLAlchemyTaskRepository.xǁSQLAlchemyTaskRepositoryǁrestore__mutmut_1  # type: ignore # mutmut generated
mutants_xǁSQLAlchemyTaskRepositoryǁrestore__mutmut[
    "xǁSQLAlchemyTaskRepositoryǁrestore__mutmut_2"
] = SQLAlchemyTaskRepository.xǁSQLAlchemyTaskRepositoryǁrestore__mutmut_2  # type: ignore # mutmut generated
