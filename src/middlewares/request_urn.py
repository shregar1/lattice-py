from rivex import Dependency
from typing import Any, Optional, Dict
from uuid import UUID

from abstractions import MiddlewareLayer
from constants import Context
from constants import HTTPHeader
from dependencies import MiddlewareUtilityDependency
from dependencies import URNUtilityDependency
from utilities import URNUtility
from utilities import MiddlewareUtility
from utilities import RequestHeaderUtility


class RequestContextMiddleware(MiddlewareLayer):
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
        urn_utility: URNUtility = Dependency(URNUtilityDependency),
        middleware_utility: MiddlewareUtility = Dependency(MiddlewareUtilityDependency),
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
        self.urn_utility: URNUtility = urn_utility
        self.middleware_utility: MiddlewareUtility = middleware_utility

    async def process(self, request_data: Dict[str, Any], call_next) -> Dict[str, Any]:
        """Generate a fresh UUID and propagate ``user_agent`` / ``ip_address`` on the request state."""
        urn: UUID = self.urn_utility.generate_uuid4()
        self.middleware_utility.set_request_state(request_data, Context.URN, str(urn))

        user_agent = (
            RequestHeaderUtility.get_request_header(request_data, HTTPHeader.USER_AGENT)
            or request_data.get("client_user_agent")
            or self.user_agent
        )

        if user_agent:
            self.middleware_utility.set_request_state(request_data, Context.USER_AGENT, user_agent)

        ip_address = (
            request_data.get("client_ip") or request_data.get("ip_address") or self.ip_address
        )

        if ip_address:
            self.middleware_utility.set_request_state(request_data, Context.IP_ADDRESS, ip_address)


        return await call_next(request_data)

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "RequestContextMiddleware"
