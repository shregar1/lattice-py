from exceptions import BadInputException
"""Create offer repository service module."""

from datetime import datetime
from rivex import Dependency
from typing import Any, Optional

from abstractions import DTOLayer
from constants import Service
from dtos import CreateOfferServiceDTO
from dependencies import OfferRepositoryDependency
from repositories import OfferRepository
from models import Offer
from .abstraction import IOfferRepositoryService


class CreateOfferService(IOfferRepositoryService):
    """Application service for create operation on offer repository."""

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
        offer_repository: OfferRepository = Dependency(OfferRepositoryDependency),
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
        self.offer_repository = offer_repository

    async def run(self, request: CreateOfferServiceDTO) -> DTOLayer:
        """Executes create business logic for offer."""
        self.logger.info("Executing service run", service=self.name)

        if request.user_id is None or request.tenant_id is None:
            raise BadInputException("user_id and tenant_id are required")

        try:

            offer: Offer = Offer.build(
            salary=request.salary,
            equity=request.equity,
            start_date=request.start_date,
            expires_at=request.expires_at,
            letter_body=request.letter_body,
            application_id=request.application_id,
            status_id=request.status_id,
            currency_id=request.currency_id,
            letter_template_id=request.letter_template_id,
            job_role_id=request.job_role_id,
            job_role_level_id=request.job_role_level_id,
            is_deleted=request.is_deleted,
            is_active=request.is_active,
            created_at=datetime.now(),
            created_by=request.created_by,
            )

            return self.offer_repository.create(model=offer)

        except Exception as exc:
            self.logger.error("Service execution failed", service=self.name, error=str(exc), exc=exc)
            raise exc

        finally:
            self.logger.info("Service execution completed", service=self.name)

    @property
    def name(self) -> str:
        """Returns the class name."""
        return Service.CREATE_OFFER_SERVICE
