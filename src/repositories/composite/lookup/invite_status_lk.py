"""Repository implementation for InviteStatusLK."""

import time
from typing import Any, List, Optional

from rivex import Dependency

from dependencies.model import (
    InviteStatusLKDependency,
    TenantDependency,
    UserDependency,
)
from dependencies.utility import LoggerUtilityDependency
from models import InviteStatusLK, Tenant, User
from repositories.atomic import InviteStatusLKRepository as AtomicInviteStatusLKRepository
from utilities import Logger

from ..abstraction import ICompositeRepository


class InviteStatusLKRepository(AtomicInviteStatusLKRepository, ICompositeRepository):
    """Repository for InviteStatusLK; extends AtomicInviteStatusLKRepository."""

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
        logger: Logger = Dependency(LoggerUtilityDependency),
        model: type[InviteStatusLK] = Dependency(InviteStatusLKDependency),
        tenant_model: type[Tenant] = Dependency(TenantDependency),
        user_model: type[User] = Dependency(UserDependency),
        *args: Any,
        **kwargs: Any,
    ) -> None:
        AtomicInviteStatusLKRepository.__init__(
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
            *args,
            **kwargs,
        )
        self.lookup_model = model
        self.tenant_model = tenant_model
        self.user_model = user_model

    def exists_by_id_user_and_tenant(
        self,
        entity_id: int,
        user_id: int,
        tenant_id: int,
    ) -> bool:
        """Verifies lookup record existence."""
        start_time = time.time()

        try:
            result = self.lookup_model.exists(id=entity_id)
            end_time = time.time()
            self.logger.info(
                "Query execution succeeded for exists_by_id_user_and_tenant",
                start_time=start_time,
                end_time=end_time,
                duration_ms=(end_time - start_time) * 1000,
                details={"entity_id": entity_id, "user_id": user_id, "tenant_id": tenant_id},
            )
            return result

        except Exception as exc:
            end_time = time.time()
            self.logger.error(
                "Query execution failed for exists_by_id_user_and_tenant",
                start_time=start_time,
                end_time=end_time,
                duration_ms=(end_time - start_time) * 1000,
                details={"entity_id": entity_id, "user_id": user_id, "tenant_id": tenant_id},
                error=str(exc),
                exc=exc,
            )
            return False

    def filter_by_code(self, code: str) -> List[InviteStatusLK]:
        """Filter InviteStatusLK records by code."""
        start_time = time.time()

        try:
            result = list(self.lookup_model.find_many(code=code))
            end_time = time.time()
            self.logger.info(
                "Query execution succeeded for filter_by_code",
                start_time=start_time,
                end_time=end_time,
                duration_ms=(end_time - start_time) * 1000,
                details={"code": code},
            )
            return result

        except Exception as exc:
            end_time = time.time()
            self.logger.error(
                "Query execution failed for filter_by_code",
                start_time=start_time,
                end_time=end_time,
                duration_ms=(end_time - start_time) * 1000,
                details={"code": code},
                error=str(exc),
                exc=exc,
            )
            raise exc

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "InviteStatusLKRepository"
