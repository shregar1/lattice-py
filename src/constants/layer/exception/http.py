"""HTTP exception layer constants."""

from typing import Final

from .abstraction import ILayerConstant


class HTTPException(ILayerConstant):

    BAD_GATEWAY: Final[str] = "BadGatewayException"
    BAD_INPUT: Final[str] = "BadInputException"
    CONFLICT: Final[str] = "ConflictException"
    FORBIDDEN: Final[str] = "ForbiddenException"
    GATEWAY_TIMEOUT: Final[str] = "GatewayTimeoutException"
    INTERNAL_SERVER: Final[str] = "InternalServerException"
    METHOD_NOT_ALLOWED: Final[str] = "MethodNotAllowedException"
    NOT_FOUND: Final[str] = "NotFoundException"
    PAYLOAD_TOO_LARGE: Final[str] = "PayloadTooLargeException"
    SERVICE_UNAVAILABLE: Final[str] = "ServiceUnavailableException"
    TOO_MANY_REQUESTS: Final[str] = "TooManyRequestsException"
    UNAUTHORIZED: Final[str] = "UnauthorizedException"
    UNPROCESSABLE_ENTITY: Final[str] = "UnprocessableEntityException"
    UNSUPPORTED_MEDIA_TYPE: Final[str] = "UnsupportedMediaTypeException"

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "HTTPException"
