from exceptions import BadInputException
"""Update scheduling_link_interviewer repository service module."""

from datetime import datetime
from rivex import Dependency
from typing import Any, Optional

from abstractions import DTOLayer
from constants import Service
from dtos import UpdateSchedulingLinkInterviewerServiceDTO
from dependencies import SchedulingLinkInterviewerRepositoryDependency
from repositories import SchedulingLinkInterviewerRepository
from models import SchedulingLinkInterviewer
from .abstraction import ISchedulingLinkInterviewerRepositoryService


class UpdateSchedulingLinkInterviewerService(ISchedulingLinkInterviewerRepositoryService):
    """Application service for update operation on scheduling_link_interviewer repository."""

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
        scheduling_link_interviewer_repository: SchedulingLinkInterviewerRepository = Dependency(SchedulingLinkInterviewerRepositoryDependency),
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
        self.scheduling_link_interviewer_repository = scheduling_link_interviewer_repository

    async def run(self, request: UpdateSchedulingLinkInterviewerServiceDTO) -> DTOLayer:
        """Executes update business logic for scheduling_link_interviewer."""
        self.logger.info("Executing service run", service=self.name)

        if request.user_id is None or request.tenant_id is None:
            raise BadInputException("user_id and tenant_id are required")

        try:

            scheduling_link_interviewer: SchedulingLinkInterviewer = SchedulingLinkInterviewer.build(
            scheduling_link_id=request.scheduling_link_id,
            interviewer_id=request.interviewer_id,
            is_deleted=request.is_deleted,
            updated_at=datetime.now()
            )

            return self.scheduling_link_interviewer_repository.update(model=scheduling_link_interviewer)

        except Exception as exc:
            self.logger.error("Service execution failed", service=self.name, error=str(exc), exc=exc)
            raise exc

        finally:
            self.logger.info("Service execution completed", service=self.name)

    @property
    def name(self) -> str:
        """Returns the class name."""
        return Service.UPDATE_SCHEDULING_LINK_INTERVIEWER_SERVICE
