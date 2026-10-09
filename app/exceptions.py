from typing import Any


class AppError(Exception):
    status_code = 500
    code = "application_error"

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


class TaskNotFoundError(NotFoundError):
    code = "task_not_found"

    def __init__(self, task_id: int):
        self.task_id = task_id
        super().__init__(
            f"Task {task_id} not found",
            details={"task_id": task_id},
        )


class ArchivedTaskError(ConflictError):
    code = "task_archived"

    def __init__(self, task_id: int):
        self.task_id = task_id
        super().__init__(
            f"Task {task_id} is archived and cannot be changed",
            details={"task_id": task_id},
        )


class TaskStateConflictError(ConflictError):
    code = "invalid_task_transition"

    def __init__(self, current_status: str, requested_status: str):
        self.current_status = current_status
        self.requested_status = requested_status
        super().__init__(
            f"Cannot change task status from {current_status} "
            f"to {requested_status}",
            details={
                "current_status": current_status,
                "requested_status": requested_status,
            },
        )


class ProjectNotFoundError(NotFoundError):
    code = "project_not_found"

    def __init__(self, project_id: int):
        self.project_id = project_id
        super().__init__(
            f"Project {project_id} not found",
            details={"project_id": project_id},
        )


class UnauthorizedActionError(PermissionDeniedError):
    def __init__(
        self,
        action: str,
        resource: str,
        resource_id: int | None = None,
    ):
        self.action = action
        self.resource = resource
        self.resource_id = resource_id
        target = (
            f" {resource} {resource_id}"
            if resource_id is not None
            else f" {resource}"
        )
        super().__init__(
            f"Not authorized to {action}{target}",
            details={
                "action": action,
                "resource": resource,
                "resource_id": resource_id,
            },
        )
