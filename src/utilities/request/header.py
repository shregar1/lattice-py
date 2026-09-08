from typing import Any, Dict, Optional

from constants import Encoding
from constants import Utility
from .abstraction import IRequestUtility


class RequestHeaderUtility(IRequestUtility):
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

    @staticmethod
    def get_request_header(request_data: Dict[str, Any], header_name: str) -> Optional[str]:
        headers = request_data.get("headers", [])
        header_name_lower = header_name.lower()

        if isinstance(headers, dict):
            for k, v in headers.items():
                if str(k).lower() == header_name_lower:
                    return str(v)
            return None

        for item in headers:
            if isinstance(item, (tuple, list)) and len(item) >= 2:
                k, v = (item[0], item[1])
                if isinstance(k, bytes):
                    k = k.decode(Encoding.UTF8)
                if isinstance(v, bytes):
                    v = v.decode(Encoding.UTF8)
                if str(k).lower() == header_name_lower:
                    return str(v)
            elif isinstance(item, dict):
                for k, v in item.items():
                    if str(k).lower() == header_name_lower:
                        return str(v)

        return None
    @property
    def name(self) -> str:
        """Returns the class name."""
        return Utility.REQUEST_HEADER
