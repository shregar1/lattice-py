from exceptions import BadInputException
from constants import DBColumn
"""Delete activity repository service module."""

from datetime import datetime
from rivex import Dependency
from typing import Any, Optional

from abstractions import DTOLayer
from constants import Service
from dtos import DeleteActivityInputDTO, DeleteActivityOutputDTO
from dependencies import ActivityRepositoryDependency, CompositeActivityRepositoryDependency
from repositories import ActivityRepository, CompositeActivityRepository
from models import Activity
from .abstraction import IActivityRepositoryService


class DeleteActivityService(IActivityRepositoryService):
    """Application service for delete operation on activity repository."""

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

    async def run(self, request: DeleteActivityInputDTO) -> DeleteActivityOutputDTO:
        """Executes delete business logic for record."""
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
            if request.id:
                if request.is_hard_delete:
                    self.activity_repository.hard_delete(id=request.id)
                else:
                    self.activity_repository.soft_delete(id=request.id)
                return DeleteActivityOutputDTO.build(
                    urn=request.urn,
                    deleted_at=datetime.now(),
                    success=True,
                )
            return DeleteActivityOutputDTO.build(success=False)
        except Exception as exc:
            self.logger.error("Service execution failed", service=self.name, error=str(exc), exc=exc)
            raise exc

        finally:
            self.logger.info("Service execution completed", service=self.name)

    @property
    def name(self) -> str:
        """Returns the class name."""
        return Service.DELETE_ACTIVITY_SERVICE
