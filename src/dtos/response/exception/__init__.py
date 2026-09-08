"""Exception response DTOs — one per HTTP error status."""

from .bad_gateway import BadGatewayResponse
from .bad_input import BadInputResponse
from .conflict import ConflictResponse
from .forbidden import ForbiddenResponse
from .gateway_timeout import GatewayTimeoutResponse
from .internal_server import InternalServerResponse
from .method_not_allowed import MethodNotAllowedResponse
from .not_found import NotFoundResponse
from .payload_too_large import PayloadTooLargeResponse
from .service_unavailable import ServiceUnavailableResponse
from .too_many_requests import TooManyRequestsResponse
from .unauthorized import UnauthorizedResponse
from .unprocessable_entity import UnprocessableEntityResponse
from .unsupported_media_type import UnsupportedMediaTypeResponse

__all__ = [
    "BadGatewayResponse",
    "BadInputResponse",
    "ConflictResponse",
    "ForbiddenResponse",
    "GatewayTimeoutResponse",
    "InternalServerResponse",
    "MethodNotAllowedResponse",
    "NotFoundResponse",
    "PayloadTooLargeResponse",
    "ServiceUnavailableResponse",
    "TooManyRequestsResponse",
    "UnauthorizedResponse",
    "UnprocessableEntityResponse",
    "UnsupportedMediaTypeResponse",
]
