from exceptions import BadInputException
"""Create ai_screening_status_lk repository service module."""

from datetime import datetime
from rivex import Dependency
from typing import Any, Optional

from abstractions import DTOLayer
from constants import Service
from dtos import CreateAiScreeningStatusLKServiceDTO
from dependencies import CompositeAiScreeningStatusLkRepositoryDependency, AIScreeningStatusLKRepositoryDependency
from repositories import AIScreeningStatusLKRepository
from models import AIScreeningStatusLK
from .abstraction import IAiScreeningStatusLKRepositoryService


class CreateAiScreeningStatusLKService(IAiScreeningStatusLKRepositoryService):
    """Application service for create operation on ai_screening_status_lk repository."""

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
        a_i_screening_status_lk_repository: AIScreeningStatusLKRepository = Dependency(AIScreeningStatusLKRepositoryDependency),
                composite_ai_screening_status_lk_repository: CompositeAiScreeningStatusLkRepository = Dependency(CompositeAiScreeningStatusLkRepositoryDependency),
        *args: Any,
        **kwargs: Any,
    ) -> None:

        self.composite_ai_screening_status_lk_repository = composite_ai_screening_status_lk_repository
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
        self.a_i_screening_status_lk_repository = a_i_screening_status_lk_repository

    async def run(self, request: CreateAiScreeningStatusLKServiceDTO) -> DTOLayer:
        """Executes create business logic for ai_screening_status_lk."""
        self.logger.info("Executing service run", service=self.name)

        if request.user_id is None or request.tenant_id is None:
            raise BadInputException("user_id and tenant_id are required")

        try:
            if request.id is not None:
                if not self.composite_ai_screening_status_lk_repository.exists_by_id_user_and_tenant(
                    lookup_id=request.id,
                    user_id=request.user_id,
                    tenant_id=request.tenant_id,
                ):
                    raise BadInputException("Forbidden or resource does not exist for current user and tenant")

            ai_screening_status_lk: AIScreeningStatusLK = AIScreeningStatusLK.build(
            code=request.code,
            label=request.label,
            description=request.description,
            is_deleted=request.is_deleted,
            is_active=request.is_active,
            created_at=datetime.now(),
            created_by=request.created_by,
            )

            return self.a_i_screening_status_lk_repository.create(model=ai_screening_status_lk)

        except Exception as exc:
            self.logger.error("Service execution failed", service=self.name, error=str(exc), exc=exc)
            raise exc

        finally:
            self.logger.info("Service execution completed", service=self.name)

    @property
    def name(self) -> str:
        """Returns the class name."""
        return Service.CREATE_AI_SCREENING_STATUS_LK_SERVICE
