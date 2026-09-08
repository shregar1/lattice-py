"""HTTP-status exceptions.

Each module declares a single exception class pinned to a specific
HTTP status code. Use these from controllers and services to signal
transport-level failures; domain-specific failures live under
``exceptions.api``.
"""

from exceptions.http.bad_gateway import BadGatewayException
from exceptions.http.bad_input import BadInputException
from exceptions.http.conflict import ConflictException
from exceptions.http.forbidden import ForbiddenException
from exceptions.http.gateway_timeout import GatewayTimeoutException
from exceptions.http.internal_server import InternalServerException
from exceptions.http.method_not_allowed import MethodNotAllowedException
from exceptions.http.not_found import NotFoundException
from exceptions.http.payload_too_large import PayloadTooLargeException
from exceptions.http.service_unavailable import ServiceUnavailableException
from exceptions.http.too_many_requests import TooManyRequestsException
from exceptions.http.unauthorized import UnauthorizedException
from exceptions.http.unprocessable_entity import UnprocessableEntityException
from exceptions.http.unsupported_media_type import UnsupportedMediaTypeException
from exceptions.http.validation import ValidationException
__all__ = [
    "BadGatewayException",
    "BadInputException",
    "ConflictException",
    "ForbiddenException",
    "GatewayTimeoutException",
    "InternalServerException",
    "MethodNotAllowedException",
    "NotFoundException",
    "PayloadTooLargeException",
    "ServiceUnavailableException",
    "TooManyRequestsException",
    "UnauthorizedException",
    "UnprocessableEntityException",
    "UnsupportedMediaTypeException",
    "ValidationException",
]
