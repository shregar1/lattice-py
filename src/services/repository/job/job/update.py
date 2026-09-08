from exceptions import BadInputException
"""Update job repository service module."""

from datetime import datetime
from rivex import Dependency
from typing import Any, Optional

from abstractions import DTOLayer
from constants import Service
from dtos import UpdateJobServiceDTO
from dependencies import JobRepositoryDependency
from repositories import JobRepository
from models import Job
from .abstraction import IJobRepositoryService


class UpdateJobService(IJobRepositoryService):
    """Application service for update operation on job repository."""

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

    async def run(self, request: UpdateJobServiceDTO) -> DTOLayer:
        """Executes update business logic for job."""
        self.logger.info("Executing service run", service=self.name)

        if request.user_id is None or request.tenant_id is None:
            raise BadInputException("user_id and tenant_id are required")

        try:
            if request.id and not self.job_repository.exists_by_id_and_tenant(
                job_id=request.id,
                tenant_id=request.tenant_id,
            ):
                from exceptions import ForbiddenException
                raise ForbiddenException("User does not have permission to update this job record.")

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
                updated_at=datetime.now()
            )

            return self.job_repository.update(model=job)

        except Exception as exc:
            self.logger.error("Service execution failed", service=self.name, error=str(exc), exc=exc)
            raise exc

        finally:
            self.logger.info("Service execution completed", service=self.name)

    @property
    def name(self) -> str:
        """Returns the class name."""
        return Service.UPDATE_JOB_SERVICE
