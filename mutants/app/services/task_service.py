from __future__ import annotations

from mutmut.mutation.trampoline import MutantDict
from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated

from app.exceptions import (
    ArchivedTaskError,
    ProjectNotFoundError,
    TaskNotFoundError,
    TaskStateConflictError,
    UnauthorizedActionError,
)
from app.models.task import (
    Task,
    TaskPriority,
    TaskStatus,
    can_transition_task_status,
)
from app.repositories.project_repository import ProjectRepository
from app.repositories.task_repository import TaskRepository
from app.schemas.task import TaskCreate, TaskUpdate

mutants_xǁTaskServiceǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁTaskServiceǁ_require_project_access__mutmut: MutantDict = {}  # type: ignore
mutants_xǁTaskServiceǁcreate__mutmut: MutantDict = {}  # type: ignore
mutants_xǁTaskServiceǁlist__mutmut: MutantDict = {}  # type: ignore
mutants_xǁTaskServiceǁget__mutmut: MutantDict = {}  # type: ignore
mutants_xǁTaskServiceǁupdate__mutmut: MutantDict = {}  # type: ignore
mutants_xǁTaskServiceǁ_require_task_update_access__mutmut: MutantDict = {}  # type: ignore
mutants_xǁTaskServiceǁarchive__mutmut: MutantDict = {}  # type: ignore
mutants_xǁTaskServiceǁdelete__mutmut: MutantDict = {}  # type: ignore
mutants_xǁTaskServiceǁlist_deleted__mutmut: MutantDict = {}  # type: ignore
mutants_xǁTaskServiceǁrestore__mutmut: MutantDict = {}  # type: ignore


class TaskService:
    """Task use cases, independent of HTTP and database implementations."""

    @_mutmut_mutated(mutants_xǁTaskServiceǁ__init____mutmut)
    def __init__(
        self,
        task_repository: TaskRepository,
        project_repository: ProjectRepository,
    ):
        self.task_repository = task_repository
        self.project_repository = project_repository

    def xǁTaskServiceǁ__init____mutmut_orig(
        self,
        task_repository: TaskRepository,
        project_repository: ProjectRepository,
    ):
        self.task_repository = task_repository
        self.project_repository = project_repository

    def xǁTaskServiceǁ__init____mutmut_1(
        self,
        task_repository: TaskRepository,
        project_repository: ProjectRepository,
    ):
        self.task_repository = None
        self.project_repository = project_repository

    def xǁTaskServiceǁ__init____mutmut_2(
        self,
        task_repository: TaskRepository,
        project_repository: ProjectRepository,
    ):
        self.task_repository = task_repository
        self.project_repository = None

    @_mutmut_mutated(mutants_xǁTaskServiceǁ_require_project_access__mutmut)
    def _require_project_access(
        self,
        project_id: int,
        user_id: int,
        role: str,
    ) -> None:
        project = self.project_repository.get_by_id(project_id)

        if project is None:
            raise ProjectNotFoundError(project_id)

        role_value = getattr(role, "value", role)
        is_admin = role_value == "admin"
        is_owner = project.owner_id == user_id
        is_member = any(member.id == user_id for member in project.members)

        if not (is_admin or is_owner or is_member):
            raise UnauthorizedActionError(
                action="access",
                resource="project",
                resource_id=project_id,
            )

    def xǁTaskServiceǁ_require_project_access__mutmut_orig(
        self,
        project_id: int,
        user_id: int,
        role: str,
    ) -> None:
        project = self.project_repository.get_by_id(project_id)

        if project is None:
            raise ProjectNotFoundError(project_id)

        role_value = getattr(role, "value", role)
        is_admin = role_value == "admin"
        is_owner = project.owner_id == user_id
        is_member = any(member.id == user_id for member in project.members)

        if not (is_admin or is_owner or is_member):
            raise UnauthorizedActionError(
                action="access",
                resource="project",
                resource_id=project_id,
            )

    def xǁTaskServiceǁ_require_project_access__mutmut_1(
        self,
        project_id: int,
        user_id: int,
        role: str,
    ) -> None:
        project = None

        if project is None:
            raise ProjectNotFoundError(project_id)

        role_value = getattr(role, "value", role)
        is_admin = role_value == "admin"
        is_owner = project.owner_id == user_id
        is_member = any(member.id == user_id for member in project.members)

        if not (is_admin or is_owner or is_member):
            raise UnauthorizedActionError(
                action="access",
                resource="project",
                resource_id=project_id,
            )

    def xǁTaskServiceǁ_require_project_access__mutmut_2(
        self,
        project_id: int,
        user_id: int,
        role: str,
    ) -> None:
        project = self.project_repository.get_by_id(None)

        if project is None:
            raise ProjectNotFoundError(project_id)

        role_value = getattr(role, "value", role)
        is_admin = role_value == "admin"
        is_owner = project.owner_id == user_id
        is_member = any(member.id == user_id for member in project.members)

        if not (is_admin or is_owner or is_member):
            raise UnauthorizedActionError(
                action="access",
                resource="project",
                resource_id=project_id,
            )

    def xǁTaskServiceǁ_require_project_access__mutmut_3(
        self,
        project_id: int,
        user_id: int,
        role: str,
    ) -> None:
        project = self.project_repository.get_by_id(project_id)

        if project is not None:
            raise ProjectNotFoundError(project_id)

        role_value = getattr(role, "value", role)
        is_admin = role_value == "admin"
        is_owner = project.owner_id == user_id
        is_member = any(member.id == user_id for member in project.members)

        if not (is_admin or is_owner or is_member):
            raise UnauthorizedActionError(
                action="access",
                resource="project",
                resource_id=project_id,
            )

    def xǁTaskServiceǁ_require_project_access__mutmut_4(
        self,
        project_id: int,
        user_id: int,
        role: str,
    ) -> None:
        project = self.project_repository.get_by_id(project_id)

        if project is None:
            raise ProjectNotFoundError(None)

        role_value = getattr(role, "value", role)
        is_admin = role_value == "admin"
        is_owner = project.owner_id == user_id
        is_member = any(member.id == user_id for member in project.members)

        if not (is_admin or is_owner or is_member):
            raise UnauthorizedActionError(
                action="access",
                resource="project",
                resource_id=project_id,
            )

    def xǁTaskServiceǁ_require_project_access__mutmut_5(
        self,
        project_id: int,
        user_id: int,
        role: str,
    ) -> None:
        project = self.project_repository.get_by_id(project_id)

        if project is None:
            raise ProjectNotFoundError(project_id)

        role_value = None
        is_admin = role_value == "admin"
        is_owner = project.owner_id == user_id
        is_member = any(member.id == user_id for member in project.members)

        if not (is_admin or is_owner or is_member):
            raise UnauthorizedActionError(
                action="access",
                resource="project",
                resource_id=project_id,
            )

    def xǁTaskServiceǁ_require_project_access__mutmut_6(
        self,
        project_id: int,
        user_id: int,
        role: str,
    ) -> None:
        project = self.project_repository.get_by_id(project_id)

        if project is None:
            raise ProjectNotFoundError(project_id)

        role_value = getattr(None, "value", role)
        is_admin = role_value == "admin"
        is_owner = project.owner_id == user_id
        is_member = any(member.id == user_id for member in project.members)

        if not (is_admin or is_owner or is_member):
            raise UnauthorizedActionError(
                action="access",
                resource="project",
                resource_id=project_id,
            )

    def xǁTaskServiceǁ_require_project_access__mutmut_7(
        self,
        project_id: int,
        user_id: int,
        role: str,
    ) -> None:
        project = self.project_repository.get_by_id(project_id)

        if project is None:
            raise ProjectNotFoundError(project_id)

        role_value = getattr(role, None, role)
        is_admin = role_value == "admin"
        is_owner = project.owner_id == user_id
        is_member = any(member.id == user_id for member in project.members)

        if not (is_admin or is_owner or is_member):
            raise UnauthorizedActionError(
                action="access",
                resource="project",
                resource_id=project_id,
            )

    def xǁTaskServiceǁ_require_project_access__mutmut_8(
        self,
        project_id: int,
        user_id: int,
        role: str,
    ) -> None:
        project = self.project_repository.get_by_id(project_id)

        if project is None:
            raise ProjectNotFoundError(project_id)

        role_value = getattr(role, "value", None)
        is_admin = role_value == "admin"
        is_owner = project.owner_id == user_id
        is_member = any(member.id == user_id for member in project.members)

        if not (is_admin or is_owner or is_member):
            raise UnauthorizedActionError(
                action="access",
                resource="project",
                resource_id=project_id,
            )

    def xǁTaskServiceǁ_require_project_access__mutmut_9(
        self,
        project_id: int,
        user_id: int,
        role: str,
    ) -> None:
        project = self.project_repository.get_by_id(project_id)

        if project is None:
            raise ProjectNotFoundError(project_id)

        role_value = getattr("value", role)
        is_admin = role_value == "admin"
        is_owner = project.owner_id == user_id
        is_member = any(member.id == user_id for member in project.members)

        if not (is_admin or is_owner or is_member):
            raise UnauthorizedActionError(
                action="access",
                resource="project",
                resource_id=project_id,
            )

    def xǁTaskServiceǁ_require_project_access__mutmut_10(
        self,
        project_id: int,
        user_id: int,
        role: str,
    ) -> None:
        project = self.project_repository.get_by_id(project_id)

        if project is None:
            raise ProjectNotFoundError(project_id)

        role_value = getattr(role, role)
        is_admin = role_value == "admin"
        is_owner = project.owner_id == user_id
        is_member = any(member.id == user_id for member in project.members)

        if not (is_admin or is_owner or is_member):
            raise UnauthorizedActionError(
                action="access",
                resource="project",
                resource_id=project_id,
            )

    def xǁTaskServiceǁ_require_project_access__mutmut_11(
        self,
        project_id: int,
        user_id: int,
        role: str,
    ) -> None:
        project = self.project_repository.get_by_id(project_id)

        if project is None:
            raise ProjectNotFoundError(project_id)

        role_value = role.value
        is_admin = role_value == "admin"
        is_owner = project.owner_id == user_id
        is_member = any(member.id == user_id for member in project.members)

        if not (is_admin or is_owner or is_member):
            raise UnauthorizedActionError(
                action="access",
                resource="project",
                resource_id=project_id,
            )

    def xǁTaskServiceǁ_require_project_access__mutmut_12(
        self,
        project_id: int,
        user_id: int,
        role: str,
    ) -> None:
        project = self.project_repository.get_by_id(project_id)

        if project is None:
            raise ProjectNotFoundError(project_id)

        role_value = getattr(role, "XXvalueXX", role)
        is_admin = role_value == "admin"
        is_owner = project.owner_id == user_id
        is_member = any(member.id == user_id for member in project.members)

        if not (is_admin or is_owner or is_member):
            raise UnauthorizedActionError(
                action="access",
                resource="project",
                resource_id=project_id,
            )

    def xǁTaskServiceǁ_require_project_access__mutmut_13(
        self,
        project_id: int,
        user_id: int,
        role: str,
    ) -> None:
        project = self.project_repository.get_by_id(project_id)

        if project is None:
            raise ProjectNotFoundError(project_id)

        role_value = getattr(role, "VALUE", role)
        is_admin = role_value == "admin"
        is_owner = project.owner_id == user_id
        is_member = any(member.id == user_id for member in project.members)

        if not (is_admin or is_owner or is_member):
            raise UnauthorizedActionError(
                action="access",
                resource="project",
                resource_id=project_id,
            )

    def xǁTaskServiceǁ_require_project_access__mutmut_14(
        self,
        project_id: int,
        user_id: int,
        role: str,
    ) -> None:
        project = self.project_repository.get_by_id(project_id)

        if project is None:
            raise ProjectNotFoundError(project_id)

        role_value = getattr(role, "value", role)
        is_admin = None
        is_owner = project.owner_id == user_id
        is_member = any(member.id == user_id for member in project.members)

        if not (is_admin or is_owner or is_member):
            raise UnauthorizedActionError(
                action="access",
                resource="project",
                resource_id=project_id,
            )

    def xǁTaskServiceǁ_require_project_access__mutmut_15(
        self,
        project_id: int,
        user_id: int,
        role: str,
    ) -> None:
        project = self.project_repository.get_by_id(project_id)

        if project is None:
            raise ProjectNotFoundError(project_id)

        role_value = getattr(role, "value", role)
        is_admin = role_value != "admin"
        is_owner = project.owner_id == user_id
        is_member = any(member.id == user_id for member in project.members)

        if not (is_admin or is_owner or is_member):
            raise UnauthorizedActionError(
                action="access",
                resource="project",
                resource_id=project_id,
            )

    def xǁTaskServiceǁ_require_project_access__mutmut_16(
        self,
        project_id: int,
        user_id: int,
        role: str,
    ) -> None:
        project = self.project_repository.get_by_id(project_id)

        if project is None:
            raise ProjectNotFoundError(project_id)

        role_value = getattr(role, "value", role)
        is_admin = role_value == "XXadminXX"
        is_owner = project.owner_id == user_id
        is_member = any(member.id == user_id for member in project.members)

        if not (is_admin or is_owner or is_member):
            raise UnauthorizedActionError(
                action="access",
                resource="project",
                resource_id=project_id,
            )

    def xǁTaskServiceǁ_require_project_access__mutmut_17(
        self,
        project_id: int,
        user_id: int,
        role: str,
    ) -> None:
        project = self.project_repository.get_by_id(project_id)

        if project is None:
            raise ProjectNotFoundError(project_id)

        role_value = getattr(role, "value", role)
        is_admin = role_value == "ADMIN"
        is_owner = project.owner_id == user_id
        is_member = any(member.id == user_id for member in project.members)

        if not (is_admin or is_owner or is_member):
            raise UnauthorizedActionError(
                action="access",
                resource="project",
                resource_id=project_id,
            )

    def xǁTaskServiceǁ_require_project_access__mutmut_18(
        self,
        project_id: int,
        user_id: int,
        role: str,
    ) -> None:
        project = self.project_repository.get_by_id(project_id)

        if project is None:
            raise ProjectNotFoundError(project_id)

        role_value = getattr(role, "value", role)
        is_admin = role_value == "admin"
        is_owner = None
        is_member = any(member.id == user_id for member in project.members)

        if not (is_admin or is_owner or is_member):
            raise UnauthorizedActionError(
                action="access",
                resource="project",
                resource_id=project_id,
            )

    def xǁTaskServiceǁ_require_project_access__mutmut_19(
        self,
        project_id: int,
        user_id: int,
        role: str,
    ) -> None:
        project = self.project_repository.get_by_id(project_id)

        if project is None:
            raise ProjectNotFoundError(project_id)

        role_value = getattr(role, "value", role)
        is_admin = role_value == "admin"
        is_owner = project.owner_id != user_id
        is_member = any(member.id == user_id for member in project.members)

        if not (is_admin or is_owner or is_member):
            raise UnauthorizedActionError(
                action="access",
                resource="project",
                resource_id=project_id,
            )

    def xǁTaskServiceǁ_require_project_access__mutmut_20(
        self,
        project_id: int,
        user_id: int,
        role: str,
    ) -> None:
        project = self.project_repository.get_by_id(project_id)

        if project is None:
            raise ProjectNotFoundError(project_id)

        role_value = getattr(role, "value", role)
        is_admin = role_value == "admin"
        is_owner = project.owner_id == user_id
        is_member = None

        if not (is_admin or is_owner or is_member):
            raise UnauthorizedActionError(
                action="access",
                resource="project",
                resource_id=project_id,
            )

    def xǁTaskServiceǁ_require_project_access__mutmut_21(
        self,
        project_id: int,
        user_id: int,
        role: str,
    ) -> None:
        project = self.project_repository.get_by_id(project_id)

        if project is None:
            raise ProjectNotFoundError(project_id)

        role_value = getattr(role, "value", role)
        is_admin = role_value == "admin"
        is_owner = project.owner_id == user_id
        is_member = any(None)

        if not (is_admin or is_owner or is_member):
            raise UnauthorizedActionError(
                action="access",
                resource="project",
                resource_id=project_id,
            )

    def xǁTaskServiceǁ_require_project_access__mutmut_22(
        self,
        project_id: int,
        user_id: int,
        role: str,
    ) -> None:
        project = self.project_repository.get_by_id(project_id)

        if project is None:
            raise ProjectNotFoundError(project_id)

        role_value = getattr(role, "value", role)
        is_admin = role_value == "admin"
        is_owner = project.owner_id == user_id
        is_member = any(member.id != user_id for member in project.members)

        if not (is_admin or is_owner or is_member):
            raise UnauthorizedActionError(
                action="access",
                resource="project",
                resource_id=project_id,
            )

    def xǁTaskServiceǁ_require_project_access__mutmut_23(
        self,
        project_id: int,
        user_id: int,
        role: str,
    ) -> None:
        project = self.project_repository.get_by_id(project_id)

        if project is None:
            raise ProjectNotFoundError(project_id)

        role_value = getattr(role, "value", role)
        is_admin = role_value == "admin"
        is_owner = project.owner_id == user_id
        is_member = any(member.id == user_id for member in project.members)

        if is_admin or is_owner or is_member:
            raise UnauthorizedActionError(
                action="access",
                resource="project",
                resource_id=project_id,
            )

    def xǁTaskServiceǁ_require_project_access__mutmut_24(
        self,
        project_id: int,
        user_id: int,
        role: str,
    ) -> None:
        project = self.project_repository.get_by_id(project_id)

        if project is None:
            raise ProjectNotFoundError(project_id)

        role_value = getattr(role, "value", role)
        is_admin = role_value == "admin"
        is_owner = project.owner_id == user_id
        is_member = any(member.id == user_id for member in project.members)

        if not (is_admin or is_owner and is_member):
            raise UnauthorizedActionError(
                action="access",
                resource="project",
                resource_id=project_id,
            )

    def xǁTaskServiceǁ_require_project_access__mutmut_25(
        self,
        project_id: int,
        user_id: int,
        role: str,
    ) -> None:
        project = self.project_repository.get_by_id(project_id)

        if project is None:
            raise ProjectNotFoundError(project_id)

        role_value = getattr(role, "value", role)
        is_admin = role_value == "admin"
        is_owner = project.owner_id == user_id
        is_member = any(member.id == user_id for member in project.members)

        if not (is_admin and is_owner or is_member):
            raise UnauthorizedActionError(
                action="access",
                resource="project",
                resource_id=project_id,
            )

    def xǁTaskServiceǁ_require_project_access__mutmut_26(
        self,
        project_id: int,
        user_id: int,
        role: str,
    ) -> None:
        project = self.project_repository.get_by_id(project_id)

        if project is None:
            raise ProjectNotFoundError(project_id)

        role_value = getattr(role, "value", role)
        is_admin = role_value == "admin"
        is_owner = project.owner_id == user_id
        is_member = any(member.id == user_id for member in project.members)

        if not (is_admin or is_owner or is_member):
            raise UnauthorizedActionError(
                action=None,
                resource="project",
                resource_id=project_id,
            )

    def xǁTaskServiceǁ_require_project_access__mutmut_27(
        self,
        project_id: int,
        user_id: int,
        role: str,
    ) -> None:
        project = self.project_repository.get_by_id(project_id)

        if project is None:
            raise ProjectNotFoundError(project_id)

        role_value = getattr(role, "value", role)
        is_admin = role_value == "admin"
        is_owner = project.owner_id == user_id
        is_member = any(member.id == user_id for member in project.members)

        if not (is_admin or is_owner or is_member):
            raise UnauthorizedActionError(
                action="access",
                resource=None,
                resource_id=project_id,
            )

    def xǁTaskServiceǁ_require_project_access__mutmut_28(
        self,
        project_id: int,
        user_id: int,
        role: str,
    ) -> None:
        project = self.project_repository.get_by_id(project_id)

        if project is None:
            raise ProjectNotFoundError(project_id)

        role_value = getattr(role, "value", role)
        is_admin = role_value == "admin"
        is_owner = project.owner_id == user_id
        is_member = any(member.id == user_id for member in project.members)

        if not (is_admin or is_owner or is_member):
            raise UnauthorizedActionError(
                action="access",
                resource="project",
                resource_id=None,
            )

    def xǁTaskServiceǁ_require_project_access__mutmut_29(
        self,
        project_id: int,
        user_id: int,
        role: str,
    ) -> None:
        project = self.project_repository.get_by_id(project_id)

        if project is None:
            raise ProjectNotFoundError(project_id)

        role_value = getattr(role, "value", role)
        is_admin = role_value == "admin"
        is_owner = project.owner_id == user_id
        is_member = any(member.id == user_id for member in project.members)

        if not (is_admin or is_owner or is_member):
            raise UnauthorizedActionError(
                resource="project",
                resource_id=project_id,
            )

    def xǁTaskServiceǁ_require_project_access__mutmut_30(
        self,
        project_id: int,
        user_id: int,
        role: str,
    ) -> None:
        project = self.project_repository.get_by_id(project_id)

        if project is None:
            raise ProjectNotFoundError(project_id)

        role_value = getattr(role, "value", role)
        is_admin = role_value == "admin"
        is_owner = project.owner_id == user_id
        is_member = any(member.id == user_id for member in project.members)

        if not (is_admin or is_owner or is_member):
            raise UnauthorizedActionError(
                action="access",
                resource_id=project_id,
            )

    def xǁTaskServiceǁ_require_project_access__mutmut_31(
        self,
        project_id: int,
        user_id: int,
        role: str,
    ) -> None:
        project = self.project_repository.get_by_id(project_id)

        if project is None:
            raise ProjectNotFoundError(project_id)

        role_value = getattr(role, "value", role)
        is_admin = role_value == "admin"
        is_owner = project.owner_id == user_id
        is_member = any(member.id == user_id for member in project.members)

        if not (is_admin or is_owner or is_member):
            raise UnauthorizedActionError(
                action="access",
                resource="project",
            )

    def xǁTaskServiceǁ_require_project_access__mutmut_32(
        self,
        project_id: int,
        user_id: int,
        role: str,
    ) -> None:
        project = self.project_repository.get_by_id(project_id)

        if project is None:
            raise ProjectNotFoundError(project_id)

        role_value = getattr(role, "value", role)
        is_admin = role_value == "admin"
        is_owner = project.owner_id == user_id
        is_member = any(member.id == user_id for member in project.members)

        if not (is_admin or is_owner or is_member):
            raise UnauthorizedActionError(
                action="XXaccessXX",
                resource="project",
                resource_id=project_id,
            )

    def xǁTaskServiceǁ_require_project_access__mutmut_33(
        self,
        project_id: int,
        user_id: int,
        role: str,
    ) -> None:
        project = self.project_repository.get_by_id(project_id)

        if project is None:
            raise ProjectNotFoundError(project_id)

        role_value = getattr(role, "value", role)
        is_admin = role_value == "admin"
        is_owner = project.owner_id == user_id
        is_member = any(member.id == user_id for member in project.members)

        if not (is_admin or is_owner or is_member):
            raise UnauthorizedActionError(
                action="ACCESS",
                resource="project",
                resource_id=project_id,
            )

    def xǁTaskServiceǁ_require_project_access__mutmut_34(
        self,
        project_id: int,
        user_id: int,
        role: str,
    ) -> None:
        project = self.project_repository.get_by_id(project_id)

        if project is None:
            raise ProjectNotFoundError(project_id)

        role_value = getattr(role, "value", role)
        is_admin = role_value == "admin"
        is_owner = project.owner_id == user_id
        is_member = any(member.id == user_id for member in project.members)

        if not (is_admin or is_owner or is_member):
            raise UnauthorizedActionError(
                action="access",
                resource="XXprojectXX",
                resource_id=project_id,
            )

    def xǁTaskServiceǁ_require_project_access__mutmut_35(
        self,
        project_id: int,
        user_id: int,
        role: str,
    ) -> None:
        project = self.project_repository.get_by_id(project_id)

        if project is None:
            raise ProjectNotFoundError(project_id)

        role_value = getattr(role, "value", role)
        is_admin = role_value == "admin"
        is_owner = project.owner_id == user_id
        is_member = any(member.id == user_id for member in project.members)

        if not (is_admin or is_owner or is_member):
            raise UnauthorizedActionError(
                action="access",
                resource="PROJECT",
                resource_id=project_id,
            )

    @_mutmut_mutated(mutants_xǁTaskServiceǁcreate__mutmut)
    def create(self, payload: TaskCreate, *, user_id: int, role: str):
        self._require_project_access(payload.project_id, user_id, role)
        return self.task_repository.create(payload, created_by=user_id)

    def xǁTaskServiceǁcreate__mutmut_orig(self, payload: TaskCreate, *, user_id: int, role: str):
        self._require_project_access(payload.project_id, user_id, role)
        return self.task_repository.create(payload, created_by=user_id)

    def xǁTaskServiceǁcreate__mutmut_1(self, payload: TaskCreate, *, user_id: int, role: str):
        self._require_project_access(None, user_id, role)
        return self.task_repository.create(payload, created_by=user_id)

    def xǁTaskServiceǁcreate__mutmut_2(self, payload: TaskCreate, *, user_id: int, role: str):
        self._require_project_access(payload.project_id, None, role)
        return self.task_repository.create(payload, created_by=user_id)

    def xǁTaskServiceǁcreate__mutmut_3(self, payload: TaskCreate, *, user_id: int, role: str):
        self._require_project_access(payload.project_id, user_id, None)
        return self.task_repository.create(payload, created_by=user_id)

    def xǁTaskServiceǁcreate__mutmut_4(self, payload: TaskCreate, *, user_id: int, role: str):
        self._require_project_access(user_id, role)
        return self.task_repository.create(payload, created_by=user_id)

    def xǁTaskServiceǁcreate__mutmut_5(self, payload: TaskCreate, *, user_id: int, role: str):
        self._require_project_access(payload.project_id, role)
        return self.task_repository.create(payload, created_by=user_id)

    def xǁTaskServiceǁcreate__mutmut_6(self, payload: TaskCreate, *, user_id: int, role: str):
        self._require_project_access(
            payload.project_id,
            user_id,
        )
        return self.task_repository.create(payload, created_by=user_id)

    def xǁTaskServiceǁcreate__mutmut_7(self, payload: TaskCreate, *, user_id: int, role: str):
        self._require_project_access(payload.project_id, user_id, role)
        return self.task_repository.create(None, created_by=user_id)

    def xǁTaskServiceǁcreate__mutmut_8(self, payload: TaskCreate, *, user_id: int, role: str):
        self._require_project_access(payload.project_id, user_id, role)
        return self.task_repository.create(payload, created_by=None)

    def xǁTaskServiceǁcreate__mutmut_9(self, payload: TaskCreate, *, user_id: int, role: str):
        self._require_project_access(payload.project_id, user_id, role)
        return self.task_repository.create(created_by=user_id)

    def xǁTaskServiceǁcreate__mutmut_10(self, payload: TaskCreate, *, user_id: int, role: str):
        self._require_project_access(payload.project_id, user_id, role)
        return self.task_repository.create(
            payload,
        )

    @_mutmut_mutated(mutants_xǁTaskServiceǁlist__mutmut)
    def list(
        self,
        *,
        user_id: int,
        role: str,
        status_filter: TaskStatus | None = None,
        priority: TaskPriority | None = None,
        project_id: int | None = None,
        search: str | None = None,
        skip: int = 0,
        limit: int = 20,
    ):
        role_value = getattr(role, "value", role)

        return self.task_repository.get_all(
            owner_id=user_id,
            is_admin=(role_value == "admin"),
            status_filter=status_filter,
            priority=priority,
            project_id=project_id,
            search=search,
            skip=skip,
            limit=limit,
        )

    def xǁTaskServiceǁlist__mutmut_orig(
        self,
        *,
        user_id: int,
        role: str,
        status_filter: TaskStatus | None = None,
        priority: TaskPriority | None = None,
        project_id: int | None = None,
        search: str | None = None,
        skip: int = 0,
        limit: int = 20,
    ):
        role_value = getattr(role, "value", role)

        return self.task_repository.get_all(
            owner_id=user_id,
            is_admin=(role_value == "admin"),
            status_filter=status_filter,
            priority=priority,
            project_id=project_id,
            search=search,
            skip=skip,
            limit=limit,
        )

    def xǁTaskServiceǁlist__mutmut_1(
        self,
        *,
        user_id: int,
        role: str,
        status_filter: TaskStatus | None = None,
        priority: TaskPriority | None = None,
        project_id: int | None = None,
        search: str | None = None,
        skip: int = 1,
        limit: int = 20,
    ):
        role_value = getattr(role, "value", role)

        return self.task_repository.get_all(
            owner_id=user_id,
            is_admin=(role_value == "admin"),
            status_filter=status_filter,
            priority=priority,
            project_id=project_id,
            search=search,
            skip=skip,
            limit=limit,
        )

    def xǁTaskServiceǁlist__mutmut_2(
        self,
        *,
        user_id: int,
        role: str,
        status_filter: TaskStatus | None = None,
        priority: TaskPriority | None = None,
        project_id: int | None = None,
        search: str | None = None,
        skip: int = 0,
        limit: int = 21,
    ):
        role_value = getattr(role, "value", role)

        return self.task_repository.get_all(
            owner_id=user_id,
            is_admin=(role_value == "admin"),
            status_filter=status_filter,
            priority=priority,
            project_id=project_id,
            search=search,
            skip=skip,
            limit=limit,
        )

    def xǁTaskServiceǁlist__mutmut_3(
        self,
        *,
        user_id: int,
        role: str,
        status_filter: TaskStatus | None = None,
        priority: TaskPriority | None = None,
        project_id: int | None = None,
        search: str | None = None,
        skip: int = 0,
        limit: int = 20,
    ):
        role_value = None

        return self.task_repository.get_all(
            owner_id=user_id,
            is_admin=(role_value == "admin"),
            status_filter=status_filter,
            priority=priority,
            project_id=project_id,
            search=search,
            skip=skip,
            limit=limit,
        )

    def xǁTaskServiceǁlist__mutmut_4(
        self,
        *,
        user_id: int,
        role: str,
        status_filter: TaskStatus | None = None,
        priority: TaskPriority | None = None,
        project_id: int | None = None,
        search: str | None = None,
        skip: int = 0,
        limit: int = 20,
    ):
        role_value = getattr(None, "value", role)

        return self.task_repository.get_all(
            owner_id=user_id,
            is_admin=(role_value == "admin"),
            status_filter=status_filter,
            priority=priority,
            project_id=project_id,
            search=search,
            skip=skip,
            limit=limit,
        )

    def xǁTaskServiceǁlist__mutmut_5(
        self,
        *,
        user_id: int,
        role: str,
        status_filter: TaskStatus | None = None,
        priority: TaskPriority | None = None,
        project_id: int | None = None,
        search: str | None = None,
        skip: int = 0,
        limit: int = 20,
    ):
        role_value = getattr(role, None, role)

        return self.task_repository.get_all(
            owner_id=user_id,
            is_admin=(role_value == "admin"),
            status_filter=status_filter,
            priority=priority,
            project_id=project_id,
            search=search,
            skip=skip,
            limit=limit,
        )

    def xǁTaskServiceǁlist__mutmut_6(
        self,
        *,
        user_id: int,
        role: str,
        status_filter: TaskStatus | None = None,
        priority: TaskPriority | None = None,
        project_id: int | None = None,
        search: str | None = None,
        skip: int = 0,
        limit: int = 20,
    ):
        role_value = getattr(role, "value", None)

        return self.task_repository.get_all(
            owner_id=user_id,
            is_admin=(role_value == "admin"),
            status_filter=status_filter,
            priority=priority,
            project_id=project_id,
            search=search,
            skip=skip,
            limit=limit,
        )

    def xǁTaskServiceǁlist__mutmut_7(
        self,
        *,
        user_id: int,
        role: str,
        status_filter: TaskStatus | None = None,
        priority: TaskPriority | None = None,
        project_id: int | None = None,
        search: str | None = None,
        skip: int = 0,
        limit: int = 20,
    ):
        role_value = getattr("value", role)

        return self.task_repository.get_all(
            owner_id=user_id,
            is_admin=(role_value == "admin"),
            status_filter=status_filter,
            priority=priority,
            project_id=project_id,
            search=search,
            skip=skip,
            limit=limit,
        )

    def xǁTaskServiceǁlist__mutmut_8(
        self,
        *,
        user_id: int,
        role: str,
        status_filter: TaskStatus | None = None,
        priority: TaskPriority | None = None,
        project_id: int | None = None,
        search: str | None = None,
        skip: int = 0,
        limit: int = 20,
    ):
        role_value = getattr(role, role)

        return self.task_repository.get_all(
            owner_id=user_id,
            is_admin=(role_value == "admin"),
            status_filter=status_filter,
            priority=priority,
            project_id=project_id,
            search=search,
            skip=skip,
            limit=limit,
        )

    def xǁTaskServiceǁlist__mutmut_9(
        self,
        *,
        user_id: int,
        role: str,
        status_filter: TaskStatus | None = None,
        priority: TaskPriority | None = None,
        project_id: int | None = None,
        search: str | None = None,
        skip: int = 0,
        limit: int = 20,
    ):
        role_value = role.value

        return self.task_repository.get_all(
            owner_id=user_id,
            is_admin=(role_value == "admin"),
            status_filter=status_filter,
            priority=priority,
            project_id=project_id,
            search=search,
            skip=skip,
            limit=limit,
        )

    def xǁTaskServiceǁlist__mutmut_10(
        self,
        *,
        user_id: int,
        role: str,
        status_filter: TaskStatus | None = None,
        priority: TaskPriority | None = None,
        project_id: int | None = None,
        search: str | None = None,
        skip: int = 0,
        limit: int = 20,
    ):
        role_value = getattr(role, "XXvalueXX", role)

        return self.task_repository.get_all(
            owner_id=user_id,
            is_admin=(role_value == "admin"),
            status_filter=status_filter,
            priority=priority,
            project_id=project_id,
            search=search,
            skip=skip,
            limit=limit,
        )

    def xǁTaskServiceǁlist__mutmut_11(
        self,
        *,
        user_id: int,
        role: str,
        status_filter: TaskStatus | None = None,
        priority: TaskPriority | None = None,
        project_id: int | None = None,
        search: str | None = None,
        skip: int = 0,
        limit: int = 20,
    ):
        role_value = getattr(role, "VALUE", role)

        return self.task_repository.get_all(
            owner_id=user_id,
            is_admin=(role_value == "admin"),
            status_filter=status_filter,
            priority=priority,
            project_id=project_id,
            search=search,
            skip=skip,
            limit=limit,
        )

    def xǁTaskServiceǁlist__mutmut_12(
        self,
        *,
        user_id: int,
        role: str,
        status_filter: TaskStatus | None = None,
        priority: TaskPriority | None = None,
        project_id: int | None = None,
        search: str | None = None,
        skip: int = 0,
        limit: int = 20,
    ):
        role_value = getattr(role, "value", role)

        return self.task_repository.get_all(
            owner_id=None,
            is_admin=(role_value == "admin"),
            status_filter=status_filter,
            priority=priority,
            project_id=project_id,
            search=search,
            skip=skip,
            limit=limit,
        )

    def xǁTaskServiceǁlist__mutmut_13(
        self,
        *,
        user_id: int,
        role: str,
        status_filter: TaskStatus | None = None,
        priority: TaskPriority | None = None,
        project_id: int | None = None,
        search: str | None = None,
        skip: int = 0,
        limit: int = 20,
    ):
        role_value = getattr(role, "value", role)

        return self.task_repository.get_all(
            owner_id=user_id,
            is_admin=None,
            status_filter=status_filter,
            priority=priority,
            project_id=project_id,
            search=search,
            skip=skip,
            limit=limit,
        )

    def xǁTaskServiceǁlist__mutmut_14(
        self,
        *,
        user_id: int,
        role: str,
        status_filter: TaskStatus | None = None,
        priority: TaskPriority | None = None,
        project_id: int | None = None,
        search: str | None = None,
        skip: int = 0,
        limit: int = 20,
    ):
        role_value = getattr(role, "value", role)

        return self.task_repository.get_all(
            owner_id=user_id,
            is_admin=(role_value == "admin"),
            status_filter=None,
            priority=priority,
            project_id=project_id,
            search=search,
            skip=skip,
            limit=limit,
        )

    def xǁTaskServiceǁlist__mutmut_15(
        self,
        *,
        user_id: int,
        role: str,
        status_filter: TaskStatus | None = None,
        priority: TaskPriority | None = None,
        project_id: int | None = None,
        search: str | None = None,
        skip: int = 0,
        limit: int = 20,
    ):
        role_value = getattr(role, "value", role)

        return self.task_repository.get_all(
            owner_id=user_id,
            is_admin=(role_value == "admin"),
            status_filter=status_filter,
            priority=None,
            project_id=project_id,
            search=search,
            skip=skip,
            limit=limit,
        )

    def xǁTaskServiceǁlist__mutmut_16(
        self,
        *,
        user_id: int,
        role: str,
        status_filter: TaskStatus | None = None,
        priority: TaskPriority | None = None,
        project_id: int | None = None,
        search: str | None = None,
        skip: int = 0,
        limit: int = 20,
    ):
        role_value = getattr(role, "value", role)

        return self.task_repository.get_all(
            owner_id=user_id,
            is_admin=(role_value == "admin"),
            status_filter=status_filter,
            priority=priority,
            project_id=None,
            search=search,
            skip=skip,
            limit=limit,
        )

    def xǁTaskServiceǁlist__mutmut_17(
        self,
        *,
        user_id: int,
        role: str,
        status_filter: TaskStatus | None = None,
        priority: TaskPriority | None = None,
        project_id: int | None = None,
        search: str | None = None,
        skip: int = 0,
        limit: int = 20,
    ):
        role_value = getattr(role, "value", role)

        return self.task_repository.get_all(
            owner_id=user_id,
            is_admin=(role_value == "admin"),
            status_filter=status_filter,
            priority=priority,
            project_id=project_id,
            search=None,
            skip=skip,
            limit=limit,
        )

    def xǁTaskServiceǁlist__mutmut_18(
        self,
        *,
        user_id: int,
        role: str,
        status_filter: TaskStatus | None = None,
        priority: TaskPriority | None = None,
        project_id: int | None = None,
        search: str | None = None,
        skip: int = 0,
        limit: int = 20,
    ):
        role_value = getattr(role, "value", role)

        return self.task_repository.get_all(
            owner_id=user_id,
            is_admin=(role_value == "admin"),
            status_filter=status_filter,
            priority=priority,
            project_id=project_id,
            search=search,
            skip=None,
            limit=limit,
        )

    def xǁTaskServiceǁlist__mutmut_19(
        self,
        *,
        user_id: int,
        role: str,
        status_filter: TaskStatus | None = None,
        priority: TaskPriority | None = None,
        project_id: int | None = None,
        search: str | None = None,
        skip: int = 0,
        limit: int = 20,
    ):
        role_value = getattr(role, "value", role)

        return self.task_repository.get_all(
            owner_id=user_id,
            is_admin=(role_value == "admin"),
            status_filter=status_filter,
            priority=priority,
            project_id=project_id,
            search=search,
            skip=skip,
            limit=None,
        )

    def xǁTaskServiceǁlist__mutmut_20(
        self,
        *,
        user_id: int,
        role: str,
        status_filter: TaskStatus | None = None,
        priority: TaskPriority | None = None,
        project_id: int | None = None,
        search: str | None = None,
        skip: int = 0,
        limit: int = 20,
    ):
        role_value = getattr(role, "value", role)

        return self.task_repository.get_all(
            is_admin=(role_value == "admin"),
            status_filter=status_filter,
            priority=priority,
            project_id=project_id,
            search=search,
            skip=skip,
            limit=limit,
        )

    def xǁTaskServiceǁlist__mutmut_21(
        self,
        *,
        user_id: int,
        role: str,
        status_filter: TaskStatus | None = None,
        priority: TaskPriority | None = None,
        project_id: int | None = None,
        search: str | None = None,
        skip: int = 0,
        limit: int = 20,
    ):
        role_value = getattr(role, "value", role)

        return self.task_repository.get_all(
            owner_id=user_id,
            status_filter=status_filter,
            priority=priority,
            project_id=project_id,
            search=search,
            skip=skip,
            limit=limit,
        )

    def xǁTaskServiceǁlist__mutmut_22(
        self,
        *,
        user_id: int,
        role: str,
        status_filter: TaskStatus | None = None,
        priority: TaskPriority | None = None,
        project_id: int | None = None,
        search: str | None = None,
        skip: int = 0,
        limit: int = 20,
    ):
        role_value = getattr(role, "value", role)

        return self.task_repository.get_all(
            owner_id=user_id,
            is_admin=(role_value == "admin"),
            priority=priority,
            project_id=project_id,
            search=search,
            skip=skip,
            limit=limit,
        )

    def xǁTaskServiceǁlist__mutmut_23(
        self,
        *,
        user_id: int,
        role: str,
        status_filter: TaskStatus | None = None,
        priority: TaskPriority | None = None,
        project_id: int | None = None,
        search: str | None = None,
        skip: int = 0,
        limit: int = 20,
    ):
        role_value = getattr(role, "value", role)

        return self.task_repository.get_all(
            owner_id=user_id,
            is_admin=(role_value == "admin"),
            status_filter=status_filter,
            project_id=project_id,
            search=search,
            skip=skip,
            limit=limit,
        )

    def xǁTaskServiceǁlist__mutmut_24(
        self,
        *,
        user_id: int,
        role: str,
        status_filter: TaskStatus | None = None,
        priority: TaskPriority | None = None,
        project_id: int | None = None,
        search: str | None = None,
        skip: int = 0,
        limit: int = 20,
    ):
        role_value = getattr(role, "value", role)

        return self.task_repository.get_all(
            owner_id=user_id,
            is_admin=(role_value == "admin"),
            status_filter=status_filter,
            priority=priority,
            search=search,
            skip=skip,
            limit=limit,
        )

    def xǁTaskServiceǁlist__mutmut_25(
        self,
        *,
        user_id: int,
        role: str,
        status_filter: TaskStatus | None = None,
        priority: TaskPriority | None = None,
        project_id: int | None = None,
        search: str | None = None,
        skip: int = 0,
        limit: int = 20,
    ):
        role_value = getattr(role, "value", role)

        return self.task_repository.get_all(
            owner_id=user_id,
            is_admin=(role_value == "admin"),
            status_filter=status_filter,
            priority=priority,
            project_id=project_id,
            skip=skip,
            limit=limit,
        )

    def xǁTaskServiceǁlist__mutmut_26(
        self,
        *,
        user_id: int,
        role: str,
        status_filter: TaskStatus | None = None,
        priority: TaskPriority | None = None,
        project_id: int | None = None,
        search: str | None = None,
        skip: int = 0,
        limit: int = 20,
    ):
        role_value = getattr(role, "value", role)

        return self.task_repository.get_all(
            owner_id=user_id,
            is_admin=(role_value == "admin"),
            status_filter=status_filter,
            priority=priority,
            project_id=project_id,
            search=search,
            limit=limit,
        )

    def xǁTaskServiceǁlist__mutmut_27(
        self,
        *,
        user_id: int,
        role: str,
        status_filter: TaskStatus | None = None,
        priority: TaskPriority | None = None,
        project_id: int | None = None,
        search: str | None = None,
        skip: int = 0,
        limit: int = 20,
    ):
        role_value = getattr(role, "value", role)

        return self.task_repository.get_all(
            owner_id=user_id,
            is_admin=(role_value == "admin"),
            status_filter=status_filter,
            priority=priority,
            project_id=project_id,
            search=search,
            skip=skip,
        )

    def xǁTaskServiceǁlist__mutmut_28(
        self,
        *,
        user_id: int,
        role: str,
        status_filter: TaskStatus | None = None,
        priority: TaskPriority | None = None,
        project_id: int | None = None,
        search: str | None = None,
        skip: int = 0,
        limit: int = 20,
    ):
        role_value = getattr(role, "value", role)

        return self.task_repository.get_all(
            owner_id=user_id,
            is_admin=(role_value != "admin"),
            status_filter=status_filter,
            priority=priority,
            project_id=project_id,
            search=search,
            skip=skip,
            limit=limit,
        )

    def xǁTaskServiceǁlist__mutmut_29(
        self,
        *,
        user_id: int,
        role: str,
        status_filter: TaskStatus | None = None,
        priority: TaskPriority | None = None,
        project_id: int | None = None,
        search: str | None = None,
        skip: int = 0,
        limit: int = 20,
    ):
        role_value = getattr(role, "value", role)

        return self.task_repository.get_all(
            owner_id=user_id,
            is_admin=(role_value == "XXadminXX"),
            status_filter=status_filter,
            priority=priority,
            project_id=project_id,
            search=search,
            skip=skip,
            limit=limit,
        )

    def xǁTaskServiceǁlist__mutmut_30(
        self,
        *,
        user_id: int,
        role: str,
        status_filter: TaskStatus | None = None,
        priority: TaskPriority | None = None,
        project_id: int | None = None,
        search: str | None = None,
        skip: int = 0,
        limit: int = 20,
    ):
        role_value = getattr(role, "value", role)

        return self.task_repository.get_all(
            owner_id=user_id,
            is_admin=(role_value == "ADMIN"),
            status_filter=status_filter,
            priority=priority,
            project_id=project_id,
            search=search,
            skip=skip,
            limit=limit,
        )

    @_mutmut_mutated(mutants_xǁTaskServiceǁget__mutmut)
    def get(self, task_id: int, *, user_id: int, role: str):
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_project_access(task.project_id, user_id, role)
        return task

    def xǁTaskServiceǁget__mutmut_orig(self, task_id: int, *, user_id: int, role: str):
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_project_access(task.project_id, user_id, role)
        return task

    def xǁTaskServiceǁget__mutmut_1(self, task_id: int, *, user_id: int, role: str):
        task = None

        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_project_access(task.project_id, user_id, role)
        return task

    def xǁTaskServiceǁget__mutmut_2(self, task_id: int, *, user_id: int, role: str):
        task = self.task_repository.get_by_id(None)

        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_project_access(task.project_id, user_id, role)
        return task

    def xǁTaskServiceǁget__mutmut_3(self, task_id: int, *, user_id: int, role: str):
        task = self.task_repository.get_by_id(task_id)

        if task is not None:
            raise TaskNotFoundError(task_id)

        self._require_project_access(task.project_id, user_id, role)
        return task

    def xǁTaskServiceǁget__mutmut_4(self, task_id: int, *, user_id: int, role: str):
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(None)

        self._require_project_access(task.project_id, user_id, role)
        return task

    def xǁTaskServiceǁget__mutmut_5(self, task_id: int, *, user_id: int, role: str):
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_project_access(None, user_id, role)
        return task

    def xǁTaskServiceǁget__mutmut_6(self, task_id: int, *, user_id: int, role: str):
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_project_access(task.project_id, None, role)
        return task

    def xǁTaskServiceǁget__mutmut_7(self, task_id: int, *, user_id: int, role: str):
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_project_access(task.project_id, user_id, None)
        return task

    def xǁTaskServiceǁget__mutmut_8(self, task_id: int, *, user_id: int, role: str):
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_project_access(user_id, role)
        return task

    def xǁTaskServiceǁget__mutmut_9(self, task_id: int, *, user_id: int, role: str):
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_project_access(task.project_id, role)
        return task

    def xǁTaskServiceǁget__mutmut_10(self, task_id: int, *, user_id: int, role: str):
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_project_access(
            task.project_id,
            user_id,
        )
        return task

    @_mutmut_mutated(mutants_xǁTaskServiceǁupdate__mutmut)
    def update(
        self,
        task_id: int,
        payload: TaskUpdate,
        *,
        user_id: int,
        role: str,
    ):
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_task_update_access(
            task,
            user_id=user_id,
            role=role,
        )

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        if payload.status != task.status:
            if payload.status == TaskStatus.archived or not can_transition_task_status(
                task.status,
                payload.status,
            ):
                raise TaskStateConflictError(
                    task.status.value,
                    payload.status.value,
                )

        return self.task_repository.update(task, payload)

    def xǁTaskServiceǁupdate__mutmut_orig(
        self,
        task_id: int,
        payload: TaskUpdate,
        *,
        user_id: int,
        role: str,
    ):
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_task_update_access(
            task,
            user_id=user_id,
            role=role,
        )

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        if payload.status != task.status:
            if payload.status == TaskStatus.archived or not can_transition_task_status(
                task.status,
                payload.status,
            ):
                raise TaskStateConflictError(
                    task.status.value,
                    payload.status.value,
                )

        return self.task_repository.update(task, payload)

    def xǁTaskServiceǁupdate__mutmut_1(
        self,
        task_id: int,
        payload: TaskUpdate,
        *,
        user_id: int,
        role: str,
    ):
        task = None

        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_task_update_access(
            task,
            user_id=user_id,
            role=role,
        )

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        if payload.status != task.status:
            if payload.status == TaskStatus.archived or not can_transition_task_status(
                task.status,
                payload.status,
            ):
                raise TaskStateConflictError(
                    task.status.value,
                    payload.status.value,
                )

        return self.task_repository.update(task, payload)

    def xǁTaskServiceǁupdate__mutmut_2(
        self,
        task_id: int,
        payload: TaskUpdate,
        *,
        user_id: int,
        role: str,
    ):
        task = self.task_repository.get_by_id(None)

        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_task_update_access(
            task,
            user_id=user_id,
            role=role,
        )

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        if payload.status != task.status:
            if payload.status == TaskStatus.archived or not can_transition_task_status(
                task.status,
                payload.status,
            ):
                raise TaskStateConflictError(
                    task.status.value,
                    payload.status.value,
                )

        return self.task_repository.update(task, payload)

    def xǁTaskServiceǁupdate__mutmut_3(
        self,
        task_id: int,
        payload: TaskUpdate,
        *,
        user_id: int,
        role: str,
    ):
        task = self.task_repository.get_by_id(task_id)

        if task is not None:
            raise TaskNotFoundError(task_id)

        self._require_task_update_access(
            task,
            user_id=user_id,
            role=role,
        )

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        if payload.status != task.status:
            if payload.status == TaskStatus.archived or not can_transition_task_status(
                task.status,
                payload.status,
            ):
                raise TaskStateConflictError(
                    task.status.value,
                    payload.status.value,
                )

        return self.task_repository.update(task, payload)

    def xǁTaskServiceǁupdate__mutmut_4(
        self,
        task_id: int,
        payload: TaskUpdate,
        *,
        user_id: int,
        role: str,
    ):
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(None)

        self._require_task_update_access(
            task,
            user_id=user_id,
            role=role,
        )

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        if payload.status != task.status:
            if payload.status == TaskStatus.archived or not can_transition_task_status(
                task.status,
                payload.status,
            ):
                raise TaskStateConflictError(
                    task.status.value,
                    payload.status.value,
                )

        return self.task_repository.update(task, payload)

    def xǁTaskServiceǁupdate__mutmut_5(
        self,
        task_id: int,
        payload: TaskUpdate,
        *,
        user_id: int,
        role: str,
    ):
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_task_update_access(
            None,
            user_id=user_id,
            role=role,
        )

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        if payload.status != task.status:
            if payload.status == TaskStatus.archived or not can_transition_task_status(
                task.status,
                payload.status,
            ):
                raise TaskStateConflictError(
                    task.status.value,
                    payload.status.value,
                )

        return self.task_repository.update(task, payload)

    def xǁTaskServiceǁupdate__mutmut_6(
        self,
        task_id: int,
        payload: TaskUpdate,
        *,
        user_id: int,
        role: str,
    ):
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_task_update_access(
            task,
            user_id=None,
            role=role,
        )

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        if payload.status != task.status:
            if payload.status == TaskStatus.archived or not can_transition_task_status(
                task.status,
                payload.status,
            ):
                raise TaskStateConflictError(
                    task.status.value,
                    payload.status.value,
                )

        return self.task_repository.update(task, payload)

    def xǁTaskServiceǁupdate__mutmut_7(
        self,
        task_id: int,
        payload: TaskUpdate,
        *,
        user_id: int,
        role: str,
    ):
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_task_update_access(
            task,
            user_id=user_id,
            role=None,
        )

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        if payload.status != task.status:
            if payload.status == TaskStatus.archived or not can_transition_task_status(
                task.status,
                payload.status,
            ):
                raise TaskStateConflictError(
                    task.status.value,
                    payload.status.value,
                )

        return self.task_repository.update(task, payload)

    def xǁTaskServiceǁupdate__mutmut_8(
        self,
        task_id: int,
        payload: TaskUpdate,
        *,
        user_id: int,
        role: str,
    ):
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_task_update_access(
            user_id=user_id,
            role=role,
        )

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        if payload.status != task.status:
            if payload.status == TaskStatus.archived or not can_transition_task_status(
                task.status,
                payload.status,
            ):
                raise TaskStateConflictError(
                    task.status.value,
                    payload.status.value,
                )

        return self.task_repository.update(task, payload)

    def xǁTaskServiceǁupdate__mutmut_9(
        self,
        task_id: int,
        payload: TaskUpdate,
        *,
        user_id: int,
        role: str,
    ):
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_task_update_access(
            task,
            role=role,
        )

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        if payload.status != task.status:
            if payload.status == TaskStatus.archived or not can_transition_task_status(
                task.status,
                payload.status,
            ):
                raise TaskStateConflictError(
                    task.status.value,
                    payload.status.value,
                )

        return self.task_repository.update(task, payload)

    def xǁTaskServiceǁupdate__mutmut_10(
        self,
        task_id: int,
        payload: TaskUpdate,
        *,
        user_id: int,
        role: str,
    ):
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_task_update_access(
            task,
            user_id=user_id,
        )

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        if payload.status != task.status:
            if payload.status == TaskStatus.archived or not can_transition_task_status(
                task.status,
                payload.status,
            ):
                raise TaskStateConflictError(
                    task.status.value,
                    payload.status.value,
                )

        return self.task_repository.update(task, payload)

    def xǁTaskServiceǁupdate__mutmut_11(
        self,
        task_id: int,
        payload: TaskUpdate,
        *,
        user_id: int,
        role: str,
    ):
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_task_update_access(
            task,
            user_id=user_id,
            role=role,
        )

        if task.status != TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        if payload.status != task.status:
            if payload.status == TaskStatus.archived or not can_transition_task_status(
                task.status,
                payload.status,
            ):
                raise TaskStateConflictError(
                    task.status.value,
                    payload.status.value,
                )

        return self.task_repository.update(task, payload)

    def xǁTaskServiceǁupdate__mutmut_12(
        self,
        task_id: int,
        payload: TaskUpdate,
        *,
        user_id: int,
        role: str,
    ):
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_task_update_access(
            task,
            user_id=user_id,
            role=role,
        )

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(None)

        if payload.status != task.status:
            if payload.status == TaskStatus.archived or not can_transition_task_status(
                task.status,
                payload.status,
            ):
                raise TaskStateConflictError(
                    task.status.value,
                    payload.status.value,
                )

        return self.task_repository.update(task, payload)

    def xǁTaskServiceǁupdate__mutmut_13(
        self,
        task_id: int,
        payload: TaskUpdate,
        *,
        user_id: int,
        role: str,
    ):
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_task_update_access(
            task,
            user_id=user_id,
            role=role,
        )

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        if payload.status == task.status:
            if payload.status == TaskStatus.archived or not can_transition_task_status(
                task.status,
                payload.status,
            ):
                raise TaskStateConflictError(
                    task.status.value,
                    payload.status.value,
                )

        return self.task_repository.update(task, payload)

    def xǁTaskServiceǁupdate__mutmut_14(
        self,
        task_id: int,
        payload: TaskUpdate,
        *,
        user_id: int,
        role: str,
    ):
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_task_update_access(
            task,
            user_id=user_id,
            role=role,
        )

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        if payload.status != task.status:
            if payload.status == TaskStatus.archived and not can_transition_task_status(
                task.status,
                payload.status,
            ):
                raise TaskStateConflictError(
                    task.status.value,
                    payload.status.value,
                )

        return self.task_repository.update(task, payload)

    def xǁTaskServiceǁupdate__mutmut_15(
        self,
        task_id: int,
        payload: TaskUpdate,
        *,
        user_id: int,
        role: str,
    ):
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_task_update_access(
            task,
            user_id=user_id,
            role=role,
        )

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        if payload.status != task.status:
            if payload.status != TaskStatus.archived or not can_transition_task_status(
                task.status,
                payload.status,
            ):
                raise TaskStateConflictError(
                    task.status.value,
                    payload.status.value,
                )

        return self.task_repository.update(task, payload)

    def xǁTaskServiceǁupdate__mutmut_16(
        self,
        task_id: int,
        payload: TaskUpdate,
        *,
        user_id: int,
        role: str,
    ):
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_task_update_access(
            task,
            user_id=user_id,
            role=role,
        )

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        if payload.status != task.status:
            if payload.status == TaskStatus.archived or can_transition_task_status(
                task.status,
                payload.status,
            ):
                raise TaskStateConflictError(
                    task.status.value,
                    payload.status.value,
                )

        return self.task_repository.update(task, payload)

    def xǁTaskServiceǁupdate__mutmut_17(
        self,
        task_id: int,
        payload: TaskUpdate,
        *,
        user_id: int,
        role: str,
    ):
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_task_update_access(
            task,
            user_id=user_id,
            role=role,
        )

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        if payload.status != task.status:
            if payload.status == TaskStatus.archived or not can_transition_task_status(
                None,
                payload.status,
            ):
                raise TaskStateConflictError(
                    task.status.value,
                    payload.status.value,
                )

        return self.task_repository.update(task, payload)

    def xǁTaskServiceǁupdate__mutmut_18(
        self,
        task_id: int,
        payload: TaskUpdate,
        *,
        user_id: int,
        role: str,
    ):
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_task_update_access(
            task,
            user_id=user_id,
            role=role,
        )

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        if payload.status != task.status:
            if payload.status == TaskStatus.archived or not can_transition_task_status(
                task.status,
                None,
            ):
                raise TaskStateConflictError(
                    task.status.value,
                    payload.status.value,
                )

        return self.task_repository.update(task, payload)

    def xǁTaskServiceǁupdate__mutmut_19(
        self,
        task_id: int,
        payload: TaskUpdate,
        *,
        user_id: int,
        role: str,
    ):
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_task_update_access(
            task,
            user_id=user_id,
            role=role,
        )

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        if payload.status != task.status:
            if payload.status == TaskStatus.archived or not can_transition_task_status(
                payload.status,
            ):
                raise TaskStateConflictError(
                    task.status.value,
                    payload.status.value,
                )

        return self.task_repository.update(task, payload)

    def xǁTaskServiceǁupdate__mutmut_20(
        self,
        task_id: int,
        payload: TaskUpdate,
        *,
        user_id: int,
        role: str,
    ):
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_task_update_access(
            task,
            user_id=user_id,
            role=role,
        )

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        if payload.status != task.status:
            if payload.status == TaskStatus.archived or not can_transition_task_status(
                task.status,
            ):
                raise TaskStateConflictError(
                    task.status.value,
                    payload.status.value,
                )

        return self.task_repository.update(task, payload)

    def xǁTaskServiceǁupdate__mutmut_21(
        self,
        task_id: int,
        payload: TaskUpdate,
        *,
        user_id: int,
        role: str,
    ):
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_task_update_access(
            task,
            user_id=user_id,
            role=role,
        )

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        if payload.status != task.status:
            if payload.status == TaskStatus.archived or not can_transition_task_status(
                task.status,
                payload.status,
            ):
                raise TaskStateConflictError(
                    None,
                    payload.status.value,
                )

        return self.task_repository.update(task, payload)

    def xǁTaskServiceǁupdate__mutmut_22(
        self,
        task_id: int,
        payload: TaskUpdate,
        *,
        user_id: int,
        role: str,
    ):
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_task_update_access(
            task,
            user_id=user_id,
            role=role,
        )

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        if payload.status != task.status:
            if payload.status == TaskStatus.archived or not can_transition_task_status(
                task.status,
                payload.status,
            ):
                raise TaskStateConflictError(
                    task.status.value,
                    None,
                )

        return self.task_repository.update(task, payload)

    def xǁTaskServiceǁupdate__mutmut_23(
        self,
        task_id: int,
        payload: TaskUpdate,
        *,
        user_id: int,
        role: str,
    ):
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_task_update_access(
            task,
            user_id=user_id,
            role=role,
        )

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        if payload.status != task.status:
            if payload.status == TaskStatus.archived or not can_transition_task_status(
                task.status,
                payload.status,
            ):
                raise TaskStateConflictError(
                    payload.status.value,
                )

        return self.task_repository.update(task, payload)

    def xǁTaskServiceǁupdate__mutmut_24(
        self,
        task_id: int,
        payload: TaskUpdate,
        *,
        user_id: int,
        role: str,
    ):
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_task_update_access(
            task,
            user_id=user_id,
            role=role,
        )

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        if payload.status != task.status:
            if payload.status == TaskStatus.archived or not can_transition_task_status(
                task.status,
                payload.status,
            ):
                raise TaskStateConflictError(
                    task.status.value,
                )

        return self.task_repository.update(task, payload)

    def xǁTaskServiceǁupdate__mutmut_25(
        self,
        task_id: int,
        payload: TaskUpdate,
        *,
        user_id: int,
        role: str,
    ):
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_task_update_access(
            task,
            user_id=user_id,
            role=role,
        )

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        if payload.status != task.status:
            if payload.status == TaskStatus.archived or not can_transition_task_status(
                task.status,
                payload.status,
            ):
                raise TaskStateConflictError(
                    task.status.value,
                    payload.status.value,
                )

        return self.task_repository.update(None, payload)

    def xǁTaskServiceǁupdate__mutmut_26(
        self,
        task_id: int,
        payload: TaskUpdate,
        *,
        user_id: int,
        role: str,
    ):
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_task_update_access(
            task,
            user_id=user_id,
            role=role,
        )

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        if payload.status != task.status:
            if payload.status == TaskStatus.archived or not can_transition_task_status(
                task.status,
                payload.status,
            ):
                raise TaskStateConflictError(
                    task.status.value,
                    payload.status.value,
                )

        return self.task_repository.update(task, None)

    def xǁTaskServiceǁupdate__mutmut_27(
        self,
        task_id: int,
        payload: TaskUpdate,
        *,
        user_id: int,
        role: str,
    ):
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_task_update_access(
            task,
            user_id=user_id,
            role=role,
        )

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        if payload.status != task.status:
            if payload.status == TaskStatus.archived or not can_transition_task_status(
                task.status,
                payload.status,
            ):
                raise TaskStateConflictError(
                    task.status.value,
                    payload.status.value,
                )

        return self.task_repository.update(payload)

    def xǁTaskServiceǁupdate__mutmut_28(
        self,
        task_id: int,
        payload: TaskUpdate,
        *,
        user_id: int,
        role: str,
    ):
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_task_update_access(
            task,
            user_id=user_id,
            role=role,
        )

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        if payload.status != task.status:
            if payload.status == TaskStatus.archived or not can_transition_task_status(
                task.status,
                payload.status,
            ):
                raise TaskStateConflictError(
                    task.status.value,
                    payload.status.value,
                )

        return self.task_repository.update(
            task,
        )

    @_mutmut_mutated(mutants_xǁTaskServiceǁ_require_task_update_access__mutmut)
    def _require_task_update_access(
        self,
        task: Task,
        *,
        user_id: int,
        role: str,
    ) -> None:
        self._require_project_access(task.project_id, user_id, role)

        role_value = getattr(role, "value", role)
        if role_value == "admin" or role_value == "manager":
            return

        if role_value == "member" and task.created_by == user_id:
            return

        raise UnauthorizedActionError(
            action="update",
            resource="task",
            resource_id=task.id,
        )

    def xǁTaskServiceǁ_require_task_update_access__mutmut_orig(
        self,
        task: Task,
        *,
        user_id: int,
        role: str,
    ) -> None:
        self._require_project_access(task.project_id, user_id, role)

        role_value = getattr(role, "value", role)
        if role_value == "admin" or role_value == "manager":
            return

        if role_value == "member" and task.created_by == user_id:
            return

        raise UnauthorizedActionError(
            action="update",
            resource="task",
            resource_id=task.id,
        )

    def xǁTaskServiceǁ_require_task_update_access__mutmut_1(
        self,
        task: Task,
        *,
        user_id: int,
        role: str,
    ) -> None:
        self._require_project_access(None, user_id, role)

        role_value = getattr(role, "value", role)
        if role_value == "admin" or role_value == "manager":
            return

        if role_value == "member" and task.created_by == user_id:
            return

        raise UnauthorizedActionError(
            action="update",
            resource="task",
            resource_id=task.id,
        )

    def xǁTaskServiceǁ_require_task_update_access__mutmut_2(
        self,
        task: Task,
        *,
        user_id: int,
        role: str,
    ) -> None:
        self._require_project_access(task.project_id, None, role)

        role_value = getattr(role, "value", role)
        if role_value == "admin" or role_value == "manager":
            return

        if role_value == "member" and task.created_by == user_id:
            return

        raise UnauthorizedActionError(
            action="update",
            resource="task",
            resource_id=task.id,
        )

    def xǁTaskServiceǁ_require_task_update_access__mutmut_3(
        self,
        task: Task,
        *,
        user_id: int,
        role: str,
    ) -> None:
        self._require_project_access(task.project_id, user_id, None)

        role_value = getattr(role, "value", role)
        if role_value == "admin" or role_value == "manager":
            return

        if role_value == "member" and task.created_by == user_id:
            return

        raise UnauthorizedActionError(
            action="update",
            resource="task",
            resource_id=task.id,
        )

    def xǁTaskServiceǁ_require_task_update_access__mutmut_4(
        self,
        task: Task,
        *,
        user_id: int,
        role: str,
    ) -> None:
        self._require_project_access(user_id, role)

        role_value = getattr(role, "value", role)
        if role_value == "admin" or role_value == "manager":
            return

        if role_value == "member" and task.created_by == user_id:
            return

        raise UnauthorizedActionError(
            action="update",
            resource="task",
            resource_id=task.id,
        )

    def xǁTaskServiceǁ_require_task_update_access__mutmut_5(
        self,
        task: Task,
        *,
        user_id: int,
        role: str,
    ) -> None:
        self._require_project_access(task.project_id, role)

        role_value = getattr(role, "value", role)
        if role_value == "admin" or role_value == "manager":
            return

        if role_value == "member" and task.created_by == user_id:
            return

        raise UnauthorizedActionError(
            action="update",
            resource="task",
            resource_id=task.id,
        )

    def xǁTaskServiceǁ_require_task_update_access__mutmut_6(
        self,
        task: Task,
        *,
        user_id: int,
        role: str,
    ) -> None:
        self._require_project_access(
            task.project_id,
            user_id,
        )

        role_value = getattr(role, "value", role)
        if role_value == "admin" or role_value == "manager":
            return

        if role_value == "member" and task.created_by == user_id:
            return

        raise UnauthorizedActionError(
            action="update",
            resource="task",
            resource_id=task.id,
        )

    def xǁTaskServiceǁ_require_task_update_access__mutmut_7(
        self,
        task: Task,
        *,
        user_id: int,
        role: str,
    ) -> None:
        self._require_project_access(task.project_id, user_id, role)

        role_value = None
        if role_value == "admin" or role_value == "manager":
            return

        if role_value == "member" and task.created_by == user_id:
            return

        raise UnauthorizedActionError(
            action="update",
            resource="task",
            resource_id=task.id,
        )

    def xǁTaskServiceǁ_require_task_update_access__mutmut_8(
        self,
        task: Task,
        *,
        user_id: int,
        role: str,
    ) -> None:
        self._require_project_access(task.project_id, user_id, role)

        role_value = getattr(None, "value", role)
        if role_value == "admin" or role_value == "manager":
            return

        if role_value == "member" and task.created_by == user_id:
            return

        raise UnauthorizedActionError(
            action="update",
            resource="task",
            resource_id=task.id,
        )

    def xǁTaskServiceǁ_require_task_update_access__mutmut_9(
        self,
        task: Task,
        *,
        user_id: int,
        role: str,
    ) -> None:
        self._require_project_access(task.project_id, user_id, role)

        role_value = getattr(role, None, role)
        if role_value == "admin" or role_value == "manager":
            return

        if role_value == "member" and task.created_by == user_id:
            return

        raise UnauthorizedActionError(
            action="update",
            resource="task",
            resource_id=task.id,
        )

    def xǁTaskServiceǁ_require_task_update_access__mutmut_10(
        self,
        task: Task,
        *,
        user_id: int,
        role: str,
    ) -> None:
        self._require_project_access(task.project_id, user_id, role)

        role_value = getattr(role, "value", None)
        if role_value == "admin" or role_value == "manager":
            return

        if role_value == "member" and task.created_by == user_id:
            return

        raise UnauthorizedActionError(
            action="update",
            resource="task",
            resource_id=task.id,
        )

    def xǁTaskServiceǁ_require_task_update_access__mutmut_11(
        self,
        task: Task,
        *,
        user_id: int,
        role: str,
    ) -> None:
        self._require_project_access(task.project_id, user_id, role)

        role_value = getattr("value", role)
        if role_value == "admin" or role_value == "manager":
            return

        if role_value == "member" and task.created_by == user_id:
            return

        raise UnauthorizedActionError(
            action="update",
            resource="task",
            resource_id=task.id,
        )

    def xǁTaskServiceǁ_require_task_update_access__mutmut_12(
        self,
        task: Task,
        *,
        user_id: int,
        role: str,
    ) -> None:
        self._require_project_access(task.project_id, user_id, role)

        role_value = getattr(role, role)
        if role_value == "admin" or role_value == "manager":
            return

        if role_value == "member" and task.created_by == user_id:
            return

        raise UnauthorizedActionError(
            action="update",
            resource="task",
            resource_id=task.id,
        )

    def xǁTaskServiceǁ_require_task_update_access__mutmut_13(
        self,
        task: Task,
        *,
        user_id: int,
        role: str,
    ) -> None:
        self._require_project_access(task.project_id, user_id, role)

        role_value = role.value
        if role_value == "admin" or role_value == "manager":
            return

        if role_value == "member" and task.created_by == user_id:
            return

        raise UnauthorizedActionError(
            action="update",
            resource="task",
            resource_id=task.id,
        )

    def xǁTaskServiceǁ_require_task_update_access__mutmut_14(
        self,
        task: Task,
        *,
        user_id: int,
        role: str,
    ) -> None:
        self._require_project_access(task.project_id, user_id, role)

        role_value = getattr(role, "XXvalueXX", role)
        if role_value == "admin" or role_value == "manager":
            return

        if role_value == "member" and task.created_by == user_id:
            return

        raise UnauthorizedActionError(
            action="update",
            resource="task",
            resource_id=task.id,
        )

    def xǁTaskServiceǁ_require_task_update_access__mutmut_15(
        self,
        task: Task,
        *,
        user_id: int,
        role: str,
    ) -> None:
        self._require_project_access(task.project_id, user_id, role)

        role_value = getattr(role, "VALUE", role)
        if role_value == "admin" or role_value == "manager":
            return

        if role_value == "member" and task.created_by == user_id:
            return

        raise UnauthorizedActionError(
            action="update",
            resource="task",
            resource_id=task.id,
        )

    def xǁTaskServiceǁ_require_task_update_access__mutmut_16(
        self,
        task: Task,
        *,
        user_id: int,
        role: str,
    ) -> None:
        self._require_project_access(task.project_id, user_id, role)

        role_value = getattr(role, "value", role)
        if role_value == "admin" and role_value == "manager":
            return

        if role_value == "member" and task.created_by == user_id:
            return

        raise UnauthorizedActionError(
            action="update",
            resource="task",
            resource_id=task.id,
        )

    def xǁTaskServiceǁ_require_task_update_access__mutmut_17(
        self,
        task: Task,
        *,
        user_id: int,
        role: str,
    ) -> None:
        self._require_project_access(task.project_id, user_id, role)

        role_value = getattr(role, "value", role)
        if role_value != "admin" or role_value == "manager":
            return

        if role_value == "member" and task.created_by == user_id:
            return

        raise UnauthorizedActionError(
            action="update",
            resource="task",
            resource_id=task.id,
        )

    def xǁTaskServiceǁ_require_task_update_access__mutmut_18(
        self,
        task: Task,
        *,
        user_id: int,
        role: str,
    ) -> None:
        self._require_project_access(task.project_id, user_id, role)

        role_value = getattr(role, "value", role)
        if role_value == "XXadminXX" or role_value == "manager":
            return

        if role_value == "member" and task.created_by == user_id:
            return

        raise UnauthorizedActionError(
            action="update",
            resource="task",
            resource_id=task.id,
        )

    def xǁTaskServiceǁ_require_task_update_access__mutmut_19(
        self,
        task: Task,
        *,
        user_id: int,
        role: str,
    ) -> None:
        self._require_project_access(task.project_id, user_id, role)

        role_value = getattr(role, "value", role)
        if role_value == "ADMIN" or role_value == "manager":
            return

        if role_value == "member" and task.created_by == user_id:
            return

        raise UnauthorizedActionError(
            action="update",
            resource="task",
            resource_id=task.id,
        )

    def xǁTaskServiceǁ_require_task_update_access__mutmut_20(
        self,
        task: Task,
        *,
        user_id: int,
        role: str,
    ) -> None:
        self._require_project_access(task.project_id, user_id, role)

        role_value = getattr(role, "value", role)
        if role_value == "admin" or role_value != "manager":
            return

        if role_value == "member" and task.created_by == user_id:
            return

        raise UnauthorizedActionError(
            action="update",
            resource="task",
            resource_id=task.id,
        )

    def xǁTaskServiceǁ_require_task_update_access__mutmut_21(
        self,
        task: Task,
        *,
        user_id: int,
        role: str,
    ) -> None:
        self._require_project_access(task.project_id, user_id, role)

        role_value = getattr(role, "value", role)
        if role_value == "admin" or role_value == "XXmanagerXX":
            return

        if role_value == "member" and task.created_by == user_id:
            return

        raise UnauthorizedActionError(
            action="update",
            resource="task",
            resource_id=task.id,
        )

    def xǁTaskServiceǁ_require_task_update_access__mutmut_22(
        self,
        task: Task,
        *,
        user_id: int,
        role: str,
    ) -> None:
        self._require_project_access(task.project_id, user_id, role)

        role_value = getattr(role, "value", role)
        if role_value == "admin" or role_value == "MANAGER":
            return

        if role_value == "member" and task.created_by == user_id:
            return

        raise UnauthorizedActionError(
            action="update",
            resource="task",
            resource_id=task.id,
        )

    def xǁTaskServiceǁ_require_task_update_access__mutmut_23(
        self,
        task: Task,
        *,
        user_id: int,
        role: str,
    ) -> None:
        self._require_project_access(task.project_id, user_id, role)

        role_value = getattr(role, "value", role)
        if role_value == "admin" or role_value == "manager":
            return

        if role_value == "member" or task.created_by == user_id:
            return

        raise UnauthorizedActionError(
            action="update",
            resource="task",
            resource_id=task.id,
        )

    def xǁTaskServiceǁ_require_task_update_access__mutmut_24(
        self,
        task: Task,
        *,
        user_id: int,
        role: str,
    ) -> None:
        self._require_project_access(task.project_id, user_id, role)

        role_value = getattr(role, "value", role)
        if role_value == "admin" or role_value == "manager":
            return

        if role_value != "member" and task.created_by == user_id:
            return

        raise UnauthorizedActionError(
            action="update",
            resource="task",
            resource_id=task.id,
        )

    def xǁTaskServiceǁ_require_task_update_access__mutmut_25(
        self,
        task: Task,
        *,
        user_id: int,
        role: str,
    ) -> None:
        self._require_project_access(task.project_id, user_id, role)

        role_value = getattr(role, "value", role)
        if role_value == "admin" or role_value == "manager":
            return

        if role_value == "XXmemberXX" and task.created_by == user_id:
            return

        raise UnauthorizedActionError(
            action="update",
            resource="task",
            resource_id=task.id,
        )

    def xǁTaskServiceǁ_require_task_update_access__mutmut_26(
        self,
        task: Task,
        *,
        user_id: int,
        role: str,
    ) -> None:
        self._require_project_access(task.project_id, user_id, role)

        role_value = getattr(role, "value", role)
        if role_value == "admin" or role_value == "manager":
            return

        if role_value == "MEMBER" and task.created_by == user_id:
            return

        raise UnauthorizedActionError(
            action="update",
            resource="task",
            resource_id=task.id,
        )

    def xǁTaskServiceǁ_require_task_update_access__mutmut_27(
        self,
        task: Task,
        *,
        user_id: int,
        role: str,
    ) -> None:
        self._require_project_access(task.project_id, user_id, role)

        role_value = getattr(role, "value", role)
        if role_value == "admin" or role_value == "manager":
            return

        if role_value == "member" and task.created_by != user_id:
            return

        raise UnauthorizedActionError(
            action="update",
            resource="task",
            resource_id=task.id,
        )

    def xǁTaskServiceǁ_require_task_update_access__mutmut_28(
        self,
        task: Task,
        *,
        user_id: int,
        role: str,
    ) -> None:
        self._require_project_access(task.project_id, user_id, role)

        role_value = getattr(role, "value", role)
        if role_value == "admin" or role_value == "manager":
            return

        if role_value == "member" and task.created_by == user_id:
            return

        raise UnauthorizedActionError(
            action=None,
            resource="task",
            resource_id=task.id,
        )

    def xǁTaskServiceǁ_require_task_update_access__mutmut_29(
        self,
        task: Task,
        *,
        user_id: int,
        role: str,
    ) -> None:
        self._require_project_access(task.project_id, user_id, role)

        role_value = getattr(role, "value", role)
        if role_value == "admin" or role_value == "manager":
            return

        if role_value == "member" and task.created_by == user_id:
            return

        raise UnauthorizedActionError(
            action="update",
            resource=None,
            resource_id=task.id,
        )

    def xǁTaskServiceǁ_require_task_update_access__mutmut_30(
        self,
        task: Task,
        *,
        user_id: int,
        role: str,
    ) -> None:
        self._require_project_access(task.project_id, user_id, role)

        role_value = getattr(role, "value", role)
        if role_value == "admin" or role_value == "manager":
            return

        if role_value == "member" and task.created_by == user_id:
            return

        raise UnauthorizedActionError(
            action="update",
            resource="task",
            resource_id=None,
        )

    def xǁTaskServiceǁ_require_task_update_access__mutmut_31(
        self,
        task: Task,
        *,
        user_id: int,
        role: str,
    ) -> None:
        self._require_project_access(task.project_id, user_id, role)

        role_value = getattr(role, "value", role)
        if role_value == "admin" or role_value == "manager":
            return

        if role_value == "member" and task.created_by == user_id:
            return

        raise UnauthorizedActionError(
            resource="task",
            resource_id=task.id,
        )

    def xǁTaskServiceǁ_require_task_update_access__mutmut_32(
        self,
        task: Task,
        *,
        user_id: int,
        role: str,
    ) -> None:
        self._require_project_access(task.project_id, user_id, role)

        role_value = getattr(role, "value", role)
        if role_value == "admin" or role_value == "manager":
            return

        if role_value == "member" and task.created_by == user_id:
            return

        raise UnauthorizedActionError(
            action="update",
            resource_id=task.id,
        )

    def xǁTaskServiceǁ_require_task_update_access__mutmut_33(
        self,
        task: Task,
        *,
        user_id: int,
        role: str,
    ) -> None:
        self._require_project_access(task.project_id, user_id, role)

        role_value = getattr(role, "value", role)
        if role_value == "admin" or role_value == "manager":
            return

        if role_value == "member" and task.created_by == user_id:
            return

        raise UnauthorizedActionError(
            action="update",
            resource="task",
        )

    def xǁTaskServiceǁ_require_task_update_access__mutmut_34(
        self,
        task: Task,
        *,
        user_id: int,
        role: str,
    ) -> None:
        self._require_project_access(task.project_id, user_id, role)

        role_value = getattr(role, "value", role)
        if role_value == "admin" or role_value == "manager":
            return

        if role_value == "member" and task.created_by == user_id:
            return

        raise UnauthorizedActionError(
            action="XXupdateXX",
            resource="task",
            resource_id=task.id,
        )

    def xǁTaskServiceǁ_require_task_update_access__mutmut_35(
        self,
        task: Task,
        *,
        user_id: int,
        role: str,
    ) -> None:
        self._require_project_access(task.project_id, user_id, role)

        role_value = getattr(role, "value", role)
        if role_value == "admin" or role_value == "manager":
            return

        if role_value == "member" and task.created_by == user_id:
            return

        raise UnauthorizedActionError(
            action="UPDATE",
            resource="task",
            resource_id=task.id,
        )

    def xǁTaskServiceǁ_require_task_update_access__mutmut_36(
        self,
        task: Task,
        *,
        user_id: int,
        role: str,
    ) -> None:
        self._require_project_access(task.project_id, user_id, role)

        role_value = getattr(role, "value", role)
        if role_value == "admin" or role_value == "manager":
            return

        if role_value == "member" and task.created_by == user_id:
            return

        raise UnauthorizedActionError(
            action="update",
            resource="XXtaskXX",
            resource_id=task.id,
        )

    def xǁTaskServiceǁ_require_task_update_access__mutmut_37(
        self,
        task: Task,
        *,
        user_id: int,
        role: str,
    ) -> None:
        self._require_project_access(task.project_id, user_id, role)

        role_value = getattr(role, "value", role)
        if role_value == "admin" or role_value == "manager":
            return

        if role_value == "member" and task.created_by == user_id:
            return

        raise UnauthorizedActionError(
            action="update",
            resource="TASK",
            resource_id=task.id,
        )

    @_mutmut_mutated(mutants_xǁTaskServiceǁarchive__mutmut)
    def archive(self, task_id: int, *, user_id: int, role: str):
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        role_value = getattr(role, "value", role)
        if role_value not in {"admin", "manager"}:
            raise UnauthorizedActionError(
                action="archive",
                resource="task",
                resource_id=task_id,
            )

        self._require_project_access(task.project_id, user_id, role)

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        if not can_transition_task_status(task.status, TaskStatus.archived):
            raise TaskStateConflictError(
                task.status.value,
                TaskStatus.archived.value,
            )

        payload = TaskUpdate(
            title=task.title,
            description=task.description,
            status=TaskStatus.archived,
            priority=task.priority,
        )
        return self.task_repository.update(task, payload)

    def xǁTaskServiceǁarchive__mutmut_orig(self, task_id: int, *, user_id: int, role: str):
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        role_value = getattr(role, "value", role)
        if role_value not in {"admin", "manager"}:
            raise UnauthorizedActionError(
                action="archive",
                resource="task",
                resource_id=task_id,
            )

        self._require_project_access(task.project_id, user_id, role)

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        if not can_transition_task_status(task.status, TaskStatus.archived):
            raise TaskStateConflictError(
                task.status.value,
                TaskStatus.archived.value,
            )

        payload = TaskUpdate(
            title=task.title,
            description=task.description,
            status=TaskStatus.archived,
            priority=task.priority,
        )
        return self.task_repository.update(task, payload)

    def xǁTaskServiceǁarchive__mutmut_1(self, task_id: int, *, user_id: int, role: str):
        task = None

        if task is None:
            raise TaskNotFoundError(task_id)

        role_value = getattr(role, "value", role)
        if role_value not in {"admin", "manager"}:
            raise UnauthorizedActionError(
                action="archive",
                resource="task",
                resource_id=task_id,
            )

        self._require_project_access(task.project_id, user_id, role)

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        if not can_transition_task_status(task.status, TaskStatus.archived):
            raise TaskStateConflictError(
                task.status.value,
                TaskStatus.archived.value,
            )

        payload = TaskUpdate(
            title=task.title,
            description=task.description,
            status=TaskStatus.archived,
            priority=task.priority,
        )
        return self.task_repository.update(task, payload)

    def xǁTaskServiceǁarchive__mutmut_2(self, task_id: int, *, user_id: int, role: str):
        task = self.task_repository.get_by_id(None)

        if task is None:
            raise TaskNotFoundError(task_id)

        role_value = getattr(role, "value", role)
        if role_value not in {"admin", "manager"}:
            raise UnauthorizedActionError(
                action="archive",
                resource="task",
                resource_id=task_id,
            )

        self._require_project_access(task.project_id, user_id, role)

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        if not can_transition_task_status(task.status, TaskStatus.archived):
            raise TaskStateConflictError(
                task.status.value,
                TaskStatus.archived.value,
            )

        payload = TaskUpdate(
            title=task.title,
            description=task.description,
            status=TaskStatus.archived,
            priority=task.priority,
        )
        return self.task_repository.update(task, payload)

    def xǁTaskServiceǁarchive__mutmut_3(self, task_id: int, *, user_id: int, role: str):
        task = self.task_repository.get_by_id(task_id)

        if task is not None:
            raise TaskNotFoundError(task_id)

        role_value = getattr(role, "value", role)
        if role_value not in {"admin", "manager"}:
            raise UnauthorizedActionError(
                action="archive",
                resource="task",
                resource_id=task_id,
            )

        self._require_project_access(task.project_id, user_id, role)

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        if not can_transition_task_status(task.status, TaskStatus.archived):
            raise TaskStateConflictError(
                task.status.value,
                TaskStatus.archived.value,
            )

        payload = TaskUpdate(
            title=task.title,
            description=task.description,
            status=TaskStatus.archived,
            priority=task.priority,
        )
        return self.task_repository.update(task, payload)

    def xǁTaskServiceǁarchive__mutmut_4(self, task_id: int, *, user_id: int, role: str):
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(None)

        role_value = getattr(role, "value", role)
        if role_value not in {"admin", "manager"}:
            raise UnauthorizedActionError(
                action="archive",
                resource="task",
                resource_id=task_id,
            )

        self._require_project_access(task.project_id, user_id, role)

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        if not can_transition_task_status(task.status, TaskStatus.archived):
            raise TaskStateConflictError(
                task.status.value,
                TaskStatus.archived.value,
            )

        payload = TaskUpdate(
            title=task.title,
            description=task.description,
            status=TaskStatus.archived,
            priority=task.priority,
        )
        return self.task_repository.update(task, payload)

    def xǁTaskServiceǁarchive__mutmut_5(self, task_id: int, *, user_id: int, role: str):
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        role_value = None
        if role_value not in {"admin", "manager"}:
            raise UnauthorizedActionError(
                action="archive",
                resource="task",
                resource_id=task_id,
            )

        self._require_project_access(task.project_id, user_id, role)

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        if not can_transition_task_status(task.status, TaskStatus.archived):
            raise TaskStateConflictError(
                task.status.value,
                TaskStatus.archived.value,
            )

        payload = TaskUpdate(
            title=task.title,
            description=task.description,
            status=TaskStatus.archived,
            priority=task.priority,
        )
        return self.task_repository.update(task, payload)

    def xǁTaskServiceǁarchive__mutmut_6(self, task_id: int, *, user_id: int, role: str):
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        role_value = getattr(None, "value", role)
        if role_value not in {"admin", "manager"}:
            raise UnauthorizedActionError(
                action="archive",
                resource="task",
                resource_id=task_id,
            )

        self._require_project_access(task.project_id, user_id, role)

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        if not can_transition_task_status(task.status, TaskStatus.archived):
            raise TaskStateConflictError(
                task.status.value,
                TaskStatus.archived.value,
            )

        payload = TaskUpdate(
            title=task.title,
            description=task.description,
            status=TaskStatus.archived,
            priority=task.priority,
        )
        return self.task_repository.update(task, payload)

    def xǁTaskServiceǁarchive__mutmut_7(self, task_id: int, *, user_id: int, role: str):
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        role_value = getattr(role, None, role)
        if role_value not in {"admin", "manager"}:
            raise UnauthorizedActionError(
                action="archive",
                resource="task",
                resource_id=task_id,
            )

        self._require_project_access(task.project_id, user_id, role)

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        if not can_transition_task_status(task.status, TaskStatus.archived):
            raise TaskStateConflictError(
                task.status.value,
                TaskStatus.archived.value,
            )

        payload = TaskUpdate(
            title=task.title,
            description=task.description,
            status=TaskStatus.archived,
            priority=task.priority,
        )
        return self.task_repository.update(task, payload)

    def xǁTaskServiceǁarchive__mutmut_8(self, task_id: int, *, user_id: int, role: str):
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        role_value = getattr(role, "value", None)
        if role_value not in {"admin", "manager"}:
            raise UnauthorizedActionError(
                action="archive",
                resource="task",
                resource_id=task_id,
            )

        self._require_project_access(task.project_id, user_id, role)

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        if not can_transition_task_status(task.status, TaskStatus.archived):
            raise TaskStateConflictError(
                task.status.value,
                TaskStatus.archived.value,
            )

        payload = TaskUpdate(
            title=task.title,
            description=task.description,
            status=TaskStatus.archived,
            priority=task.priority,
        )
        return self.task_repository.update(task, payload)

    def xǁTaskServiceǁarchive__mutmut_9(self, task_id: int, *, user_id: int, role: str):
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        role_value = getattr("value", role)
        if role_value not in {"admin", "manager"}:
            raise UnauthorizedActionError(
                action="archive",
                resource="task",
                resource_id=task_id,
            )

        self._require_project_access(task.project_id, user_id, role)

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        if not can_transition_task_status(task.status, TaskStatus.archived):
            raise TaskStateConflictError(
                task.status.value,
                TaskStatus.archived.value,
            )

        payload = TaskUpdate(
            title=task.title,
            description=task.description,
            status=TaskStatus.archived,
            priority=task.priority,
        )
        return self.task_repository.update(task, payload)

    def xǁTaskServiceǁarchive__mutmut_10(self, task_id: int, *, user_id: int, role: str):
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        role_value = getattr(role, role)
        if role_value not in {"admin", "manager"}:
            raise UnauthorizedActionError(
                action="archive",
                resource="task",
                resource_id=task_id,
            )

        self._require_project_access(task.project_id, user_id, role)

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        if not can_transition_task_status(task.status, TaskStatus.archived):
            raise TaskStateConflictError(
                task.status.value,
                TaskStatus.archived.value,
            )

        payload = TaskUpdate(
            title=task.title,
            description=task.description,
            status=TaskStatus.archived,
            priority=task.priority,
        )
        return self.task_repository.update(task, payload)

    def xǁTaskServiceǁarchive__mutmut_11(self, task_id: int, *, user_id: int, role: str):
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        role_value = role.value
        if role_value not in {"admin", "manager"}:
            raise UnauthorizedActionError(
                action="archive",
                resource="task",
                resource_id=task_id,
            )

        self._require_project_access(task.project_id, user_id, role)

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        if not can_transition_task_status(task.status, TaskStatus.archived):
            raise TaskStateConflictError(
                task.status.value,
                TaskStatus.archived.value,
            )

        payload = TaskUpdate(
            title=task.title,
            description=task.description,
            status=TaskStatus.archived,
            priority=task.priority,
        )
        return self.task_repository.update(task, payload)

    def xǁTaskServiceǁarchive__mutmut_12(self, task_id: int, *, user_id: int, role: str):
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        role_value = getattr(role, "XXvalueXX", role)
        if role_value not in {"admin", "manager"}:
            raise UnauthorizedActionError(
                action="archive",
                resource="task",
                resource_id=task_id,
            )

        self._require_project_access(task.project_id, user_id, role)

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        if not can_transition_task_status(task.status, TaskStatus.archived):
            raise TaskStateConflictError(
                task.status.value,
                TaskStatus.archived.value,
            )

        payload = TaskUpdate(
            title=task.title,
            description=task.description,
            status=TaskStatus.archived,
            priority=task.priority,
        )
        return self.task_repository.update(task, payload)

    def xǁTaskServiceǁarchive__mutmut_13(self, task_id: int, *, user_id: int, role: str):
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        role_value = getattr(role, "VALUE", role)
        if role_value not in {"admin", "manager"}:
            raise UnauthorizedActionError(
                action="archive",
                resource="task",
                resource_id=task_id,
            )

        self._require_project_access(task.project_id, user_id, role)

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        if not can_transition_task_status(task.status, TaskStatus.archived):
            raise TaskStateConflictError(
                task.status.value,
                TaskStatus.archived.value,
            )

        payload = TaskUpdate(
            title=task.title,
            description=task.description,
            status=TaskStatus.archived,
            priority=task.priority,
        )
        return self.task_repository.update(task, payload)

    def xǁTaskServiceǁarchive__mutmut_14(self, task_id: int, *, user_id: int, role: str):
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        role_value = getattr(role, "value", role)
        if role_value in {"admin", "manager"}:
            raise UnauthorizedActionError(
                action="archive",
                resource="task",
                resource_id=task_id,
            )

        self._require_project_access(task.project_id, user_id, role)

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        if not can_transition_task_status(task.status, TaskStatus.archived):
            raise TaskStateConflictError(
                task.status.value,
                TaskStatus.archived.value,
            )

        payload = TaskUpdate(
            title=task.title,
            description=task.description,
            status=TaskStatus.archived,
            priority=task.priority,
        )
        return self.task_repository.update(task, payload)

    def xǁTaskServiceǁarchive__mutmut_15(self, task_id: int, *, user_id: int, role: str):
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        role_value = getattr(role, "value", role)
        if role_value not in {"XXadminXX", "manager"}:
            raise UnauthorizedActionError(
                action="archive",
                resource="task",
                resource_id=task_id,
            )

        self._require_project_access(task.project_id, user_id, role)

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        if not can_transition_task_status(task.status, TaskStatus.archived):
            raise TaskStateConflictError(
                task.status.value,
                TaskStatus.archived.value,
            )

        payload = TaskUpdate(
            title=task.title,
            description=task.description,
            status=TaskStatus.archived,
            priority=task.priority,
        )
        return self.task_repository.update(task, payload)

    def xǁTaskServiceǁarchive__mutmut_16(self, task_id: int, *, user_id: int, role: str):
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        role_value = getattr(role, "value", role)
        if role_value not in {"ADMIN", "manager"}:
            raise UnauthorizedActionError(
                action="archive",
                resource="task",
                resource_id=task_id,
            )

        self._require_project_access(task.project_id, user_id, role)

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        if not can_transition_task_status(task.status, TaskStatus.archived):
            raise TaskStateConflictError(
                task.status.value,
                TaskStatus.archived.value,
            )

        payload = TaskUpdate(
            title=task.title,
            description=task.description,
            status=TaskStatus.archived,
            priority=task.priority,
        )
        return self.task_repository.update(task, payload)

    def xǁTaskServiceǁarchive__mutmut_17(self, task_id: int, *, user_id: int, role: str):
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        role_value = getattr(role, "value", role)
        if role_value not in {"admin", "XXmanagerXX"}:
            raise UnauthorizedActionError(
                action="archive",
                resource="task",
                resource_id=task_id,
            )

        self._require_project_access(task.project_id, user_id, role)

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        if not can_transition_task_status(task.status, TaskStatus.archived):
            raise TaskStateConflictError(
                task.status.value,
                TaskStatus.archived.value,
            )

        payload = TaskUpdate(
            title=task.title,
            description=task.description,
            status=TaskStatus.archived,
            priority=task.priority,
        )
        return self.task_repository.update(task, payload)

    def xǁTaskServiceǁarchive__mutmut_18(self, task_id: int, *, user_id: int, role: str):
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        role_value = getattr(role, "value", role)
        if role_value not in {"admin", "MANAGER"}:
            raise UnauthorizedActionError(
                action="archive",
                resource="task",
                resource_id=task_id,
            )

        self._require_project_access(task.project_id, user_id, role)

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        if not can_transition_task_status(task.status, TaskStatus.archived):
            raise TaskStateConflictError(
                task.status.value,
                TaskStatus.archived.value,
            )

        payload = TaskUpdate(
            title=task.title,
            description=task.description,
            status=TaskStatus.archived,
            priority=task.priority,
        )
        return self.task_repository.update(task, payload)

    def xǁTaskServiceǁarchive__mutmut_19(self, task_id: int, *, user_id: int, role: str):
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        role_value = getattr(role, "value", role)
        if role_value not in {"admin", "manager"}:
            raise UnauthorizedActionError(
                action=None,
                resource="task",
                resource_id=task_id,
            )

        self._require_project_access(task.project_id, user_id, role)

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        if not can_transition_task_status(task.status, TaskStatus.archived):
            raise TaskStateConflictError(
                task.status.value,
                TaskStatus.archived.value,
            )

        payload = TaskUpdate(
            title=task.title,
            description=task.description,
            status=TaskStatus.archived,
            priority=task.priority,
        )
        return self.task_repository.update(task, payload)

    def xǁTaskServiceǁarchive__mutmut_20(self, task_id: int, *, user_id: int, role: str):
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        role_value = getattr(role, "value", role)
        if role_value not in {"admin", "manager"}:
            raise UnauthorizedActionError(
                action="archive",
                resource=None,
                resource_id=task_id,
            )

        self._require_project_access(task.project_id, user_id, role)

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        if not can_transition_task_status(task.status, TaskStatus.archived):
            raise TaskStateConflictError(
                task.status.value,
                TaskStatus.archived.value,
            )

        payload = TaskUpdate(
            title=task.title,
            description=task.description,
            status=TaskStatus.archived,
            priority=task.priority,
        )
        return self.task_repository.update(task, payload)

    def xǁTaskServiceǁarchive__mutmut_21(self, task_id: int, *, user_id: int, role: str):
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        role_value = getattr(role, "value", role)
        if role_value not in {"admin", "manager"}:
            raise UnauthorizedActionError(
                action="archive",
                resource="task",
                resource_id=None,
            )

        self._require_project_access(task.project_id, user_id, role)

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        if not can_transition_task_status(task.status, TaskStatus.archived):
            raise TaskStateConflictError(
                task.status.value,
                TaskStatus.archived.value,
            )

        payload = TaskUpdate(
            title=task.title,
            description=task.description,
            status=TaskStatus.archived,
            priority=task.priority,
        )
        return self.task_repository.update(task, payload)

    def xǁTaskServiceǁarchive__mutmut_22(self, task_id: int, *, user_id: int, role: str):
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        role_value = getattr(role, "value", role)
        if role_value not in {"admin", "manager"}:
            raise UnauthorizedActionError(
                resource="task",
                resource_id=task_id,
            )

        self._require_project_access(task.project_id, user_id, role)

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        if not can_transition_task_status(task.status, TaskStatus.archived):
            raise TaskStateConflictError(
                task.status.value,
                TaskStatus.archived.value,
            )

        payload = TaskUpdate(
            title=task.title,
            description=task.description,
            status=TaskStatus.archived,
            priority=task.priority,
        )
        return self.task_repository.update(task, payload)

    def xǁTaskServiceǁarchive__mutmut_23(self, task_id: int, *, user_id: int, role: str):
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        role_value = getattr(role, "value", role)
        if role_value not in {"admin", "manager"}:
            raise UnauthorizedActionError(
                action="archive",
                resource_id=task_id,
            )

        self._require_project_access(task.project_id, user_id, role)

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        if not can_transition_task_status(task.status, TaskStatus.archived):
            raise TaskStateConflictError(
                task.status.value,
                TaskStatus.archived.value,
            )

        payload = TaskUpdate(
            title=task.title,
            description=task.description,
            status=TaskStatus.archived,
            priority=task.priority,
        )
        return self.task_repository.update(task, payload)

    def xǁTaskServiceǁarchive__mutmut_24(self, task_id: int, *, user_id: int, role: str):
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        role_value = getattr(role, "value", role)
        if role_value not in {"admin", "manager"}:
            raise UnauthorizedActionError(
                action="archive",
                resource="task",
            )

        self._require_project_access(task.project_id, user_id, role)

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        if not can_transition_task_status(task.status, TaskStatus.archived):
            raise TaskStateConflictError(
                task.status.value,
                TaskStatus.archived.value,
            )

        payload = TaskUpdate(
            title=task.title,
            description=task.description,
            status=TaskStatus.archived,
            priority=task.priority,
        )
        return self.task_repository.update(task, payload)

    def xǁTaskServiceǁarchive__mutmut_25(self, task_id: int, *, user_id: int, role: str):
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        role_value = getattr(role, "value", role)
        if role_value not in {"admin", "manager"}:
            raise UnauthorizedActionError(
                action="XXarchiveXX",
                resource="task",
                resource_id=task_id,
            )

        self._require_project_access(task.project_id, user_id, role)

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        if not can_transition_task_status(task.status, TaskStatus.archived):
            raise TaskStateConflictError(
                task.status.value,
                TaskStatus.archived.value,
            )

        payload = TaskUpdate(
            title=task.title,
            description=task.description,
            status=TaskStatus.archived,
            priority=task.priority,
        )
        return self.task_repository.update(task, payload)

    def xǁTaskServiceǁarchive__mutmut_26(self, task_id: int, *, user_id: int, role: str):
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        role_value = getattr(role, "value", role)
        if role_value not in {"admin", "manager"}:
            raise UnauthorizedActionError(
                action="ARCHIVE",
                resource="task",
                resource_id=task_id,
            )

        self._require_project_access(task.project_id, user_id, role)

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        if not can_transition_task_status(task.status, TaskStatus.archived):
            raise TaskStateConflictError(
                task.status.value,
                TaskStatus.archived.value,
            )

        payload = TaskUpdate(
            title=task.title,
            description=task.description,
            status=TaskStatus.archived,
            priority=task.priority,
        )
        return self.task_repository.update(task, payload)

    def xǁTaskServiceǁarchive__mutmut_27(self, task_id: int, *, user_id: int, role: str):
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        role_value = getattr(role, "value", role)
        if role_value not in {"admin", "manager"}:
            raise UnauthorizedActionError(
                action="archive",
                resource="XXtaskXX",
                resource_id=task_id,
            )

        self._require_project_access(task.project_id, user_id, role)

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        if not can_transition_task_status(task.status, TaskStatus.archived):
            raise TaskStateConflictError(
                task.status.value,
                TaskStatus.archived.value,
            )

        payload = TaskUpdate(
            title=task.title,
            description=task.description,
            status=TaskStatus.archived,
            priority=task.priority,
        )
        return self.task_repository.update(task, payload)

    def xǁTaskServiceǁarchive__mutmut_28(self, task_id: int, *, user_id: int, role: str):
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        role_value = getattr(role, "value", role)
        if role_value not in {"admin", "manager"}:
            raise UnauthorizedActionError(
                action="archive",
                resource="TASK",
                resource_id=task_id,
            )

        self._require_project_access(task.project_id, user_id, role)

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        if not can_transition_task_status(task.status, TaskStatus.archived):
            raise TaskStateConflictError(
                task.status.value,
                TaskStatus.archived.value,
            )

        payload = TaskUpdate(
            title=task.title,
            description=task.description,
            status=TaskStatus.archived,
            priority=task.priority,
        )
        return self.task_repository.update(task, payload)

    def xǁTaskServiceǁarchive__mutmut_29(self, task_id: int, *, user_id: int, role: str):
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        role_value = getattr(role, "value", role)
        if role_value not in {"admin", "manager"}:
            raise UnauthorizedActionError(
                action="archive",
                resource="task",
                resource_id=task_id,
            )

        self._require_project_access(None, user_id, role)

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        if not can_transition_task_status(task.status, TaskStatus.archived):
            raise TaskStateConflictError(
                task.status.value,
                TaskStatus.archived.value,
            )

        payload = TaskUpdate(
            title=task.title,
            description=task.description,
            status=TaskStatus.archived,
            priority=task.priority,
        )
        return self.task_repository.update(task, payload)

    def xǁTaskServiceǁarchive__mutmut_30(self, task_id: int, *, user_id: int, role: str):
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        role_value = getattr(role, "value", role)
        if role_value not in {"admin", "manager"}:
            raise UnauthorizedActionError(
                action="archive",
                resource="task",
                resource_id=task_id,
            )

        self._require_project_access(task.project_id, None, role)

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        if not can_transition_task_status(task.status, TaskStatus.archived):
            raise TaskStateConflictError(
                task.status.value,
                TaskStatus.archived.value,
            )

        payload = TaskUpdate(
            title=task.title,
            description=task.description,
            status=TaskStatus.archived,
            priority=task.priority,
        )
        return self.task_repository.update(task, payload)

    def xǁTaskServiceǁarchive__mutmut_31(self, task_id: int, *, user_id: int, role: str):
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        role_value = getattr(role, "value", role)
        if role_value not in {"admin", "manager"}:
            raise UnauthorizedActionError(
                action="archive",
                resource="task",
                resource_id=task_id,
            )

        self._require_project_access(task.project_id, user_id, None)

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        if not can_transition_task_status(task.status, TaskStatus.archived):
            raise TaskStateConflictError(
                task.status.value,
                TaskStatus.archived.value,
            )

        payload = TaskUpdate(
            title=task.title,
            description=task.description,
            status=TaskStatus.archived,
            priority=task.priority,
        )
        return self.task_repository.update(task, payload)

    def xǁTaskServiceǁarchive__mutmut_32(self, task_id: int, *, user_id: int, role: str):
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        role_value = getattr(role, "value", role)
        if role_value not in {"admin", "manager"}:
            raise UnauthorizedActionError(
                action="archive",
                resource="task",
                resource_id=task_id,
            )

        self._require_project_access(user_id, role)

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        if not can_transition_task_status(task.status, TaskStatus.archived):
            raise TaskStateConflictError(
                task.status.value,
                TaskStatus.archived.value,
            )

        payload = TaskUpdate(
            title=task.title,
            description=task.description,
            status=TaskStatus.archived,
            priority=task.priority,
        )
        return self.task_repository.update(task, payload)

    def xǁTaskServiceǁarchive__mutmut_33(self, task_id: int, *, user_id: int, role: str):
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        role_value = getattr(role, "value", role)
        if role_value not in {"admin", "manager"}:
            raise UnauthorizedActionError(
                action="archive",
                resource="task",
                resource_id=task_id,
            )

        self._require_project_access(task.project_id, role)

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        if not can_transition_task_status(task.status, TaskStatus.archived):
            raise TaskStateConflictError(
                task.status.value,
                TaskStatus.archived.value,
            )

        payload = TaskUpdate(
            title=task.title,
            description=task.description,
            status=TaskStatus.archived,
            priority=task.priority,
        )
        return self.task_repository.update(task, payload)

    def xǁTaskServiceǁarchive__mutmut_34(self, task_id: int, *, user_id: int, role: str):
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        role_value = getattr(role, "value", role)
        if role_value not in {"admin", "manager"}:
            raise UnauthorizedActionError(
                action="archive",
                resource="task",
                resource_id=task_id,
            )

        self._require_project_access(
            task.project_id,
            user_id,
        )

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        if not can_transition_task_status(task.status, TaskStatus.archived):
            raise TaskStateConflictError(
                task.status.value,
                TaskStatus.archived.value,
            )

        payload = TaskUpdate(
            title=task.title,
            description=task.description,
            status=TaskStatus.archived,
            priority=task.priority,
        )
        return self.task_repository.update(task, payload)

    def xǁTaskServiceǁarchive__mutmut_35(self, task_id: int, *, user_id: int, role: str):
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        role_value = getattr(role, "value", role)
        if role_value not in {"admin", "manager"}:
            raise UnauthorizedActionError(
                action="archive",
                resource="task",
                resource_id=task_id,
            )

        self._require_project_access(task.project_id, user_id, role)

        if task.status != TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        if not can_transition_task_status(task.status, TaskStatus.archived):
            raise TaskStateConflictError(
                task.status.value,
                TaskStatus.archived.value,
            )

        payload = TaskUpdate(
            title=task.title,
            description=task.description,
            status=TaskStatus.archived,
            priority=task.priority,
        )
        return self.task_repository.update(task, payload)

    def xǁTaskServiceǁarchive__mutmut_36(self, task_id: int, *, user_id: int, role: str):
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        role_value = getattr(role, "value", role)
        if role_value not in {"admin", "manager"}:
            raise UnauthorizedActionError(
                action="archive",
                resource="task",
                resource_id=task_id,
            )

        self._require_project_access(task.project_id, user_id, role)

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(None)

        if not can_transition_task_status(task.status, TaskStatus.archived):
            raise TaskStateConflictError(
                task.status.value,
                TaskStatus.archived.value,
            )

        payload = TaskUpdate(
            title=task.title,
            description=task.description,
            status=TaskStatus.archived,
            priority=task.priority,
        )
        return self.task_repository.update(task, payload)

    def xǁTaskServiceǁarchive__mutmut_37(self, task_id: int, *, user_id: int, role: str):
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        role_value = getattr(role, "value", role)
        if role_value not in {"admin", "manager"}:
            raise UnauthorizedActionError(
                action="archive",
                resource="task",
                resource_id=task_id,
            )

        self._require_project_access(task.project_id, user_id, role)

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        if can_transition_task_status(task.status, TaskStatus.archived):
            raise TaskStateConflictError(
                task.status.value,
                TaskStatus.archived.value,
            )

        payload = TaskUpdate(
            title=task.title,
            description=task.description,
            status=TaskStatus.archived,
            priority=task.priority,
        )
        return self.task_repository.update(task, payload)

    def xǁTaskServiceǁarchive__mutmut_38(self, task_id: int, *, user_id: int, role: str):
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        role_value = getattr(role, "value", role)
        if role_value not in {"admin", "manager"}:
            raise UnauthorizedActionError(
                action="archive",
                resource="task",
                resource_id=task_id,
            )

        self._require_project_access(task.project_id, user_id, role)

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        if not can_transition_task_status(None, TaskStatus.archived):
            raise TaskStateConflictError(
                task.status.value,
                TaskStatus.archived.value,
            )

        payload = TaskUpdate(
            title=task.title,
            description=task.description,
            status=TaskStatus.archived,
            priority=task.priority,
        )
        return self.task_repository.update(task, payload)

    def xǁTaskServiceǁarchive__mutmut_39(self, task_id: int, *, user_id: int, role: str):
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        role_value = getattr(role, "value", role)
        if role_value not in {"admin", "manager"}:
            raise UnauthorizedActionError(
                action="archive",
                resource="task",
                resource_id=task_id,
            )

        self._require_project_access(task.project_id, user_id, role)

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        if not can_transition_task_status(task.status, None):
            raise TaskStateConflictError(
                task.status.value,
                TaskStatus.archived.value,
            )

        payload = TaskUpdate(
            title=task.title,
            description=task.description,
            status=TaskStatus.archived,
            priority=task.priority,
        )
        return self.task_repository.update(task, payload)

    def xǁTaskServiceǁarchive__mutmut_40(self, task_id: int, *, user_id: int, role: str):
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        role_value = getattr(role, "value", role)
        if role_value not in {"admin", "manager"}:
            raise UnauthorizedActionError(
                action="archive",
                resource="task",
                resource_id=task_id,
            )

        self._require_project_access(task.project_id, user_id, role)

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        if not can_transition_task_status(TaskStatus.archived):
            raise TaskStateConflictError(
                task.status.value,
                TaskStatus.archived.value,
            )

        payload = TaskUpdate(
            title=task.title,
            description=task.description,
            status=TaskStatus.archived,
            priority=task.priority,
        )
        return self.task_repository.update(task, payload)

    def xǁTaskServiceǁarchive__mutmut_41(self, task_id: int, *, user_id: int, role: str):
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        role_value = getattr(role, "value", role)
        if role_value not in {"admin", "manager"}:
            raise UnauthorizedActionError(
                action="archive",
                resource="task",
                resource_id=task_id,
            )

        self._require_project_access(task.project_id, user_id, role)

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        if not can_transition_task_status(
            task.status,
        ):
            raise TaskStateConflictError(
                task.status.value,
                TaskStatus.archived.value,
            )

        payload = TaskUpdate(
            title=task.title,
            description=task.description,
            status=TaskStatus.archived,
            priority=task.priority,
        )
        return self.task_repository.update(task, payload)

    def xǁTaskServiceǁarchive__mutmut_42(self, task_id: int, *, user_id: int, role: str):
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        role_value = getattr(role, "value", role)
        if role_value not in {"admin", "manager"}:
            raise UnauthorizedActionError(
                action="archive",
                resource="task",
                resource_id=task_id,
            )

        self._require_project_access(task.project_id, user_id, role)

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        if not can_transition_task_status(task.status, TaskStatus.archived):
            raise TaskStateConflictError(
                None,
                TaskStatus.archived.value,
            )

        payload = TaskUpdate(
            title=task.title,
            description=task.description,
            status=TaskStatus.archived,
            priority=task.priority,
        )
        return self.task_repository.update(task, payload)

    def xǁTaskServiceǁarchive__mutmut_43(self, task_id: int, *, user_id: int, role: str):
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        role_value = getattr(role, "value", role)
        if role_value not in {"admin", "manager"}:
            raise UnauthorizedActionError(
                action="archive",
                resource="task",
                resource_id=task_id,
            )

        self._require_project_access(task.project_id, user_id, role)

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        if not can_transition_task_status(task.status, TaskStatus.archived):
            raise TaskStateConflictError(
                task.status.value,
                None,
            )

        payload = TaskUpdate(
            title=task.title,
            description=task.description,
            status=TaskStatus.archived,
            priority=task.priority,
        )
        return self.task_repository.update(task, payload)

    def xǁTaskServiceǁarchive__mutmut_44(self, task_id: int, *, user_id: int, role: str):
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        role_value = getattr(role, "value", role)
        if role_value not in {"admin", "manager"}:
            raise UnauthorizedActionError(
                action="archive",
                resource="task",
                resource_id=task_id,
            )

        self._require_project_access(task.project_id, user_id, role)

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        if not can_transition_task_status(task.status, TaskStatus.archived):
            raise TaskStateConflictError(
                TaskStatus.archived.value,
            )

        payload = TaskUpdate(
            title=task.title,
            description=task.description,
            status=TaskStatus.archived,
            priority=task.priority,
        )
        return self.task_repository.update(task, payload)

    def xǁTaskServiceǁarchive__mutmut_45(self, task_id: int, *, user_id: int, role: str):
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        role_value = getattr(role, "value", role)
        if role_value not in {"admin", "manager"}:
            raise UnauthorizedActionError(
                action="archive",
                resource="task",
                resource_id=task_id,
            )

        self._require_project_access(task.project_id, user_id, role)

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        if not can_transition_task_status(task.status, TaskStatus.archived):
            raise TaskStateConflictError(
                task.status.value,
            )

        payload = TaskUpdate(
            title=task.title,
            description=task.description,
            status=TaskStatus.archived,
            priority=task.priority,
        )
        return self.task_repository.update(task, payload)

    def xǁTaskServiceǁarchive__mutmut_46(self, task_id: int, *, user_id: int, role: str):
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        role_value = getattr(role, "value", role)
        if role_value not in {"admin", "manager"}:
            raise UnauthorizedActionError(
                action="archive",
                resource="task",
                resource_id=task_id,
            )

        self._require_project_access(task.project_id, user_id, role)

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        if not can_transition_task_status(task.status, TaskStatus.archived):
            raise TaskStateConflictError(
                task.status.value,
                TaskStatus.archived.value,
            )

        payload = None
        return self.task_repository.update(task, payload)

    def xǁTaskServiceǁarchive__mutmut_47(self, task_id: int, *, user_id: int, role: str):
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        role_value = getattr(role, "value", role)
        if role_value not in {"admin", "manager"}:
            raise UnauthorizedActionError(
                action="archive",
                resource="task",
                resource_id=task_id,
            )

        self._require_project_access(task.project_id, user_id, role)

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        if not can_transition_task_status(task.status, TaskStatus.archived):
            raise TaskStateConflictError(
                task.status.value,
                TaskStatus.archived.value,
            )

        payload = TaskUpdate(
            title=None,
            description=task.description,
            status=TaskStatus.archived,
            priority=task.priority,
        )
        return self.task_repository.update(task, payload)

    def xǁTaskServiceǁarchive__mutmut_48(self, task_id: int, *, user_id: int, role: str):
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        role_value = getattr(role, "value", role)
        if role_value not in {"admin", "manager"}:
            raise UnauthorizedActionError(
                action="archive",
                resource="task",
                resource_id=task_id,
            )

        self._require_project_access(task.project_id, user_id, role)

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        if not can_transition_task_status(task.status, TaskStatus.archived):
            raise TaskStateConflictError(
                task.status.value,
                TaskStatus.archived.value,
            )

        payload = TaskUpdate(
            title=task.title,
            description=None,
            status=TaskStatus.archived,
            priority=task.priority,
        )
        return self.task_repository.update(task, payload)

    def xǁTaskServiceǁarchive__mutmut_49(self, task_id: int, *, user_id: int, role: str):
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        role_value = getattr(role, "value", role)
        if role_value not in {"admin", "manager"}:
            raise UnauthorizedActionError(
                action="archive",
                resource="task",
                resource_id=task_id,
            )

        self._require_project_access(task.project_id, user_id, role)

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        if not can_transition_task_status(task.status, TaskStatus.archived):
            raise TaskStateConflictError(
                task.status.value,
                TaskStatus.archived.value,
            )

        payload = TaskUpdate(
            title=task.title,
            description=task.description,
            status=None,
            priority=task.priority,
        )
        return self.task_repository.update(task, payload)

    def xǁTaskServiceǁarchive__mutmut_50(self, task_id: int, *, user_id: int, role: str):
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        role_value = getattr(role, "value", role)
        if role_value not in {"admin", "manager"}:
            raise UnauthorizedActionError(
                action="archive",
                resource="task",
                resource_id=task_id,
            )

        self._require_project_access(task.project_id, user_id, role)

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        if not can_transition_task_status(task.status, TaskStatus.archived):
            raise TaskStateConflictError(
                task.status.value,
                TaskStatus.archived.value,
            )

        payload = TaskUpdate(
            title=task.title,
            description=task.description,
            status=TaskStatus.archived,
            priority=None,
        )
        return self.task_repository.update(task, payload)

    def xǁTaskServiceǁarchive__mutmut_51(self, task_id: int, *, user_id: int, role: str):
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        role_value = getattr(role, "value", role)
        if role_value not in {"admin", "manager"}:
            raise UnauthorizedActionError(
                action="archive",
                resource="task",
                resource_id=task_id,
            )

        self._require_project_access(task.project_id, user_id, role)

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        if not can_transition_task_status(task.status, TaskStatus.archived):
            raise TaskStateConflictError(
                task.status.value,
                TaskStatus.archived.value,
            )

        payload = TaskUpdate(
            description=task.description,
            status=TaskStatus.archived,
            priority=task.priority,
        )
        return self.task_repository.update(task, payload)

    def xǁTaskServiceǁarchive__mutmut_52(self, task_id: int, *, user_id: int, role: str):
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        role_value = getattr(role, "value", role)
        if role_value not in {"admin", "manager"}:
            raise UnauthorizedActionError(
                action="archive",
                resource="task",
                resource_id=task_id,
            )

        self._require_project_access(task.project_id, user_id, role)

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        if not can_transition_task_status(task.status, TaskStatus.archived):
            raise TaskStateConflictError(
                task.status.value,
                TaskStatus.archived.value,
            )

        payload = TaskUpdate(
            title=task.title,
            status=TaskStatus.archived,
            priority=task.priority,
        )
        return self.task_repository.update(task, payload)

    def xǁTaskServiceǁarchive__mutmut_53(self, task_id: int, *, user_id: int, role: str):
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        role_value = getattr(role, "value", role)
        if role_value not in {"admin", "manager"}:
            raise UnauthorizedActionError(
                action="archive",
                resource="task",
                resource_id=task_id,
            )

        self._require_project_access(task.project_id, user_id, role)

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        if not can_transition_task_status(task.status, TaskStatus.archived):
            raise TaskStateConflictError(
                task.status.value,
                TaskStatus.archived.value,
            )

        payload = TaskUpdate(
            title=task.title,
            description=task.description,
            priority=task.priority,
        )
        return self.task_repository.update(task, payload)

    def xǁTaskServiceǁarchive__mutmut_54(self, task_id: int, *, user_id: int, role: str):
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        role_value = getattr(role, "value", role)
        if role_value not in {"admin", "manager"}:
            raise UnauthorizedActionError(
                action="archive",
                resource="task",
                resource_id=task_id,
            )

        self._require_project_access(task.project_id, user_id, role)

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        if not can_transition_task_status(task.status, TaskStatus.archived):
            raise TaskStateConflictError(
                task.status.value,
                TaskStatus.archived.value,
            )

        payload = TaskUpdate(
            title=task.title,
            description=task.description,
            status=TaskStatus.archived,
        )
        return self.task_repository.update(task, payload)

    def xǁTaskServiceǁarchive__mutmut_55(self, task_id: int, *, user_id: int, role: str):
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        role_value = getattr(role, "value", role)
        if role_value not in {"admin", "manager"}:
            raise UnauthorizedActionError(
                action="archive",
                resource="task",
                resource_id=task_id,
            )

        self._require_project_access(task.project_id, user_id, role)

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        if not can_transition_task_status(task.status, TaskStatus.archived):
            raise TaskStateConflictError(
                task.status.value,
                TaskStatus.archived.value,
            )

        payload = TaskUpdate(
            title=task.title,
            description=task.description,
            status=TaskStatus.archived,
            priority=task.priority,
        )
        return self.task_repository.update(None, payload)

    def xǁTaskServiceǁarchive__mutmut_56(self, task_id: int, *, user_id: int, role: str):
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        role_value = getattr(role, "value", role)
        if role_value not in {"admin", "manager"}:
            raise UnauthorizedActionError(
                action="archive",
                resource="task",
                resource_id=task_id,
            )

        self._require_project_access(task.project_id, user_id, role)

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        if not can_transition_task_status(task.status, TaskStatus.archived):
            raise TaskStateConflictError(
                task.status.value,
                TaskStatus.archived.value,
            )

        payload = TaskUpdate(
            title=task.title,
            description=task.description,
            status=TaskStatus.archived,
            priority=task.priority,
        )
        return self.task_repository.update(task, None)

    def xǁTaskServiceǁarchive__mutmut_57(self, task_id: int, *, user_id: int, role: str):
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        role_value = getattr(role, "value", role)
        if role_value not in {"admin", "manager"}:
            raise UnauthorizedActionError(
                action="archive",
                resource="task",
                resource_id=task_id,
            )

        self._require_project_access(task.project_id, user_id, role)

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        if not can_transition_task_status(task.status, TaskStatus.archived):
            raise TaskStateConflictError(
                task.status.value,
                TaskStatus.archived.value,
            )

        payload = TaskUpdate(
            title=task.title,
            description=task.description,
            status=TaskStatus.archived,
            priority=task.priority,
        )
        return self.task_repository.update(payload)

    def xǁTaskServiceǁarchive__mutmut_58(self, task_id: int, *, user_id: int, role: str):
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        role_value = getattr(role, "value", role)
        if role_value not in {"admin", "manager"}:
            raise UnauthorizedActionError(
                action="archive",
                resource="task",
                resource_id=task_id,
            )

        self._require_project_access(task.project_id, user_id, role)

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        if not can_transition_task_status(task.status, TaskStatus.archived):
            raise TaskStateConflictError(
                task.status.value,
                TaskStatus.archived.value,
            )

        payload = TaskUpdate(
            title=task.title,
            description=task.description,
            status=TaskStatus.archived,
            priority=task.priority,
        )
        return self.task_repository.update(
            task,
        )

    @_mutmut_mutated(mutants_xǁTaskServiceǁdelete__mutmut)
    def delete(self, task_id: int, *, user_id: int, role: str) -> None:
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_project_access(task.project_id, user_id, role)

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        role_value = getattr(role, "value", role)
        if role_value != "admin":
            raise UnauthorizedActionError(
                action="delete",
                resource="task",
                resource_id=task_id,
            )

        self.task_repository.soft_delete(task)

    def xǁTaskServiceǁdelete__mutmut_orig(self, task_id: int, *, user_id: int, role: str) -> None:
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_project_access(task.project_id, user_id, role)

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        role_value = getattr(role, "value", role)
        if role_value != "admin":
            raise UnauthorizedActionError(
                action="delete",
                resource="task",
                resource_id=task_id,
            )

        self.task_repository.soft_delete(task)

    def xǁTaskServiceǁdelete__mutmut_1(self, task_id: int, *, user_id: int, role: str) -> None:
        task = None

        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_project_access(task.project_id, user_id, role)

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        role_value = getattr(role, "value", role)
        if role_value != "admin":
            raise UnauthorizedActionError(
                action="delete",
                resource="task",
                resource_id=task_id,
            )

        self.task_repository.soft_delete(task)

    def xǁTaskServiceǁdelete__mutmut_2(self, task_id: int, *, user_id: int, role: str) -> None:
        task = self.task_repository.get_by_id(None)

        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_project_access(task.project_id, user_id, role)

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        role_value = getattr(role, "value", role)
        if role_value != "admin":
            raise UnauthorizedActionError(
                action="delete",
                resource="task",
                resource_id=task_id,
            )

        self.task_repository.soft_delete(task)

    def xǁTaskServiceǁdelete__mutmut_3(self, task_id: int, *, user_id: int, role: str) -> None:
        task = self.task_repository.get_by_id(task_id)

        if task is not None:
            raise TaskNotFoundError(task_id)

        self._require_project_access(task.project_id, user_id, role)

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        role_value = getattr(role, "value", role)
        if role_value != "admin":
            raise UnauthorizedActionError(
                action="delete",
                resource="task",
                resource_id=task_id,
            )

        self.task_repository.soft_delete(task)

    def xǁTaskServiceǁdelete__mutmut_4(self, task_id: int, *, user_id: int, role: str) -> None:
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(None)

        self._require_project_access(task.project_id, user_id, role)

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        role_value = getattr(role, "value", role)
        if role_value != "admin":
            raise UnauthorizedActionError(
                action="delete",
                resource="task",
                resource_id=task_id,
            )

        self.task_repository.soft_delete(task)

    def xǁTaskServiceǁdelete__mutmut_5(self, task_id: int, *, user_id: int, role: str) -> None:
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_project_access(None, user_id, role)

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        role_value = getattr(role, "value", role)
        if role_value != "admin":
            raise UnauthorizedActionError(
                action="delete",
                resource="task",
                resource_id=task_id,
            )

        self.task_repository.soft_delete(task)

    def xǁTaskServiceǁdelete__mutmut_6(self, task_id: int, *, user_id: int, role: str) -> None:
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_project_access(task.project_id, None, role)

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        role_value = getattr(role, "value", role)
        if role_value != "admin":
            raise UnauthorizedActionError(
                action="delete",
                resource="task",
                resource_id=task_id,
            )

        self.task_repository.soft_delete(task)

    def xǁTaskServiceǁdelete__mutmut_7(self, task_id: int, *, user_id: int, role: str) -> None:
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_project_access(task.project_id, user_id, None)

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        role_value = getattr(role, "value", role)
        if role_value != "admin":
            raise UnauthorizedActionError(
                action="delete",
                resource="task",
                resource_id=task_id,
            )

        self.task_repository.soft_delete(task)

    def xǁTaskServiceǁdelete__mutmut_8(self, task_id: int, *, user_id: int, role: str) -> None:
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_project_access(user_id, role)

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        role_value = getattr(role, "value", role)
        if role_value != "admin":
            raise UnauthorizedActionError(
                action="delete",
                resource="task",
                resource_id=task_id,
            )

        self.task_repository.soft_delete(task)

    def xǁTaskServiceǁdelete__mutmut_9(self, task_id: int, *, user_id: int, role: str) -> None:
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_project_access(task.project_id, role)

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        role_value = getattr(role, "value", role)
        if role_value != "admin":
            raise UnauthorizedActionError(
                action="delete",
                resource="task",
                resource_id=task_id,
            )

        self.task_repository.soft_delete(task)

    def xǁTaskServiceǁdelete__mutmut_10(self, task_id: int, *, user_id: int, role: str) -> None:
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_project_access(
            task.project_id,
            user_id,
        )

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        role_value = getattr(role, "value", role)
        if role_value != "admin":
            raise UnauthorizedActionError(
                action="delete",
                resource="task",
                resource_id=task_id,
            )

        self.task_repository.soft_delete(task)

    def xǁTaskServiceǁdelete__mutmut_11(self, task_id: int, *, user_id: int, role: str) -> None:
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_project_access(task.project_id, user_id, role)

        if task.status != TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        role_value = getattr(role, "value", role)
        if role_value != "admin":
            raise UnauthorizedActionError(
                action="delete",
                resource="task",
                resource_id=task_id,
            )

        self.task_repository.soft_delete(task)

    def xǁTaskServiceǁdelete__mutmut_12(self, task_id: int, *, user_id: int, role: str) -> None:
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_project_access(task.project_id, user_id, role)

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(None)

        role_value = getattr(role, "value", role)
        if role_value != "admin":
            raise UnauthorizedActionError(
                action="delete",
                resource="task",
                resource_id=task_id,
            )

        self.task_repository.soft_delete(task)

    def xǁTaskServiceǁdelete__mutmut_13(self, task_id: int, *, user_id: int, role: str) -> None:
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_project_access(task.project_id, user_id, role)

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        role_value = None
        if role_value != "admin":
            raise UnauthorizedActionError(
                action="delete",
                resource="task",
                resource_id=task_id,
            )

        self.task_repository.soft_delete(task)

    def xǁTaskServiceǁdelete__mutmut_14(self, task_id: int, *, user_id: int, role: str) -> None:
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_project_access(task.project_id, user_id, role)

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        role_value = getattr(None, "value", role)
        if role_value != "admin":
            raise UnauthorizedActionError(
                action="delete",
                resource="task",
                resource_id=task_id,
            )

        self.task_repository.soft_delete(task)

    def xǁTaskServiceǁdelete__mutmut_15(self, task_id: int, *, user_id: int, role: str) -> None:
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_project_access(task.project_id, user_id, role)

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        role_value = getattr(role, None, role)
        if role_value != "admin":
            raise UnauthorizedActionError(
                action="delete",
                resource="task",
                resource_id=task_id,
            )

        self.task_repository.soft_delete(task)

    def xǁTaskServiceǁdelete__mutmut_16(self, task_id: int, *, user_id: int, role: str) -> None:
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_project_access(task.project_id, user_id, role)

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        role_value = getattr(role, "value", None)
        if role_value != "admin":
            raise UnauthorizedActionError(
                action="delete",
                resource="task",
                resource_id=task_id,
            )

        self.task_repository.soft_delete(task)

    def xǁTaskServiceǁdelete__mutmut_17(self, task_id: int, *, user_id: int, role: str) -> None:
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_project_access(task.project_id, user_id, role)

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        role_value = getattr("value", role)
        if role_value != "admin":
            raise UnauthorizedActionError(
                action="delete",
                resource="task",
                resource_id=task_id,
            )

        self.task_repository.soft_delete(task)

    def xǁTaskServiceǁdelete__mutmut_18(self, task_id: int, *, user_id: int, role: str) -> None:
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_project_access(task.project_id, user_id, role)

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        role_value = getattr(role, role)
        if role_value != "admin":
            raise UnauthorizedActionError(
                action="delete",
                resource="task",
                resource_id=task_id,
            )

        self.task_repository.soft_delete(task)

    def xǁTaskServiceǁdelete__mutmut_19(self, task_id: int, *, user_id: int, role: str) -> None:
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_project_access(task.project_id, user_id, role)

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        role_value = role.value
        if role_value != "admin":
            raise UnauthorizedActionError(
                action="delete",
                resource="task",
                resource_id=task_id,
            )

        self.task_repository.soft_delete(task)

    def xǁTaskServiceǁdelete__mutmut_20(self, task_id: int, *, user_id: int, role: str) -> None:
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_project_access(task.project_id, user_id, role)

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        role_value = getattr(role, "XXvalueXX", role)
        if role_value != "admin":
            raise UnauthorizedActionError(
                action="delete",
                resource="task",
                resource_id=task_id,
            )

        self.task_repository.soft_delete(task)

    def xǁTaskServiceǁdelete__mutmut_21(self, task_id: int, *, user_id: int, role: str) -> None:
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_project_access(task.project_id, user_id, role)

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        role_value = getattr(role, "VALUE", role)
        if role_value != "admin":
            raise UnauthorizedActionError(
                action="delete",
                resource="task",
                resource_id=task_id,
            )

        self.task_repository.soft_delete(task)

    def xǁTaskServiceǁdelete__mutmut_22(self, task_id: int, *, user_id: int, role: str) -> None:
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_project_access(task.project_id, user_id, role)

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        role_value = getattr(role, "value", role)
        if role_value == "admin":
            raise UnauthorizedActionError(
                action="delete",
                resource="task",
                resource_id=task_id,
            )

        self.task_repository.soft_delete(task)

    def xǁTaskServiceǁdelete__mutmut_23(self, task_id: int, *, user_id: int, role: str) -> None:
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_project_access(task.project_id, user_id, role)

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        role_value = getattr(role, "value", role)
        if role_value != "XXadminXX":
            raise UnauthorizedActionError(
                action="delete",
                resource="task",
                resource_id=task_id,
            )

        self.task_repository.soft_delete(task)

    def xǁTaskServiceǁdelete__mutmut_24(self, task_id: int, *, user_id: int, role: str) -> None:
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_project_access(task.project_id, user_id, role)

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        role_value = getattr(role, "value", role)
        if role_value != "ADMIN":
            raise UnauthorizedActionError(
                action="delete",
                resource="task",
                resource_id=task_id,
            )

        self.task_repository.soft_delete(task)

    def xǁTaskServiceǁdelete__mutmut_25(self, task_id: int, *, user_id: int, role: str) -> None:
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_project_access(task.project_id, user_id, role)

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        role_value = getattr(role, "value", role)
        if role_value != "admin":
            raise UnauthorizedActionError(
                action=None,
                resource="task",
                resource_id=task_id,
            )

        self.task_repository.soft_delete(task)

    def xǁTaskServiceǁdelete__mutmut_26(self, task_id: int, *, user_id: int, role: str) -> None:
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_project_access(task.project_id, user_id, role)

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        role_value = getattr(role, "value", role)
        if role_value != "admin":
            raise UnauthorizedActionError(
                action="delete",
                resource=None,
                resource_id=task_id,
            )

        self.task_repository.soft_delete(task)

    def xǁTaskServiceǁdelete__mutmut_27(self, task_id: int, *, user_id: int, role: str) -> None:
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_project_access(task.project_id, user_id, role)

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        role_value = getattr(role, "value", role)
        if role_value != "admin":
            raise UnauthorizedActionError(
                action="delete",
                resource="task",
                resource_id=None,
            )

        self.task_repository.soft_delete(task)

    def xǁTaskServiceǁdelete__mutmut_28(self, task_id: int, *, user_id: int, role: str) -> None:
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_project_access(task.project_id, user_id, role)

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        role_value = getattr(role, "value", role)
        if role_value != "admin":
            raise UnauthorizedActionError(
                resource="task",
                resource_id=task_id,
            )

        self.task_repository.soft_delete(task)

    def xǁTaskServiceǁdelete__mutmut_29(self, task_id: int, *, user_id: int, role: str) -> None:
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_project_access(task.project_id, user_id, role)

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        role_value = getattr(role, "value", role)
        if role_value != "admin":
            raise UnauthorizedActionError(
                action="delete",
                resource_id=task_id,
            )

        self.task_repository.soft_delete(task)

    def xǁTaskServiceǁdelete__mutmut_30(self, task_id: int, *, user_id: int, role: str) -> None:
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_project_access(task.project_id, user_id, role)

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        role_value = getattr(role, "value", role)
        if role_value != "admin":
            raise UnauthorizedActionError(
                action="delete",
                resource="task",
            )

        self.task_repository.soft_delete(task)

    def xǁTaskServiceǁdelete__mutmut_31(self, task_id: int, *, user_id: int, role: str) -> None:
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_project_access(task.project_id, user_id, role)

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        role_value = getattr(role, "value", role)
        if role_value != "admin":
            raise UnauthorizedActionError(
                action="XXdeleteXX",
                resource="task",
                resource_id=task_id,
            )

        self.task_repository.soft_delete(task)

    def xǁTaskServiceǁdelete__mutmut_32(self, task_id: int, *, user_id: int, role: str) -> None:
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_project_access(task.project_id, user_id, role)

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        role_value = getattr(role, "value", role)
        if role_value != "admin":
            raise UnauthorizedActionError(
                action="DELETE",
                resource="task",
                resource_id=task_id,
            )

        self.task_repository.soft_delete(task)

    def xǁTaskServiceǁdelete__mutmut_33(self, task_id: int, *, user_id: int, role: str) -> None:
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_project_access(task.project_id, user_id, role)

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        role_value = getattr(role, "value", role)
        if role_value != "admin":
            raise UnauthorizedActionError(
                action="delete",
                resource="XXtaskXX",
                resource_id=task_id,
            )

        self.task_repository.soft_delete(task)

    def xǁTaskServiceǁdelete__mutmut_34(self, task_id: int, *, user_id: int, role: str) -> None:
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_project_access(task.project_id, user_id, role)

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        role_value = getattr(role, "value", role)
        if role_value != "admin":
            raise UnauthorizedActionError(
                action="delete",
                resource="TASK",
                resource_id=task_id,
            )

        self.task_repository.soft_delete(task)

    def xǁTaskServiceǁdelete__mutmut_35(self, task_id: int, *, user_id: int, role: str) -> None:
        task = self.task_repository.get_by_id(task_id)

        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_project_access(task.project_id, user_id, role)

        if task.status == TaskStatus.archived:
            raise ArchivedTaskError(task_id)

        role_value = getattr(role, "value", role)
        if role_value != "admin":
            raise UnauthorizedActionError(
                action="delete",
                resource="task",
                resource_id=task_id,
            )

        self.task_repository.soft_delete(None)

    @_mutmut_mutated(mutants_xǁTaskServiceǁlist_deleted__mutmut)
    def list_deleted(self, *, user_id: int, role: str) -> list[Task]:
        role_value = getattr(role, "value", role)
        if role_value != "admin":
            raise UnauthorizedActionError(
                action="view deleted",
                resource="tasks",
            )

        return self.task_repository.get_deleted()

    def xǁTaskServiceǁlist_deleted__mutmut_orig(self, *, user_id: int, role: str) -> list[Task]:
        role_value = getattr(role, "value", role)
        if role_value != "admin":
            raise UnauthorizedActionError(
                action="view deleted",
                resource="tasks",
            )

        return self.task_repository.get_deleted()

    def xǁTaskServiceǁlist_deleted__mutmut_1(self, *, user_id: int, role: str) -> list[Task]:
        role_value = None
        if role_value != "admin":
            raise UnauthorizedActionError(
                action="view deleted",
                resource="tasks",
            )

        return self.task_repository.get_deleted()

    def xǁTaskServiceǁlist_deleted__mutmut_2(self, *, user_id: int, role: str) -> list[Task]:
        role_value = getattr(None, "value", role)
        if role_value != "admin":
            raise UnauthorizedActionError(
                action="view deleted",
                resource="tasks",
            )

        return self.task_repository.get_deleted()

    def xǁTaskServiceǁlist_deleted__mutmut_3(self, *, user_id: int, role: str) -> list[Task]:
        role_value = getattr(role, None, role)
        if role_value != "admin":
            raise UnauthorizedActionError(
                action="view deleted",
                resource="tasks",
            )

        return self.task_repository.get_deleted()

    def xǁTaskServiceǁlist_deleted__mutmut_4(self, *, user_id: int, role: str) -> list[Task]:
        role_value = getattr(role, "value", None)
        if role_value != "admin":
            raise UnauthorizedActionError(
                action="view deleted",
                resource="tasks",
            )

        return self.task_repository.get_deleted()

    def xǁTaskServiceǁlist_deleted__mutmut_5(self, *, user_id: int, role: str) -> list[Task]:
        role_value = getattr("value", role)
        if role_value != "admin":
            raise UnauthorizedActionError(
                action="view deleted",
                resource="tasks",
            )

        return self.task_repository.get_deleted()

    def xǁTaskServiceǁlist_deleted__mutmut_6(self, *, user_id: int, role: str) -> list[Task]:
        role_value = getattr(role, role)
        if role_value != "admin":
            raise UnauthorizedActionError(
                action="view deleted",
                resource="tasks",
            )

        return self.task_repository.get_deleted()

    def xǁTaskServiceǁlist_deleted__mutmut_7(self, *, user_id: int, role: str) -> list[Task]:
        role_value = role.value
        if role_value != "admin":
            raise UnauthorizedActionError(
                action="view deleted",
                resource="tasks",
            )

        return self.task_repository.get_deleted()

    def xǁTaskServiceǁlist_deleted__mutmut_8(self, *, user_id: int, role: str) -> list[Task]:
        role_value = getattr(role, "XXvalueXX", role)
        if role_value != "admin":
            raise UnauthorizedActionError(
                action="view deleted",
                resource="tasks",
            )

        return self.task_repository.get_deleted()

    def xǁTaskServiceǁlist_deleted__mutmut_9(self, *, user_id: int, role: str) -> list[Task]:
        role_value = getattr(role, "VALUE", role)
        if role_value != "admin":
            raise UnauthorizedActionError(
                action="view deleted",
                resource="tasks",
            )

        return self.task_repository.get_deleted()

    def xǁTaskServiceǁlist_deleted__mutmut_10(self, *, user_id: int, role: str) -> list[Task]:
        role_value = getattr(role, "value", role)
        if role_value == "admin":
            raise UnauthorizedActionError(
                action="view deleted",
                resource="tasks",
            )

        return self.task_repository.get_deleted()

    def xǁTaskServiceǁlist_deleted__mutmut_11(self, *, user_id: int, role: str) -> list[Task]:
        role_value = getattr(role, "value", role)
        if role_value != "XXadminXX":
            raise UnauthorizedActionError(
                action="view deleted",
                resource="tasks",
            )

        return self.task_repository.get_deleted()

    def xǁTaskServiceǁlist_deleted__mutmut_12(self, *, user_id: int, role: str) -> list[Task]:
        role_value = getattr(role, "value", role)
        if role_value != "ADMIN":
            raise UnauthorizedActionError(
                action="view deleted",
                resource="tasks",
            )

        return self.task_repository.get_deleted()

    def xǁTaskServiceǁlist_deleted__mutmut_13(self, *, user_id: int, role: str) -> list[Task]:
        role_value = getattr(role, "value", role)
        if role_value != "admin":
            raise UnauthorizedActionError(
                action=None,
                resource="tasks",
            )

        return self.task_repository.get_deleted()

    def xǁTaskServiceǁlist_deleted__mutmut_14(self, *, user_id: int, role: str) -> list[Task]:
        role_value = getattr(role, "value", role)
        if role_value != "admin":
            raise UnauthorizedActionError(
                action="view deleted",
                resource=None,
            )

        return self.task_repository.get_deleted()

    def xǁTaskServiceǁlist_deleted__mutmut_15(self, *, user_id: int, role: str) -> list[Task]:
        role_value = getattr(role, "value", role)
        if role_value != "admin":
            raise UnauthorizedActionError(
                resource="tasks",
            )

        return self.task_repository.get_deleted()

    def xǁTaskServiceǁlist_deleted__mutmut_16(self, *, user_id: int, role: str) -> list[Task]:
        role_value = getattr(role, "value", role)
        if role_value != "admin":
            raise UnauthorizedActionError(
                action="view deleted",
            )

        return self.task_repository.get_deleted()

    def xǁTaskServiceǁlist_deleted__mutmut_17(self, *, user_id: int, role: str) -> list[Task]:
        role_value = getattr(role, "value", role)
        if role_value != "admin":
            raise UnauthorizedActionError(
                action="XXview deletedXX",
                resource="tasks",
            )

        return self.task_repository.get_deleted()

    def xǁTaskServiceǁlist_deleted__mutmut_18(self, *, user_id: int, role: str) -> list[Task]:
        role_value = getattr(role, "value", role)
        if role_value != "admin":
            raise UnauthorizedActionError(
                action="VIEW DELETED",
                resource="tasks",
            )

        return self.task_repository.get_deleted()

    def xǁTaskServiceǁlist_deleted__mutmut_19(self, *, user_id: int, role: str) -> list[Task]:
        role_value = getattr(role, "value", role)
        if role_value != "admin":
            raise UnauthorizedActionError(
                action="view deleted",
                resource="XXtasksXX",
            )

        return self.task_repository.get_deleted()

    def xǁTaskServiceǁlist_deleted__mutmut_20(self, *, user_id: int, role: str) -> list[Task]:
        role_value = getattr(role, "value", role)
        if role_value != "admin":
            raise UnauthorizedActionError(
                action="view deleted",
                resource="TASKS",
            )

        return self.task_repository.get_deleted()

    @_mutmut_mutated(mutants_xǁTaskServiceǁrestore__mutmut)
    def restore(self, task_id: int, *, user_id: int, role: str) -> Task:
        role_value = getattr(role, "value", role)
        if role_value != "admin":
            raise UnauthorizedActionError(
                action="restore",
                resource="task",
                resource_id=task_id,
            )

        task = self.task_repository.get_deleted_by_id(task_id)
        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_project_access(task.project_id, user_id, role)
        return self.task_repository.restore(task)

    def xǁTaskServiceǁrestore__mutmut_orig(self, task_id: int, *, user_id: int, role: str) -> Task:
        role_value = getattr(role, "value", role)
        if role_value != "admin":
            raise UnauthorizedActionError(
                action="restore",
                resource="task",
                resource_id=task_id,
            )

        task = self.task_repository.get_deleted_by_id(task_id)
        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_project_access(task.project_id, user_id, role)
        return self.task_repository.restore(task)

    def xǁTaskServiceǁrestore__mutmut_1(self, task_id: int, *, user_id: int, role: str) -> Task:
        role_value = None
        if role_value != "admin":
            raise UnauthorizedActionError(
                action="restore",
                resource="task",
                resource_id=task_id,
            )

        task = self.task_repository.get_deleted_by_id(task_id)
        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_project_access(task.project_id, user_id, role)
        return self.task_repository.restore(task)

    def xǁTaskServiceǁrestore__mutmut_2(self, task_id: int, *, user_id: int, role: str) -> Task:
        role_value = getattr(None, "value", role)
        if role_value != "admin":
            raise UnauthorizedActionError(
                action="restore",
                resource="task",
                resource_id=task_id,
            )

        task = self.task_repository.get_deleted_by_id(task_id)
        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_project_access(task.project_id, user_id, role)
        return self.task_repository.restore(task)

    def xǁTaskServiceǁrestore__mutmut_3(self, task_id: int, *, user_id: int, role: str) -> Task:
        role_value = getattr(role, None, role)
        if role_value != "admin":
            raise UnauthorizedActionError(
                action="restore",
                resource="task",
                resource_id=task_id,
            )

        task = self.task_repository.get_deleted_by_id(task_id)
        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_project_access(task.project_id, user_id, role)
        return self.task_repository.restore(task)

    def xǁTaskServiceǁrestore__mutmut_4(self, task_id: int, *, user_id: int, role: str) -> Task:
        role_value = getattr(role, "value", None)
        if role_value != "admin":
            raise UnauthorizedActionError(
                action="restore",
                resource="task",
                resource_id=task_id,
            )

        task = self.task_repository.get_deleted_by_id(task_id)
        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_project_access(task.project_id, user_id, role)
        return self.task_repository.restore(task)

    def xǁTaskServiceǁrestore__mutmut_5(self, task_id: int, *, user_id: int, role: str) -> Task:
        role_value = getattr("value", role)
        if role_value != "admin":
            raise UnauthorizedActionError(
                action="restore",
                resource="task",
                resource_id=task_id,
            )

        task = self.task_repository.get_deleted_by_id(task_id)
        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_project_access(task.project_id, user_id, role)
        return self.task_repository.restore(task)

    def xǁTaskServiceǁrestore__mutmut_6(self, task_id: int, *, user_id: int, role: str) -> Task:
        role_value = getattr(role, role)
        if role_value != "admin":
            raise UnauthorizedActionError(
                action="restore",
                resource="task",
                resource_id=task_id,
            )

        task = self.task_repository.get_deleted_by_id(task_id)
        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_project_access(task.project_id, user_id, role)
        return self.task_repository.restore(task)

    def xǁTaskServiceǁrestore__mutmut_7(self, task_id: int, *, user_id: int, role: str) -> Task:
        role_value = role.value
        if role_value != "admin":
            raise UnauthorizedActionError(
                action="restore",
                resource="task",
                resource_id=task_id,
            )

        task = self.task_repository.get_deleted_by_id(task_id)
        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_project_access(task.project_id, user_id, role)
        return self.task_repository.restore(task)

    def xǁTaskServiceǁrestore__mutmut_8(self, task_id: int, *, user_id: int, role: str) -> Task:
        role_value = getattr(role, "XXvalueXX", role)
        if role_value != "admin":
            raise UnauthorizedActionError(
                action="restore",
                resource="task",
                resource_id=task_id,
            )

        task = self.task_repository.get_deleted_by_id(task_id)
        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_project_access(task.project_id, user_id, role)
        return self.task_repository.restore(task)

    def xǁTaskServiceǁrestore__mutmut_9(self, task_id: int, *, user_id: int, role: str) -> Task:
        role_value = getattr(role, "VALUE", role)
        if role_value != "admin":
            raise UnauthorizedActionError(
                action="restore",
                resource="task",
                resource_id=task_id,
            )

        task = self.task_repository.get_deleted_by_id(task_id)
        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_project_access(task.project_id, user_id, role)
        return self.task_repository.restore(task)

    def xǁTaskServiceǁrestore__mutmut_10(self, task_id: int, *, user_id: int, role: str) -> Task:
        role_value = getattr(role, "value", role)
        if role_value == "admin":
            raise UnauthorizedActionError(
                action="restore",
                resource="task",
                resource_id=task_id,
            )

        task = self.task_repository.get_deleted_by_id(task_id)
        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_project_access(task.project_id, user_id, role)
        return self.task_repository.restore(task)

    def xǁTaskServiceǁrestore__mutmut_11(self, task_id: int, *, user_id: int, role: str) -> Task:
        role_value = getattr(role, "value", role)
        if role_value != "XXadminXX":
            raise UnauthorizedActionError(
                action="restore",
                resource="task",
                resource_id=task_id,
            )

        task = self.task_repository.get_deleted_by_id(task_id)
        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_project_access(task.project_id, user_id, role)
        return self.task_repository.restore(task)

    def xǁTaskServiceǁrestore__mutmut_12(self, task_id: int, *, user_id: int, role: str) -> Task:
        role_value = getattr(role, "value", role)
        if role_value != "ADMIN":
            raise UnauthorizedActionError(
                action="restore",
                resource="task",
                resource_id=task_id,
            )

        task = self.task_repository.get_deleted_by_id(task_id)
        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_project_access(task.project_id, user_id, role)
        return self.task_repository.restore(task)

    def xǁTaskServiceǁrestore__mutmut_13(self, task_id: int, *, user_id: int, role: str) -> Task:
        role_value = getattr(role, "value", role)
        if role_value != "admin":
            raise UnauthorizedActionError(
                action=None,
                resource="task",
                resource_id=task_id,
            )

        task = self.task_repository.get_deleted_by_id(task_id)
        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_project_access(task.project_id, user_id, role)
        return self.task_repository.restore(task)

    def xǁTaskServiceǁrestore__mutmut_14(self, task_id: int, *, user_id: int, role: str) -> Task:
        role_value = getattr(role, "value", role)
        if role_value != "admin":
            raise UnauthorizedActionError(
                action="restore",
                resource=None,
                resource_id=task_id,
            )

        task = self.task_repository.get_deleted_by_id(task_id)
        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_project_access(task.project_id, user_id, role)
        return self.task_repository.restore(task)

    def xǁTaskServiceǁrestore__mutmut_15(self, task_id: int, *, user_id: int, role: str) -> Task:
        role_value = getattr(role, "value", role)
        if role_value != "admin":
            raise UnauthorizedActionError(
                action="restore",
                resource="task",
                resource_id=None,
            )

        task = self.task_repository.get_deleted_by_id(task_id)
        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_project_access(task.project_id, user_id, role)
        return self.task_repository.restore(task)

    def xǁTaskServiceǁrestore__mutmut_16(self, task_id: int, *, user_id: int, role: str) -> Task:
        role_value = getattr(role, "value", role)
        if role_value != "admin":
            raise UnauthorizedActionError(
                resource="task",
                resource_id=task_id,
            )

        task = self.task_repository.get_deleted_by_id(task_id)
        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_project_access(task.project_id, user_id, role)
        return self.task_repository.restore(task)

    def xǁTaskServiceǁrestore__mutmut_17(self, task_id: int, *, user_id: int, role: str) -> Task:
        role_value = getattr(role, "value", role)
        if role_value != "admin":
            raise UnauthorizedActionError(
                action="restore",
                resource_id=task_id,
            )

        task = self.task_repository.get_deleted_by_id(task_id)
        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_project_access(task.project_id, user_id, role)
        return self.task_repository.restore(task)

    def xǁTaskServiceǁrestore__mutmut_18(self, task_id: int, *, user_id: int, role: str) -> Task:
        role_value = getattr(role, "value", role)
        if role_value != "admin":
            raise UnauthorizedActionError(
                action="restore",
                resource="task",
            )

        task = self.task_repository.get_deleted_by_id(task_id)
        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_project_access(task.project_id, user_id, role)
        return self.task_repository.restore(task)

    def xǁTaskServiceǁrestore__mutmut_19(self, task_id: int, *, user_id: int, role: str) -> Task:
        role_value = getattr(role, "value", role)
        if role_value != "admin":
            raise UnauthorizedActionError(
                action="XXrestoreXX",
                resource="task",
                resource_id=task_id,
            )

        task = self.task_repository.get_deleted_by_id(task_id)
        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_project_access(task.project_id, user_id, role)
        return self.task_repository.restore(task)

    def xǁTaskServiceǁrestore__mutmut_20(self, task_id: int, *, user_id: int, role: str) -> Task:
        role_value = getattr(role, "value", role)
        if role_value != "admin":
            raise UnauthorizedActionError(
                action="RESTORE",
                resource="task",
                resource_id=task_id,
            )

        task = self.task_repository.get_deleted_by_id(task_id)
        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_project_access(task.project_id, user_id, role)
        return self.task_repository.restore(task)

    def xǁTaskServiceǁrestore__mutmut_21(self, task_id: int, *, user_id: int, role: str) -> Task:
        role_value = getattr(role, "value", role)
        if role_value != "admin":
            raise UnauthorizedActionError(
                action="restore",
                resource="XXtaskXX",
                resource_id=task_id,
            )

        task = self.task_repository.get_deleted_by_id(task_id)
        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_project_access(task.project_id, user_id, role)
        return self.task_repository.restore(task)

    def xǁTaskServiceǁrestore__mutmut_22(self, task_id: int, *, user_id: int, role: str) -> Task:
        role_value = getattr(role, "value", role)
        if role_value != "admin":
            raise UnauthorizedActionError(
                action="restore",
                resource="TASK",
                resource_id=task_id,
            )

        task = self.task_repository.get_deleted_by_id(task_id)
        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_project_access(task.project_id, user_id, role)
        return self.task_repository.restore(task)

    def xǁTaskServiceǁrestore__mutmut_23(self, task_id: int, *, user_id: int, role: str) -> Task:
        role_value = getattr(role, "value", role)
        if role_value != "admin":
            raise UnauthorizedActionError(
                action="restore",
                resource="task",
                resource_id=task_id,
            )

        task = None
        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_project_access(task.project_id, user_id, role)
        return self.task_repository.restore(task)

    def xǁTaskServiceǁrestore__mutmut_24(self, task_id: int, *, user_id: int, role: str) -> Task:
        role_value = getattr(role, "value", role)
        if role_value != "admin":
            raise UnauthorizedActionError(
                action="restore",
                resource="task",
                resource_id=task_id,
            )

        task = self.task_repository.get_deleted_by_id(None)
        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_project_access(task.project_id, user_id, role)
        return self.task_repository.restore(task)

    def xǁTaskServiceǁrestore__mutmut_25(self, task_id: int, *, user_id: int, role: str) -> Task:
        role_value = getattr(role, "value", role)
        if role_value != "admin":
            raise UnauthorizedActionError(
                action="restore",
                resource="task",
                resource_id=task_id,
            )

        task = self.task_repository.get_deleted_by_id(task_id)
        if task is not None:
            raise TaskNotFoundError(task_id)

        self._require_project_access(task.project_id, user_id, role)
        return self.task_repository.restore(task)

    def xǁTaskServiceǁrestore__mutmut_26(self, task_id: int, *, user_id: int, role: str) -> Task:
        role_value = getattr(role, "value", role)
        if role_value != "admin":
            raise UnauthorizedActionError(
                action="restore",
                resource="task",
                resource_id=task_id,
            )

        task = self.task_repository.get_deleted_by_id(task_id)
        if task is None:
            raise TaskNotFoundError(None)

        self._require_project_access(task.project_id, user_id, role)
        return self.task_repository.restore(task)

    def xǁTaskServiceǁrestore__mutmut_27(self, task_id: int, *, user_id: int, role: str) -> Task:
        role_value = getattr(role, "value", role)
        if role_value != "admin":
            raise UnauthorizedActionError(
                action="restore",
                resource="task",
                resource_id=task_id,
            )

        task = self.task_repository.get_deleted_by_id(task_id)
        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_project_access(None, user_id, role)
        return self.task_repository.restore(task)

    def xǁTaskServiceǁrestore__mutmut_28(self, task_id: int, *, user_id: int, role: str) -> Task:
        role_value = getattr(role, "value", role)
        if role_value != "admin":
            raise UnauthorizedActionError(
                action="restore",
                resource="task",
                resource_id=task_id,
            )

        task = self.task_repository.get_deleted_by_id(task_id)
        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_project_access(task.project_id, None, role)
        return self.task_repository.restore(task)

    def xǁTaskServiceǁrestore__mutmut_29(self, task_id: int, *, user_id: int, role: str) -> Task:
        role_value = getattr(role, "value", role)
        if role_value != "admin":
            raise UnauthorizedActionError(
                action="restore",
                resource="task",
                resource_id=task_id,
            )

        task = self.task_repository.get_deleted_by_id(task_id)
        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_project_access(task.project_id, user_id, None)
        return self.task_repository.restore(task)

    def xǁTaskServiceǁrestore__mutmut_30(self, task_id: int, *, user_id: int, role: str) -> Task:
        role_value = getattr(role, "value", role)
        if role_value != "admin":
            raise UnauthorizedActionError(
                action="restore",
                resource="task",
                resource_id=task_id,
            )

        task = self.task_repository.get_deleted_by_id(task_id)
        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_project_access(user_id, role)
        return self.task_repository.restore(task)

    def xǁTaskServiceǁrestore__mutmut_31(self, task_id: int, *, user_id: int, role: str) -> Task:
        role_value = getattr(role, "value", role)
        if role_value != "admin":
            raise UnauthorizedActionError(
                action="restore",
                resource="task",
                resource_id=task_id,
            )

        task = self.task_repository.get_deleted_by_id(task_id)
        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_project_access(task.project_id, role)
        return self.task_repository.restore(task)

    def xǁTaskServiceǁrestore__mutmut_32(self, task_id: int, *, user_id: int, role: str) -> Task:
        role_value = getattr(role, "value", role)
        if role_value != "admin":
            raise UnauthorizedActionError(
                action="restore",
                resource="task",
                resource_id=task_id,
            )

        task = self.task_repository.get_deleted_by_id(task_id)
        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_project_access(
            task.project_id,
            user_id,
        )
        return self.task_repository.restore(task)

    def xǁTaskServiceǁrestore__mutmut_33(self, task_id: int, *, user_id: int, role: str) -> Task:
        role_value = getattr(role, "value", role)
        if role_value != "admin":
            raise UnauthorizedActionError(
                action="restore",
                resource="task",
                resource_id=task_id,
            )

        task = self.task_repository.get_deleted_by_id(task_id)
        if task is None:
            raise TaskNotFoundError(task_id)

        self._require_project_access(task.project_id, user_id, role)
        return self.task_repository.restore(None)


mutants_xǁTaskServiceǁ__init____mutmut["_mutmut_orig"] = (
    TaskService.xǁTaskServiceǁ__init____mutmut_orig
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁ__init____mutmut["xǁTaskServiceǁ__init____mutmut_1"] = (
    TaskService.xǁTaskServiceǁ__init____mutmut_1
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁ__init____mutmut["xǁTaskServiceǁ__init____mutmut_2"] = (
    TaskService.xǁTaskServiceǁ__init____mutmut_2
)  # type: ignore # mutmut generated

mutants_xǁTaskServiceǁ_require_project_access__mutmut["_mutmut_orig"] = (
    TaskService.xǁTaskServiceǁ_require_project_access__mutmut_orig
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁ_require_project_access__mutmut[
    "xǁTaskServiceǁ_require_project_access__mutmut_1"
] = TaskService.xǁTaskServiceǁ_require_project_access__mutmut_1  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁ_require_project_access__mutmut[
    "xǁTaskServiceǁ_require_project_access__mutmut_2"
] = TaskService.xǁTaskServiceǁ_require_project_access__mutmut_2  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁ_require_project_access__mutmut[
    "xǁTaskServiceǁ_require_project_access__mutmut_3"
] = TaskService.xǁTaskServiceǁ_require_project_access__mutmut_3  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁ_require_project_access__mutmut[
    "xǁTaskServiceǁ_require_project_access__mutmut_4"
] = TaskService.xǁTaskServiceǁ_require_project_access__mutmut_4  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁ_require_project_access__mutmut[
    "xǁTaskServiceǁ_require_project_access__mutmut_5"
] = TaskService.xǁTaskServiceǁ_require_project_access__mutmut_5  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁ_require_project_access__mutmut[
    "xǁTaskServiceǁ_require_project_access__mutmut_6"
] = TaskService.xǁTaskServiceǁ_require_project_access__mutmut_6  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁ_require_project_access__mutmut[
    "xǁTaskServiceǁ_require_project_access__mutmut_7"
] = TaskService.xǁTaskServiceǁ_require_project_access__mutmut_7  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁ_require_project_access__mutmut[
    "xǁTaskServiceǁ_require_project_access__mutmut_8"
] = TaskService.xǁTaskServiceǁ_require_project_access__mutmut_8  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁ_require_project_access__mutmut[
    "xǁTaskServiceǁ_require_project_access__mutmut_9"
] = TaskService.xǁTaskServiceǁ_require_project_access__mutmut_9  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁ_require_project_access__mutmut[
    "xǁTaskServiceǁ_require_project_access__mutmut_10"
] = TaskService.xǁTaskServiceǁ_require_project_access__mutmut_10  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁ_require_project_access__mutmut[
    "xǁTaskServiceǁ_require_project_access__mutmut_11"
] = TaskService.xǁTaskServiceǁ_require_project_access__mutmut_11  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁ_require_project_access__mutmut[
    "xǁTaskServiceǁ_require_project_access__mutmut_12"
] = TaskService.xǁTaskServiceǁ_require_project_access__mutmut_12  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁ_require_project_access__mutmut[
    "xǁTaskServiceǁ_require_project_access__mutmut_13"
] = TaskService.xǁTaskServiceǁ_require_project_access__mutmut_13  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁ_require_project_access__mutmut[
    "xǁTaskServiceǁ_require_project_access__mutmut_14"
] = TaskService.xǁTaskServiceǁ_require_project_access__mutmut_14  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁ_require_project_access__mutmut[
    "xǁTaskServiceǁ_require_project_access__mutmut_15"
] = TaskService.xǁTaskServiceǁ_require_project_access__mutmut_15  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁ_require_project_access__mutmut[
    "xǁTaskServiceǁ_require_project_access__mutmut_16"
] = TaskService.xǁTaskServiceǁ_require_project_access__mutmut_16  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁ_require_project_access__mutmut[
    "xǁTaskServiceǁ_require_project_access__mutmut_17"
] = TaskService.xǁTaskServiceǁ_require_project_access__mutmut_17  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁ_require_project_access__mutmut[
    "xǁTaskServiceǁ_require_project_access__mutmut_18"
] = TaskService.xǁTaskServiceǁ_require_project_access__mutmut_18  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁ_require_project_access__mutmut[
    "xǁTaskServiceǁ_require_project_access__mutmut_19"
] = TaskService.xǁTaskServiceǁ_require_project_access__mutmut_19  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁ_require_project_access__mutmut[
    "xǁTaskServiceǁ_require_project_access__mutmut_20"
] = TaskService.xǁTaskServiceǁ_require_project_access__mutmut_20  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁ_require_project_access__mutmut[
    "xǁTaskServiceǁ_require_project_access__mutmut_21"
] = TaskService.xǁTaskServiceǁ_require_project_access__mutmut_21  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁ_require_project_access__mutmut[
    "xǁTaskServiceǁ_require_project_access__mutmut_22"
] = TaskService.xǁTaskServiceǁ_require_project_access__mutmut_22  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁ_require_project_access__mutmut[
    "xǁTaskServiceǁ_require_project_access__mutmut_23"
] = TaskService.xǁTaskServiceǁ_require_project_access__mutmut_23  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁ_require_project_access__mutmut[
    "xǁTaskServiceǁ_require_project_access__mutmut_24"
] = TaskService.xǁTaskServiceǁ_require_project_access__mutmut_24  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁ_require_project_access__mutmut[
    "xǁTaskServiceǁ_require_project_access__mutmut_25"
] = TaskService.xǁTaskServiceǁ_require_project_access__mutmut_25  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁ_require_project_access__mutmut[
    "xǁTaskServiceǁ_require_project_access__mutmut_26"
] = TaskService.xǁTaskServiceǁ_require_project_access__mutmut_26  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁ_require_project_access__mutmut[
    "xǁTaskServiceǁ_require_project_access__mutmut_27"
] = TaskService.xǁTaskServiceǁ_require_project_access__mutmut_27  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁ_require_project_access__mutmut[
    "xǁTaskServiceǁ_require_project_access__mutmut_28"
] = TaskService.xǁTaskServiceǁ_require_project_access__mutmut_28  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁ_require_project_access__mutmut[
    "xǁTaskServiceǁ_require_project_access__mutmut_29"
] = TaskService.xǁTaskServiceǁ_require_project_access__mutmut_29  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁ_require_project_access__mutmut[
    "xǁTaskServiceǁ_require_project_access__mutmut_30"
] = TaskService.xǁTaskServiceǁ_require_project_access__mutmut_30  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁ_require_project_access__mutmut[
    "xǁTaskServiceǁ_require_project_access__mutmut_31"
] = TaskService.xǁTaskServiceǁ_require_project_access__mutmut_31  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁ_require_project_access__mutmut[
    "xǁTaskServiceǁ_require_project_access__mutmut_32"
] = TaskService.xǁTaskServiceǁ_require_project_access__mutmut_32  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁ_require_project_access__mutmut[
    "xǁTaskServiceǁ_require_project_access__mutmut_33"
] = TaskService.xǁTaskServiceǁ_require_project_access__mutmut_33  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁ_require_project_access__mutmut[
    "xǁTaskServiceǁ_require_project_access__mutmut_34"
] = TaskService.xǁTaskServiceǁ_require_project_access__mutmut_34  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁ_require_project_access__mutmut[
    "xǁTaskServiceǁ_require_project_access__mutmut_35"
] = TaskService.xǁTaskServiceǁ_require_project_access__mutmut_35  # type: ignore # mutmut generated

mutants_xǁTaskServiceǁcreate__mutmut["_mutmut_orig"] = TaskService.xǁTaskServiceǁcreate__mutmut_orig  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁcreate__mutmut["xǁTaskServiceǁcreate__mutmut_1"] = (
    TaskService.xǁTaskServiceǁcreate__mutmut_1
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁcreate__mutmut["xǁTaskServiceǁcreate__mutmut_2"] = (
    TaskService.xǁTaskServiceǁcreate__mutmut_2
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁcreate__mutmut["xǁTaskServiceǁcreate__mutmut_3"] = (
    TaskService.xǁTaskServiceǁcreate__mutmut_3
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁcreate__mutmut["xǁTaskServiceǁcreate__mutmut_4"] = (
    TaskService.xǁTaskServiceǁcreate__mutmut_4
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁcreate__mutmut["xǁTaskServiceǁcreate__mutmut_5"] = (
    TaskService.xǁTaskServiceǁcreate__mutmut_5
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁcreate__mutmut["xǁTaskServiceǁcreate__mutmut_6"] = (
    TaskService.xǁTaskServiceǁcreate__mutmut_6
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁcreate__mutmut["xǁTaskServiceǁcreate__mutmut_7"] = (
    TaskService.xǁTaskServiceǁcreate__mutmut_7
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁcreate__mutmut["xǁTaskServiceǁcreate__mutmut_8"] = (
    TaskService.xǁTaskServiceǁcreate__mutmut_8
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁcreate__mutmut["xǁTaskServiceǁcreate__mutmut_9"] = (
    TaskService.xǁTaskServiceǁcreate__mutmut_9
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁcreate__mutmut["xǁTaskServiceǁcreate__mutmut_10"] = (
    TaskService.xǁTaskServiceǁcreate__mutmut_10
)  # type: ignore # mutmut generated

mutants_xǁTaskServiceǁlist__mutmut["_mutmut_orig"] = TaskService.xǁTaskServiceǁlist__mutmut_orig  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁlist__mutmut["xǁTaskServiceǁlist__mutmut_1"] = (
    TaskService.xǁTaskServiceǁlist__mutmut_1
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁlist__mutmut["xǁTaskServiceǁlist__mutmut_2"] = (
    TaskService.xǁTaskServiceǁlist__mutmut_2
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁlist__mutmut["xǁTaskServiceǁlist__mutmut_3"] = (
    TaskService.xǁTaskServiceǁlist__mutmut_3
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁlist__mutmut["xǁTaskServiceǁlist__mutmut_4"] = (
    TaskService.xǁTaskServiceǁlist__mutmut_4
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁlist__mutmut["xǁTaskServiceǁlist__mutmut_5"] = (
    TaskService.xǁTaskServiceǁlist__mutmut_5
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁlist__mutmut["xǁTaskServiceǁlist__mutmut_6"] = (
    TaskService.xǁTaskServiceǁlist__mutmut_6
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁlist__mutmut["xǁTaskServiceǁlist__mutmut_7"] = (
    TaskService.xǁTaskServiceǁlist__mutmut_7
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁlist__mutmut["xǁTaskServiceǁlist__mutmut_8"] = (
    TaskService.xǁTaskServiceǁlist__mutmut_8
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁlist__mutmut["xǁTaskServiceǁlist__mutmut_9"] = (
    TaskService.xǁTaskServiceǁlist__mutmut_9
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁlist__mutmut["xǁTaskServiceǁlist__mutmut_10"] = (
    TaskService.xǁTaskServiceǁlist__mutmut_10
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁlist__mutmut["xǁTaskServiceǁlist__mutmut_11"] = (
    TaskService.xǁTaskServiceǁlist__mutmut_11
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁlist__mutmut["xǁTaskServiceǁlist__mutmut_12"] = (
    TaskService.xǁTaskServiceǁlist__mutmut_12
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁlist__mutmut["xǁTaskServiceǁlist__mutmut_13"] = (
    TaskService.xǁTaskServiceǁlist__mutmut_13
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁlist__mutmut["xǁTaskServiceǁlist__mutmut_14"] = (
    TaskService.xǁTaskServiceǁlist__mutmut_14
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁlist__mutmut["xǁTaskServiceǁlist__mutmut_15"] = (
    TaskService.xǁTaskServiceǁlist__mutmut_15
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁlist__mutmut["xǁTaskServiceǁlist__mutmut_16"] = (
    TaskService.xǁTaskServiceǁlist__mutmut_16
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁlist__mutmut["xǁTaskServiceǁlist__mutmut_17"] = (
    TaskService.xǁTaskServiceǁlist__mutmut_17
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁlist__mutmut["xǁTaskServiceǁlist__mutmut_18"] = (
    TaskService.xǁTaskServiceǁlist__mutmut_18
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁlist__mutmut["xǁTaskServiceǁlist__mutmut_19"] = (
    TaskService.xǁTaskServiceǁlist__mutmut_19
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁlist__mutmut["xǁTaskServiceǁlist__mutmut_20"] = (
    TaskService.xǁTaskServiceǁlist__mutmut_20
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁlist__mutmut["xǁTaskServiceǁlist__mutmut_21"] = (
    TaskService.xǁTaskServiceǁlist__mutmut_21
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁlist__mutmut["xǁTaskServiceǁlist__mutmut_22"] = (
    TaskService.xǁTaskServiceǁlist__mutmut_22
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁlist__mutmut["xǁTaskServiceǁlist__mutmut_23"] = (
    TaskService.xǁTaskServiceǁlist__mutmut_23
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁlist__mutmut["xǁTaskServiceǁlist__mutmut_24"] = (
    TaskService.xǁTaskServiceǁlist__mutmut_24
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁlist__mutmut["xǁTaskServiceǁlist__mutmut_25"] = (
    TaskService.xǁTaskServiceǁlist__mutmut_25
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁlist__mutmut["xǁTaskServiceǁlist__mutmut_26"] = (
    TaskService.xǁTaskServiceǁlist__mutmut_26
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁlist__mutmut["xǁTaskServiceǁlist__mutmut_27"] = (
    TaskService.xǁTaskServiceǁlist__mutmut_27
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁlist__mutmut["xǁTaskServiceǁlist__mutmut_28"] = (
    TaskService.xǁTaskServiceǁlist__mutmut_28
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁlist__mutmut["xǁTaskServiceǁlist__mutmut_29"] = (
    TaskService.xǁTaskServiceǁlist__mutmut_29
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁlist__mutmut["xǁTaskServiceǁlist__mutmut_30"] = (
    TaskService.xǁTaskServiceǁlist__mutmut_30
)  # type: ignore # mutmut generated

mutants_xǁTaskServiceǁget__mutmut["_mutmut_orig"] = TaskService.xǁTaskServiceǁget__mutmut_orig  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁget__mutmut["xǁTaskServiceǁget__mutmut_1"] = (
    TaskService.xǁTaskServiceǁget__mutmut_1
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁget__mutmut["xǁTaskServiceǁget__mutmut_2"] = (
    TaskService.xǁTaskServiceǁget__mutmut_2
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁget__mutmut["xǁTaskServiceǁget__mutmut_3"] = (
    TaskService.xǁTaskServiceǁget__mutmut_3
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁget__mutmut["xǁTaskServiceǁget__mutmut_4"] = (
    TaskService.xǁTaskServiceǁget__mutmut_4
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁget__mutmut["xǁTaskServiceǁget__mutmut_5"] = (
    TaskService.xǁTaskServiceǁget__mutmut_5
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁget__mutmut["xǁTaskServiceǁget__mutmut_6"] = (
    TaskService.xǁTaskServiceǁget__mutmut_6
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁget__mutmut["xǁTaskServiceǁget__mutmut_7"] = (
    TaskService.xǁTaskServiceǁget__mutmut_7
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁget__mutmut["xǁTaskServiceǁget__mutmut_8"] = (
    TaskService.xǁTaskServiceǁget__mutmut_8
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁget__mutmut["xǁTaskServiceǁget__mutmut_9"] = (
    TaskService.xǁTaskServiceǁget__mutmut_9
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁget__mutmut["xǁTaskServiceǁget__mutmut_10"] = (
    TaskService.xǁTaskServiceǁget__mutmut_10
)  # type: ignore # mutmut generated

mutants_xǁTaskServiceǁupdate__mutmut["_mutmut_orig"] = TaskService.xǁTaskServiceǁupdate__mutmut_orig  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁupdate__mutmut["xǁTaskServiceǁupdate__mutmut_1"] = (
    TaskService.xǁTaskServiceǁupdate__mutmut_1
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁupdate__mutmut["xǁTaskServiceǁupdate__mutmut_2"] = (
    TaskService.xǁTaskServiceǁupdate__mutmut_2
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁupdate__mutmut["xǁTaskServiceǁupdate__mutmut_3"] = (
    TaskService.xǁTaskServiceǁupdate__mutmut_3
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁupdate__mutmut["xǁTaskServiceǁupdate__mutmut_4"] = (
    TaskService.xǁTaskServiceǁupdate__mutmut_4
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁupdate__mutmut["xǁTaskServiceǁupdate__mutmut_5"] = (
    TaskService.xǁTaskServiceǁupdate__mutmut_5
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁupdate__mutmut["xǁTaskServiceǁupdate__mutmut_6"] = (
    TaskService.xǁTaskServiceǁupdate__mutmut_6
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁupdate__mutmut["xǁTaskServiceǁupdate__mutmut_7"] = (
    TaskService.xǁTaskServiceǁupdate__mutmut_7
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁupdate__mutmut["xǁTaskServiceǁupdate__mutmut_8"] = (
    TaskService.xǁTaskServiceǁupdate__mutmut_8
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁupdate__mutmut["xǁTaskServiceǁupdate__mutmut_9"] = (
    TaskService.xǁTaskServiceǁupdate__mutmut_9
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁupdate__mutmut["xǁTaskServiceǁupdate__mutmut_10"] = (
    TaskService.xǁTaskServiceǁupdate__mutmut_10
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁupdate__mutmut["xǁTaskServiceǁupdate__mutmut_11"] = (
    TaskService.xǁTaskServiceǁupdate__mutmut_11
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁupdate__mutmut["xǁTaskServiceǁupdate__mutmut_12"] = (
    TaskService.xǁTaskServiceǁupdate__mutmut_12
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁupdate__mutmut["xǁTaskServiceǁupdate__mutmut_13"] = (
    TaskService.xǁTaskServiceǁupdate__mutmut_13
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁupdate__mutmut["xǁTaskServiceǁupdate__mutmut_14"] = (
    TaskService.xǁTaskServiceǁupdate__mutmut_14
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁupdate__mutmut["xǁTaskServiceǁupdate__mutmut_15"] = (
    TaskService.xǁTaskServiceǁupdate__mutmut_15
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁupdate__mutmut["xǁTaskServiceǁupdate__mutmut_16"] = (
    TaskService.xǁTaskServiceǁupdate__mutmut_16
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁupdate__mutmut["xǁTaskServiceǁupdate__mutmut_17"] = (
    TaskService.xǁTaskServiceǁupdate__mutmut_17
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁupdate__mutmut["xǁTaskServiceǁupdate__mutmut_18"] = (
    TaskService.xǁTaskServiceǁupdate__mutmut_18
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁupdate__mutmut["xǁTaskServiceǁupdate__mutmut_19"] = (
    TaskService.xǁTaskServiceǁupdate__mutmut_19
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁupdate__mutmut["xǁTaskServiceǁupdate__mutmut_20"] = (
    TaskService.xǁTaskServiceǁupdate__mutmut_20
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁupdate__mutmut["xǁTaskServiceǁupdate__mutmut_21"] = (
    TaskService.xǁTaskServiceǁupdate__mutmut_21
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁupdate__mutmut["xǁTaskServiceǁupdate__mutmut_22"] = (
    TaskService.xǁTaskServiceǁupdate__mutmut_22
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁupdate__mutmut["xǁTaskServiceǁupdate__mutmut_23"] = (
    TaskService.xǁTaskServiceǁupdate__mutmut_23
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁupdate__mutmut["xǁTaskServiceǁupdate__mutmut_24"] = (
    TaskService.xǁTaskServiceǁupdate__mutmut_24
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁupdate__mutmut["xǁTaskServiceǁupdate__mutmut_25"] = (
    TaskService.xǁTaskServiceǁupdate__mutmut_25
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁupdate__mutmut["xǁTaskServiceǁupdate__mutmut_26"] = (
    TaskService.xǁTaskServiceǁupdate__mutmut_26
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁupdate__mutmut["xǁTaskServiceǁupdate__mutmut_27"] = (
    TaskService.xǁTaskServiceǁupdate__mutmut_27
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁupdate__mutmut["xǁTaskServiceǁupdate__mutmut_28"] = (
    TaskService.xǁTaskServiceǁupdate__mutmut_28
)  # type: ignore # mutmut generated

mutants_xǁTaskServiceǁ_require_task_update_access__mutmut["_mutmut_orig"] = (
    TaskService.xǁTaskServiceǁ_require_task_update_access__mutmut_orig
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁ_require_task_update_access__mutmut[
    "xǁTaskServiceǁ_require_task_update_access__mutmut_1"
] = TaskService.xǁTaskServiceǁ_require_task_update_access__mutmut_1  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁ_require_task_update_access__mutmut[
    "xǁTaskServiceǁ_require_task_update_access__mutmut_2"
] = TaskService.xǁTaskServiceǁ_require_task_update_access__mutmut_2  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁ_require_task_update_access__mutmut[
    "xǁTaskServiceǁ_require_task_update_access__mutmut_3"
] = TaskService.xǁTaskServiceǁ_require_task_update_access__mutmut_3  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁ_require_task_update_access__mutmut[
    "xǁTaskServiceǁ_require_task_update_access__mutmut_4"
] = TaskService.xǁTaskServiceǁ_require_task_update_access__mutmut_4  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁ_require_task_update_access__mutmut[
    "xǁTaskServiceǁ_require_task_update_access__mutmut_5"
] = TaskService.xǁTaskServiceǁ_require_task_update_access__mutmut_5  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁ_require_task_update_access__mutmut[
    "xǁTaskServiceǁ_require_task_update_access__mutmut_6"
] = TaskService.xǁTaskServiceǁ_require_task_update_access__mutmut_6  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁ_require_task_update_access__mutmut[
    "xǁTaskServiceǁ_require_task_update_access__mutmut_7"
] = TaskService.xǁTaskServiceǁ_require_task_update_access__mutmut_7  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁ_require_task_update_access__mutmut[
    "xǁTaskServiceǁ_require_task_update_access__mutmut_8"
] = TaskService.xǁTaskServiceǁ_require_task_update_access__mutmut_8  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁ_require_task_update_access__mutmut[
    "xǁTaskServiceǁ_require_task_update_access__mutmut_9"
] = TaskService.xǁTaskServiceǁ_require_task_update_access__mutmut_9  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁ_require_task_update_access__mutmut[
    "xǁTaskServiceǁ_require_task_update_access__mutmut_10"
] = TaskService.xǁTaskServiceǁ_require_task_update_access__mutmut_10  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁ_require_task_update_access__mutmut[
    "xǁTaskServiceǁ_require_task_update_access__mutmut_11"
] = TaskService.xǁTaskServiceǁ_require_task_update_access__mutmut_11  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁ_require_task_update_access__mutmut[
    "xǁTaskServiceǁ_require_task_update_access__mutmut_12"
] = TaskService.xǁTaskServiceǁ_require_task_update_access__mutmut_12  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁ_require_task_update_access__mutmut[
    "xǁTaskServiceǁ_require_task_update_access__mutmut_13"
] = TaskService.xǁTaskServiceǁ_require_task_update_access__mutmut_13  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁ_require_task_update_access__mutmut[
    "xǁTaskServiceǁ_require_task_update_access__mutmut_14"
] = TaskService.xǁTaskServiceǁ_require_task_update_access__mutmut_14  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁ_require_task_update_access__mutmut[
    "xǁTaskServiceǁ_require_task_update_access__mutmut_15"
] = TaskService.xǁTaskServiceǁ_require_task_update_access__mutmut_15  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁ_require_task_update_access__mutmut[
    "xǁTaskServiceǁ_require_task_update_access__mutmut_16"
] = TaskService.xǁTaskServiceǁ_require_task_update_access__mutmut_16  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁ_require_task_update_access__mutmut[
    "xǁTaskServiceǁ_require_task_update_access__mutmut_17"
] = TaskService.xǁTaskServiceǁ_require_task_update_access__mutmut_17  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁ_require_task_update_access__mutmut[
    "xǁTaskServiceǁ_require_task_update_access__mutmut_18"
] = TaskService.xǁTaskServiceǁ_require_task_update_access__mutmut_18  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁ_require_task_update_access__mutmut[
    "xǁTaskServiceǁ_require_task_update_access__mutmut_19"
] = TaskService.xǁTaskServiceǁ_require_task_update_access__mutmut_19  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁ_require_task_update_access__mutmut[
    "xǁTaskServiceǁ_require_task_update_access__mutmut_20"
] = TaskService.xǁTaskServiceǁ_require_task_update_access__mutmut_20  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁ_require_task_update_access__mutmut[
    "xǁTaskServiceǁ_require_task_update_access__mutmut_21"
] = TaskService.xǁTaskServiceǁ_require_task_update_access__mutmut_21  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁ_require_task_update_access__mutmut[
    "xǁTaskServiceǁ_require_task_update_access__mutmut_22"
] = TaskService.xǁTaskServiceǁ_require_task_update_access__mutmut_22  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁ_require_task_update_access__mutmut[
    "xǁTaskServiceǁ_require_task_update_access__mutmut_23"
] = TaskService.xǁTaskServiceǁ_require_task_update_access__mutmut_23  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁ_require_task_update_access__mutmut[
    "xǁTaskServiceǁ_require_task_update_access__mutmut_24"
] = TaskService.xǁTaskServiceǁ_require_task_update_access__mutmut_24  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁ_require_task_update_access__mutmut[
    "xǁTaskServiceǁ_require_task_update_access__mutmut_25"
] = TaskService.xǁTaskServiceǁ_require_task_update_access__mutmut_25  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁ_require_task_update_access__mutmut[
    "xǁTaskServiceǁ_require_task_update_access__mutmut_26"
] = TaskService.xǁTaskServiceǁ_require_task_update_access__mutmut_26  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁ_require_task_update_access__mutmut[
    "xǁTaskServiceǁ_require_task_update_access__mutmut_27"
] = TaskService.xǁTaskServiceǁ_require_task_update_access__mutmut_27  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁ_require_task_update_access__mutmut[
    "xǁTaskServiceǁ_require_task_update_access__mutmut_28"
] = TaskService.xǁTaskServiceǁ_require_task_update_access__mutmut_28  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁ_require_task_update_access__mutmut[
    "xǁTaskServiceǁ_require_task_update_access__mutmut_29"
] = TaskService.xǁTaskServiceǁ_require_task_update_access__mutmut_29  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁ_require_task_update_access__mutmut[
    "xǁTaskServiceǁ_require_task_update_access__mutmut_30"
] = TaskService.xǁTaskServiceǁ_require_task_update_access__mutmut_30  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁ_require_task_update_access__mutmut[
    "xǁTaskServiceǁ_require_task_update_access__mutmut_31"
] = TaskService.xǁTaskServiceǁ_require_task_update_access__mutmut_31  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁ_require_task_update_access__mutmut[
    "xǁTaskServiceǁ_require_task_update_access__mutmut_32"
] = TaskService.xǁTaskServiceǁ_require_task_update_access__mutmut_32  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁ_require_task_update_access__mutmut[
    "xǁTaskServiceǁ_require_task_update_access__mutmut_33"
] = TaskService.xǁTaskServiceǁ_require_task_update_access__mutmut_33  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁ_require_task_update_access__mutmut[
    "xǁTaskServiceǁ_require_task_update_access__mutmut_34"
] = TaskService.xǁTaskServiceǁ_require_task_update_access__mutmut_34  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁ_require_task_update_access__mutmut[
    "xǁTaskServiceǁ_require_task_update_access__mutmut_35"
] = TaskService.xǁTaskServiceǁ_require_task_update_access__mutmut_35  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁ_require_task_update_access__mutmut[
    "xǁTaskServiceǁ_require_task_update_access__mutmut_36"
] = TaskService.xǁTaskServiceǁ_require_task_update_access__mutmut_36  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁ_require_task_update_access__mutmut[
    "xǁTaskServiceǁ_require_task_update_access__mutmut_37"
] = TaskService.xǁTaskServiceǁ_require_task_update_access__mutmut_37  # type: ignore # mutmut generated

mutants_xǁTaskServiceǁarchive__mutmut["_mutmut_orig"] = (
    TaskService.xǁTaskServiceǁarchive__mutmut_orig
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁarchive__mutmut["xǁTaskServiceǁarchive__mutmut_1"] = (
    TaskService.xǁTaskServiceǁarchive__mutmut_1
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁarchive__mutmut["xǁTaskServiceǁarchive__mutmut_2"] = (
    TaskService.xǁTaskServiceǁarchive__mutmut_2
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁarchive__mutmut["xǁTaskServiceǁarchive__mutmut_3"] = (
    TaskService.xǁTaskServiceǁarchive__mutmut_3
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁarchive__mutmut["xǁTaskServiceǁarchive__mutmut_4"] = (
    TaskService.xǁTaskServiceǁarchive__mutmut_4
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁarchive__mutmut["xǁTaskServiceǁarchive__mutmut_5"] = (
    TaskService.xǁTaskServiceǁarchive__mutmut_5
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁarchive__mutmut["xǁTaskServiceǁarchive__mutmut_6"] = (
    TaskService.xǁTaskServiceǁarchive__mutmut_6
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁarchive__mutmut["xǁTaskServiceǁarchive__mutmut_7"] = (
    TaskService.xǁTaskServiceǁarchive__mutmut_7
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁarchive__mutmut["xǁTaskServiceǁarchive__mutmut_8"] = (
    TaskService.xǁTaskServiceǁarchive__mutmut_8
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁarchive__mutmut["xǁTaskServiceǁarchive__mutmut_9"] = (
    TaskService.xǁTaskServiceǁarchive__mutmut_9
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁarchive__mutmut["xǁTaskServiceǁarchive__mutmut_10"] = (
    TaskService.xǁTaskServiceǁarchive__mutmut_10
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁarchive__mutmut["xǁTaskServiceǁarchive__mutmut_11"] = (
    TaskService.xǁTaskServiceǁarchive__mutmut_11
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁarchive__mutmut["xǁTaskServiceǁarchive__mutmut_12"] = (
    TaskService.xǁTaskServiceǁarchive__mutmut_12
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁarchive__mutmut["xǁTaskServiceǁarchive__mutmut_13"] = (
    TaskService.xǁTaskServiceǁarchive__mutmut_13
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁarchive__mutmut["xǁTaskServiceǁarchive__mutmut_14"] = (
    TaskService.xǁTaskServiceǁarchive__mutmut_14
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁarchive__mutmut["xǁTaskServiceǁarchive__mutmut_15"] = (
    TaskService.xǁTaskServiceǁarchive__mutmut_15
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁarchive__mutmut["xǁTaskServiceǁarchive__mutmut_16"] = (
    TaskService.xǁTaskServiceǁarchive__mutmut_16
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁarchive__mutmut["xǁTaskServiceǁarchive__mutmut_17"] = (
    TaskService.xǁTaskServiceǁarchive__mutmut_17
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁarchive__mutmut["xǁTaskServiceǁarchive__mutmut_18"] = (
    TaskService.xǁTaskServiceǁarchive__mutmut_18
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁarchive__mutmut["xǁTaskServiceǁarchive__mutmut_19"] = (
    TaskService.xǁTaskServiceǁarchive__mutmut_19
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁarchive__mutmut["xǁTaskServiceǁarchive__mutmut_20"] = (
    TaskService.xǁTaskServiceǁarchive__mutmut_20
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁarchive__mutmut["xǁTaskServiceǁarchive__mutmut_21"] = (
    TaskService.xǁTaskServiceǁarchive__mutmut_21
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁarchive__mutmut["xǁTaskServiceǁarchive__mutmut_22"] = (
    TaskService.xǁTaskServiceǁarchive__mutmut_22
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁarchive__mutmut["xǁTaskServiceǁarchive__mutmut_23"] = (
    TaskService.xǁTaskServiceǁarchive__mutmut_23
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁarchive__mutmut["xǁTaskServiceǁarchive__mutmut_24"] = (
    TaskService.xǁTaskServiceǁarchive__mutmut_24
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁarchive__mutmut["xǁTaskServiceǁarchive__mutmut_25"] = (
    TaskService.xǁTaskServiceǁarchive__mutmut_25
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁarchive__mutmut["xǁTaskServiceǁarchive__mutmut_26"] = (
    TaskService.xǁTaskServiceǁarchive__mutmut_26
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁarchive__mutmut["xǁTaskServiceǁarchive__mutmut_27"] = (
    TaskService.xǁTaskServiceǁarchive__mutmut_27
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁarchive__mutmut["xǁTaskServiceǁarchive__mutmut_28"] = (
    TaskService.xǁTaskServiceǁarchive__mutmut_28
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁarchive__mutmut["xǁTaskServiceǁarchive__mutmut_29"] = (
    TaskService.xǁTaskServiceǁarchive__mutmut_29
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁarchive__mutmut["xǁTaskServiceǁarchive__mutmut_30"] = (
    TaskService.xǁTaskServiceǁarchive__mutmut_30
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁarchive__mutmut["xǁTaskServiceǁarchive__mutmut_31"] = (
    TaskService.xǁTaskServiceǁarchive__mutmut_31
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁarchive__mutmut["xǁTaskServiceǁarchive__mutmut_32"] = (
    TaskService.xǁTaskServiceǁarchive__mutmut_32
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁarchive__mutmut["xǁTaskServiceǁarchive__mutmut_33"] = (
    TaskService.xǁTaskServiceǁarchive__mutmut_33
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁarchive__mutmut["xǁTaskServiceǁarchive__mutmut_34"] = (
    TaskService.xǁTaskServiceǁarchive__mutmut_34
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁarchive__mutmut["xǁTaskServiceǁarchive__mutmut_35"] = (
    TaskService.xǁTaskServiceǁarchive__mutmut_35
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁarchive__mutmut["xǁTaskServiceǁarchive__mutmut_36"] = (
    TaskService.xǁTaskServiceǁarchive__mutmut_36
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁarchive__mutmut["xǁTaskServiceǁarchive__mutmut_37"] = (
    TaskService.xǁTaskServiceǁarchive__mutmut_37
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁarchive__mutmut["xǁTaskServiceǁarchive__mutmut_38"] = (
    TaskService.xǁTaskServiceǁarchive__mutmut_38
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁarchive__mutmut["xǁTaskServiceǁarchive__mutmut_39"] = (
    TaskService.xǁTaskServiceǁarchive__mutmut_39
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁarchive__mutmut["xǁTaskServiceǁarchive__mutmut_40"] = (
    TaskService.xǁTaskServiceǁarchive__mutmut_40
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁarchive__mutmut["xǁTaskServiceǁarchive__mutmut_41"] = (
    TaskService.xǁTaskServiceǁarchive__mutmut_41
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁarchive__mutmut["xǁTaskServiceǁarchive__mutmut_42"] = (
    TaskService.xǁTaskServiceǁarchive__mutmut_42
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁarchive__mutmut["xǁTaskServiceǁarchive__mutmut_43"] = (
    TaskService.xǁTaskServiceǁarchive__mutmut_43
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁarchive__mutmut["xǁTaskServiceǁarchive__mutmut_44"] = (
    TaskService.xǁTaskServiceǁarchive__mutmut_44
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁarchive__mutmut["xǁTaskServiceǁarchive__mutmut_45"] = (
    TaskService.xǁTaskServiceǁarchive__mutmut_45
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁarchive__mutmut["xǁTaskServiceǁarchive__mutmut_46"] = (
    TaskService.xǁTaskServiceǁarchive__mutmut_46
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁarchive__mutmut["xǁTaskServiceǁarchive__mutmut_47"] = (
    TaskService.xǁTaskServiceǁarchive__mutmut_47
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁarchive__mutmut["xǁTaskServiceǁarchive__mutmut_48"] = (
    TaskService.xǁTaskServiceǁarchive__mutmut_48
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁarchive__mutmut["xǁTaskServiceǁarchive__mutmut_49"] = (
    TaskService.xǁTaskServiceǁarchive__mutmut_49
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁarchive__mutmut["xǁTaskServiceǁarchive__mutmut_50"] = (
    TaskService.xǁTaskServiceǁarchive__mutmut_50
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁarchive__mutmut["xǁTaskServiceǁarchive__mutmut_51"] = (
    TaskService.xǁTaskServiceǁarchive__mutmut_51
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁarchive__mutmut["xǁTaskServiceǁarchive__mutmut_52"] = (
    TaskService.xǁTaskServiceǁarchive__mutmut_52
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁarchive__mutmut["xǁTaskServiceǁarchive__mutmut_53"] = (
    TaskService.xǁTaskServiceǁarchive__mutmut_53
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁarchive__mutmut["xǁTaskServiceǁarchive__mutmut_54"] = (
    TaskService.xǁTaskServiceǁarchive__mutmut_54
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁarchive__mutmut["xǁTaskServiceǁarchive__mutmut_55"] = (
    TaskService.xǁTaskServiceǁarchive__mutmut_55
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁarchive__mutmut["xǁTaskServiceǁarchive__mutmut_56"] = (
    TaskService.xǁTaskServiceǁarchive__mutmut_56
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁarchive__mutmut["xǁTaskServiceǁarchive__mutmut_57"] = (
    TaskService.xǁTaskServiceǁarchive__mutmut_57
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁarchive__mutmut["xǁTaskServiceǁarchive__mutmut_58"] = (
    TaskService.xǁTaskServiceǁarchive__mutmut_58
)  # type: ignore # mutmut generated

mutants_xǁTaskServiceǁdelete__mutmut["_mutmut_orig"] = TaskService.xǁTaskServiceǁdelete__mutmut_orig  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁdelete__mutmut["xǁTaskServiceǁdelete__mutmut_1"] = (
    TaskService.xǁTaskServiceǁdelete__mutmut_1
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁdelete__mutmut["xǁTaskServiceǁdelete__mutmut_2"] = (
    TaskService.xǁTaskServiceǁdelete__mutmut_2
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁdelete__mutmut["xǁTaskServiceǁdelete__mutmut_3"] = (
    TaskService.xǁTaskServiceǁdelete__mutmut_3
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁdelete__mutmut["xǁTaskServiceǁdelete__mutmut_4"] = (
    TaskService.xǁTaskServiceǁdelete__mutmut_4
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁdelete__mutmut["xǁTaskServiceǁdelete__mutmut_5"] = (
    TaskService.xǁTaskServiceǁdelete__mutmut_5
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁdelete__mutmut["xǁTaskServiceǁdelete__mutmut_6"] = (
    TaskService.xǁTaskServiceǁdelete__mutmut_6
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁdelete__mutmut["xǁTaskServiceǁdelete__mutmut_7"] = (
    TaskService.xǁTaskServiceǁdelete__mutmut_7
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁdelete__mutmut["xǁTaskServiceǁdelete__mutmut_8"] = (
    TaskService.xǁTaskServiceǁdelete__mutmut_8
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁdelete__mutmut["xǁTaskServiceǁdelete__mutmut_9"] = (
    TaskService.xǁTaskServiceǁdelete__mutmut_9
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁdelete__mutmut["xǁTaskServiceǁdelete__mutmut_10"] = (
    TaskService.xǁTaskServiceǁdelete__mutmut_10
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁdelete__mutmut["xǁTaskServiceǁdelete__mutmut_11"] = (
    TaskService.xǁTaskServiceǁdelete__mutmut_11
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁdelete__mutmut["xǁTaskServiceǁdelete__mutmut_12"] = (
    TaskService.xǁTaskServiceǁdelete__mutmut_12
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁdelete__mutmut["xǁTaskServiceǁdelete__mutmut_13"] = (
    TaskService.xǁTaskServiceǁdelete__mutmut_13
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁdelete__mutmut["xǁTaskServiceǁdelete__mutmut_14"] = (
    TaskService.xǁTaskServiceǁdelete__mutmut_14
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁdelete__mutmut["xǁTaskServiceǁdelete__mutmut_15"] = (
    TaskService.xǁTaskServiceǁdelete__mutmut_15
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁdelete__mutmut["xǁTaskServiceǁdelete__mutmut_16"] = (
    TaskService.xǁTaskServiceǁdelete__mutmut_16
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁdelete__mutmut["xǁTaskServiceǁdelete__mutmut_17"] = (
    TaskService.xǁTaskServiceǁdelete__mutmut_17
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁdelete__mutmut["xǁTaskServiceǁdelete__mutmut_18"] = (
    TaskService.xǁTaskServiceǁdelete__mutmut_18
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁdelete__mutmut["xǁTaskServiceǁdelete__mutmut_19"] = (
    TaskService.xǁTaskServiceǁdelete__mutmut_19
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁdelete__mutmut["xǁTaskServiceǁdelete__mutmut_20"] = (
    TaskService.xǁTaskServiceǁdelete__mutmut_20
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁdelete__mutmut["xǁTaskServiceǁdelete__mutmut_21"] = (
    TaskService.xǁTaskServiceǁdelete__mutmut_21
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁdelete__mutmut["xǁTaskServiceǁdelete__mutmut_22"] = (
    TaskService.xǁTaskServiceǁdelete__mutmut_22
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁdelete__mutmut["xǁTaskServiceǁdelete__mutmut_23"] = (
    TaskService.xǁTaskServiceǁdelete__mutmut_23
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁdelete__mutmut["xǁTaskServiceǁdelete__mutmut_24"] = (
    TaskService.xǁTaskServiceǁdelete__mutmut_24
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁdelete__mutmut["xǁTaskServiceǁdelete__mutmut_25"] = (
    TaskService.xǁTaskServiceǁdelete__mutmut_25
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁdelete__mutmut["xǁTaskServiceǁdelete__mutmut_26"] = (
    TaskService.xǁTaskServiceǁdelete__mutmut_26
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁdelete__mutmut["xǁTaskServiceǁdelete__mutmut_27"] = (
    TaskService.xǁTaskServiceǁdelete__mutmut_27
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁdelete__mutmut["xǁTaskServiceǁdelete__mutmut_28"] = (
    TaskService.xǁTaskServiceǁdelete__mutmut_28
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁdelete__mutmut["xǁTaskServiceǁdelete__mutmut_29"] = (
    TaskService.xǁTaskServiceǁdelete__mutmut_29
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁdelete__mutmut["xǁTaskServiceǁdelete__mutmut_30"] = (
    TaskService.xǁTaskServiceǁdelete__mutmut_30
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁdelete__mutmut["xǁTaskServiceǁdelete__mutmut_31"] = (
    TaskService.xǁTaskServiceǁdelete__mutmut_31
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁdelete__mutmut["xǁTaskServiceǁdelete__mutmut_32"] = (
    TaskService.xǁTaskServiceǁdelete__mutmut_32
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁdelete__mutmut["xǁTaskServiceǁdelete__mutmut_33"] = (
    TaskService.xǁTaskServiceǁdelete__mutmut_33
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁdelete__mutmut["xǁTaskServiceǁdelete__mutmut_34"] = (
    TaskService.xǁTaskServiceǁdelete__mutmut_34
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁdelete__mutmut["xǁTaskServiceǁdelete__mutmut_35"] = (
    TaskService.xǁTaskServiceǁdelete__mutmut_35
)  # type: ignore # mutmut generated

mutants_xǁTaskServiceǁlist_deleted__mutmut["_mutmut_orig"] = (
    TaskService.xǁTaskServiceǁlist_deleted__mutmut_orig
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁlist_deleted__mutmut["xǁTaskServiceǁlist_deleted__mutmut_1"] = (
    TaskService.xǁTaskServiceǁlist_deleted__mutmut_1
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁlist_deleted__mutmut["xǁTaskServiceǁlist_deleted__mutmut_2"] = (
    TaskService.xǁTaskServiceǁlist_deleted__mutmut_2
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁlist_deleted__mutmut["xǁTaskServiceǁlist_deleted__mutmut_3"] = (
    TaskService.xǁTaskServiceǁlist_deleted__mutmut_3
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁlist_deleted__mutmut["xǁTaskServiceǁlist_deleted__mutmut_4"] = (
    TaskService.xǁTaskServiceǁlist_deleted__mutmut_4
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁlist_deleted__mutmut["xǁTaskServiceǁlist_deleted__mutmut_5"] = (
    TaskService.xǁTaskServiceǁlist_deleted__mutmut_5
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁlist_deleted__mutmut["xǁTaskServiceǁlist_deleted__mutmut_6"] = (
    TaskService.xǁTaskServiceǁlist_deleted__mutmut_6
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁlist_deleted__mutmut["xǁTaskServiceǁlist_deleted__mutmut_7"] = (
    TaskService.xǁTaskServiceǁlist_deleted__mutmut_7
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁlist_deleted__mutmut["xǁTaskServiceǁlist_deleted__mutmut_8"] = (
    TaskService.xǁTaskServiceǁlist_deleted__mutmut_8
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁlist_deleted__mutmut["xǁTaskServiceǁlist_deleted__mutmut_9"] = (
    TaskService.xǁTaskServiceǁlist_deleted__mutmut_9
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁlist_deleted__mutmut["xǁTaskServiceǁlist_deleted__mutmut_10"] = (
    TaskService.xǁTaskServiceǁlist_deleted__mutmut_10
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁlist_deleted__mutmut["xǁTaskServiceǁlist_deleted__mutmut_11"] = (
    TaskService.xǁTaskServiceǁlist_deleted__mutmut_11
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁlist_deleted__mutmut["xǁTaskServiceǁlist_deleted__mutmut_12"] = (
    TaskService.xǁTaskServiceǁlist_deleted__mutmut_12
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁlist_deleted__mutmut["xǁTaskServiceǁlist_deleted__mutmut_13"] = (
    TaskService.xǁTaskServiceǁlist_deleted__mutmut_13
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁlist_deleted__mutmut["xǁTaskServiceǁlist_deleted__mutmut_14"] = (
    TaskService.xǁTaskServiceǁlist_deleted__mutmut_14
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁlist_deleted__mutmut["xǁTaskServiceǁlist_deleted__mutmut_15"] = (
    TaskService.xǁTaskServiceǁlist_deleted__mutmut_15
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁlist_deleted__mutmut["xǁTaskServiceǁlist_deleted__mutmut_16"] = (
    TaskService.xǁTaskServiceǁlist_deleted__mutmut_16
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁlist_deleted__mutmut["xǁTaskServiceǁlist_deleted__mutmut_17"] = (
    TaskService.xǁTaskServiceǁlist_deleted__mutmut_17
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁlist_deleted__mutmut["xǁTaskServiceǁlist_deleted__mutmut_18"] = (
    TaskService.xǁTaskServiceǁlist_deleted__mutmut_18
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁlist_deleted__mutmut["xǁTaskServiceǁlist_deleted__mutmut_19"] = (
    TaskService.xǁTaskServiceǁlist_deleted__mutmut_19
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁlist_deleted__mutmut["xǁTaskServiceǁlist_deleted__mutmut_20"] = (
    TaskService.xǁTaskServiceǁlist_deleted__mutmut_20
)  # type: ignore # mutmut generated

mutants_xǁTaskServiceǁrestore__mutmut["_mutmut_orig"] = (
    TaskService.xǁTaskServiceǁrestore__mutmut_orig
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁrestore__mutmut["xǁTaskServiceǁrestore__mutmut_1"] = (
    TaskService.xǁTaskServiceǁrestore__mutmut_1
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁrestore__mutmut["xǁTaskServiceǁrestore__mutmut_2"] = (
    TaskService.xǁTaskServiceǁrestore__mutmut_2
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁrestore__mutmut["xǁTaskServiceǁrestore__mutmut_3"] = (
    TaskService.xǁTaskServiceǁrestore__mutmut_3
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁrestore__mutmut["xǁTaskServiceǁrestore__mutmut_4"] = (
    TaskService.xǁTaskServiceǁrestore__mutmut_4
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁrestore__mutmut["xǁTaskServiceǁrestore__mutmut_5"] = (
    TaskService.xǁTaskServiceǁrestore__mutmut_5
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁrestore__mutmut["xǁTaskServiceǁrestore__mutmut_6"] = (
    TaskService.xǁTaskServiceǁrestore__mutmut_6
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁrestore__mutmut["xǁTaskServiceǁrestore__mutmut_7"] = (
    TaskService.xǁTaskServiceǁrestore__mutmut_7
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁrestore__mutmut["xǁTaskServiceǁrestore__mutmut_8"] = (
    TaskService.xǁTaskServiceǁrestore__mutmut_8
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁrestore__mutmut["xǁTaskServiceǁrestore__mutmut_9"] = (
    TaskService.xǁTaskServiceǁrestore__mutmut_9
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁrestore__mutmut["xǁTaskServiceǁrestore__mutmut_10"] = (
    TaskService.xǁTaskServiceǁrestore__mutmut_10
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁrestore__mutmut["xǁTaskServiceǁrestore__mutmut_11"] = (
    TaskService.xǁTaskServiceǁrestore__mutmut_11
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁrestore__mutmut["xǁTaskServiceǁrestore__mutmut_12"] = (
    TaskService.xǁTaskServiceǁrestore__mutmut_12
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁrestore__mutmut["xǁTaskServiceǁrestore__mutmut_13"] = (
    TaskService.xǁTaskServiceǁrestore__mutmut_13
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁrestore__mutmut["xǁTaskServiceǁrestore__mutmut_14"] = (
    TaskService.xǁTaskServiceǁrestore__mutmut_14
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁrestore__mutmut["xǁTaskServiceǁrestore__mutmut_15"] = (
    TaskService.xǁTaskServiceǁrestore__mutmut_15
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁrestore__mutmut["xǁTaskServiceǁrestore__mutmut_16"] = (
    TaskService.xǁTaskServiceǁrestore__mutmut_16
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁrestore__mutmut["xǁTaskServiceǁrestore__mutmut_17"] = (
    TaskService.xǁTaskServiceǁrestore__mutmut_17
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁrestore__mutmut["xǁTaskServiceǁrestore__mutmut_18"] = (
    TaskService.xǁTaskServiceǁrestore__mutmut_18
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁrestore__mutmut["xǁTaskServiceǁrestore__mutmut_19"] = (
    TaskService.xǁTaskServiceǁrestore__mutmut_19
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁrestore__mutmut["xǁTaskServiceǁrestore__mutmut_20"] = (
    TaskService.xǁTaskServiceǁrestore__mutmut_20
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁrestore__mutmut["xǁTaskServiceǁrestore__mutmut_21"] = (
    TaskService.xǁTaskServiceǁrestore__mutmut_21
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁrestore__mutmut["xǁTaskServiceǁrestore__mutmut_22"] = (
    TaskService.xǁTaskServiceǁrestore__mutmut_22
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁrestore__mutmut["xǁTaskServiceǁrestore__mutmut_23"] = (
    TaskService.xǁTaskServiceǁrestore__mutmut_23
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁrestore__mutmut["xǁTaskServiceǁrestore__mutmut_24"] = (
    TaskService.xǁTaskServiceǁrestore__mutmut_24
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁrestore__mutmut["xǁTaskServiceǁrestore__mutmut_25"] = (
    TaskService.xǁTaskServiceǁrestore__mutmut_25
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁrestore__mutmut["xǁTaskServiceǁrestore__mutmut_26"] = (
    TaskService.xǁTaskServiceǁrestore__mutmut_26
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁrestore__mutmut["xǁTaskServiceǁrestore__mutmut_27"] = (
    TaskService.xǁTaskServiceǁrestore__mutmut_27
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁrestore__mutmut["xǁTaskServiceǁrestore__mutmut_28"] = (
    TaskService.xǁTaskServiceǁrestore__mutmut_28
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁrestore__mutmut["xǁTaskServiceǁrestore__mutmut_29"] = (
    TaskService.xǁTaskServiceǁrestore__mutmut_29
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁrestore__mutmut["xǁTaskServiceǁrestore__mutmut_30"] = (
    TaskService.xǁTaskServiceǁrestore__mutmut_30
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁrestore__mutmut["xǁTaskServiceǁrestore__mutmut_31"] = (
    TaskService.xǁTaskServiceǁrestore__mutmut_31
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁrestore__mutmut["xǁTaskServiceǁrestore__mutmut_32"] = (
    TaskService.xǁTaskServiceǁrestore__mutmut_32
)  # type: ignore # mutmut generated
mutants_xǁTaskServiceǁrestore__mutmut["xǁTaskServiceǁrestore__mutmut_33"] = (
    TaskService.xǁTaskServiceǁrestore__mutmut_33
)  # type: ignore # mutmut generated
