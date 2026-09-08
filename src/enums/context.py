"""context enum module."""

from enum import Enum
from abstractions import EnumLayer
from constants import Context


class ContextENUM(EnumLayer):
    URN = Context.URN
    TENANT_URN = Context.TENANT_URN
    USER_URN = Context.USER_URN
    API_NAME = Context.API_NAME
    IP_ADDRESS = Context.IP_ADDRESS
    USER_AGENT = Context.USER_AGENT
    PROPAGATE = Context.PROPAGATE

    @property
    def name(self) -> str:
        """Returns the layer name."""
        return "ContextENUM"

