from typing import Final
from rivex import status
from .abstraction import IHTTPConstant


class HTTPStatus(IHTTPConstant):

    CONTINUE: Final[int] = int(status.HTTP_100_CONTINUE)
    SWITCHING_PROTOCOLS: Final[int] = int(status.HTTP_101_SWITCHING_PROTOCOLS)
    OK: Final[int] = int(status.HTTP_200_OK)
    CREATED: Final[int] = int(status.HTTP_201_CREATED)
    ACCEPTED: Final[int] = int(status.HTTP_202_ACCEPTED)
    NO_CONTENT: Final[int] = int(status.HTTP_204_NO_CONTENT)
    MOVED_PERMANENTLY: Final[int] = int(status.HTTP_301_MOVED_PERMANENTLY)
    FOUND: Final[int] = int(status.HTTP_302_FOUND)
    NOT_MODIFIED: Final[int] = int(status.HTTP_304_NOT_MODIFIED)
    TEMPORARY_REDIRECT: Final[int] = int(status.HTTP_307_TEMPORARY_REDIRECT)
    PERMANENT_REDIRECT: Final[int] = int(status.HTTP_308_PERMANENT_REDIRECT)
    BAD_REQUEST: Final[int] = int(status.HTTP_400_BAD_REQUEST)
    UNAUTHORIZED: Final[int] = int(status.HTTP_401_UNAUTHORIZED)
    FORBIDDEN: Final[int] = int(status.HTTP_403_FORBIDDEN)
    NOT_FOUND: Final[int] = int(status.HTTP_404_NOT_FOUND)
    METHOD_NOT_ALLOWED: Final[int] = int(status.HTTP_405_METHOD_NOT_ALLOWED)
    CONFLICT: Final[int] = int(status.HTTP_409_CONFLICT)
    PAYLOAD_TOO_LARGE: Final[int] = getattr(status, "HTTP_413_REQUEST_ENTITY_TOO_LARGE", 413)
    UNSUPPORTED_MEDIA_TYPE: Final[int] = getattr(status, "HTTP_415_UNSUPPORTED_MEDIA_TYPE", 415)
    UNPROCESSABLE_ENTITY: Final[int] = int(status.HTTP_422_UNPROCESSABLE_ENTITY)
    TOO_MANY_REQUESTS: Final[int] = int(status.HTTP_429_TOO_MANY_REQUESTS)
    INTERNAL_SERVER_ERROR: Final[int] = int(status.HTTP_500_INTERNAL_SERVER_ERROR)
    BAD_GATEWAY: Final[int] = int(status.HTTP_502_BAD_GATEWAY)
    SERVICE_UNAVAILABLE: Final[int] = int(status.HTTP_503_SERVICE_UNAVAILABLE)
    GATEWAY_TIMEOUT: Final[int] = int(status.HTTP_504_GATEWAY_TIMEOUT)

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "HTTPStatus"
