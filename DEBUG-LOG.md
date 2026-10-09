# Debug log

## Day 2: Mocks and fakes

I considered mocking each repository method in the task-service tests. That would make the tests focus on expected calls rather than task behavior. I used an in-memory fake repository instead so the service tests can exercise repository-like behavior without HTTP requests or a database.

## Day 3: RBAC and task lifecycle

Task permissions are checked after confirming that the task exists. A missing task returns **404**; an existing task outside the caller's project access returns **403**. This keeps “not found” distinct from “forbidden” and makes the API's response policy explicit.

Admins may read, create, update, and delete any non-archived task. Managers may read, create, update, and archive tasks only in projects they own or belong to. Members may read and create tasks in projects they belong to, and may update only tasks they created. Members cannot archive or delete tasks; managers cannot delete them either.

Tasks start as `pending` and move only through `pending → in_progress → done`. A manager or admin can archive a task from any non-archived state. Archived tasks remain readable, but nobody—including an admin—can update or delete them. Admin deletion remains available for non-archived tasks and is a soft delete: the row is retained with `deleted_at` set, hidden from ordinary reads and lists, and recoverable by an admin through `GET /tasks/deleted` and `POST /tasks/{task_id}/restore`.

For an existing MySQL database, apply `migrations/001_add_archived_task_status.sql` if the archived enum change has not already been applied, then apply `migrations/002_add_task_soft_delete.sql`. `Base.metadata.create_all()` does not add the new column to an existing table.

## Day 4: API contract fuzzing

Installed Schemathesis with `pip install schemathesis==4.30.0` and ran all 20 OpenAPI operations on an isolated SQLite database with a temporary admin token:

```powershell
schemathesis run http://127.0.0.1:8765/openapi.json --header "Authorization: Bearer <temporary-admin-token>" --max-examples 20 --workers 1
```

The test database and account were created under the session's temporary files; the configured MySQL database was not used. The final authenticated run generated **955 cases and passed all 955** across Coverage, Fuzzing, and Stateful, with no failed cases or server errors. The deliberate `/__boom` test route is absent from the public OpenAPI paths.

The first authenticated run found these contract and robustness defects:

- Task creation advertised every task status, including `archived`, although the API only accepts `pending` when creating a task. The schema now declares only `pending`.
- `PUT /tasks/deleted` matched the integer task route and returned 422 instead of 405. Integer path converters now prevent static routes from being interpreted as IDs.
- An object-valued update status caused a `TypeError` during membership testing and returned 500. Status validation now rejects non-string values safely with 422.
- IDs larger than the database's signed 32-bit integer range and an unbounded pagination offset overflowed SQLite integer bindings and returned 500. Route/schema ID bounds and a pagination-offset bound now reject these values with 422.

The final run still reports non-failing warnings: task mutation operations often receive generated IDs that do not identify an existing task, so they correctly return 404; generated auth inputs also do not always satisfy the API's request validation. These are data-generation/schema-constraint coverage limitations, not server errors. The integration tests separately verify the intended 404/422 behavior and the shared error envelope.