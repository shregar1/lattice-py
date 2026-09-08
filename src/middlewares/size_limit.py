from typing import Any, Optional, Dict

from abstractions import MiddlewareLayer
from constants import APIResponseContentType
from constants import ExceptionCode
from constants import HTTPHeader, HTTPStatus
from dtos import IResponseDTO
from dtos import HTTPResponse
from utilities import RequestHeaderUtility


class SizeLimitMiddleware(MiddlewareLayer):
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
        max_bytes: int = 2000000,
        *args: Any,
        **kwargs: Any,
    ) -> None:

        super().__init__(
            urn=urn,
            tenant_id=tenant_id,
            tenant_urn=tenant_urn,
            user_id=user_id,
            user_urn=user_urn,
            api_name=api_name,
            ip_address=ip_address,
            user_agent=user_agent,
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
        self.max_bytes = max_bytes

    async def process(self, request_data: Dict[str, Any], call_next) -> HTTPResponse:
        body_bytes: bytes = request_data.get("body", b"")
        content_length_str = RequestHeaderUtility.get_request_header(
            request_data, HTTPHeader.CONTENT_LENGTH
        )
        content_length = len(body_bytes)

        if content_length_str and content_length_str.isdigit():
            content_length = max(content_length, int(content_length_str))

        if content_length > self.max_bytes:
            envelope = IResponseDTO.failed(
                response_message=f"Payload Too Large: Request body size ({content_length} bytes) exceeds limit of {self.max_bytes} bytes.",
                response_key=ExceptionCode.PAYLOAD_TOO_LARGE,
            )

            return HTTPResponse.build(
                status=HTTPStatus.PAYLOAD_TOO_LARGE,
                headers=[(HTTPHeader.CONTENT_TYPE, APIResponseContentType.APPLICATION_JSON)],
                body={"raw": envelope.to_http_body()},
            )

            return await call_next(request_data)

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "SizeLimitMiddleware"
