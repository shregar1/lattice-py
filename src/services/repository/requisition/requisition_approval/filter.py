from exceptions import BadInputException
"""Filter requisition_approval repository service module."""

from datetime import datetime
from rivex import Dependency
from typing import Any, Optional

from abstractions import DTOLayer
from constants import Service
from dtos import FilterRequisitionApprovalServiceDTO
from dependencies import RequisitionApprovalRepositoryDependency
from repositories import RequisitionApprovalRepository
from .abstraction import IRequisitionApprovalRepositoryService


class FilterRequisitionApprovalService(IRequisitionApprovalRepositoryService):
    """Application service for filter operation on requisition_approval repository."""

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
        requisition_approval_repository: RequisitionApprovalRepository = Dependency(RequisitionApprovalRepositoryDependency),
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
        self.requisition_approval_repository = requisition_approval_repository

    async def run(self, request: FilterRequisitionApprovalServiceDTO) -> DTOLayer:
        """Executes filter business logic for requisition_approval."""
        self.logger.info("Executing service run", service=self.name)

        if request.user_id is None or request.tenant_id is None:
            raise BadInputException("user_id and tenant_id are required")

        try:
            filter_kwargs = {k: v for k, v in request.model_dump().items() if v is not None}
            if filter_kwargs:
                column, value = next(iter(filter_kwargs.items()))
                return self.requisition_approval_repository.filter(column=column, value=value)
            return self.requisition_approval_repository.list_all()
        except Exception as exc:
            self.logger.error("Service execution failed", service=self.name, error=str(exc), exc=exc)
            raise exc

        finally:
            self.logger.info("Service execution completed", service=self.name)

    @property
    def name(self) -> str:
        """Returns the class name."""
        return Service.FILTER_REQUISITION_APPROVAL_SERVICE
