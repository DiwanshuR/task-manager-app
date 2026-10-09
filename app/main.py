import app.logging_config
from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import logging

from app.database import Base, engine
from app.routes import auth, projects, tasks
from app.models import user, project, task  # noqa: F401  -- registers tables with Base

from app.exceptions import (
    ArchivedTaskError,
    ProjectNotFoundError,
    TaskNotFoundError,
    TaskStateConflictError,
    UnauthorizedActionError,
)

logger = logging.getLogger(__name__)

app = FastAPI(
    title="Task Management System - v2 (MySQL)",
    description="Multi-user Task Management API with auth, projects, and tasks.",
    version="2.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)


app.include_router(auth.router)
app.include_router(projects.router)
app.include_router(tasks.router)


@app.get("/")
def root():
    return {"message": "Task Management System v2 (MySQL) is running", "docs": "/docs"}


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = [
        {"field": " -> ".join(str(loc) for loc in err["loc"] if loc != "body"), "message": err["msg"]}
        for err in exc.errors()
    ]
    return JSONResponse(status_code=422, content={"detail": "Invalid input", "errors": errors})


@app.exception_handler(TaskNotFoundError)
async def task_not_found_handler(request: Request, exc: TaskNotFoundError):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={
            "error": "task_not_found",
            "detail": str(exc),
            "task_id": exc.task_id,
        },
    )


@app.exception_handler(ArchivedTaskError)
async def archived_task_handler(request: Request, exc: ArchivedTaskError):
    return JSONResponse(
        status_code=status.HTTP_409_CONFLICT,
        content={"error": "task_archived", "detail": str(exc)},
    )


@app.exception_handler(TaskStateConflictError)
async def task_state_conflict_handler(
    request: Request,
    exc: TaskStateConflictError,
):
    return JSONResponse(
        status_code=status.HTTP_409_CONFLICT,
        content={
            "error": "invalid_task_transition",
            "detail": str(exc),
        },
    )


@app.exception_handler(ProjectNotFoundError)
async def project_not_found_handler(
    request: Request,
    exc: ProjectNotFoundError,
):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={
            "error": "project_not_found",
            "detail": str(exc),
            "project_id": exc.project_id,
        },
    )


@app.exception_handler(UnauthorizedActionError)
async def unauthorized_action_handler(
    request: Request,
    exc: UnauthorizedActionError,
):
    return JSONResponse(
        status_code=status.HTTP_403_FORBIDDEN,
        content={
            "error": "forbidden",
            "detail": str(exc),
        },
    )

@app.exception_handler(Exception)
async def unhandled_exception_handler(request: Request, exc: Exception):
    logger.exception("Unhandled error on %s %s", request.method, request.url)
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"detail": "An unexpected error occurred. Please try again later."},
    )