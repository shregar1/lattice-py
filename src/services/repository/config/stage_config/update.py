from exceptions import BadInputException
"""Update stage_config repository service module."""

from datetime import datetime
from rivex import Dependency
from typing import Any, Optional

from abstractions import DTOLayer
from constants import Service
from dtos import UpdateStageConfigServiceDTO
from dependencies import StageConfigRepositoryDependency
from repositories import StageConfigRepository
from models import StageConfig
from .abstraction import IStageConfigRepositoryService


class UpdateStageConfigService(IStageConfigRepositoryService):
    """Application service for update operation on stage_config repository."""

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
        stage_config_repository: StageConfigRepository = Dependency(StageConfigRepositoryDependency),
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
        self.stage_config_repository = stage_config_repository

    async def run(self, request: UpdateStageConfigServiceDTO) -> DTOLayer:
        """Executes update business logic for stage_config."""
        self.logger.info("Executing service run", service=self.name)

        if request.user_id is None or request.tenant_id is None:
            raise BadInputException("user_id and tenant_id are required")

        try:

            stage_config: StageConfig = StageConfig.build(
            code=request.code,
            label=request.label,
            color=request.color,
            is_default=request.is_default,
            sort_order=request.sort_order,
            sla_days=request.sla_days,
            is_deleted=request.is_deleted,
            updated_at=datetime.now()
            )

            return self.stage_config_repository.update(model=stage_config)

        except Exception as exc:
            self.logger.error("Service execution failed", service=self.name, error=str(exc), exc=exc)
            raise exc

        finally:
            self.logger.info("Service execution completed", service=self.name)

    @property
    def name(self) -> str:
        """Returns the class name."""
        return Service.UPDATE_STAGE_CONFIG_SERVICE
