"""Base class for business-logic services."""

from abc import abstractmethod
from rivex import Dependency
from typing import Any, Optional

from .abstraction import ILayer
from abstractions import DTOLayer

from dependencies import LoggerUtilityDependency
from utilities import Logger


class ServiceLayer(ILayer):
    """
    Base class for application services that implement a single use case.

    A service is wired with the repositories, utilities and sessions it
    needs and exposes one async :meth:`run` entrypoint that maps a
    ``TRequest`` DTO to a ``TResponse`` DTO.

    Attributes:
        repositories: Repositories the service may invoke.
        utilities: Auxiliary utilities the service may invoke.
        db_sessions: Database sessions shared across the service's calls.
        cache_sessions: Cache sessions shared across the service's calls.
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
        """Stores wired dependencies plus request-scoped context."""


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
    async def run(self, request: DTOLayer) -> DTOLayer:
        """
        Executes the service's business logic.

        Args:
            request: Validated DTO carrying the service's input.


        returns:
            The DTO produced by the service.
        """
    @property
    @abstractmethod
    def name(self) -> str:
        """Returns the class name."""
        pass
