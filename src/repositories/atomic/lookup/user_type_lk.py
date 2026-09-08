"""Repository for UserTypeLK persistence and domain queries."""

from typing import Any, Optional

from rivex import Dependency

from dependencies.model import UserTypeLKDependency
from dependencies.utility import LoggerUtilityDependency
from models import UserTypeLK
from utilities import Logger

from .abstraction import ILookupRepository


class UserTypeLKRepository(ILookupRepository[UserTypeLK, int]):
    """Atomic repository for UserTypeLK."""

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
        logger: Logger = Dependency(LoggerUtilityDependency),
        model: type[UserTypeLK] = Dependency(UserTypeLKDependency),
        *args: Any,
        **kwargs: Any,
    ) -> None:
        if model is None:
            logger.error("No model found")
            raise ModuleNotFoundError("No model found")

        ILookupRepository.__init__(
            self,
            urn=urn,
            tenant_id=tenant_id,
            tenant_urn=tenant_urn,
            user_id=user_id,
            user_urn=user_urn,
            api_name=api_name,
            ip_address=ip_address,
            user_agent=user_agent,
            logger=logger,
            model=model,
            **kwargs,
        )

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "UserTypeLKRepository"
