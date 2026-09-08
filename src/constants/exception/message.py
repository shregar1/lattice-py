from typing import Final

from .abstraction import IConstant


class ExceptionMessage(IConstant):

    NOT_FOUND: Final[str] = "Resource not found"
    UNAUTHORIZED: Final[str] = "Unauthorized access"
    FORBIDDEN: Final[str] = "Action forbidden"
    METHOD_NOT_ALLOWED: Final[str] = "HTTP method not allowed for this resource"
    CONFLICT: Final[str] = "Resource state conflict"
    VALIDATION: Final[str] = "Validation error"
    INTERNAL_ERROR: Final[str] = "An internal server error occurred"
    UNSUPPORTED_MEDIA_TYPE: Final[str] = "Unsupported media type"
    PAYLOAD_TOO_LARGE: Final[str] = "Payload size exceeds maximum allowed limit"
    UNPROCESSABLE_ENTITY: Final[str] = "Unprocessable entity"
    TOO_MANY_REQUESTS: Final[str] = "Too many requests"
    INTERNAL_SERVER_ERROR: Final[str] = "An internal server error occurred"
    BAD_GATEWAY: Final[str] = "Bad gateway"
    SERVICE_UNAVAILABLE: Final[str] = "Service unavailable"
    GATEWAY_TIMEOUT: Final[str] = "Gateway timeout"

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "ExceptionMessage"
