from exceptions import BadInputException
"""Filter campaign_step repository service module."""

from datetime import datetime
from rivex import Dependency
from typing import Any, Optional

from abstractions import DTOLayer
from constants import Service
from dtos import FilterCampaignStepServiceDTO
from dependencies import CampaignStepRepositoryDependency
from repositories import CampaignStepRepository
from .abstraction import ICampaignStepRepositoryService


class FilterCampaignStepService(ICampaignStepRepositoryService):
    """Application service for filter operation on campaign_step repository."""

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
        campaign_step_repository: CampaignStepRepository = Dependency(CampaignStepRepositoryDependency),
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
        self.campaign_step_repository = campaign_step_repository

    async def run(self, request: FilterCampaignStepServiceDTO) -> DTOLayer:
        """Executes filter business logic for campaign_step."""
        self.logger.info("Executing service run", service=self.name)

        if request.user_id is None or request.tenant_id is None:
            raise BadInputException("user_id and tenant_id are required")

        try:
            filter_kwargs = {k: v for k, v in request.model_dump().items() if v is not None}
            if filter_kwargs:
                column, value = next(iter(filter_kwargs.items()))
                return self.campaign_step_repository.filter(column=column, value=value)
            return self.campaign_step_repository.list_all()
        except Exception as exc:
            self.logger.error("Service execution failed", service=self.name, error=str(exc), exc=exc)
            raise exc

        finally:
            self.logger.info("Service execution completed", service=self.name)

    @property
    def name(self) -> str:
        """Returns the class name."""
        return Service.FILTER_CAMPAIGN_STEP_SERVICE
