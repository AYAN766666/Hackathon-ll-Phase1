from typing import Any, Dict, Optional
from fastapi import HTTPException, status


class APIResponse:
    """Utility class for standard API responses."""

    @staticmethod
    def success(data: Any = None, message: str = "Success", status_code: int = 200) -> Dict[str, Any]:
        """Create a success response."""
        return {
            "status": "success",
            "message": message,
            "data": data,
            "status_code": status_code
        }

    @staticmethod
    def error(message: str = "Error occurred", status_code: int = 400) -> Dict[str, Any]:
        """Create an error response."""
        return {
            "status": "error",
            "message": message,
            "status_code": status_code
        }


def raise_http_exception(
    status_code: int = status.HTTP_400_BAD_REQUEST,
    detail: str = "Bad Request"
) -> None:
    """Raise an HTTP exception with standardized detail."""
    raise HTTPException(
        status_code=status_code,
        detail=detail
    )


def not_found_exception(resource: str = "Resource") -> None:
    """Raise a not found exception."""
    raise_http_exception(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"{resource} not found"
    )


def unauthorized_exception(detail: str = "Not authenticated") -> None:
    """Raise an unauthorized exception."""
    raise_http_exception(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=detail
    )


def forbidden_exception(detail: str = "Access denied") -> None:
    """Raise a forbidden exception."""
    raise_http_exception(
        status_code=status.HTTP_403_FORBIDDEN,
        detail=detail
    )