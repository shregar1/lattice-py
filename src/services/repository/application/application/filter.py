from exceptions import BadInputException
"""Filter application repository service module."""

from datetime import datetime
from rivex import Dependency
from typing import Any, Optional

from abstractions import DTOLayer
from constants import Service
from dtos import FilterApplicationServiceDTO
from dependencies import CompositeApplicationRepositoryDependency, ApplicationRepositoryDependency
from repositories import ApplicationRepository
from .abstraction import IApplicationRepositoryService


class FilterApplicationService(IApplicationRepositoryService):
    """Application service for filter operation on application repository."""

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
        application_repository: ApplicationRepository = Dependency(ApplicationRepositoryDependency),
                composite_application_repository: CompositeApplicationRepository = Dependency(CompositeApplicationRepositoryDependency),
        *args: Any,
        **kwargs: Any,
    ) -> None:

        self.composite_application_repository = composite_application_repository
        super().__init__(
            urn=urn,
            user_urn=user_urn,
            user_id=user_id,
            tenant_urn=tenant_urn,
            tenant_id=tenant_id,
            api_name=api_name,
            ip_address=ip_address,
            user_agent=user_agent,
            *args,
            **kwargs,
        )
        self.application_repository = application_repository

    async def run(self, request: FilterApplicationServiceDTO) -> DTOLayer:
        """Executes filter business logic for application."""
        self.logger.info("Executing service run", service=self.name)

        if request.user_id is None or request.tenant_id is None:
            raise BadInputException("user_id and tenant_id are required")

        try:
            return self.composite_application_repository.filter_by_user_and_tenant(
                user_id=request.user_id,
                tenant_id=request.tenant_id,
            )
        except Exception as exc:
            self.logger.error("Service execution failed", service=self.name, error=str(exc), exc=exc)
            raise exc

        finally:
            self.logger.info("Service execution completed", service=self.name)

    @property
    def name(self) -> str:
        """Returns the class name."""
        return Service.FILTER_APPLICATION_SERVICE
