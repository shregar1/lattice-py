import json

from rivex import HTTPException, Dependency
from typing import Any, Optional, Dict, List, Tuple, Sequence

from constants import ApiResponseContentType
from constants import HTTPStatus, ResponseEntity
from .abstraction import IResponseDTO
from dtos import (
    BadGatewayResponse,
    BadInputResponse,
    ConflictResponse,
    ForbiddenResponse,
    GatewayTimeoutResponse,
    InternalServerResponse,
    MethodNotAllowedResponse,
    NotFoundResponse,
    PayloadTooLargeResponse,
    ServiceUnavailableResponse,
    TooManyRequestsResponse,
    UnauthorizedResponse,
    UnprocessableEntityResponse,
    UnsupportedMediaTypeResponse,
)
from dependencies import LoggerUtilityDependency
from .abstraction import IUtility
from utilities import Logger


class ResponseUtility(IUtility):
    def __init__(
        self,
        urn: Optional[str] = None,
        tenant_id: Optional[int] = None,
        tenant_urn: Optional[str] = None,
        user_id: Optional[int] = None,
        user_urn: Optional[str] = None,
        api_name: Optional[str] = None,
        ip_address: Optional[str] = None,
        user_agent: Optional[str] = None,
        logger: Logger = Dependency(LoggerUtilityDependency),
        *args: Any,
        **kwargs: Any,
    ) -> None:
        IUtility.__init__(
            self,
            urn=urn,
            tenant_id=tenant_id,
            tenant_urn=tenant_urn,
            user_id=user_id,
            user_urn=user_urn,
            api_name=api_name,
            ip_address=ip_address,
            user_agent=user_agent,
            logger=logger,
            *args,
            **kwargs,
        )

        self.urn=urn
        self.tenant_id=tenant_id
        self.tenant_urn=tenant_urn
        self.user_id=user_id
        self.user_urn=user_urn
        self.api_name=api_name
        self.ip_address=ip_address
        self.user_agent=user_agent
        self.logger=logger

    @staticmethod
    def _build_response_entity(
        status: int,
        response_dto: Any,
        headers: Optional[Sequence[Tuple[str, str]]] = None,
        content_type: str = ApiResponseContentType.APPLICATION_JSON,
    ) -> Dict[str, Any]:
        """
        Method to ....
        """
        return ResponseEntity.build(
            status=status,
            body=response_dto,
            headers=headers,
            content_type=content_type,
        )

    @classmethod
    def build_bad_gateway_response(
        cls,
        message: str = "Bad gateway error",
        reference_urn: Optional[str] = None,
        **kwargs: Any,
    ) -> Dict[str, Any]:
        dto = BadGatewayResponse.build(message=message, reference_urn=reference_urn, **kwargs)

        return cls._build_response_entity(HTTPStatus.BAD_GATEWAY, dto)

    @classmethod
    def build_bad_input_response(
        cls,
        message: str = "Invalid input provided",
        reference_urn: Optional[str] = None,
        **kwargs: Any,
    ) -> Dict[str, Any]:
        dto = BadInputResponse.build(message=message, reference_urn=reference_urn, **kwargs)

        return cls._build_response_entity(HTTPStatus.BAD_REQUEST, dto)

    @classmethod
    def build_conflict_response(
        cls,
        message: str = "Resource state conflict",
        reference_urn: Optional[str] = None,
        **kwargs: Any,
    ) -> Dict[str, Any]:
        dto = ConflictResponse.build(message=message, reference_urn=reference_urn, **kwargs)

        return cls._build_response_entity(HTTPStatus.CONFLICT, dto)

    @classmethod
    def build_forbidden_response(
        cls,
        message: str = "Access forbidden",
        reference_urn: Optional[str] = None,
        **kwargs: Any,
    ) -> Dict[str, Any]:
        dto = ForbiddenResponse.build(message=message, reference_urn=reference_urn, **kwargs)

        return cls._build_response_entity(HTTPStatus.FORBIDDEN, dto)

    @classmethod
    def build_gateway_timeout_response(
        cls,
        message: str = "Gateway timed out",
        reference_urn: Optional[str] = None,
        **kwargs: Any,
    ) -> Dict[str, Any]:
        dto = GatewayTimeoutResponse.build(message=message, reference_urn=reference_urn, **kwargs)

        return cls._build_response_entity(HTTPStatus.GATEWAY_TIMEOUT, dto)

    @classmethod
    def build_internal_server_response(
        cls,
        message: str = "Internal server error",
        reference_urn: Optional[str] = None,
        **kwargs: Any,
    ) -> Dict[str, Any]:
        dto = InternalServerResponse.build(message=message, reference_urn=reference_urn, **kwargs)

        return cls._build_response_entity(HTTPStatus.INTERNAL_SERVER_ERROR, dto)

    @classmethod
    def build_method_not_allowed_response(
        cls,
        message: str = "HTTP method not allowed",
        reference_urn: Optional[str] = None,
        **kwargs: Any,
    ) -> Dict[str, Any]:
        dto = MethodNotAllowedResponse.build(message=message, reference_urn=reference_urn, **kwargs)

        return cls._build_response_entity(HTTPStatus.METHOD_NOT_ALLOWED, dto)

    @classmethod
    def build_not_found_response(
        cls,
        message: str = "Resource not found",
        reference_urn: Optional[str] = None,
        **kwargs: Any,
    ) -> Dict[str, Any]:
        dto = NotFoundResponse.build(message=message, reference_urn=reference_urn, **kwargs)

        return cls._build_response_entity(HTTPStatus.NOT_FOUND, dto)

    @classmethod
    def build_payload_too_large_response(
        cls,
        message: str = "Payload exceeds size limit",
        reference_urn: Optional[str] = None,
        **kwargs: Any,
    ) -> Dict[str, Any]:
        dto = PayloadTooLargeResponse.build(message=message, reference_urn=reference_urn, **kwargs)

        return cls._build_response_entity(HTTPStatus.PAYLOAD_TOO_LARGE, dto)

    @classmethod
    def build_service_unavailable_response(
        cls,
        message: str = "Service currently unavailable",
        reference_urn: Optional[str] = None,
        **kwargs: Any,
    ) -> Dict[str, Any]:
        dto = ServiceUnavailableResponse.build(
            message=message, reference_urn=reference_urn, **kwargs
        )

        return cls._build_response_entity(HTTPStatus.SERVICE_UNAVAILABLE, dto)

    @classmethod
    def build_too_many_requests_response(
        cls,
        message: str = "Too many requests",
        reference_urn: Optional[str] = None,
        **kwargs: Any,
    ) -> Dict[str, Any]:
        dto = TooManyRequestsResponse.build(message=message, reference_urn=reference_urn, **kwargs)

        return cls._build_response_entity(HTTPStatus.TOO_MANY_REQUESTS, dto)

    @classmethod
    def build_unauthorized_response(
        cls,
        message: str = "Unauthorized request",
        reference_urn: Optional[str] = None,
        **kwargs: Any,
    ) -> Dict[str, Any]:
        dto = UnauthorizedResponse.build(message=message, reference_urn=reference_urn, **kwargs)

        return cls._build_response_entity(HTTPStatus.UNAUTHORIZED, dto)

    @classmethod
    def build_unprocessable_entity_response(
        cls,
        message: str = "Unprocessable entity payload",
        reference_urn: Optional[str] = None,
        **kwargs: Any,
    ) -> Dict[str, Any]:
        dto = UnprocessableEntityResponse.build(
            message=message, reference_urn=reference_urn, **kwargs
        )

        return cls._build_response_entity(HTTPStatus.UNPROCESSABLE_ENTITY, dto)

    @classmethod
    def build_unsupported_media_type_response(
        cls,
        message: str = "Unsupported media type",
        reference_urn: Optional[str] = None,
        **kwargs: Any,
    ) -> Dict[str, Any]:
        dto = UnsupportedMediaTypeResponse.build(
            message=message, reference_urn=reference_urn, **kwargs
        )

        return cls._build_response_entity(HTTPStatus.UNSUPPORTED_MEDIA_TYPE, dto)

    @staticmethod
    def http_exception_detail(envelope: IResponseDTO) -> Dict[str, Any]:
        """
        Method to ....
        """
        return envelope.model_dump(by_alias=True, mode="json")

    @staticmethod
    def envelope_from_http_exception(
        exc: HTTPException, *, reference_urn: Optional[str] = None
    ) -> IResponseDTO:
        detail = exc.detail

        if IResponseDTO.is_envelope_payload(detail):
            return IResponseDTO.model_validate(detail)

        if isinstance(detail, dict):
            message = str(detail.get("message") or detail.get("detail") or "Request failed")
            code = str(detail.get("code") or "HTTP_ERROR")

        return IResponseDTO.failed(message, code, reference_urn=reference_urn)

        return IResponseDTO.failed(str(detail), "HTTP_ERROR", reference_urn=reference_urn)

    @staticmethod
    def render_http_exception(
        exc: HTTPException, *, reference_urn: Optional[str] = None
    ) -> Dict[str, Any]:
        envelope = ResponseUtility.envelope_from_http_exception(exc, reference_urn=reference_urn)

        return envelope.model_dump(by_alias=True, mode="json")

    @staticmethod
    def render_envelope_bytes(envelope: IResponseDTO) -> bytes:
        """
        Method to ....
        """
        return envelope.to_http_body()

    @staticmethod
    def envelope_http_response(
        envelope: IResponseDTO,
        status_code: int,
        extra_headers: List[Tuple[str, str]] | None = None,
    ) -> Dict[str, Any]:
        headers: List[Tuple[str, str]] = [("content-type", ApiResponseContentType.APPLICATION_JSON)]

        if extra_headers:
            headers.extend(extra_headers)

        return {
            "status": status_code,
            "headers": headers,
            "body_json": envelope.model_dump(by_alias=True, mode="json"),
        }

    @staticmethod
    def parse_envelope_json(raw: bytes | str) -> IResponseDTO | None:

        try:
            text = raw.decode() if isinstance(raw, bytes) else raw
            payload = json.loads(text)
        except (json.JSONDecodeError, UnicodeDecodeError):
            return None

        if not IResponseDTO.is_envelope_payload(payload):
            return None

        return IResponseDTO.model_validate(payload)

    @staticmethod
    def merge_timing(metadata: Dict[str, Any] | None = None) -> Dict[str, Any]:
        from utilities import RequestTimingUtility

        return RequestTimingUtility.merge_timing_metadata(metadata)

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "ResponseUtility"
