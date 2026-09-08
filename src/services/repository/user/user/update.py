from exceptions import BadInputException
"""Update user repository service module."""

from datetime import datetime
from rivex import Dependency
from typing import Any, Optional

from abstractions import DTOLayer
from constants import Service
from dtos import UpdateUserServiceDTO
from dependencies import UserRepositoryDependency
from repositories import UserRepository
from models import User
from .abstraction import IUserRepositoryService


class UpdateUserService(IUserRepositoryService):
    """Application service for update operation on user repository."""

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
        user_repository: UserRepository = Dependency(UserRepositoryDependency),
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
        self.user_repository = user_repository

    async def run(self, request: UpdateUserServiceDTO) -> DTOLayer:
        """Executes update business logic for user."""
        self.logger.info("Executing service run", service=self.name)

        if request.user_id is None or request.tenant_id is None:
            raise BadInputException("user_id and tenant_id are required")

        try:

            user: User = User.build(
            email=request.email,
            password=request.password,
            is_mfa_enabled=request.is_mfa_enabled,
            mfa_secret=request.mfa_secret,
            last_login=request.last_login,
            mfa_type_id=request.mfa_type_id,
            auth_type_id=request.auth_type_id,
            is_deleted=request.is_deleted,
            updated_at=datetime.now()
            )

            return self.user_repository.update(model=user)

        except Exception as exc:
            self.logger.error("Service execution failed", service=self.name, error=str(exc), exc=exc)
            raise exc

        finally:
            self.logger.info("Service execution completed", service=self.name)

    @property
    def name(self) -> str:
        """Returns the class name."""
        return Service.UPDATE_USER_SERVICE
