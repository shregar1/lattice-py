from exceptions import BadInputException
"""Update scheduling_link repository service module."""

from datetime import datetime
from rivex import Dependency
from typing import Any, Optional

from abstractions import DTOLayer
from constants import Service
from dtos import UpdateSchedulingLinkServiceDTO
from dependencies import SchedulingLinkRepositoryDependency
from repositories import SchedulingLinkRepository
from models import SchedulingLink
from .abstraction import ISchedulingLinkRepositoryService


class UpdateSchedulingLinkService(ISchedulingLinkRepositoryService):
    """Application service for update operation on scheduling_link repository."""

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
        scheduling_link_repository: SchedulingLinkRepository = Dependency(SchedulingLinkRepositoryDependency),
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
        self.scheduling_link_repository = scheduling_link_repository

    async def run(self, request: UpdateSchedulingLinkServiceDTO) -> DTOLayer:
        """Executes update business logic for scheduling_link."""
        self.logger.info("Executing service run", service=self.name)

        if request.user_id is None or request.tenant_id is None:
            raise BadInputException("user_id and tenant_id are required")

        try:

            scheduling_link: SchedulingLink = SchedulingLink.build(
            title=request.title,
            duration_min=request.duration_min,
            slug=request.slug,
            booked_at=request.booked_at,
            candidate_id=request.candidate_id,
            job_id=request.job_id,
            stage_id=request.stage_id,
            status_id=request.status_id,
            is_deleted=request.is_deleted,
            updated_at=datetime.now()
            )

            return self.scheduling_link_repository.update(model=scheduling_link)

        except Exception as exc:
            self.logger.error("Service execution failed", service=self.name, error=str(exc), exc=exc)
            raise exc

        finally:
            self.logger.info("Service execution completed", service=self.name)

    @property
    def name(self) -> str:
        """Returns the class name."""
        return Service.UPDATE_SCHEDULING_LINK_SERVICE
