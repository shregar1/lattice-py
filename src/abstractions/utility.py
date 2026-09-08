"""Base class for cross-cutting utility services."""

from abc import abstractmethod
from typing import Any, Optional

from .abstraction import ILayer


class UtilityLayer(ILayer):
    """
    Base class for stateless utility services such as crypto, hashing and JWT.

    Subclasses must implement :meth:`name` (a stable identifier used by the
    utility factory). On subclass creation, every coroutine method that is
    not already wrapped is automatically decorated with the timing helper so
    slow utilities are logged uniformly.
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
        """Initializes the utility with request-scoped context."""

        if logger is None:
            raise RuntimeError("Logger not configured")


        ILayer.__init__(
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

    @property
    @abstractmethod
    def name(self) -> str:
        """Returns the class name."""
        pass
