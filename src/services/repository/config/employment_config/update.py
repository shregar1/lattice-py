from exceptions import BadInputException
"""Update employment_config repository service module."""

from datetime import datetime
from rivex import Dependency
from typing import Any, Optional

from abstractions import DTOLayer
from constants import Service
from dtos import UpdateEmploymentConfigInputDTO
from dependencies import EmploymentConfigRepositoryDependency
from repositories import EmploymentConfigRepository
from models import EmploymentConfig
from .abstraction import IEmploymentConfigRepositoryService


class UpdateEmploymentConfigService(IEmploymentConfigRepositoryService):
    """Application service for update operation on employment_config repository."""

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
        employment_config_repository: EmploymentConfigRepository = Dependency(EmploymentConfigRepositoryDependency),
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
        self.employment_config_repository = employment_config_repository

    async def run(self, request: UpdateEmploymentConfigInputDTO) -> DTOLayer:
        """Executes update business logic for employment_config."""
        self.logger.info("Executing service run", service=self.name)

        if request.user_id is None or request.tenant_id is None:
            raise BadInputException("user_id and tenant_id are required")

        try:

            employment_config: EmploymentConfig = EmploymentConfig.build(
            title=request.title,
            description=request.description,
            hours_per_week=request.hours_per_week,
            working_days_per_week=request.working_days_per_week,
            is_remote_policy=request.is_remote_policy,
            employment_type_id=request.employment_type_id,
            is_deleted=request.is_deleted,
            updated_at=datetime.now()
            )

            return self.employment_config_repository.update(model=employment_config)

        except Exception as exc:
            self.logger.error("Service execution failed", service=self.name, error=str(exc), exc=exc)
            raise exc

        finally:
            self.logger.info("Service execution completed", service=self.name)

    @property
    def name(self) -> str:
        """Returns the class name."""
        return Service.UPDATE_EMPLOYMENT_CONFIG_SERVICE
