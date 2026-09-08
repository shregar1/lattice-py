from exceptions import BadInputException
"""Update automation_rule repository service module."""

from datetime import datetime
from rivex import Dependency
from typing import Any, Optional

from abstractions import DTOLayer
from constants import Service
from dtos import UpdateAutomationRuleServiceDTO
from dependencies import AutomationRuleRepositoryDependency
from repositories import AutomationRuleRepository
from models import AutomationRule
from .abstraction import IAutomationRuleRepositoryService


class UpdateAutomationRuleService(IAutomationRuleRepositoryService):
    """Application service for update operation on automation_rule repository."""

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
        automation_rule_repository: AutomationRuleRepository = Dependency(AutomationRuleRepositoryDependency),
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
        self.automation_rule_repository = automation_rule_repository

    async def run(self, request: UpdateAutomationRuleServiceDTO) -> DTOLayer:
        """Executes update business logic for automation_rule."""
        self.logger.info("Executing service run", service=self.name)

        if request.user_id is None or request.tenant_id is None:
            raise BadInputException("user_id and tenant_id are required")

        try:

            automation_rule: AutomationRule = AutomationRule.build(
            label=request.label,
            min_avg_rating=request.min_avg_rating,
            max_days=request.max_days,
            action_tag=request.action_tag,
            runs=request.runs,
            trigger_id=request.trigger_id,
            trigger_stage_id=request.trigger_stage_id,
            action_id=request.action_id,
            action_stage_id=request.action_stage_id,
            is_deleted=request.is_deleted,
            updated_at=datetime.now()
            )

            return self.automation_rule_repository.update(model=automation_rule)

        except Exception as exc:
            self.logger.error("Service execution failed", service=self.name, error=str(exc), exc=exc)
            raise exc

        finally:
            self.logger.info("Service execution completed", service=self.name)

    @property
    def name(self) -> str:
        """Returns the class name."""
        return Service.UPDATE_AUTOMATION_RULE_SERVICE
