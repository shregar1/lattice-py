from exceptions import BadInputException
from constants import DBColumn
"""Delete ai_screening_criteria repository service module."""

from datetime import datetime
from rivex import Dependency
from typing import Any, Optional

from abstractions import DTOLayer
from constants import Service
from dtos import DeleteAiScreeningCriteriaServiceDTO
from dependencies import CompositeAIScreeningCriteriaRepositoryDependency, AIScreeningCriteriaRepositoryDependency
from repositories import AIScreeningCriteriaRepository
from .abstraction import IAiScreeningCriteriaRepositoryService


class DeleteAiScreeningCriteriaService(IAiScreeningCriteriaRepositoryService):
    """Application service for delete operation on ai_screening_criteria repository."""

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
        ai_screening_criteria_repository: AIScreeningCriteriaRepository = Dependency(AIScreeningCriteriaRepositoryDependency),
                composite_ai_screening_criteria_repository: CompositeAIScreeningCriteriaRepository = Dependency(CompositeAIScreeningCriteriaRepositoryDependency),
        *args: Any,
        **kwargs: Any,
    ) -> None:

        self.composite_ai_screening_criteria_repository = composite_ai_screening_criteria_repository
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
        self.ai_screening_criteria_repository = ai_screening_criteria_repository

    async def run(self, request: DeleteAiScreeningCriteriaServiceDTO) -> DTOLayer:
        """Executes delete business logic for record."""
        self.logger.info("Executing service run", service=self.name)

        if request.user_id is None or request.tenant_id is None:
            raise BadInputException("user_id and tenant_id are required")

        try:
            if request.id is not None:
                if not self.composite_ai_screening_criteria_repository.exists_by_id_user_and_tenant(
                    criteria_id=request.id,
                    user_id=request.user_id,
                    tenant_id=request.tenant_id,
                ):
                    raise BadInputException("Forbidden or resource does not exist for current user and tenant")
            if request.id:
                if request.is_hard_delete:
                    return self.ai_screening_criteria_repository.hard_delete(id=request.id)
                return self.ai_screening_criteria_repository.soft_delete(id=request.id)
            return request
        except Exception as exc:
            self.logger.error("Service execution failed", service=self.name, error=str(exc), exc=exc)
            raise exc

        finally:
            self.logger.info("Service execution completed", service=self.name)

    @property
    def name(self) -> str:
        """Returns the class name."""
        return Service.DELETE_AI_SCREENING_CRITERIA_SERVICE
