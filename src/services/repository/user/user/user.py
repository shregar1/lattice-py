"""User service module."""

from datetime import datetime
from rivex import Dependency
from typing import Any, Optional



from abstractions import DTOLayer
from constants import Service
from dependencies import UserRepositoryDependency
from repositories import UserRepository
from .abstraction import IUserService


class UserService(IUserService):
    """Application service for user-related repository operations."""

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

    async def run(self, request: DTOLayer) -> DTOLayer:
        """Executes user service business logic."""
        return request

    @property
    def name(self) -> str:
        """Returns the class name."""
        return Service.USER
