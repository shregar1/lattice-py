"""message enum module."""

from enum import Enum
from abstractions import EnumLayer
from constants import ExceptionMessage


class ExceptionMessageENUM(EnumLayer):
    NOT_FOUND = ExceptionMessage.NOT_FOUND
    UNAUTHORIZED = ExceptionMessage.UNAUTHORIZED
    FORBIDDEN = ExceptionMessage.FORBIDDEN
    METHOD_NOT_ALLOWED = ExceptionMessage.METHOD_NOT_ALLOWED
    CONFLICT = ExceptionMessage.CONFLICT
    VALIDATION = ExceptionMessage.VALIDATION
    INTERNAL_ERROR = ExceptionMessage.INTERNAL_ERROR
    UNSUPPORTED_MEDIA_TYPE = ExceptionMessage.UNSUPPORTED_MEDIA_TYPE
    PAYLOAD_TOO_LARGE = ExceptionMessage.PAYLOAD_TOO_LARGE
    UNPROCESSABLE_ENTITY = ExceptionMessage.UNPROCESSABLE_ENTITY
    TOO_MANY_REQUESTS = ExceptionMessage.TOO_MANY_REQUESTS
    INTERNAL_SERVER_ERROR = ExceptionMessage.INTERNAL_SERVER_ERROR
    BAD_GATEWAY = ExceptionMessage.BAD_GATEWAY
    SERVICE_UNAVAILABLE = ExceptionMessage.SERVICE_UNAVAILABLE
    GATEWAY_TIMEOUT = ExceptionMessage.GATEWAY_TIMEOUT

    @property
    def name(self) -> str:
        """Returns the layer name."""
        return "ExceptionMessageENUM"

