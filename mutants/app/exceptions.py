from typing import Any

from mutmut.mutation.trampoline import MutantDict
from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated

mutants_xǁAppErrorǁ__init____mutmut: MutantDict = {}  # type: ignore


class AppError(Exception):
    status_code = 500
    code = "application_error"

    @_mutmut_mutated(mutants_xǁAppErrorǁ__init____mutmut)
    def __init__(
        self,
        message: str,
        *,
        details: Any = None,
        headers: dict[str, str] | None = None,
    ) -> None:
        self.message = message
        self.details = details
        self.headers = headers
        super().__init__(message)

    def xǁAppErrorǁ__init____mutmut_orig(
        self,
        message: str,
        *,
        details: Any = None,
        headers: dict[str, str] | None = None,
    ) -> None:
        self.message = message
        self.details = details
        self.headers = headers
        super().__init__(message)

    def xǁAppErrorǁ__init____mutmut_1(
        self,
        message: str,
        *,
        details: Any = None,
        headers: dict[str, str] | None = None,
    ) -> None:
        self.message = None
        self.details = details
        self.headers = headers
        super().__init__(message)

    def xǁAppErrorǁ__init____mutmut_2(
        self,
        message: str,
        *,
        details: Any = None,
        headers: dict[str, str] | None = None,
    ) -> None:
        self.message = message
        self.details = None
        self.headers = headers
        super().__init__(message)

    def xǁAppErrorǁ__init____mutmut_3(
        self,
        message: str,
        *,
        details: Any = None,
        headers: dict[str, str] | None = None,
    ) -> None:
        self.message = message
        self.details = details
        self.headers = None
        super().__init__(message)

    def xǁAppErrorǁ__init____mutmut_4(
        self,
        message: str,
        *,
        details: Any = None,
        headers: dict[str, str] | None = None,
    ) -> None:
        self.message = message
        self.details = details
        self.headers = headers
        super().__init__(None)


mutants_xǁAppErrorǁ__init____mutmut["_mutmut_orig"] = AppError.xǁAppErrorǁ__init____mutmut_orig  # type: ignore # mutmut generated
mutants_xǁAppErrorǁ__init____mutmut["xǁAppErrorǁ__init____mutmut_1"] = (
    AppError.xǁAppErrorǁ__init____mutmut_1
)  # type: ignore # mutmut generated
mutants_xǁAppErrorǁ__init____mutmut["xǁAppErrorǁ__init____mutmut_2"] = (
    AppError.xǁAppErrorǁ__init____mutmut_2
)  # type: ignore # mutmut generated
mutants_xǁAppErrorǁ__init____mutmut["xǁAppErrorǁ__init____mutmut_3"] = (
    AppError.xǁAppErrorǁ__init____mutmut_3
)  # type: ignore # mutmut generated
mutants_xǁAppErrorǁ__init____mutmut["xǁAppErrorǁ__init____mutmut_4"] = (
    AppError.xǁAppErrorǁ__init____mutmut_4
)  # type: ignore # mutmut generated


class NotFoundError(AppError):
    status_code = 404
    code = "not_found"


class ValidationError(AppError):
    status_code = 422
    code = "validation_error"


class AuthenticationError(AppError):
    status_code = 401
    code = "authentication_error"


class PermissionDeniedError(AppError):
    status_code = 403
    code = "permission_denied"


class ConflictError(AppError):
    status_code = 409
    code = "conflict"


mutants_xǁTaskNotFoundErrorǁ__init____mutmut: MutantDict = {}  # type: ignore


class TaskNotFoundError(NotFoundError):
    code = "task_not_found"

    @_mutmut_mutated(mutants_xǁTaskNotFoundErrorǁ__init____mutmut)
    def __init__(self, task_id: int):
        self.task_id = task_id
        super().__init__(
            f"Task {task_id} not found",
            details={"task_id": task_id},
        )

    def xǁTaskNotFoundErrorǁ__init____mutmut_orig(self, task_id: int):
        self.task_id = task_id
        super().__init__(
            f"Task {task_id} not found",
            details={"task_id": task_id},
        )

    def xǁTaskNotFoundErrorǁ__init____mutmut_1(self, task_id: int):
        self.task_id = None
        super().__init__(
            f"Task {task_id} not found",
            details={"task_id": task_id},
        )

    def xǁTaskNotFoundErrorǁ__init____mutmut_2(self, task_id: int):
        self.task_id = task_id
        super().__init__(
            None,
            details={"task_id": task_id},
        )

    def xǁTaskNotFoundErrorǁ__init____mutmut_3(self, task_id: int):
        self.task_id = task_id
        super().__init__(
            f"Task {task_id} not found",
            details=None,
        )

    def xǁTaskNotFoundErrorǁ__init____mutmut_4(self, task_id: int):
        self.task_id = task_id
        super().__init__(
            details={"task_id": task_id},
        )

    def xǁTaskNotFoundErrorǁ__init____mutmut_5(self, task_id: int):
        self.task_id = task_id
        super().__init__(
            f"Task {task_id} not found",
        )

    def xǁTaskNotFoundErrorǁ__init____mutmut_6(self, task_id: int):
        self.task_id = task_id
        super().__init__(
            f"Task {task_id} not found",
            details={"XXtask_idXX": task_id},
        )

    def xǁTaskNotFoundErrorǁ__init____mutmut_7(self, task_id: int):
        self.task_id = task_id
        super().__init__(
            f"Task {task_id} not found",
            details={"TASK_ID": task_id},
        )


mutants_xǁTaskNotFoundErrorǁ__init____mutmut["_mutmut_orig"] = (
    TaskNotFoundError.xǁTaskNotFoundErrorǁ__init____mutmut_orig
)  # type: ignore # mutmut generated
mutants_xǁTaskNotFoundErrorǁ__init____mutmut["xǁTaskNotFoundErrorǁ__init____mutmut_1"] = (
    TaskNotFoundError.xǁTaskNotFoundErrorǁ__init____mutmut_1
)  # type: ignore # mutmut generated
mutants_xǁTaskNotFoundErrorǁ__init____mutmut["xǁTaskNotFoundErrorǁ__init____mutmut_2"] = (
    TaskNotFoundError.xǁTaskNotFoundErrorǁ__init____mutmut_2
)  # type: ignore # mutmut generated
mutants_xǁTaskNotFoundErrorǁ__init____mutmut["xǁTaskNotFoundErrorǁ__init____mutmut_3"] = (
    TaskNotFoundError.xǁTaskNotFoundErrorǁ__init____mutmut_3
)  # type: ignore # mutmut generated
mutants_xǁTaskNotFoundErrorǁ__init____mutmut["xǁTaskNotFoundErrorǁ__init____mutmut_4"] = (
    TaskNotFoundError.xǁTaskNotFoundErrorǁ__init____mutmut_4
)  # type: ignore # mutmut generated
mutants_xǁTaskNotFoundErrorǁ__init____mutmut["xǁTaskNotFoundErrorǁ__init____mutmut_5"] = (
    TaskNotFoundError.xǁTaskNotFoundErrorǁ__init____mutmut_5
)  # type: ignore # mutmut generated
mutants_xǁTaskNotFoundErrorǁ__init____mutmut["xǁTaskNotFoundErrorǁ__init____mutmut_6"] = (
    TaskNotFoundError.xǁTaskNotFoundErrorǁ__init____mutmut_6
)  # type: ignore # mutmut generated
mutants_xǁTaskNotFoundErrorǁ__init____mutmut["xǁTaskNotFoundErrorǁ__init____mutmut_7"] = (
    TaskNotFoundError.xǁTaskNotFoundErrorǁ__init____mutmut_7
)  # type: ignore # mutmut generated
mutants_xǁArchivedTaskErrorǁ__init____mutmut: MutantDict = {}  # type: ignore


class ArchivedTaskError(ConflictError):
    code = "task_archived"

    @_mutmut_mutated(mutants_xǁArchivedTaskErrorǁ__init____mutmut)
    def __init__(self, task_id: int):
        self.task_id = task_id
        super().__init__(
            f"Task {task_id} is archived and cannot be changed",
            details={"task_id": task_id},
        )

    def xǁArchivedTaskErrorǁ__init____mutmut_orig(self, task_id: int):
        self.task_id = task_id
        super().__init__(
            f"Task {task_id} is archived and cannot be changed",
            details={"task_id": task_id},
        )

    def xǁArchivedTaskErrorǁ__init____mutmut_1(self, task_id: int):
        self.task_id = None
        super().__init__(
            f"Task {task_id} is archived and cannot be changed",
            details={"task_id": task_id},
        )

    def xǁArchivedTaskErrorǁ__init____mutmut_2(self, task_id: int):
        self.task_id = task_id
        super().__init__(
            None,
            details={"task_id": task_id},
        )

    def xǁArchivedTaskErrorǁ__init____mutmut_3(self, task_id: int):
        self.task_id = task_id
        super().__init__(
            f"Task {task_id} is archived and cannot be changed",
            details=None,
        )

    def xǁArchivedTaskErrorǁ__init____mutmut_4(self, task_id: int):
        self.task_id = task_id
        super().__init__(
            details={"task_id": task_id},
        )

    def xǁArchivedTaskErrorǁ__init____mutmut_5(self, task_id: int):
        self.task_id = task_id
        super().__init__(
            f"Task {task_id} is archived and cannot be changed",
        )

    def xǁArchivedTaskErrorǁ__init____mutmut_6(self, task_id: int):
        self.task_id = task_id
        super().__init__(
            f"Task {task_id} is archived and cannot be changed",
            details={"XXtask_idXX": task_id},
        )

    def xǁArchivedTaskErrorǁ__init____mutmut_7(self, task_id: int):
        self.task_id = task_id
        super().__init__(
            f"Task {task_id} is archived and cannot be changed",
            details={"TASK_ID": task_id},
        )


mutants_xǁArchivedTaskErrorǁ__init____mutmut["_mutmut_orig"] = (
    ArchivedTaskError.xǁArchivedTaskErrorǁ__init____mutmut_orig
)  # type: ignore # mutmut generated
mutants_xǁArchivedTaskErrorǁ__init____mutmut["xǁArchivedTaskErrorǁ__init____mutmut_1"] = (
    ArchivedTaskError.xǁArchivedTaskErrorǁ__init____mutmut_1
)  # type: ignore # mutmut generated
mutants_xǁArchivedTaskErrorǁ__init____mutmut["xǁArchivedTaskErrorǁ__init____mutmut_2"] = (
    ArchivedTaskError.xǁArchivedTaskErrorǁ__init____mutmut_2
)  # type: ignore # mutmut generated
mutants_xǁArchivedTaskErrorǁ__init____mutmut["xǁArchivedTaskErrorǁ__init____mutmut_3"] = (
    ArchivedTaskError.xǁArchivedTaskErrorǁ__init____mutmut_3
)  # type: ignore # mutmut generated
mutants_xǁArchivedTaskErrorǁ__init____mutmut["xǁArchivedTaskErrorǁ__init____mutmut_4"] = (
    ArchivedTaskError.xǁArchivedTaskErrorǁ__init____mutmut_4
)  # type: ignore # mutmut generated
mutants_xǁArchivedTaskErrorǁ__init____mutmut["xǁArchivedTaskErrorǁ__init____mutmut_5"] = (
    ArchivedTaskError.xǁArchivedTaskErrorǁ__init____mutmut_5
)  # type: ignore # mutmut generated
mutants_xǁArchivedTaskErrorǁ__init____mutmut["xǁArchivedTaskErrorǁ__init____mutmut_6"] = (
    ArchivedTaskError.xǁArchivedTaskErrorǁ__init____mutmut_6
)  # type: ignore # mutmut generated
mutants_xǁArchivedTaskErrorǁ__init____mutmut["xǁArchivedTaskErrorǁ__init____mutmut_7"] = (
    ArchivedTaskError.xǁArchivedTaskErrorǁ__init____mutmut_7
)  # type: ignore # mutmut generated
mutants_xǁTaskStateConflictErrorǁ__init____mutmut: MutantDict = {}  # type: ignore


class TaskStateConflictError(ConflictError):
    code = "invalid_task_transition"

    @_mutmut_mutated(mutants_xǁTaskStateConflictErrorǁ__init____mutmut)
    def __init__(self, current_status: str, requested_status: str):
        self.current_status = current_status
        self.requested_status = requested_status
        super().__init__(
            f"Cannot change task status from {current_status} to {requested_status}",
            details={
                "current_status": current_status,
                "requested_status": requested_status,
            },
        )

    def xǁTaskStateConflictErrorǁ__init____mutmut_orig(
        self, current_status: str, requested_status: str
    ):
        self.current_status = current_status
        self.requested_status = requested_status
        super().__init__(
            f"Cannot change task status from {current_status} to {requested_status}",
            details={
                "current_status": current_status,
                "requested_status": requested_status,
            },
        )

    def xǁTaskStateConflictErrorǁ__init____mutmut_1(
        self, current_status: str, requested_status: str
    ):
        self.current_status = None
        self.requested_status = requested_status
        super().__init__(
            f"Cannot change task status from {current_status} to {requested_status}",
            details={
                "current_status": current_status,
                "requested_status": requested_status,
            },
        )

    def xǁTaskStateConflictErrorǁ__init____mutmut_2(
        self, current_status: str, requested_status: str
    ):
        self.current_status = current_status
        self.requested_status = None
        super().__init__(
            f"Cannot change task status from {current_status} to {requested_status}",
            details={
                "current_status": current_status,
                "requested_status": requested_status,
            },
        )

    def xǁTaskStateConflictErrorǁ__init____mutmut_3(
        self, current_status: str, requested_status: str
    ):
        self.current_status = current_status
        self.requested_status = requested_status
        super().__init__(
            None,
            details={
                "current_status": current_status,
                "requested_status": requested_status,
            },
        )

    def xǁTaskStateConflictErrorǁ__init____mutmut_4(
        self, current_status: str, requested_status: str
    ):
        self.current_status = current_status
        self.requested_status = requested_status
        super().__init__(
            f"Cannot change task status from {current_status} to {requested_status}",
            details=None,
        )

    def xǁTaskStateConflictErrorǁ__init____mutmut_5(
        self, current_status: str, requested_status: str
    ):
        self.current_status = current_status
        self.requested_status = requested_status
        super().__init__(
            details={
                "current_status": current_status,
                "requested_status": requested_status,
            },
        )

    def xǁTaskStateConflictErrorǁ__init____mutmut_6(
        self, current_status: str, requested_status: str
    ):
        self.current_status = current_status
        self.requested_status = requested_status
        super().__init__(
            f"Cannot change task status from {current_status} to {requested_status}",
        )

    def xǁTaskStateConflictErrorǁ__init____mutmut_7(
        self, current_status: str, requested_status: str
    ):
        self.current_status = current_status
        self.requested_status = requested_status
        super().__init__(
            f"Cannot change task status from {current_status} to {requested_status}",
            details={
                "XXcurrent_statusXX": current_status,
                "requested_status": requested_status,
            },
        )

    def xǁTaskStateConflictErrorǁ__init____mutmut_8(
        self, current_status: str, requested_status: str
    ):
        self.current_status = current_status
        self.requested_status = requested_status
        super().__init__(
            f"Cannot change task status from {current_status} to {requested_status}",
            details={
                "CURRENT_STATUS": current_status,
                "requested_status": requested_status,
            },
        )

    def xǁTaskStateConflictErrorǁ__init____mutmut_9(
        self, current_status: str, requested_status: str
    ):
        self.current_status = current_status
        self.requested_status = requested_status
        super().__init__(
            f"Cannot change task status from {current_status} to {requested_status}",
            details={
                "current_status": current_status,
                "XXrequested_statusXX": requested_status,
            },
        )

    def xǁTaskStateConflictErrorǁ__init____mutmut_10(
        self, current_status: str, requested_status: str
    ):
        self.current_status = current_status
        self.requested_status = requested_status
        super().__init__(
            f"Cannot change task status from {current_status} to {requested_status}",
            details={
                "current_status": current_status,
                "REQUESTED_STATUS": requested_status,
            },
        )


mutants_xǁTaskStateConflictErrorǁ__init____mutmut["_mutmut_orig"] = (
    TaskStateConflictError.xǁTaskStateConflictErrorǁ__init____mutmut_orig
)  # type: ignore # mutmut generated
mutants_xǁTaskStateConflictErrorǁ__init____mutmut["xǁTaskStateConflictErrorǁ__init____mutmut_1"] = (
    TaskStateConflictError.xǁTaskStateConflictErrorǁ__init____mutmut_1
)  # type: ignore # mutmut generated
mutants_xǁTaskStateConflictErrorǁ__init____mutmut["xǁTaskStateConflictErrorǁ__init____mutmut_2"] = (
    TaskStateConflictError.xǁTaskStateConflictErrorǁ__init____mutmut_2
)  # type: ignore # mutmut generated
mutants_xǁTaskStateConflictErrorǁ__init____mutmut["xǁTaskStateConflictErrorǁ__init____mutmut_3"] = (
    TaskStateConflictError.xǁTaskStateConflictErrorǁ__init____mutmut_3
)  # type: ignore # mutmut generated
mutants_xǁTaskStateConflictErrorǁ__init____mutmut["xǁTaskStateConflictErrorǁ__init____mutmut_4"] = (
    TaskStateConflictError.xǁTaskStateConflictErrorǁ__init____mutmut_4
)  # type: ignore # mutmut generated
mutants_xǁTaskStateConflictErrorǁ__init____mutmut["xǁTaskStateConflictErrorǁ__init____mutmut_5"] = (
    TaskStateConflictError.xǁTaskStateConflictErrorǁ__init____mutmut_5
)  # type: ignore # mutmut generated
mutants_xǁTaskStateConflictErrorǁ__init____mutmut["xǁTaskStateConflictErrorǁ__init____mutmut_6"] = (
    TaskStateConflictError.xǁTaskStateConflictErrorǁ__init____mutmut_6
)  # type: ignore # mutmut generated
mutants_xǁTaskStateConflictErrorǁ__init____mutmut["xǁTaskStateConflictErrorǁ__init____mutmut_7"] = (
    TaskStateConflictError.xǁTaskStateConflictErrorǁ__init____mutmut_7
)  # type: ignore # mutmut generated
mutants_xǁTaskStateConflictErrorǁ__init____mutmut["xǁTaskStateConflictErrorǁ__init____mutmut_8"] = (
    TaskStateConflictError.xǁTaskStateConflictErrorǁ__init____mutmut_8
)  # type: ignore # mutmut generated
mutants_xǁTaskStateConflictErrorǁ__init____mutmut["xǁTaskStateConflictErrorǁ__init____mutmut_9"] = (
    TaskStateConflictError.xǁTaskStateConflictErrorǁ__init____mutmut_9
)  # type: ignore # mutmut generated
mutants_xǁTaskStateConflictErrorǁ__init____mutmut[
    "xǁTaskStateConflictErrorǁ__init____mutmut_10"
] = TaskStateConflictError.xǁTaskStateConflictErrorǁ__init____mutmut_10  # type: ignore # mutmut generated
mutants_xǁProjectNotFoundErrorǁ__init____mutmut: MutantDict = {}  # type: ignore


class ProjectNotFoundError(NotFoundError):
    code = "project_not_found"

    @_mutmut_mutated(mutants_xǁProjectNotFoundErrorǁ__init____mutmut)
    def __init__(self, project_id: int):
        self.project_id = project_id
        super().__init__(
            f"Project {project_id} not found",
            details={"project_id": project_id},
        )

    def xǁProjectNotFoundErrorǁ__init____mutmut_orig(self, project_id: int):
        self.project_id = project_id
        super().__init__(
            f"Project {project_id} not found",
            details={"project_id": project_id},
        )

    def xǁProjectNotFoundErrorǁ__init____mutmut_1(self, project_id: int):
        self.project_id = None
        super().__init__(
            f"Project {project_id} not found",
            details={"project_id": project_id},
        )

    def xǁProjectNotFoundErrorǁ__init____mutmut_2(self, project_id: int):
        self.project_id = project_id
        super().__init__(
            None,
            details={"project_id": project_id},
        )

    def xǁProjectNotFoundErrorǁ__init____mutmut_3(self, project_id: int):
        self.project_id = project_id
        super().__init__(
            f"Project {project_id} not found",
            details=None,
        )

    def xǁProjectNotFoundErrorǁ__init____mutmut_4(self, project_id: int):
        self.project_id = project_id
        super().__init__(
            details={"project_id": project_id},
        )

    def xǁProjectNotFoundErrorǁ__init____mutmut_5(self, project_id: int):
        self.project_id = project_id
        super().__init__(
            f"Project {project_id} not found",
        )

    def xǁProjectNotFoundErrorǁ__init____mutmut_6(self, project_id: int):
        self.project_id = project_id
        super().__init__(
            f"Project {project_id} not found",
            details={"XXproject_idXX": project_id},
        )

    def xǁProjectNotFoundErrorǁ__init____mutmut_7(self, project_id: int):
        self.project_id = project_id
        super().__init__(
            f"Project {project_id} not found",
            details={"PROJECT_ID": project_id},
        )


mutants_xǁProjectNotFoundErrorǁ__init____mutmut["_mutmut_orig"] = (
    ProjectNotFoundError.xǁProjectNotFoundErrorǁ__init____mutmut_orig
)  # type: ignore # mutmut generated
mutants_xǁProjectNotFoundErrorǁ__init____mutmut["xǁProjectNotFoundErrorǁ__init____mutmut_1"] = (
    ProjectNotFoundError.xǁProjectNotFoundErrorǁ__init____mutmut_1
)  # type: ignore # mutmut generated
mutants_xǁProjectNotFoundErrorǁ__init____mutmut["xǁProjectNotFoundErrorǁ__init____mutmut_2"] = (
    ProjectNotFoundError.xǁProjectNotFoundErrorǁ__init____mutmut_2
)  # type: ignore # mutmut generated
mutants_xǁProjectNotFoundErrorǁ__init____mutmut["xǁProjectNotFoundErrorǁ__init____mutmut_3"] = (
    ProjectNotFoundError.xǁProjectNotFoundErrorǁ__init____mutmut_3
)  # type: ignore # mutmut generated
mutants_xǁProjectNotFoundErrorǁ__init____mutmut["xǁProjectNotFoundErrorǁ__init____mutmut_4"] = (
    ProjectNotFoundError.xǁProjectNotFoundErrorǁ__init____mutmut_4
)  # type: ignore # mutmut generated
mutants_xǁProjectNotFoundErrorǁ__init____mutmut["xǁProjectNotFoundErrorǁ__init____mutmut_5"] = (
    ProjectNotFoundError.xǁProjectNotFoundErrorǁ__init____mutmut_5
)  # type: ignore # mutmut generated
mutants_xǁProjectNotFoundErrorǁ__init____mutmut["xǁProjectNotFoundErrorǁ__init____mutmut_6"] = (
    ProjectNotFoundError.xǁProjectNotFoundErrorǁ__init____mutmut_6
)  # type: ignore # mutmut generated
mutants_xǁProjectNotFoundErrorǁ__init____mutmut["xǁProjectNotFoundErrorǁ__init____mutmut_7"] = (
    ProjectNotFoundError.xǁProjectNotFoundErrorǁ__init____mutmut_7
)  # type: ignore # mutmut generated
mutants_xǁUnauthorizedActionErrorǁ__init____mutmut: MutantDict = {}  # type: ignore


class UnauthorizedActionError(PermissionDeniedError):
    @_mutmut_mutated(mutants_xǁUnauthorizedActionErrorǁ__init____mutmut)
    def __init__(
        self,
        action: str,
        resource: str,
        resource_id: int | None = None,
    ):
        self.action = action
        self.resource = resource
        self.resource_id = resource_id
        target = f" {resource} {resource_id}" if resource_id is not None else f" {resource}"
        super().__init__(
            f"Not authorized to {action}{target}",
            details={
                "action": action,
                "resource": resource,
                "resource_id": resource_id,
            },
        )

    def xǁUnauthorizedActionErrorǁ__init____mutmut_orig(
        self,
        action: str,
        resource: str,
        resource_id: int | None = None,
    ):
        self.action = action
        self.resource = resource
        self.resource_id = resource_id
        target = f" {resource} {resource_id}" if resource_id is not None else f" {resource}"
        super().__init__(
            f"Not authorized to {action}{target}",
            details={
                "action": action,
                "resource": resource,
                "resource_id": resource_id,
            },
        )

    def xǁUnauthorizedActionErrorǁ__init____mutmut_1(
        self,
        action: str,
        resource: str,
        resource_id: int | None = None,
    ):
        self.action = None
        self.resource = resource
        self.resource_id = resource_id
        target = f" {resource} {resource_id}" if resource_id is not None else f" {resource}"
        super().__init__(
            f"Not authorized to {action}{target}",
            details={
                "action": action,
                "resource": resource,
                "resource_id": resource_id,
            },
        )

    def xǁUnauthorizedActionErrorǁ__init____mutmut_2(
        self,
        action: str,
        resource: str,
        resource_id: int | None = None,
    ):
        self.action = action
        self.resource = None
        self.resource_id = resource_id
        target = f" {resource} {resource_id}" if resource_id is not None else f" {resource}"
        super().__init__(
            f"Not authorized to {action}{target}",
            details={
                "action": action,
                "resource": resource,
                "resource_id": resource_id,
            },
        )

    def xǁUnauthorizedActionErrorǁ__init____mutmut_3(
        self,
        action: str,
        resource: str,
        resource_id: int | None = None,
    ):
        self.action = action
        self.resource = resource
        self.resource_id = None
        target = f" {resource} {resource_id}" if resource_id is not None else f" {resource}"
        super().__init__(
            f"Not authorized to {action}{target}",
            details={
                "action": action,
                "resource": resource,
                "resource_id": resource_id,
            },
        )

    def xǁUnauthorizedActionErrorǁ__init____mutmut_4(
        self,
        action: str,
        resource: str,
        resource_id: int | None = None,
    ):
        self.action = action
        self.resource = resource
        self.resource_id = resource_id
        target = None
        super().__init__(
            f"Not authorized to {action}{target}",
            details={
                "action": action,
                "resource": resource,
                "resource_id": resource_id,
            },
        )

    def xǁUnauthorizedActionErrorǁ__init____mutmut_5(
        self,
        action: str,
        resource: str,
        resource_id: int | None = None,
    ):
        self.action = action
        self.resource = resource
        self.resource_id = resource_id
        target = (
            f" {resource} {resource_id}" if (resource_id is not None) and False else f" {resource}"
        )
        super().__init__(
            f"Not authorized to {action}{target}",
            details={
                "action": action,
                "resource": resource,
                "resource_id": resource_id,
            },
        )

    def xǁUnauthorizedActionErrorǁ__init____mutmut_6(
        self,
        action: str,
        resource: str,
        resource_id: int | None = None,
    ):
        self.action = action
        self.resource = resource
        self.resource_id = resource_id
        target = (
            f" {resource} {resource_id}" if (resource_id is not None) or True else f" {resource}"
        )
        super().__init__(
            f"Not authorized to {action}{target}",
            details={
                "action": action,
                "resource": resource,
                "resource_id": resource_id,
            },
        )

    def xǁUnauthorizedActionErrorǁ__init____mutmut_7(
        self,
        action: str,
        resource: str,
        resource_id: int | None = None,
    ):
        self.action = action
        self.resource = resource
        self.resource_id = resource_id
        target = f" {resource} {resource_id}" if resource_id is None else f" {resource}"
        super().__init__(
            f"Not authorized to {action}{target}",
            details={
                "action": action,
                "resource": resource,
                "resource_id": resource_id,
            },
        )

    def xǁUnauthorizedActionErrorǁ__init____mutmut_8(
        self,
        action: str,
        resource: str,
        resource_id: int | None = None,
    ):
        self.action = action
        self.resource = resource
        self.resource_id = resource_id
        target = f" {resource} {resource_id}" if resource_id is not None else f" {resource}"
        super().__init__(
            None,
            details={
                "action": action,
                "resource": resource,
                "resource_id": resource_id,
            },
        )

    def xǁUnauthorizedActionErrorǁ__init____mutmut_9(
        self,
        action: str,
        resource: str,
        resource_id: int | None = None,
    ):
        self.action = action
        self.resource = resource
        self.resource_id = resource_id
        target = f" {resource} {resource_id}" if resource_id is not None else f" {resource}"
        super().__init__(
            f"Not authorized to {action}{target}",
            details=None,
        )

    def xǁUnauthorizedActionErrorǁ__init____mutmut_10(
        self,
        action: str,
        resource: str,
        resource_id: int | None = None,
    ):
        self.action = action
        self.resource = resource
        self.resource_id = resource_id
        target = f" {resource} {resource_id}" if resource_id is not None else f" {resource}"
        super().__init__(
            details={
                "action": action,
                "resource": resource,
                "resource_id": resource_id,
            },
        )

    def xǁUnauthorizedActionErrorǁ__init____mutmut_11(
        self,
        action: str,
        resource: str,
        resource_id: int | None = None,
    ):
        self.action = action
        self.resource = resource
        self.resource_id = resource_id
        target = f" {resource} {resource_id}" if resource_id is not None else f" {resource}"
        super().__init__(
            f"Not authorized to {action}{target}",
        )

    def xǁUnauthorizedActionErrorǁ__init____mutmut_12(
        self,
        action: str,
        resource: str,
        resource_id: int | None = None,
    ):
        self.action = action
        self.resource = resource
        self.resource_id = resource_id
        target = f" {resource} {resource_id}" if resource_id is not None else f" {resource}"
        super().__init__(
            f"Not authorized to {action}{target}",
            details={
                "XXactionXX": action,
                "resource": resource,
                "resource_id": resource_id,
            },
        )

    def xǁUnauthorizedActionErrorǁ__init____mutmut_13(
        self,
        action: str,
        resource: str,
        resource_id: int | None = None,
    ):
        self.action = action
        self.resource = resource
        self.resource_id = resource_id
        target = f" {resource} {resource_id}" if resource_id is not None else f" {resource}"
        super().__init__(
            f"Not authorized to {action}{target}",
            details={
                "ACTION": action,
                "resource": resource,
                "resource_id": resource_id,
            },
        )

    def xǁUnauthorizedActionErrorǁ__init____mutmut_14(
        self,
        action: str,
        resource: str,
        resource_id: int | None = None,
    ):
        self.action = action
        self.resource = resource
        self.resource_id = resource_id
        target = f" {resource} {resource_id}" if resource_id is not None else f" {resource}"
        super().__init__(
            f"Not authorized to {action}{target}",
            details={
                "action": action,
                "XXresourceXX": resource,
                "resource_id": resource_id,
            },
        )

    def xǁUnauthorizedActionErrorǁ__init____mutmut_15(
        self,
        action: str,
        resource: str,
        resource_id: int | None = None,
    ):
        self.action = action
        self.resource = resource
        self.resource_id = resource_id
        target = f" {resource} {resource_id}" if resource_id is not None else f" {resource}"
        super().__init__(
            f"Not authorized to {action}{target}",
            details={
                "action": action,
                "RESOURCE": resource,
                "resource_id": resource_id,
            },
        )

    def xǁUnauthorizedActionErrorǁ__init____mutmut_16(
        self,
        action: str,
        resource: str,
        resource_id: int | None = None,
    ):
        self.action = action
        self.resource = resource
        self.resource_id = resource_id
        target = f" {resource} {resource_id}" if resource_id is not None else f" {resource}"
        super().__init__(
            f"Not authorized to {action}{target}",
            details={
                "action": action,
                "resource": resource,
                "XXresource_idXX": resource_id,
            },
        )

    def xǁUnauthorizedActionErrorǁ__init____mutmut_17(
        self,
        action: str,
        resource: str,
        resource_id: int | None = None,
    ):
        self.action = action
        self.resource = resource
        self.resource_id = resource_id
        target = f" {resource} {resource_id}" if resource_id is not None else f" {resource}"
        super().__init__(
            f"Not authorized to {action}{target}",
            details={
                "action": action,
                "resource": resource,
                "RESOURCE_ID": resource_id,
            },
        )


mutants_xǁUnauthorizedActionErrorǁ__init____mutmut["_mutmut_orig"] = (
    UnauthorizedActionError.xǁUnauthorizedActionErrorǁ__init____mutmut_orig
)  # type: ignore # mutmut generated
mutants_xǁUnauthorizedActionErrorǁ__init____mutmut[
    "xǁUnauthorizedActionErrorǁ__init____mutmut_1"
] = UnauthorizedActionError.xǁUnauthorizedActionErrorǁ__init____mutmut_1  # type: ignore # mutmut generated
mutants_xǁUnauthorizedActionErrorǁ__init____mutmut[
    "xǁUnauthorizedActionErrorǁ__init____mutmut_2"
] = UnauthorizedActionError.xǁUnauthorizedActionErrorǁ__init____mutmut_2  # type: ignore # mutmut generated
mutants_xǁUnauthorizedActionErrorǁ__init____mutmut[
    "xǁUnauthorizedActionErrorǁ__init____mutmut_3"
] = UnauthorizedActionError.xǁUnauthorizedActionErrorǁ__init____mutmut_3  # type: ignore # mutmut generated
mutants_xǁUnauthorizedActionErrorǁ__init____mutmut[
    "xǁUnauthorizedActionErrorǁ__init____mutmut_4"
] = UnauthorizedActionError.xǁUnauthorizedActionErrorǁ__init____mutmut_4  # type: ignore # mutmut generated
mutants_xǁUnauthorizedActionErrorǁ__init____mutmut[
    "xǁUnauthorizedActionErrorǁ__init____mutmut_5"
] = UnauthorizedActionError.xǁUnauthorizedActionErrorǁ__init____mutmut_5  # type: ignore # mutmut generated
mutants_xǁUnauthorizedActionErrorǁ__init____mutmut[
    "xǁUnauthorizedActionErrorǁ__init____mutmut_6"
] = UnauthorizedActionError.xǁUnauthorizedActionErrorǁ__init____mutmut_6  # type: ignore # mutmut generated
mutants_xǁUnauthorizedActionErrorǁ__init____mutmut[
    "xǁUnauthorizedActionErrorǁ__init____mutmut_7"
] = UnauthorizedActionError.xǁUnauthorizedActionErrorǁ__init____mutmut_7  # type: ignore # mutmut generated
mutants_xǁUnauthorizedActionErrorǁ__init____mutmut[
    "xǁUnauthorizedActionErrorǁ__init____mutmut_8"
] = UnauthorizedActionError.xǁUnauthorizedActionErrorǁ__init____mutmut_8  # type: ignore # mutmut generated
mutants_xǁUnauthorizedActionErrorǁ__init____mutmut[
    "xǁUnauthorizedActionErrorǁ__init____mutmut_9"
] = UnauthorizedActionError.xǁUnauthorizedActionErrorǁ__init____mutmut_9  # type: ignore # mutmut generated
mutants_xǁUnauthorizedActionErrorǁ__init____mutmut[
    "xǁUnauthorizedActionErrorǁ__init____mutmut_10"
] = UnauthorizedActionError.xǁUnauthorizedActionErrorǁ__init____mutmut_10  # type: ignore # mutmut generated
mutants_xǁUnauthorizedActionErrorǁ__init____mutmut[
    "xǁUnauthorizedActionErrorǁ__init____mutmut_11"
] = UnauthorizedActionError.xǁUnauthorizedActionErrorǁ__init____mutmut_11  # type: ignore # mutmut generated
mutants_xǁUnauthorizedActionErrorǁ__init____mutmut[
    "xǁUnauthorizedActionErrorǁ__init____mutmut_12"
] = UnauthorizedActionError.xǁUnauthorizedActionErrorǁ__init____mutmut_12  # type: ignore # mutmut generated
mutants_xǁUnauthorizedActionErrorǁ__init____mutmut[
    "xǁUnauthorizedActionErrorǁ__init____mutmut_13"
] = UnauthorizedActionError.xǁUnauthorizedActionErrorǁ__init____mutmut_13  # type: ignore # mutmut generated
mutants_xǁUnauthorizedActionErrorǁ__init____mutmut[
    "xǁUnauthorizedActionErrorǁ__init____mutmut_14"
] = UnauthorizedActionError.xǁUnauthorizedActionErrorǁ__init____mutmut_14  # type: ignore # mutmut generated
mutants_xǁUnauthorizedActionErrorǁ__init____mutmut[
    "xǁUnauthorizedActionErrorǁ__init____mutmut_15"
] = UnauthorizedActionError.xǁUnauthorizedActionErrorǁ__init____mutmut_15  # type: ignore # mutmut generated
mutants_xǁUnauthorizedActionErrorǁ__init____mutmut[
    "xǁUnauthorizedActionErrorǁ__init____mutmut_16"
] = UnauthorizedActionError.xǁUnauthorizedActionErrorǁ__init____mutmut_16  # type: ignore # mutmut generated
mutants_xǁUnauthorizedActionErrorǁ__init____mutmut[
    "xǁUnauthorizedActionErrorǁ__init____mutmut_17"
] = UnauthorizedActionError.xǁUnauthorizedActionErrorǁ__init____mutmut_17  # type: ignore # mutmut generated
