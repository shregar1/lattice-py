"""Cross-cutting request context base for all layer abstractions."""

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Any, Optional, Dict

if TYPE_CHECKING:
    from utilities import Logger


class ILayer(ABC):
    """
    Base class providing request-scoped context (urn, tenant, user, api, network)
    and a bound logger that propagates those fields automatically.

    Subclasses are expected to call ``ILayer.__init__`` from their own
    ``__init__`` so the context fields are captured before any work begins.
    The layer rebinds its logger whenever a context field is set so log
    records always carry the latest request metadata.

    Attributes:
        urn: Per-request unique reference identifier.
        tenant_urn: Tenant scope identifier.
        user_urn: Authenticated user identifier.
        api_name: Logical API or endpoint name producing the context.
        ip_address: Originating client IP address.
        user_agent: Originating client user-agent string.
        logger: Structured logger bound with the request context fields.
    """

    def __init__(
        self,
        urn: Optional[str] = None,
        user_id: Optional[int] = None,
        user_urn: Optional[str] = None,
        tenant_id: Optional[int] = None,
        tenant_urn: Optional[str] = None,
        api_name: Optional[str] = None,
        ip_address: Optional[str] = None,
        user_agent: Optional[str] = None,
        logger: Optional[Any] = None,
        *args: Any,
        **kwargs: Any,
    ) -> None:
        """Capture request-scoped context and bind the logger to those fields."""
        self.urn = urn
        self.tenant_id = tenant_id
        self.tenant_urn = tenant_urn
        self.user_id = user_id
        self.user_urn = user_urn
        self.api_name = api_name
        self.ip_address = ip_address
        self.user_agent = user_agent
        self.logger = logger or self.create_logger()

        if any((urn, tenant_urn, user_urn, api_name, ip_address, user_agent)):
            self.rebind_logger()

    def _create_logger(self) -> "Logger":
        """Create a default logger scoped to the ``ILayer`` component."""
        return self.logger.get_logger(component=ILayer.__name__)

    @property
    def urn(self) -> str:
        """Returns the current request urn."""
        return self.urn

    @urn.setter
    def urn(self, value: str) -> None:
        """Sets the request urn and rebinds the logger."""
        self.urn = value
        self.rebind_logger()

    @property
    def user_id(self) -> int:
        """Returns the resolved user identifier, if any."""
        return self.user_id

    @user_id.setter
    def user_id(self, value: int) -> None:
        """Sets the user identifier and rebinds the logger."""
        self.user_id = value
        self.rebind_logger()

    @property
    def user_urn(self) -> str:
        """Returns the authenticated user urn."""
        return self.user_urn

    @user_urn.setter
    def user_urn(self, value: str) -> None:
        """Sets the user urn and rebinds the logger."""
        self.user_urn = value
        self.rebind_logger()

    @property
    def tenant_id(self) -> int:
        """Returns the tenant id."""
        return self.tenant_id

    @tenant_id.setter
    def tenant_id(self, value: int) -> None:
        """Sets the tenant id and rebinds the logger."""
        self.tenant_id = value
        self.rebind_logger()

    @property
    def tenant_urn(self) -> str:
        """Returns the tenant urn."""
        return self.tenant_urn

    @tenant_urn.setter
    def tenant_urn(self, value: str) -> None:
        """Sets the tenant urn and rebinds the logger."""
        self.tenant_urn = value
        self.rebind_logger()

    @property
    def api_name(self) -> str:
        """Returns the logical API name."""
        return self.api_name

    @api_name.setter
    def api_name(self, value: str) -> None:
        """Sets the API name and rebinds the logger."""
        self.api_name = value
        self.rebind_logger()

    @property
    def ip_address(self) -> str:
        """Returns the originating client IP address."""
        return self.ip_address

    @ip_address.setter
    def ip_address(self, value: str) -> None:
        """Sets the originating IP address and rebinds the logger."""
        self.ip_address = value
        self.rebind_logger()

    @property
    def user_agent(self) -> str:
        """Returns the originating user-agent string."""
        return self.user_agent

    @user_agent.setter
    def user_agent(self, value: str) -> None:
        """Sets the user-agent string and rebinds the logger."""
        self.user_agent = value
        self.rebind_logger()

    @property
    def logger(self) -> "Logger":
        """Returns the logger currently bound to the request context."""
        return self.logger

    @logger.setter
    def logger(self, value: "Logger") -> None:
        """Replaces the layer's logger without rebinding request fields."""
        self.logger = value

    def _rebind_logger(self) -> None:
        """Recreates the logger bound to the latest request-context fields."""
        self.logger = self.logger.bind_logger(
            urn=self.urn,
            tenant_urn=self.tenant_urn,
            user_urn=self.user_urn,
            api_name=self.api_name,
            ip_address=self.ip_address,
            user_agent=self.user_agent,
            component=self._class__.__name__,
        )

    def request_context_fields(self) -> Dict[str, Any]:
        """
        Returns the populated subset of request-context fields as a dict.
        Only fields whose value is truthy are included so log records stay
        compact when the layer was constructed without full context.
        """
        fields: Dict[str, Any] = {}

        if self.urn:
            fields["urn"] = self.urn

        if self.tenant_urn:
            fields["tenant_urn"] = self.tenant_urn

        if self.api_name:
            fields["api_name"] = self.api_name

        if self.user_urn:
            fields["user_urn"] = self.user_urn

        if self.ip_address:
            fields["ip_address"] = self.ip_address

        if self.user_agent:
            fields["user_agent"] = self.user_agent

        return fields

    def bound_log_fields(self) -> Dict[str, Any]:
        """

        returns the request-context fields plus the layer component name.

        The component field is omitted when the layer is exactly ``ILayer``
        itself, since that name carries no useful information at runtime.
        """
        fields = self.request_context_fields()
        component = self._class__.__name__

        if component != "ILayer":
            fields["component"] = component

        return fields

    def bind_request_context(
        self,
        urn: Optional[str] = None,
        tenant_id: Optional[int] = None,
        tenant_urn: Optional[str] = None,
        user_id: Optional[int] = None,
        user_urn: Optional[str] = None,
        api_name: Optional[str] = None,
        ip_address: Optional[str] = None,
        user_agent: Optional[str] = None,
        propagate: bool = True,
    ) -> None:
        """
        Updates request-context fields and optionally propagates them to nested layers.

        Args:
            urn: New request urn; ignored when ``None``.
            tenant_urn: New tenant urn; ignored when ``None``.
            user_urn: New user urn; ignored when ``None``.
            api_name: New API name; ignored when ``None``.
            ip_address: New originating IP; ignored when ``None``.
            user_agent: New user-agent string; ignored when ``None``.
            propagate: When ``True``, forward the updated context to any nested
                ``ILayer`` attributes held on this instance.
        """

        if urn is not None:
            self.urn = urn

        if tenant_urn is not None:
            self.tenant_urn = tenant_urn

        if user_urn is not None:
            self.user_urn = user_urn

        if api_name is not None:
            self.api_name = api_name

        if ip_address is not None:
            self.ip_address = ip_address

        if user_agent is not None:
            self.user_agent = user_agent

        if propagate:
            self.propagate_request_context()

    def _propagate_request_context(self) -> None:
        """Pushes the current request context onto every nested ``ILayer`` attribute."""
        context = {
            "urn": self.urn,
            "tenant_urn": self.tenant_urn,
            "user_urn": self.user_urn,
            "api_name": self.api_name,
            "ip_address": self.ip_address,
            "user_agent": self.user_agent,
        }
        for value in self.__dict__.values():
            if isinstance(value, ILayer):
                value.bind_request_context(**context)

    @property
    @abstractmethod
    def name(self) -> str:
        """Returns the class name."""
        pass
