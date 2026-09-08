from rivex import Dependency
from typing import Any, Optional, Dict

from abstractions import MiddlewareLayer
from dependencies import URNUtilityDependency
from utilities import URNUtility


class TracingMiddleware(MiddlewareLayer):
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
        trace_header_name: str = "traceparent",
        urn_utility: URNUtility = Dependency(URNUtilityDependency),
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
        self.trace_header_name: str = trace_header_name
        self.urn_utility: URNUtility = urn_utility

    async def process(self, request_data: Dict[str, Any], call_next) -> Dict[str, Any]:
        headers = dict(request_data.get("headers", []))
        incoming_trace = headers.get(self.trace_header_name) or headers.get(
            self.trace_header_name.lower()
        )

        if not incoming_trace:
            trace_id = self.urn_utility.generate_uuid4().hex
            span_id = self.urn_utility.generate_uuid4().hex
            traceparent = f"00-{trace_id}-{span_id}-01"
        else:
            traceparent = incoming_trace
        response: Dict[str, Any] = await call_next(request_data)
        response["headers"] = response.get("headers", []) + [(self.trace_header_name, traceparent)]

        return response

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "TracingMiddleware"
