"""Repository implementation for TenantProfile."""

import time
from typing import Any, List, Optional

from rivex import Dependency

from dependencies.model import (
    CompanyDependency,
    TenantDependency,
    TenantProfileDependency,
    UserDependency,
)
from dependencies.utility import LoggerUtilityDependency
from models import Company, Tenant, TenantProfile, User
from repositories.atomic import TenantProfileRepository as AtomicTenantProfileRepository
from utilities import Logger

from ..abstraction import ICompositeRepository


class TenantProfileRepository(AtomicTenantProfileRepository, ICompositeRepository):
    """Repository for TenantProfile; extends AtomicTenantProfileRepository."""

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
        model: type[TenantProfile] = Dependency(TenantProfileDependency),
        company_model: type[Company] = Dependency(CompanyDependency),
        tenant_model: type[Tenant] = Dependency(TenantDependency),
        user_model: type[User] = Dependency(UserDependency),
        *args: Any,
        **kwargs: Any,
    ) -> None:
        AtomicTenantProfileRepository.__init__(
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
        self.tenant_profile_model = model
        self.company_model = company_model
        self.tenant_model = tenant_model
        self.user_model = user_model

    def exists_by_id_user_and_tenant(
        self,
        entity_id: int,
        user_id: int,
        tenant_id: int,
    ) -> bool:
        """Prevents IDOR: record in tenant and caller is a company member."""
        start_time = time.time()

        try:
            result = (
                self.tenant_profile_model.exists(id=entity_id, tenant_id=tenant_id)
                and self.company_model.exists(user_id=user_id, tenant_id=tenant_id)
            )
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

    def filter_by_tenant_id(self, tenant_id: int) -> List[TenantProfile]:
        """Filter TenantProfile records by tenant_id."""
        start_time = time.time()

        try:
            result = list(self.tenant_profile_model.find_many(tenant_id=tenant_id))
            end_time = time.time()
            self.logger.info(
                "Query execution succeeded for filter_by_tenant_id",
                start_time=start_time,
                end_time=end_time,
                duration_ms=(end_time - start_time) * 1000,
                details={"tenant_id": tenant_id},
            )
            return result

        except Exception as exc:
            end_time = time.time()
            self.logger.error(
                "Query execution failed for filter_by_tenant_id",
                start_time=start_time,
                end_time=end_time,
                duration_ms=(end_time - start_time) * 1000,
                details={"tenant_id": tenant_id},
                error=str(exc),
                exc=exc,
            )
            raise exc

    def filter_by_name(self, name: str) -> List[TenantProfile]:
        """Filter TenantProfile records by name."""
        start_time = time.time()

        try:
            result = list(self.tenant_profile_model.find_many(name=name))
            end_time = time.time()
            self.logger.info(
                "Query execution succeeded for filter_by_name",
                start_time=start_time,
                end_time=end_time,
                duration_ms=(end_time - start_time) * 1000,
                details={"name": name},
            )
            return result

        except Exception as exc:
            end_time = time.time()
            self.logger.error(
                "Query execution failed for filter_by_name",
                start_time=start_time,
                end_time=end_time,
                duration_ms=(end_time - start_time) * 1000,
                details={"name": name},
                error=str(exc),
                exc=exc,
            )
            raise exc

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "TenantProfileRepository"
