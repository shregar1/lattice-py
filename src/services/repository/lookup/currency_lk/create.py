from exceptions import BadInputException
"""Create currency_lk repository service module."""

from datetime import datetime
from rivex import Dependency
from typing import Any, Optional

from abstractions import DTOLayer
from constants import Service
from dtos import CreateCurrencyLKServiceDTO
from dependencies import CurrencyLKRepositoryDependency
from repositories import CurrencyLKRepository
from models import CurrencyLK
from .abstraction import ICurrencyLKRepositoryService


class CreateCurrencyLKService(ICurrencyLKRepositoryService):
    """Application service for create operation on currency_lk repository."""

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
        currency_lk_repository: CurrencyLKRepository = Dependency(CurrencyLKRepositoryDependency),
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
        self.currency_lk_repository = currency_lk_repository

    async def run(self, request: CreateCurrencyLKServiceDTO) -> DTOLayer:
        """Executes create business logic for currency_lk."""
        self.logger.info("Executing service run", service=self.name)

        if request.user_id is None or request.tenant_id is None:
            raise BadInputException("user_id and tenant_id are required")

        try:

            currency_lk: CurrencyLK = CurrencyLK.build(
            code=request.code,
            description=request.description,
            symbol=request.symbol,
            is_deleted=request.is_deleted,
            is_active=request.is_active,
            created_at=datetime.now(),
            created_by=request.created_by,
            )

            return self.currency_lk_repository.create(model=currency_lk)

        except Exception as exc:
            self.logger.error("Service execution failed", service=self.name, error=str(exc), exc=exc)
            raise exc

        finally:
            self.logger.info("Service execution completed", service=self.name)

    @property
    def name(self) -> str:
        """Returns the class name."""
        return Service.CREATE_CURRENCY_LK_SERVICE
