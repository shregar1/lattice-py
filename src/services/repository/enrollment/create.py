from exceptions import BadInputException
"""Create enrollment repository service module."""

from datetime import datetime
from rivex import Dependency
from typing import Any, Optional

from abstractions import DTOLayer
from constants import Service
from dtos import CreateEnrollmentServiceDTO
from dependencies import EnrollmentRepositoryDependency
from repositories import EnrollmentRepository
from models import Enrollment
from .abstraction import IEnrollmentRepositoryService


class CreateEnrollmentService(IEnrollmentRepositoryService):
    """Application service for create operation on enrollment repository."""

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
        enrollment_repository: EnrollmentRepository = Dependency(EnrollmentRepositoryDependency),
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
        self.enrollment_repository = enrollment_repository

    async def run(self, request: CreateEnrollmentServiceDTO) -> DTOLayer:
        """Executes create business logic for enrollment."""
        self.logger.info("Executing service run", service=self.name)

        if request.user_id is None or request.tenant_id is None:
            raise BadInputException("user_id and tenant_id are required")

        try:

            enrollment: Enrollment = Enrollment.build(
            started_at=request.started_at,
            current_step=request.current_step,
            opens=request.opens,
            last_activity_at=request.last_activity_at,
            campaign_id=request.campaign_id,
            candidate_id=request.candidate_id,
            status_id=request.status_id,
            is_deleted=request.is_deleted,
            is_active=request.is_active,
            created_at=datetime.now(),
            created_by=request.created_by,
            )

            return self.enrollment_repository.create(model=enrollment)

        except Exception as exc:
            self.logger.error("Service execution failed", service=self.name, error=str(exc), exc=exc)
            raise exc

        finally:
            self.logger.info("Service execution completed", service=self.name)

    @property
    def name(self) -> str:
        """Returns the class name."""
        return Service.CREATE_ENROLLMENT_SERVICE
