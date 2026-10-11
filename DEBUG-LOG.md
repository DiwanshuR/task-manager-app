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
schemathesis run http://127.0.0.1:8000/openapi.json --header "Authorization: Bearer <temporary-admin-token>" --max-examples 20 --workers 1
```

The test database and account were created under the session's temporary files; the configured MySQL database was not used. The final authenticated run generated **955 cases and passed all 955** across Coverage, Fuzzing, and Stateful, with no failed cases or server errors. The deliberate `/__boom` test route is absent from the public OpenAPI paths.

The first authenticated run found these contract and robustness defects:

- Task creation advertised every task status, including `archived`, although the API only accepts `pending` when creating a task. The schema now declares only `pending`.
- `PUT /tasks/deleted` matched the integer task route and returned 422 instead of 405. Integer path converters now prevent static routes from being interpreted as IDs.
- An object-valued update status caused a `TypeError` during membership testing and returned 500. Status validation now rejects non-string values safely with 422.
- IDs larger than the database's signed 32-bit integer range and an unbounded pagination offset overflowed SQLite integer bindings and returned 500. Route/schema ID bounds and a pagination-offset bound now reject these values with 422.

The final run still reports non-failing warnings: task mutation operations often receive generated IDs that do not identify an existing task, so they correctly return 404; generated auth inputs also do not always satisfy the API's request validation. These are data-generation/schema-constraint coverage limitations, not server errors. The integration tests separately verify the intended 404/422 behavior and the shared error envelope.

#### sCHEMATHESS output
>> schemathesis run http://localhost:8000/openapi.json
Schemathesis v4.30.0
━━━━━━━━━━━━━━━━━━━━

 ✅  Loaded specification from http://localhost:8000/openapi.json (in 4.25s)     

     Base URL:         http://localhost:8000/                                    
     Specification:    Open API 3.1.0                                            
     Operations:       20 selected / 20 total                                    

 ✅  API capabilities:                                                           

     Supports NULL byte in headers:                            ✘                 
     Accepts backslash and control characters in URL paths:    ✓                 

 ⏭   Examples (in 0.13s)                                                         
                                                                                 
     ⏭  20 skipped                                                               

 ✅  Coverage (in 9.55s)                                                         
                                                                                 
     ✅ 20 passed                                                                

 ✅  Fuzzing (in 122.47s)                                                        
                                                                                 
     ✅ 20 passed                                                                

 ✅  Stateful (in 37.60s)                                                        

     Scenarios:    261                                                           
     API Links:    1 covered / 94 selected / 94 total (94 inferred)              

     ✅ 261 passed                                                               

==================================== WARNINGS ===================================

Authentication failed: 7 operations returned authentication errors

401 Unauthorized (7 operations):
  - DELETE /auth/users/{user_id}
  - GET /auth/current-user
  - GET /projects/
  - GET /tasks/
  - GET /tasks/deleted
  - POST /projects/
  - POST /tasks/

💡 Ensure valid authentication credentials are set via --auth or -H

Missing test data: 10 operations repeatedly returned 404 Not Found, preventing tests from reaching your API's core logic

No links point to this operation - POST /auth/register appears to supply the data it needs:
  - DELETE /auth/users/{user_id}

💡 Add a link from POST /auth/register, or supply the identifiers it returns in your config file

No links point to these operations - POST /projects/ appears to supply the data they need (4 operations):
  - DELETE /projects/{project_id}
  - GET /projects/{project_id}
  - POST /projects/{project_id}/members
  - PUT /projects/{project_id}

💡 Add a link from POST /projects/, or supply the identifiers it returns in yourconfig file

No links point to these operations - POST /tasks/ appears to supply the data they need (5 operations):
  - DELETE /tasks/{task_id}
  - GET /tasks/{task_id}
  - POST /tasks/{task_id}/archive
  - POST /tasks/{task_id}/restore
  - PUT /tasks/{task_id}

💡 Add a link from POST /tasks/, or supply the identifiers it returns in your config file

Schema validation mismatch: 2 operations mostly rejected generated data due to validation errors, indicating schema constraints don't match API validation

  - POST /auth/login
  - POST /auth/register

💡 Check your schema constraints - API validation may be stricter than documented

==================================== SUMMARY ====================================

API Operations:
  Selected: 20/20
  Tested: 20

Test Phases:
  ⏭  Examples
  ✅ Coverage
  ✅ Fuzzing
  ✅ Stateful

Warnings:
  ⚠️ Missing authentication: 7 operations returned only 401/403 responses
  ⚠️ Missing valid test data: 10 operations repeatedly returned 404 responses
  ⚠️ Schema validation mismatch: 2 operations mostly rejected generated data

Test cases:
  3489 generated, 3489 passed, 2 errored

Seed: 337846117038312568756142909416697298929

============================= 3 warnings in 174.18s =========================



### Hunt 1: Title whitespace was not trimmed

- **Reproduction:** Ran `test_normalize_title_trims_surrounding_whitespace` in the VS Code debugger.
- **Symptom:** The test expects `normalize_title("  Write tests  ")` to return `"Write tests"`, but the function returns the original title with surrounding spaces.
- **Hypothesis:** The function computes a trimmed value but returns a different value.
- **Debugger evidence:** At the breakpoint on the return statement, `title` was [record the value you observed] and `normalized` was [record the value you observed].
- **Root cause:** `normalize_title` returns `title` instead of the already-trimmed `normalized` value.
- **Fix:** Change the return to `return normalized`.
- **Regression test:** `test_normalize_title_trims_surrounding_whitespace` checks the trimmed result.
- **Verification:** [After fixing it, record the focused test command and whether it passed.]
d:\Infoorigin-Project\Task-Manager\tests\unit\test_task_rules.py::test_normalize_title_trims_surrounding_whitespace failed: def test_normalize_title_trims_surrounding_whitespace():
>       assert normalize_title("  Write tests  ") == "Write tests"
E       AssertionError: assert '  Write tests  ' == 'Write tests'
E         
E         - Write tests
E         +   Write tests  
E         ? ++           ++

tests\unit\test_task_rules.py:34: AssertionError

### Hunt 2 : Incorrect task creator ID

File: app/services/task_service.py

Method: TaskService.create()

Test: test_create_task_uses_fake_repository_and_records_creator

Intentional change: Replaced created_by=user_id with created_by=0.

Expected behavior: The task should record the ID of the user who created it.

Actual behavior: The task records creator ID 0 instead of 10.

Failed assertion:

assert task.created_by == 10

Root cause: The service passes a hardcoded ID to the repository instead of the authenticated user's ID.

Fix: Pass created_by=user_id to task_repository.create().


### ## Bug 3: Incorrect admin flag when listing tasks

**File:** `app/services/task_service.py`

**Method:** `TaskService.list()`

**Test:** `test_list_tasks_passes_filters_to_repository`

**Intentional change:** Replaced `is_admin=(role_value == "admin")` with `is_admin=True`.

**Expected behavior:** Only users with the admin role should be passed to the repository with `is_admin=True`.

**Actual behavior:** The service passes `is_admin=True` even when the user's role is `"member"`.

**Failed assertion:** The expected dictionary contains `"is_admin": False`, but the actual dictionary contains `"is_admin": True`.

**Root cause:** The service uses a hardcoded Boolean instead of checking the user's role.

**Fix:** Restore `is_admin=(role_value == "admin")`.

### open source repo tests run ": https://github.com/appstiwari/py-calculator/blob/main/calc_app/core.py