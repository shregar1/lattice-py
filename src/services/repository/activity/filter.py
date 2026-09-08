from exceptions import BadInputException
"""Filter activity repository service module."""

from datetime import datetime
from rivex import Dependency
from typing import Any, Optional

from abstractions import DTOLayer
from constants import Service
from dtos import ActivityDTO, FilterActivityInputDTO, FilterActivityOutputDTO
from dependencies import ActivityRepositoryDependency, CompositeActivityRepositoryDependency
from repositories import ActivityRepository, CompositeActivityRepository
from models import Activity
from .abstraction import IActivityRepositoryService


class FilterActivityService(IActivityRepositoryService):
    """Application service for filter operation on activity repository."""

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
        activity_repository: ActivityRepository = Dependency(ActivityRepositoryDependency),
        composite_activity_repository: CompositeActivityRepository = Dependency(CompositeActivityRepositoryDependency),
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
        self.activity_repository = activity_repository
        self.composite_activity_repository = composite_activity_repository

    async def run(self, request: FilterActivityInputDTO) -> FilterActivityOutputDTO:
        """Executes filter business logic for activity."""
        self.logger.info("Executing service run", service=self.name)

        if request.user_id is None or request.tenant_id is None:
            raise BadInputException("user_id and tenant_id are required")

        try:
            records = self.composite_activity_repository.filter_by_user_and_tenant(
                user_id=request.user_id,
                tenant_id=request.tenant_id,
            )
            activity_dtos = [
                ActivityDTO.build(
                    urn=str(getattr(item, "urn", "")) if getattr(item, "urn", None) else None,
                    activity_type_code=str(getattr(item, "activity_type_code", getattr(item, "activity_type_id", ""))),
                    description=item.description,
                    candidate_urn=str(getattr(item, "candidate_urn", "")) if getattr(item, "candidate_urn", None) else None,
                    job_urn=str(getattr(item, "job_urn", "")) if getattr(item, "job_urn", None) else None,
                )
                for item in records
            ]
            return FilterActivityOutputDTO.build(activities=activity_dtos)
        except Exception as exc:
            self.logger.error("Service execution failed", service=self.name, error=str(exc), exc=exc)
            raise exc

        finally:
            self.logger.info("Service execution completed", service=self.name)

    @property
    def name(self) -> str:
        """Returns the class name."""
        return Service.FILTER_ACTIVITY_SERVICE
