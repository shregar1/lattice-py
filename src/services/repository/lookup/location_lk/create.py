from exceptions import BadInputException
"""Create location_lk repository service module."""

from datetime import datetime
from rivex import Dependency
from typing import Any, Optional

from abstractions import DTOLayer
from constants import Service
from dtos import CreateLocationLKServiceDTO
from dependencies import LocationLKRepositoryDependency
from repositories import LocationLKRepository
from models import LocationLK
from .abstraction import ILocationLKRepositoryService


class CreateLocationLKService(ILocationLKRepositoryService):
    """Application service for create operation on location_lk repository."""

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
        location_lk_repository: LocationLKRepository = Dependency(LocationLKRepositoryDependency),
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
        self.location_lk_repository = location_lk_repository

    async def run(self, request: CreateLocationLKServiceDTO) -> DTOLayer:
        """Executes create business logic for location_lk."""
        self.logger.info("Executing service run", service=self.name)

        if request.user_id is None or request.tenant_id is None:
            raise BadInputException("user_id and tenant_id are required")

        try:

            location_lk: LocationLK = LocationLK.build(
            address_line_1=request.address_line_1,
            address_line_2=request.address_line_2,
            city=request.city,
            state=request.state,
            zip_code=request.zip_code,
            timezone=request.timezone,
            latitude=request.latitude,
            longitude=request.longitude,
            google_place_id=request.google_place_id,
            google_map_url=request.google_map_url,
            formatted_address=request.formatted_address,
            country_id=request.country_id,
            is_deleted=request.is_deleted,
            is_active=request.is_active,
            created_at=datetime.now(),
            created_by=request.created_by,
            )

            return self.location_lk_repository.create(model=location_lk)

        except Exception as exc:
            self.logger.error("Service execution failed", service=self.name, error=str(exc), exc=exc)
            raise exc

        finally:
            self.logger.info("Service execution completed", service=self.name)

    @property
    def name(self) -> str:
        """Returns the class name."""
        return Service.CREATE_LOCATION_LK_SERVICE
