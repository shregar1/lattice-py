from exceptions import BadInputException
"""Create requisition repository service module."""

from datetime import datetime
from rivex import Dependency
from typing import Any, Optional

from abstractions import DTOLayer
from constants import Service
from dtos import CreateRequisitionServiceDTO
from dependencies import RequisitionRepositoryDependency
from repositories import RequisitionRepository
from models import Requisition
from .abstraction import IRequisitionRepositoryService


class CreateRequisitionService(IRequisitionRepositoryService):
    """Application service for create operation on requisition repository."""

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
        requisition_repository: RequisitionRepository = Dependency(RequisitionRepositoryDependency),
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
        self.requisition_repository = requisition_repository

    async def run(self, request: CreateRequisitionServiceDTO) -> DTOLayer:
        """Executes create business logic for requisition."""
        self.logger.info("Executing service run", service=self.name)

        if request.user_id is None or request.tenant_id is None:
            raise BadInputException("user_id and tenant_id are required")

        try:

            requisition: Requisition = Requisition.build(
            title=request.title,
            department=request.department,
            openings=request.openings,
            salary_min=request.salary_min,
            salary_max=request.salary_max,
            justification=request.justification,
            requested_by_id=request.requested_by_id,
            status_id=request.status_id,
            domain_id=request.domain_id,
            location_id=request.location_id,
            currency_id=request.currency_id,
            employment_config_id=request.employment_config_id,
            job_role_id=request.job_role_id,
            job_role_level_id=request.job_role_level_id,
            job_id=request.job_id,
            is_deleted=request.is_deleted,
            is_active=request.is_active,
            created_at=datetime.now(),
            created_by=request.created_by,
            )

            return self.requisition_repository.create(model=requisition)

        except Exception as exc:
            self.logger.error("Service execution failed", service=self.name, error=str(exc), exc=exc)
            raise exc

        finally:
            self.logger.info("Service execution completed", service=self.name)

    @property
    def name(self) -> str:
        """Returns the class name."""
        return Service.CREATE_REQUISITION_SERVICE
