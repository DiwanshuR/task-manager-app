class TaskNotFoundError(Exception):
    def __init__(self, task_id: int):
        self.task_id = task_id
        super().__init__(f"Task {task_id} not found")


class ProjectNotFoundError(Exception):
    def __init__(self, project_id: int):
        self.project_id = project_id
        super().__init__(f"Project {project_id} not found")


class UnauthorizedActionError(Exception):
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
        super().__init__(f"Not authorized to {action}{target}")