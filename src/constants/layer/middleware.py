"""MiddlewareName — PascalCase class-name constants for the middleware layer."""

from typing import Final

from .abstraction import ILayerConstant


class Middleware(ILayerConstant):

    AUTHENTICATION: Final[str] = "AuthenticationMiddleware"
    CONTENT_TYPE_VALIDATION: Final[str] = "ContentTypeValidationMiddleware"
    OPEN_TELEMETRY_TRACING: Final[str] = "TracingMiddleware"
    PAYLOAD_SIZE_LIMIT: Final[str] = "SizeLimitMiddleware"
    REQUEST_ID: Final[str] = "RequestContextMiddleware"
    REQUEST_VALIDATION: Final[str] = "RequestValidationMiddleware"
    SECURITY_HEADERS: Final[str] = "SecurityHeadersMiddleware"

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "Middleware"
