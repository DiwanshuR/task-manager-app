from typing import Any

from pydantic import BaseModel


class ErrorBody(BaseModel):
    code: str
    message: str
    details: Any | None = None


class ErrorEnvelope(BaseModel):
    error: ErrorBody


API_ERROR_RESPONSES = {
    400: {"model": ErrorEnvelope, "description": "Malformed request"},
    401: {"model": ErrorEnvelope, "description": "Authentication required"},
    403: {"model": ErrorEnvelope, "description": "Permission denied"},
    404: {"model": ErrorEnvelope, "description": "Resource not found"},
    405: {"model": ErrorEnvelope, "description": "Method not allowed"},
    409: {"model": ErrorEnvelope, "description": "Request conflicts with state"},
    422: {"model": ErrorEnvelope, "description": "Request validation failed"},
    500: {"model": ErrorEnvelope, "description": "Unexpected server error"},
}
