"""Orchestrator abstraction that composes services around a request/response pair."""

from abc import abstractmethod
from typing import Any, Optional

from .abstraction import ILayer
from .dto import DTOLayer


class OrchestratorLayer(ILayer):
    """
    Base class for orchestrators that coordinate one or more services to
    fulfil a single request.

    Orchestrators are typically the only place where cross-service workflows
    and shared sessions are stitched together. They expose a single async
    :meth:`execute` entrypoint that maps a ``TRequest`` to a ``TResponse``.

    Attributes:
        services: Optional list of services the orchestrator may invoke.
        cache_sessions: Optional list of cache sessions shared across services.
    """

    def __init__(
        self,
        urn: str,
        tenant_id: Optional[int] = None,
        tenant_urn: Optional[str] = None,
        user_id: Optional[int] = None,
        user_urn: Optional[str] = None,
        api_name: Optional[str] = None,
        ip_address: Optional[str] = None,
        user_agent: Optional[str] = None,
        logger: Optional[Any] = None,
        *args: Any,
        **kwargs: Any,
    ) -> None:
        """Stores the wired services and cache sessions plus request context."""
    

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
    async def execute(self, request: DTOLayer) -> DTOLayer:
        """
        Runs the orchestrated workflow for ``request``.

        Args:
            request: Validated DTO carrying the orchestrator's input.

        returns:
            The DTO produced by the orchestrator's workflow.
        """
        pass

    @property
    @abstractmethod
    def name(self) -> str:
        """Returns the layer name that every subclass must define."""
        pass
