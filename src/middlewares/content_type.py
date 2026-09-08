from rivex import Dependency
from typing import Any, Optional, Dict

from abstractions import MiddlewareLayer
from constants import APIResponseContentType
from constants import ExceptionCode
from constants import HTTPHeader, HTTPMethod, HTTPStatus
from dependencies import RequestHeaderUtilityDependency
from .abstraction import IResponseDTO
from dtos import HTTPResponse
from utilities import RequestHeaderUtility


class ContentTypeValidationMiddleware(MiddlewareLayer):
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
        request_header_utility: RequestHeaderUtility = Dependency(RequestHeaderUtilityDependency),
        *args: Any,
        **kwargs: Any,
    ) -> None:
        MiddlewareLayer.__init__(
            self,
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
        self.request_header_utility: RequestHeaderUtility = request_header_utility

    async def process(self, request_data: Dict[str, Any], call_next) -> Dict[str, Any]:
        method: str = request_data.get("method", HTTPMethod.GET).upper()
        path: str = request_data.get("path", "")

        if method in {HTTPMethod.POST, HTTPMethod.PUT, HTTPMethod.PATCH} and path != "/health":
            content_type = self.request_header_utility.get_request_header(
                request_data, HTTPHeader.CONTENT_TYPE
            )
            if not content_type or APIResponseContentType.APPLICATION_JSON not in content_type.lower():
                envelope = IResponseDTO.failed(
                    response_message=f"Unsupported Media Type: Method {method} requires '{HTTPHeader.CONTENT_TYPE}: {APIResponseContentType.APPLICATION_JSON}'. Got '{content_type}'.",
                    response_key=ExceptionCode.UNSUPPORTED_MEDIA_TYPE,
                )
                return HTTPResponse(
                    status=HTTPStatus.UNSUPPORTED_MEDIA_TYPE,
                    headers=[(HTTPHeader.CONTENT_TYPE, APIResponseContentType.APPLICATION_JSON)],
                    body=envelope.to_http_body(),
                )

        return await call_next(request_data)

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "ContentTypeValidationMiddleware"
