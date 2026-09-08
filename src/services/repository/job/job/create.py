from exceptions import BadInputException
"""Create job repository service module."""

from datetime import datetime
from rivex import Dependency
from typing import Any, Optional

from abstractions import DTOLayer
from constants import Service
from dtos import CreateJobServiceDTO
from dependencies import JobRepositoryDependency
from repositories import JobRepository
from models import Job
from .abstraction import IJobRepositoryService


class CreateJobService(IJobRepositoryService):
    """Application service for create operation on job repository."""

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
        job_repository: JobRepository = Dependency(JobRepositoryDependency),
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
        self.job_repository = job_repository

    async def run(self, request: CreateJobServiceDTO) -> DTOLayer:
        """Executes create business logic for job."""
        self.logger.info("Executing service run", service=self.name)

        if request.user_id is None or request.tenant_id is None:
            raise BadInputException("user_id and tenant_id are required")

        try:

            job: Job = Job.build(
            title=request.title,
            department=request.department,
            description=request.description,
            openings=request.openings,
            job_role_id=request.job_role_id,
            job_role_level_id=request.job_role_level_id,
            currency_id=request.currency_id,
            salary_min=request.salary_min,
            salary_max=request.salary_max,
            posted_at=request.posted_at,
            hiring_manager_id=request.hiring_manager_id,
            recruiter_id=request.recruiter_id,
            status_id=request.status_id,
            domain_id=request.domain_id,
            employment_config_id=request.employment_config_id,
            is_deleted=request.is_deleted,
            is_active=request.is_active,
            created_at=datetime.now(),
            created_by=request.created_by,
            )

            return self.job_repository.create(model=job)

        except Exception as exc:
            self.logger.error("Service execution failed", service=self.name, error=str(exc), exc=exc)
            raise exc

        finally:
            self.logger.info("Service execution completed", service=self.name)

    @property
    def name(self) -> str:
        """Returns the class name."""
        return Service.CREATE_JOB_SERVICE
