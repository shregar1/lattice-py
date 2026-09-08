"""Base abstraction for middleware components."""

from abc import abstractmethod
from typing import Any, Dict, Optional
from abstractions import MiddlewareLayer


class IMiddleware(MiddlewareLayer):
    """Base abstraction interface for custom middleware components."""

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

    @abstractmethod
    async def process(self, request_data: Dict[str, Any], call_next: Any) -> Dict[str, Any]:
        """Process an incoming request and delegate to the next callable."""
        pass

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "IMiddleware"
