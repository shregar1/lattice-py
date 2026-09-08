from abstractions import ConstantLayer as IConstant
from typing import Final


class Context(IConstant):

    URN: Final[str] = "urn"
    TENANT_URN: Final[str] = "tenant_urn"
    USER_URN: Final[str] = "user_urn"
    API_NAME: Final[str] = "api_name"
    IP_ADDRESS: Final[str] = "ip_address"
    USER_AGENT: Final[str] = "user_agent"
    PROPAGATE: Final[bool] = False

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "Context"
