from exceptions import BadInputException
"""Create candidate_location repository service module."""

from datetime import datetime
from rivex import Dependency
from typing import Any, Optional

from abstractions import DTOLayer
from constants import Service
from dtos import CreateCandidateLocationServiceDTO
from dependencies import CandidateLocationRepositoryDependency
from repositories import CandidateLocationRepository
from models import CandidateLocation
from .abstraction import ICandidateLocationRepositoryService


class CreateCandidateLocationService(ICandidateLocationRepositoryService):
    """Application service for create operation on candidate_location repository."""

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
        candidate_location_repository: CandidateLocationRepository = Dependency(CandidateLocationRepositoryDependency),
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
        self.candidate_location_repository = candidate_location_repository

    async def run(self, request: CreateCandidateLocationServiceDTO) -> DTOLayer:
        """Executes create business logic for candidate_location."""
        self.logger.info("Executing service run", service=self.name)

        if request.user_id is None or request.tenant_id is None:
            raise BadInputException("user_id and tenant_id are required")

        try:

            candidate_location: CandidateLocation = CandidateLocation.build(
            is_current=request.is_current,
            candidate_id=request.candidate_id,
            location_id=request.location_id,
            is_deleted=request.is_deleted,
            is_active=request.is_active,
            created_at=datetime.now(),
            created_by=request.created_by,
            )

            return self.candidate_location_repository.create(model=candidate_location)

        except Exception as exc:
            self.logger.error("Service execution failed", service=self.name, error=str(exc), exc=exc)
            raise exc

        finally:
            self.logger.info("Service execution completed", service=self.name)

    @property
    def name(self) -> str:
        """Returns the class name."""
        return Service.CREATE_CANDIDATE_LOCATION_SERVICE
