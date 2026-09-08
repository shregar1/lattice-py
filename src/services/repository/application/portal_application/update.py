from exceptions import BadInputException
"""Update portal_application repository service module."""

from datetime import datetime
from rivex import Dependency
from typing import Any, Optional

from abstractions import DTOLayer
from constants import Service
from dtos import UpdatePortalApplicationServiceDTO
from dependencies import CompositePortalApplicationRepositoryDependency, PortalApplicationRepositoryDependency
from repositories import PortalApplicationRepository
from models import PortalApplication
from .abstraction import IPortalApplicationRepositoryService


class UpdatePortalApplicationService(IPortalApplicationRepositoryService):
    """Application service for update operation on portal_application repository."""

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
        portal_application_repository: PortalApplicationRepository = Dependency(PortalApplicationRepositoryDependency),
                composite_portal_application_repository: CompositePortalApplicationRepository = Dependency(CompositePortalApplicationRepositoryDependency),
        *args: Any,
        **kwargs: Any,
    ) -> None:

        self.composite_portal_application_repository = composite_portal_application_repository
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
        self.portal_application_repository = portal_application_repository

    async def run(self, request: UpdatePortalApplicationServiceDTO) -> DTOLayer:
        """Executes update business logic for portal_application."""
        self.logger.info("Executing service run", service=self.name)

        if request.user_id is None or request.tenant_id is None:
            raise BadInputException("user_id and tenant_id are required")

        try:
            if request.id is not None:
                if not self.composite_portal_application_repository.exists_by_id_user_and_tenant(
                    portal_application_id=request.id,
                    user_id=request.user_id,
                    tenant_id=request.tenant_id,
                ):
                    raise BadInputException("Forbidden or resource does not exist for current user and tenant")

            portal_application: PortalApplication = PortalApplication.build(
            code=request.code,
            candidate_id=request.candidate_id,
            job_id=request.job_id,
            is_deleted=request.is_deleted,
            updated_at=datetime.now()
            )

            return self.portal_application_repository.update(model=portal_application)

        except Exception as exc:
            self.logger.error("Service execution failed", service=self.name, error=str(exc), exc=exc)
            raise exc

        finally:
            self.logger.info("Service execution completed", service=self.name)

    @property
    def name(self) -> str:
        """Returns the class name."""
        return Service.UPDATE_PORTAL_APPLICATION_SERVICE
