from exceptions import BadInputException
"""Create auth_type_lk repository service module."""

from datetime import datetime
from rivex import Dependency
from typing import Any, Optional

from abstractions import DTOLayer
from constants import Service
from dtos import CreateAuthTypeLKServiceDTO
from dependencies import AuthTypeLKRepositoryDependency
from repositories import AuthTypeLKRepository
from models import AuthTypeLK
from .abstraction import IAuthTypeLKRepositoryService


class CreateAuthTypeLKService(IAuthTypeLKRepositoryService):
    """Application service for create operation on auth_type_lk repository."""

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
        auth_type_lk_repository: AuthTypeLKRepository = Dependency(AuthTypeLKRepositoryDependency),
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
        self.auth_type_lk_repository = auth_type_lk_repository

    async def run(self, request: CreateAuthTypeLKServiceDTO) -> DTOLayer:
        """Executes create business logic for auth_type_lk."""
        self.logger.info("Executing service run", service=self.name)

        if request.user_id is None or request.tenant_id is None:
            raise BadInputException("user_id and tenant_id are required")

        try:

            auth_type_lk: AuthTypeLK = AuthTypeLK.build(
            code=request.code,
            label=request.label,
            description=request.description,
            is_deleted=request.is_deleted,
            is_active=request.is_active,
            created_at=datetime.now(),
            created_by=request.created_by,
            )

            return self.auth_type_lk_repository.create(model=auth_type_lk)

        except Exception as exc:
            self.logger.error("Service execution failed", service=self.name, error=str(exc), exc=exc)
            raise exc

        finally:
            self.logger.info("Service execution completed", service=self.name)

    @property
    def name(self) -> str:
        """Returns the class name."""
        return Service.CREATE_AUTH_TYPE_LK_SERVICE
