from exceptions import BadInputException
"""Update activity_type_lk repository service module."""

from datetime import datetime
from rivex import Dependency
from typing import Any, Optional

from abstractions import DTOLayer
from constants import Service
from dtos import UpdateActivityTypeLKServiceDTO
from dependencies import ActivityTypeLKRepositoryDependency
from repositories import ActivityTypeLKRepository
from models import ActivityTypeLK
from .abstraction import IActivityTypeLKRepositoryService


class UpdateActivityTypeLKService(IActivityTypeLKRepositoryService):
    """Application service for update operation on activity_type_lk repository."""

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
        activity_type_lk_repository: ActivityTypeLKRepository = Dependency(ActivityTypeLKRepositoryDependency),
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
        self.activity_type_lk_repository = activity_type_lk_repository

    async def run(self, request: UpdateActivityTypeLKServiceDTO) -> DTOLayer:
        """Executes update business logic for activity_type_lk."""
        self.logger.info("Executing service run", service=self.name)

        if request.user_id is None or request.tenant_id is None:
            raise BadInputException("user_id and tenant_id are required")

        try:

            activity_type_lk: ActivityTypeLK = ActivityTypeLK.build(
            code=request.code,
            label=request.label,
            description=request.description,
            is_deleted=request.is_deleted,
            updated_at=datetime.now()
            )

            return self.activity_type_lk_repository.update(model=activity_type_lk)

        except Exception as exc:
            self.logger.error("Service execution failed", service=self.name, error=str(exc), exc=exc)
            raise exc

        finally:
            self.logger.info("Service execution completed", service=self.name)

    @property
    def name(self) -> str:
        """Returns the class name."""
        return Service.UPDATE_ACTIVITY_TYPE_LK_SERVICE
