from typing import Any, Optional, Dict

from abstractions import MiddlewareLayer
from constants import Middleware


class SecurityHeadersMiddleware(MiddlewareLayer):
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
        *args: Any,
        **kwargs: Any,
    ) -> None:
        MiddlewareLayer.__init__(
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

    async def process(self, request_data: Dict[str, Any], call_next) -> Dict[str, Any]:
        response: Dict[str, Any] = await call_next(request_data)
        response["headers"] = response.get("headers", []) + Middleware.SECURITY_HEADERS

        return response

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "SecurityHeadersMiddleware"
