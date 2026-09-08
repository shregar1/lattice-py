"""Generic factory abstraction for constructing typed objects."""

from abc import ABC, abstractmethod
from rivex import Dependency
from typing import Any, Generic, Optional, TypeVar

from .abstraction import ILayer
from dependencies import LoggerUtilityDependency
from utilities import Logger

T = TypeVar("T")


class FactoryLayer(ILayer, ABC, Generic[T]):
    """
    Generic factory base that builds instances of type ``T``.

    Subclasses implement :meth:`factory_name` (stable identifier) and
    :meth:`_create_instance` (the actual construction logic). The public
    :meth:`build` delegates to :meth:`_create_instance`.
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
        logger: Logger = Dependency(LoggerUtilityDependency),
        *args: Any,
        **kwargs: Any,
    ) -> None:
        """Initializes the factory with request-scoped context."""


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

    @abstractmethod
    def get_instance(self, key: str, *args: Any, **kwargs: Any) -> T:
        """
        Public entry point that delegates to :meth:`_create_instance`.

        Args:
            *args: Positional arguments forwarded to ``_create_instance``.
            **kwargs: Keyword arguments forwarded to ``_create_instance``.

        returns:
            The newly constructed ``T`` instance.
        """
        pass

    @property
    @abstractmethod
    def name(self) -> str:
        """Returns the layer name that every subclass must define."""
        pass
