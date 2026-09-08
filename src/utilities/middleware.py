from rivex import Dependency
from typing import Any, Dict, Optional

from dependencies import LoggerUtilityDependency
from .abstraction import IUtility
from utilities import Logger


class MiddlewareUtility(IUtility):
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
    def set_request_header(request_data: Dict[str, Any], name: str, value: str) -> None:
        headers = list(request_data.get("headers", []))
        lowered = name.lower()
        headers = [(key, val) for key, val in headers if key.lower() != lowered]
        headers.append((name, value))
        request_data["headers"] = headers

    @staticmethod
    def set_request_state(request_data: Dict[str, Any], key: str, value: Any) -> None:
        state = request_data.setdefault("state", {})
        state[key] = value

    @staticmethod
    def get_request_state(request_data: Dict[str, Any], key: str, default: Any = None) -> Any:
        state = request_data.get("state", {})

        return state.get(key, default)

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "MiddlewareUtility"
