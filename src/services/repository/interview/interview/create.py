from exceptions import BadInputException
"""Create interview repository service module."""

from datetime import datetime
from rivex import Dependency
from typing import Any, Optional

from abstractions import DTOLayer
from constants import Service
from dtos import CreateInterviewServiceDTO
from dependencies import InterviewRepositoryDependency
from repositories import InterviewRepository
from .abstraction import Interview
from .abstraction import IInterviewRepositoryService


class CreateInterviewService(IInterviewRepositoryService):
    """Application service for create operation on interview repository."""

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
        interview_repository: InterviewRepository = Dependency(InterviewRepositoryDependency),
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
        self.interview_repository = interview_repository

    async def run(self, request: CreateInterviewServiceDTO) -> DTOLayer:
        """Executes create business logic for interview."""
        self.logger.info("Executing service run", service=self.name)

        if request.user_id is None or request.tenant_id is None:
            raise BadInputException("user_id and tenant_id are required")

        try:

            interview: Interview = Interview.build(
            title=request.title,
            starts_at=request.starts_at,
            duration_min=request.duration_min,
            location_id=request.location_id,
            application_id=request.application_id,
            stage_id=request.stage_id,
            type_id=request.type_id,
            status_id=request.status_id,
            is_deleted=request.is_deleted,
            is_active=request.is_active,
            created_at=datetime.now(),
            created_by=request.created_by,
            )

            return self.interview_repository.create(model=interview)

        except Exception as exc:
            self.logger.error("Service execution failed", service=self.name, error=str(exc), exc=exc)
            raise exc

        finally:
            self.logger.info("Service execution completed", service=self.name)

    @property
    def name(self) -> str:
        """Returns the class name."""
        return Service.CREATE_INTERVIEW_SERVICE
