from exceptions import BadInputException
"""Update ai_screening_run repository service module."""

from datetime import datetime
from rivex import Dependency
from typing import Any, Optional

from abstractions import DTOLayer
from constants import Service
from dtos import UpdateAiScreeningRunServiceDTO
from dependencies import CompositeAIScreeningRunRepositoryDependency, AIScreeningRunRepositoryDependency
from repositories import AIScreeningRunRepository
from models import AiScreeningRun
from .abstraction import IAiScreeningRunRepositoryService


class UpdateAiScreeningRunService(IAiScreeningRunRepositoryService):
    """Application service for update operation on ai_screening_run repository."""

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
        a_i_screening_run_repository: AIScreeningRunRepository = Dependency(AIScreeningRunRepositoryDependency),
                composite_ai_screening_run_repository: CompositeAIScreeningRunRepository = Dependency(CompositeAIScreeningRunRepositoryDependency),
        *args: Any,
        **kwargs: Any,
    ) -> None:

        self.composite_ai_screening_run_repository = composite_ai_screening_run_repository
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
        self.a_i_screening_run_repository = a_i_screening_run_repository

    async def run(self, request: UpdateAiScreeningRunServiceDTO) -> DTOLayer:
        """Executes update business logic for ai_screening_run."""
        self.logger.info("Executing service run", service=self.name)

        if request.user_id is None or request.tenant_id is None:
            raise BadInputException("user_id and tenant_id are required")

        try:
            if request.id is not None:
                if not self.composite_ai_screening_run_repository.exists_by_id_user_and_tenant(
                    run_id=request.id,
                    user_id=request.user_id,
                    tenant_id=request.tenant_id,
                ):
                    raise BadInputException("Forbidden or resource does not exist for current user and tenant")

            ai_screening_run: AiScreeningRun = AiScreeningRun.build(
            application_id=request.application_id,
            status_id=request.status_id,
            overall_score=request.overall_score,
            decision=request.decision,
            summary=request.summary,
            raw_input=request.raw_input,
            raw_output=request.raw_output,
            error_message=request.error_message,
            completed_at=request.completed_at,
            is_deleted=request.is_deleted,
            updated_at=datetime.now()
            )

            return self.a_i_screening_run_repository.update(model=ai_screening_run)

        except Exception as exc:
            self.logger.error("Service execution failed", service=self.name, error=str(exc), exc=exc)
            raise exc

        finally:
            self.logger.info("Service execution completed", service=self.name)

    @property
    def name(self) -> str:
        """Returns the class name."""
        return Service.UPDATE_AI_SCREENING_RUN_SERVICE
