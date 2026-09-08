"""Repository for WebhookEndpoint persistence and domain queries."""

from typing import Any, Optional

from rivex import Dependency

from dependencies.model import WebhookEndpointDependency
from dependencies.utility import LoggerUtilityDependency
from models import WebhookEndpoint
from utilities import Logger

from ..abstraction import IAtomicRepository


class WebhookEndpointRepository(IAtomicRepository[WebhookEndpoint, int]):
    """Atomic repository for WebhookEndpoint."""

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
        model: type[WebhookEndpoint] = Dependency(WebhookEndpointDependency),
        *args: Any,
        **kwargs: Any,
    ) -> None:
        if model is None:
            logger.error("No model found")
            raise ModuleNotFoundError("No model found")

        IAtomicRepository.__init__(
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
            **kwargs,
        )
        self.model = model
        self.model_class = model

    def exists_by_id_user_and_tenant(self, entity_id: int, user_id: int, tenant_id: int) -> bool:
        """Verifies tenant-scoped record existence (IDOR guard)."""
        return self.model.exists(id=entity_id, tenant_id=tenant_id)

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "WebhookEndpointRepository"
