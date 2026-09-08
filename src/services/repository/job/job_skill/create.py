from exceptions import BadInputException
"""Create job_skill repository service module."""

from datetime import datetime
from rivex import Dependency
from typing import Any, Optional

from abstractions import DTOLayer
from constants import Service
from dtos import CreateJobSkillServiceDTO
from dependencies import JobSkillRepositoryDependency
from repositories import JobSkillRepository
from models import JobSkill
from .abstraction import IJobSkillRepositoryService


class CreateJobSkillService(IJobSkillRepositoryService):
    """Application service for create operation on job_skill repository."""

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
        job_skill_repository: JobSkillRepository = Dependency(JobSkillRepositoryDependency),
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
        self.job_skill_repository = job_skill_repository

    async def run(self, request: CreateJobSkillServiceDTO) -> DTOLayer:
        """Executes create business logic for job_skill."""
        self.logger.info("Executing service run", service=self.name)

        if request.user_id is None or request.tenant_id is None:
            raise BadInputException("user_id and tenant_id are required")

        try:

            job_skill: JobSkill = JobSkill.build(
            is_required=request.is_required,
            job_id=request.job_id,
            skill_id=request.skill_id,
            is_deleted=request.is_deleted,
            is_active=request.is_active,
            created_at=datetime.now(),
            created_by=request.created_by,
            )

            return self.job_skill_repository.create(model=job_skill)

        except Exception as exc:
            self.logger.error("Service execution failed", service=self.name, error=str(exc), exc=exc)
            raise exc

        finally:
            self.logger.info("Service execution completed", service=self.name)

    @property
    def name(self) -> str:
        """Returns the class name."""
        return Service.CREATE_JOB_SKILL_SERVICE
