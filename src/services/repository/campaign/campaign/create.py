from exceptions import BadInputException
"""Create campaign repository service module."""

from datetime import datetime
from rivex import Dependency
from typing import Any, Optional

from abstractions import DTOLayer
from constants import Service
from dtos import CreateCampaignServiceDTO
from dependencies import CampaignRepositoryDependency
from repositories import CampaignRepository
from models import Campaign
from .abstraction import ICampaignRepositoryService


class CreateCampaignService(ICampaignRepositoryService):
    """Application service for create operation on campaign repository."""

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
        campaign_repository: CampaignRepository = Dependency(CampaignRepositoryDependency),
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
        self.campaign_repository = campaign_repository

    async def run(self, request: CreateCampaignServiceDTO) -> DTOLayer:
        """Executes create business logic for campaign."""
        self.logger.info("Executing service run", service=self.name)

        if request.user_id is None or request.tenant_id is None:
            raise BadInputException("user_id and tenant_id are required")

        try:

            campaign: Campaign = Campaign.build(
            label=request.label,
            description=request.description,
            owner_id=request.owner_id,
            is_deleted=request.is_deleted,
            is_active=request.is_active,
            created_at=datetime.now(),
            created_by=request.created_by,
            )

            return self.campaign_repository.create(model=campaign)

        except Exception as exc:
            self.logger.error("Service execution failed", service=self.name, error=str(exc), exc=exc)
            raise exc

        finally:
            self.logger.info("Service execution completed", service=self.name)

    @property
    def name(self) -> str:
        """Returns the class name."""
        return Service.CREATE_CAMPAIGN_SERVICE
