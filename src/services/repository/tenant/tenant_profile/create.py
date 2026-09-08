from exceptions import BadInputException
"""Create tenant_profile repository service module."""

from datetime import datetime
from rivex import Dependency
from typing import Any, Optional

from abstractions import DTOLayer
from constants import Service
from dtos import CreateTenantProfileServiceDTO
from dependencies import TenantProfileRepositoryDependency
from repositories import TenantProfileRepository
from models import TenantProfile
from .abstraction import ITenantProfileRepositoryService


class CreateTenantProfileService(ITenantProfileRepositoryService):
    """Application service for create operation on tenant_profile repository."""

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
        tenant_profile_repository: TenantProfileRepository = Dependency(TenantProfileRepositoryDependency),
        *args: Any,
        **kwargs: Any,
    ) -> None:

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
        self.tenant_profile_repository = tenant_profile_repository

    async def run(self, request: CreateTenantProfileServiceDTO) -> DTOLayer:
        """Executes create business logic for tenant_profile."""
        self.logger.info("Executing service run", service=self.name)

        if request.user_id is None or request.tenant_id is None:
            raise BadInputException("user_id and tenant_id are required")

        try:

            tenant_profile: TenantProfile = TenantProfile.build(
            label=request.label,
            logo_url=request.logo_url,
            website=request.website,
            industry=request.industry,
            description=request.description,
            is_deleted=request.is_deleted,
            is_active=request.is_active,
            created_at=datetime.now(),
            created_by=request.created_by,
            )

            return self.tenant_profile_repository.create(model=tenant_profile)

        except Exception as exc:
            self.logger.error("Service execution failed", service=self.name, error=str(exc), exc=exc)
            raise exc

        finally:
            self.logger.info("Service execution completed", service=self.name)

    @property
    def name(self) -> str:
        """Returns the class name."""
        return Service.CREATE_TENANT_PROFILE_SERVICE
