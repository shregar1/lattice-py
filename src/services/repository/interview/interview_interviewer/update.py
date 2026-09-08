from exceptions import BadInputException
"""Update interview_interviewer repository service module."""

from datetime import datetime
from rivex import Dependency
from typing import Any, Optional

from abstractions import DTOLayer
from constants import Service
from dtos import UpdateInterviewInterviewerServiceDTO
from dependencies import InterviewInterviewerRepositoryDependency
from repositories import InterviewInterviewerRepository
from .abstraction import InterviewInterviewer
from .abstraction import IInterviewInterviewerRepositoryService


class UpdateInterviewInterviewerService(IInterviewInterviewerRepositoryService):
    """Application service for update operation on interview_interviewer repository."""

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
        interview_interviewer_repository: InterviewInterviewerRepository = Dependency(InterviewInterviewerRepositoryDependency),
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
        self.interview_interviewer_repository = interview_interviewer_repository

    async def run(self, request: UpdateInterviewInterviewerServiceDTO) -> DTOLayer:
        """Executes update business logic for interview_interviewer."""
        self.logger.info("Executing service run", service=self.name)

        if request.user_id is None or request.tenant_id is None:
            raise BadInputException("user_id and tenant_id are required")

        try:

            interview_interviewer: InterviewInterviewer = InterviewInterviewer.build(
            interview_id=request.interview_id,
            interviewer_id=request.interviewer_id,
            is_deleted=request.is_deleted,
            updated_at=datetime.now()
            )

            return self.interview_interviewer_repository.update(model=interview_interviewer)

        except Exception as exc:
            self.logger.error("Service execution failed", service=self.name, error=str(exc), exc=exc)
            raise exc

        finally:
            self.logger.info("Service execution completed", service=self.name)

    @property
    def name(self) -> str:
        """Returns the class name."""
        return Service.UPDATE_INTERVIEW_INTERVIEWER_SERVICE
