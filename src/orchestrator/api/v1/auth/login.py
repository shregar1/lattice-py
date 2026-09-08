from datetime import datetime
from rivex import Dependency
from typing import Any, Optional



from abstractions import DTOLayer
from constants import Orchestrator
from dependencies import UserRepositoryDependency
from dependencies import JWTUtilityDependency
from .abstraction import IAuthOrchestrator
from repositories import UserRepository
from utilities import JWTUtility


class LoginAuthOrchestrator(IAuthOrchestrator):
    """Orchestration service for user login workflow."""

    def __init__(
        self,
        urn: Optional[str] = None,
        tenant_id: Optional[int] = None,
        tenant_urn: Optional[str] = None,
        user_id: Optional[int] = None,
        user_urn: Optional[str] = None,
        api_name: Optional[str] = None,
        ip_address: Optional[str] = None,
        user_agent: Optional[str] = None,
        jwt_utility: JWTUtility = Dependency(JWTUtilityDependency),
        user_repository: UserRepository = Dependency(UserRepositoryDependency),
        *args: Any,
        **kwargs: Any,
    ) -> None:

        super().__init__(
            urn=urn,
            tenant_id=tenant_id,
            tenant_urn=tenant_urn,
            user_id=user_id,
            user_urn=user_urn,
            api_name=api_name,
            ip_address=ip_address,
            user_agent=user_agent,
            *args,
            **kwargs,
        )
        self.urn=urn
        self.tenant_id=tenant_id
        self.tenant_urn=tenant_urn
        self.user_id=user_id
        self.user_urn=user_urn
        self.api_name=api_name
        self.ip_address=ip_address
        self.user_agent=user_agent
        self.jwt_utility = jwt_utility
        self.user_repository = user_repository

    async def execute(self, request: DTOLayer) -> DTOLayer:
        """Execute user login workflow."""
        return request

    @property
    def name(self) -> str:
        """Returns the class name."""
        return Orchestrator.LOGIN_AUTH
