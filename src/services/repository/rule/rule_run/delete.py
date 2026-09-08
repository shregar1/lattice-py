from exceptions import BadInputException
from constants import DBColumn
"""Delete rule_run repository service module."""

from datetime import datetime
from rivex import Dependency
from typing import Any, Optional

from abstractions import DTOLayer
from constants import Service
from dtos import DeleteRuleRunServiceDTO
from dependencies import RuleRunRepositoryDependency
from repositories import RuleRunRepository
from .abstraction import IRuleRunRepositoryService


class DeleteRuleRunService(IRuleRunRepositoryService):
    """Application service for delete operation on rule_run repository."""

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
        rule_run_repository: RuleRunRepository = Dependency(RuleRunRepositoryDependency),
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
        self.rule_run_repository = rule_run_repository

    async def run(self, request: DeleteRuleRunServiceDTO) -> DTOLayer:
        """Executes delete business logic for record."""
        self.logger.info("Executing service run", service=self.name)

        if request.user_id is None or request.tenant_id is None:
            raise BadInputException("user_id and tenant_id are required")

        try:
            if request.id:
                if request.is_hard_delete:
                    return self.rule_run_repository.hard_delete(id=request.id)
                return self.rule_run_repository.soft_delete(id=request.id)
            return request
        except Exception as exc:
            self.logger.error("Service execution failed", service=self.name, error=str(exc), exc=exc)
            raise exc

        finally:
            self.logger.info("Service execution completed", service=self.name)

    @property
    def name(self) -> str:
        """Returns the class name."""
        return Service.DELETE_RULE_RUN_SERVICE
