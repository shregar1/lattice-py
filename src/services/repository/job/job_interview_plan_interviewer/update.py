from exceptions import BadInputException
"""Update job_interview_plan_interviewer repository service module."""

from datetime import datetime
from rivex import Dependency
from typing import Any, Optional

from abstractions import DTOLayer
from constants import Service
from dtos import UpdateJobInterviewPlanInterviewerServiceDTO
from dependencies import JobInterviewPlanInterviewerRepositoryDependency
from repositories import JobInterviewPlanInterviewerRepository
from models import JobInterviewPlanInterviewer
from .abstraction import IJobInterviewPlanInterviewerRepositoryService


class UpdateJobInterviewPlanInterviewerService(IJobInterviewPlanInterviewerRepositoryService):
    """Application service for update operation on job_interview_plan_interviewer repository."""

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
        job_interview_plan_interviewer_repository: JobInterviewPlanInterviewerRepository = Dependency(JobInterviewPlanInterviewerRepositoryDependency),
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
        self.job_interview_plan_interviewer_repository = job_interview_plan_interviewer_repository

    async def run(self, request: UpdateJobInterviewPlanInterviewerServiceDTO) -> DTOLayer:
        """Executes update business logic for job_interview_plan_interviewer."""
        self.logger.info("Executing service run", service=self.name)

        if request.user_id is None or request.tenant_id is None:
            raise BadInputException("user_id and tenant_id are required")

        try:

            job_interview_plan_interviewer: JobInterviewPlanInterviewer = JobInterviewPlanInterviewer.build(
            plan_item_id=request.plan_item_id,
            interviewer_id=request.interviewer_id,
            is_deleted=request.is_deleted,
            updated_at=datetime.now()
            )

            return self.job_interview_plan_interviewer_repository.update(model=job_interview_plan_interviewer)

        except Exception as exc:
            self.logger.error("Service execution failed", service=self.name, error=str(exc), exc=exc)
            raise exc

        finally:
            self.logger.info("Service execution completed", service=self.name)

    @property
    def name(self) -> str:
        """Returns the class name."""
        return Service.UPDATE_JOB_INTERVIEW_PLAN_INTERVIEWER_SERVICE
