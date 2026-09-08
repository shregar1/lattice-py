from exceptions import BadInputException
"""Update activity repository service module."""

from datetime import datetime
from rivex import Dependency
from typing import Any, Optional

from abstractions import DTOLayer
from constants import Service
from dtos import UpdateActivityInputDTO
from dependencies import ActivityRepositoryDependency, CompositeActivityRepositoryDependency
from repositories import ActivityRepository, CompositeActivityRepository
from models import Activity
from .abstraction import IActivityRepositoryService


class UpdateActivityService(IActivityRepositoryService):
    """Application service for update operation on activity repository."""

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

    async def run(self, request: UpdateActivityInputDTO) -> DTOLayer:
        """Executes update business logic for activity."""
        self.logger.info("Executing service run", service=self.name)

        if request.user_id is None or request.tenant_id is None:
            raise BadInputException("user_id and tenant_id are required")

        try:
            if request.id is not None:
                if not self.composite_activity_repository.exists_by_id_user_and_tenant(
                    activity_id=request.id,
                    user_id=request.user_id,
                    tenant_id=request.tenant_id,
                ):
                    raise BadInputException("Forbidden or resource does not exist for current user and tenant")

            activity: Activity = Activity.build(
            user_id=request.user_id,
            activity_type_id=request.activity_type_id,
            candidate_id=request.candidate_id,
            job_id=request.job_id,
            description=request.description,
            is_deleted=request.is_deleted,
            updated_at=datetime.now()
            )

            return self.activity_repository.update(model=activity)

        except Exception as exc:
            self.logger.error("Service execution failed", service=self.name, error=str(exc), exc=exc)
            raise exc

        finally:
            self.logger.info("Service execution completed", service=self.name)

    @property
    def name(self) -> str:
        """Returns the class name."""
        return Service.UPDATE_ACTIVITY_SERVICE
