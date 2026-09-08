from typing import Dict, Any, Type

from .abstraction import IFactory
from exceptions import IException
from constants import ExceptionKey
from exceptions.http.bad_gateway import BadGatewayException
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
from exceptions.http.unsupported_media_type import UnsupportedMediaTypeException
from exceptions.http.bad_input import BadInputException


class ErrorFactory(IFactory[IException]):
    _registry: Dict[str, Type[IException]] = {

        ExceptionKey.DOMAIN: IException,

        ExceptionKey.NOT_FOUND: NotFoundException,

        ExceptionKey.VALIDATION: BadInputException,

        ExceptionKey.CONFLICT: ConflictException,

        ExceptionKey.FORBIDDEN: ForbiddenException,

        ExceptionKey.UNAUTHORIZED: UnauthorizedException,

        ExceptionKey.METHOD_NOT_ALLOWED: MethodNotAllowedException,

        ExceptionKey.PAYLOAD_TOO_LARGE: PayloadTooLargeException,

        ExceptionKey.UNSUPPORTED_MEDIA_TYPE: UnsupportedMediaTypeException,

        ExceptionKey.TOO_MANY_REQUESTS: TooManyRequestsException,

        ExceptionKey.INTERNAL_SERVER_ERROR: InternalServerException,

        ExceptionKey.BAD_GATEWAY: BadGatewayException,

        ExceptionKey.SERVICE_UNAVAILABLE: ServiceUnavailableException,

        ExceptionKey.GATEWAY_TIMEOUT: GatewayTimeoutException,
    }

    def get(self, error_type: str = ExceptionKey.DOMAIN, **overrides: Any) -> IException:
        key = error_type.lower()

        if key not in self._registry:
            raise KeyError(
                f"Unknown error type: '{error_type}'. Available: {list(self._registry.keys())}"
            )
        error_cls = self._registry[key]

        return error_cls(**overrides)

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "ErrorFactory"
