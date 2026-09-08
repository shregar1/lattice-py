from exceptions import BadInputException
"""Filter ai_screening_evaluation repository service module."""

from datetime import datetime
from rivex import Dependency
from typing import Any, Optional

from abstractions import DTOLayer
from constants import Service
from dtos import FilterAiScreeningEvaluationServiceDTO
from dependencies import CompositeAIScreeningEvaluationRepositoryDependency, AIScreeningEvaluationRepositoryDependency
from repositories import AIScreeningEvaluationRepository
from .abstraction import IAiScreeningEvaluationRepositoryService


class FilterAiScreeningEvaluationService(IAiScreeningEvaluationRepositoryService):
    """Application service for filter operation on ai_screening_evaluation repository."""

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
        ai_screening_evaluation_repository: AIScreeningEvaluationRepository = Dependency(AIScreeningEvaluationRepositoryDependency),
                composite_ai_screening_evaluation_repository: CompositeAIScreeningEvaluationRepository = Dependency(CompositeAIScreeningEvaluationRepositoryDependency),
        *args: Any,
        **kwargs: Any,
    ) -> None:

        self.composite_ai_screening_evaluation_repository = composite_ai_screening_evaluation_repository
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
        self.ai_screening_evaluation_repository = ai_screening_evaluation_repository

    async def run(self, request: FilterAiScreeningEvaluationServiceDTO) -> DTOLayer:
        """Executes filter business logic for ai_screening_evaluation."""
        self.logger.info("Executing service run", service=self.name)

        if request.user_id is None or request.tenant_id is None:
            raise BadInputException("user_id and tenant_id are required")

        try:
            return self.composite_ai_screening_evaluation_repository.filter_by_user_and_tenant(
                user_id=request.user_id,
                tenant_id=request.tenant_id,
            )
        except Exception as exc:
            self.logger.error("Service execution failed", service=self.name, error=str(exc), exc=exc)
            raise exc

        finally:
            self.logger.info("Service execution completed", service=self.name)

    @property
    def name(self) -> str:
        """Returns the class name."""
        return Service.FILTER_AI_SCREENING_EVALUATION_SERVICE
