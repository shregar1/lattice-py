from exceptions import BadInputException
"""Create sourced_profile repository service module."""

from datetime import datetime
from rivex import Dependency
from typing import Any, Optional

from abstractions import DTOLayer
from constants import Service
from dtos import CreateSourcedProfileServiceDTO
from dependencies import SourcedProfileRepositoryDependency
from repositories import SourcedProfileRepository
from models import SourcedProfile
from .abstraction import ISourcedProfileRepositoryService


class CreateSourcedProfileService(ISourcedProfileRepositoryService):
    """Application service for create operation on sourced_profile repository."""

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
        sourced_profile_repository: SourcedProfileRepository = Dependency(SourcedProfileRepositoryDependency),
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
        self.sourced_profile_repository = sourced_profile_repository

    async def run(self, request: CreateSourcedProfileServiceDTO) -> DTOLayer:
        """Executes create business logic for sourced_profile."""
        self.logger.info("Executing service run", service=self.name)

        if request.user_id is None or request.tenant_id is None:
            raise BadInputException("user_id and tenant_id are required")

        try:

            sourced_profile: SourcedProfile = SourcedProfile.build(
            label=request.label,
            headline=request.headline,
            location_id=request.location_id,
            match_score=request.match_score,
            reasoning=request.reasoning,
            added_to_pool=request.added_to_pool,
            is_deleted=request.is_deleted,
            is_active=request.is_active,
            created_at=datetime.now(),
            created_by=request.created_by,
            )

            return self.sourced_profile_repository.create(model=sourced_profile)

        except Exception as exc:
            self.logger.error("Service execution failed", service=self.name, error=str(exc), exc=exc)
            raise exc

        finally:
            self.logger.info("Service execution completed", service=self.name)

    @property
    def name(self) -> str:
        """Returns the class name."""
        return Service.CREATE_SOURCED_PROFILE_SERVICE
