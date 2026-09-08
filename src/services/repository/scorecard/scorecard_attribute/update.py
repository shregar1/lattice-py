from exceptions import BadInputException
"""Update scorecard_attribute repository service module."""

from datetime import datetime
from rivex import Dependency
from typing import Any, Optional

from abstractions import DTOLayer
from constants import Service
from dtos import UpdateScorecardAttributeServiceDTO
from dependencies import ScorecardAttributeRepositoryDependency
from repositories import ScorecardAttributeRepository
from models import ScorecardAttribute
from .abstraction import IScorecardAttributeRepositoryService


class UpdateScorecardAttributeService(IScorecardAttributeRepositoryService):
    """Application service for update operation on scorecard_attribute repository."""

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
        scorecard_attribute_repository: ScorecardAttributeRepository = Dependency(ScorecardAttributeRepositoryDependency),
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
        self.scorecard_attribute_repository = scorecard_attribute_repository

    async def run(self, request: UpdateScorecardAttributeServiceDTO) -> DTOLayer:
        """Executes update business logic for scorecard_attribute."""
        self.logger.info("Executing service run", service=self.name)

        if request.user_id is None or request.tenant_id is None:
            raise BadInputException("user_id and tenant_id are required")

        try:

            scorecard_attribute: ScorecardAttribute = ScorecardAttribute.build(
            label=request.label,
            rating=request.rating,
            scorecard_id=request.scorecard_id,
            is_deleted=request.is_deleted,
            updated_at=datetime.now()
            )

            return self.scorecard_attribute_repository.update(model=scorecard_attribute)

        except Exception as exc:
            self.logger.error("Service execution failed", service=self.name, error=str(exc), exc=exc)
            raise exc

        finally:
            self.logger.info("Service execution completed", service=self.name)

    @property
    def name(self) -> str:
        """Returns the class name."""
        return Service.UPDATE_SCORECARD_ATTRIBUTE_SERVICE
