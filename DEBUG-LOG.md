# Debug log

## Day 2: Mocks and fakes

I considered mocking each repository method in the task-service tests. That would make the tests focus on expected calls rather than task behavior. I used an in-memory fake repository instead so the service tests can exercise repository-like behavior without HTTP requests or a database.

## Day 3: RBAC and task lifecycle

Task permissions are checked after confirming that the task exists. A missing task returns **404**; an existing task outside the caller's project access returns **403**. This keeps “not found” distinct from “forbidden” and makes the API's response policy explicit.

Admins may read, create, update, and delete any non-archived task. Managers may read, create, update, and archive tasks only in projects they own or belong to. Members may read and create tasks in projects they belong to, and may update only tasks they created. Members cannot archive or delete tasks; managers cannot delete them either.

Tasks start as `pending` and move only through `pending → in_progress → done`. A manager or admin can archive a task from any non-archived state. Archived tasks remain readable, but nobody—including an admin—can update or delete them. Admin deletion remains available for non-archived tasks and is a soft delete: the row is retained with `deleted_at` set, hidden from ordinary reads and lists, and recoverable by an admin through `GET /tasks/deleted` and `POST /tasks/{task_id}/restore`.

For an existing MySQL database, apply `migrations/001_add_archived_task_status.sql` if the archived enum change has not already been applied, then apply `migrations/002_add_task_soft_delete.sql`. `Base.metadata.create_all()` does not add the new column to an existing table.