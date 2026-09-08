from exceptions import BadInputException
from constants import DBColumn
"""Delete requisition repository service module."""

from datetime import datetime
from rivex import Dependency
from typing import Any, Optional

from abstractions import DTOLayer
from constants import Service
from dtos import DeleteRequisitionServiceDTO
from dependencies import RequisitionRepositoryDependency
from repositories import RequisitionRepository
from .abstraction import IRequisitionRepositoryService


class DeleteRequisitionService(IRequisitionRepositoryService):
    """Application service for delete operation on requisition repository."""

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

    async def run(self, request: DeleteRequisitionServiceDTO) -> DTOLayer:
        """Executes delete business logic for record."""
        self.logger.info("Executing service run", service=self.name)

        if request.user_id is None or request.tenant_id is None:
            raise BadInputException("user_id and tenant_id are required")

        try:
            if request.id:
                if not self.requisition_repository.exists_by_id_and_tenant(
                    requisition_id=request.id,
                    tenant_id=request.tenant_id,
                ):
                    from exceptions import ForbiddenException
                    raise ForbiddenException("User does not have permission to delete this requisition record.")

                if request.is_hard_delete:
                    return self.requisition_repository.hard_delete(id=request.id)
                return self.requisition_repository.soft_delete(id=request.id)
            return request
        except Exception as exc:
            self.logger.error("Service execution failed", service=self.name, error=str(exc), exc=exc)
            raise exc

        finally:
            self.logger.info("Service execution completed", service=self.name)

    @property
    def name(self) -> str:
        """Returns the class name."""
        return Service.DELETE_REQUISITION_SERVICE
