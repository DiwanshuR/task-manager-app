import app.logging_config
from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import logging
from starlette.exceptions import HTTPException as StarletteHTTPException
from starlette.routing import Match

from app.database import Base, engine
from app.routes import auth, projects, tasks
from app.models import user, project, task  # noqa: F401  -- registers tables with Base

from app.exceptions import AppError

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

# 2. Add a deliberate /__boom endpoint that raises RuntimeError, so your catch-all is testable
@app.get("/__boom", include_in_schema=False)
def deliberate_server_error():
    raise RuntimeError("Intentional exception-handler test failure")


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = [
        {
            "field": " -> ".join(
                str(location) for location in err["loc"] if location != "body"
            ),
            "message": err["msg"],
            "type": err["type"],
        }
        for err in exc.errors()
    ]
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={
            "error": {
                "code": "validation_error",
                "message": "Request validation failed",
                "details": errors,
            }
        },
    )


@app.exception_handler(AppError)
async def app_error_handler(request: Request, exc: AppError):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": {
                "code": exc.code,
                "message": exc.message,
                "details": exc.details,
            }
        },
        headers=exc.headers,
    )


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(
    request: Request,
    exc: StarletteHTTPException,
):
    code_by_status = {
        status.HTTP_400_BAD_REQUEST: "bad_request",
        status.HTTP_401_UNAUTHORIZED: "authentication_error",
        status.HTTP_403_FORBIDDEN: "permission_denied",
        status.HTTP_404_NOT_FOUND: "not_found",
        status.HTTP_409_CONFLICT: "conflict",
        status.HTTP_422_UNPROCESSABLE_ENTITY: "validation_error",
    }
    message = exc.detail if isinstance(exc.detail, str) else "Request failed"
    response_headers = dict(exc.headers or {})
    if exc.status_code == status.HTTP_405_METHOD_NOT_ALLOWED:
        matched_routes = []
        for router in (auth.router, projects.router, tasks.router):
            for route in router.routes:
                match, _ = route.matches(request.scope)
                if match is not Match.NONE:
                    specificity = sum(
                        not segment.startswith("{")
                        for segment in route.path.strip("/").split("/")
                        if segment
                    )
                    matched_routes.append((specificity, route.methods or ()))
        if matched_routes:
            highest_specificity = max(item[0] for item in matched_routes)
            allowed_methods = {
                method
                for specificity, methods in matched_routes
                if specificity == highest_specificity
                for method in methods
            }
        else:
            allowed_methods = set()
        if allowed_methods:
            response_headers["Allow"] = ", ".join(sorted(allowed_methods))

    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": {
                "code": code_by_status.get(exc.status_code, "http_error"),
                "message": message,
                "details": None,
            }
        },
        headers=response_headers,
    )


@app.exception_handler(Exception)
async def unhandled_exception_handler(request: Request, exc: Exception):
    logger.exception("Unhandled error on %s %s", request.method, request.url.path)
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "error": {
                "code": "internal_error",
                "message": "An unexpected error occurred. Please try again later.",
                "details": None,
            }
        },
    )