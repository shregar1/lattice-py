from exceptions import BadInputException
"""Create job_role_level_lk repository service module."""

from datetime import datetime
from rivex import Dependency
from typing import Any, Optional

from abstractions import DTOLayer
from constants import Service
from dtos import CreateJobRoleLevelLKServiceDTO
from dependencies import JobRoleLevelLKRepositoryDependency
from repositories import JobRoleLevelLKRepository
from models import JobRoleLevelLK
from .abstraction import IJobRoleLevelLKRepositoryService


class CreateJobRoleLevelLKService(IJobRoleLevelLKRepositoryService):
    """Application service for create operation on job_role_level_lk repository."""

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
        job_role_level_lk_repository: JobRoleLevelLKRepository = Dependency(JobRoleLevelLKRepositoryDependency),
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
        self.job_role_level_lk_repository = job_role_level_lk_repository

    async def run(self, request: CreateJobRoleLevelLKServiceDTO) -> DTOLayer:
        """Executes create business logic for job_role_level_lk."""
        self.logger.info("Executing service run", service=self.name)

        if request.user_id is None or request.tenant_id is None:
            raise BadInputException("user_id and tenant_id are required")

        try:

            job_role_level_lk: JobRoleLevelLK = JobRoleLevelLK.build(
            code=request.code,
            label=request.label,
            description=request.description,
            is_deleted=request.is_deleted,
            is_active=request.is_active,
            created_at=datetime.now(),
            created_by=request.created_by,
            )

            return self.job_role_level_lk_repository.create(model=job_role_level_lk)

        except Exception as exc:
            self.logger.error("Service execution failed", service=self.name, error=str(exc), exc=exc)
            raise exc

        finally:
            self.logger.info("Service execution completed", service=self.name)

    @property
    def name(self) -> str:
        """Returns the class name."""
        return Service.CREATE_JOB_ROLE_LEVEL_LK_SERVICE
