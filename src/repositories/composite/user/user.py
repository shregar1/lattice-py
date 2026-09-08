"""Repository implementation for User."""

import time
from typing import Any, List, Optional

from rivex import Dependency

from dependencies.model import (
    AuthTypeLKDependency,
    CompanyDependency,
    MFATypeLKDependency,
    TenantDependency,
    UserDependency,
)
from dependencies.utility import LoggerUtilityDependency
from models import AuthTypeLK, Company, MFATypeLK, Tenant, User
from repositories.atomic import UserRepository as AtomicUserRepository
from utilities import Logger

from ..abstraction import ICompositeRepository


class UserRepository(AtomicUserRepository, ICompositeRepository):
    """Repository for User; extends AtomicUserRepository."""

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
        model: type[User] = Dependency(UserDependency),
        company_model: type[Company] = Dependency(CompanyDependency),
        tenant_model: type[Tenant] = Dependency(TenantDependency),
        user_model: type[User] = Dependency(UserDependency),
        auth_type_lk_model: type[AuthTypeLK] = Dependency(AuthTypeLKDependency),
        mfa_type_lk_model: type[MFATypeLK] = Dependency(MFATypeLKDependency),
        *args: Any,
        **kwargs: Any,
    ) -> None:
        AtomicUserRepository.__init__(
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
        self.user_model = model
        self.company_model = company_model
        self.tenant_model = tenant_model
        self.user_model = user_model
        self.auth_type_lk_model = auth_type_lk_model
        self.mfa_type_lk_model = mfa_type_lk_model

    def exists_by_id_user_and_tenant(
        self,
        entity_id: int,
        user_id: int,
        tenant_id: int,
    ) -> bool:
        """Prevents IDOR: target user and caller both belong to the tenant."""
        start_time = time.time()

        try:
            result = (
                self.user_model.exists(id=entity_id)
                and self.company_model.exists(user_id=entity_id, tenant_id=tenant_id)
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

    def filter_by_email(self, email: str) -> List[User]:
        """Filter User records by email."""
        start_time = time.time()

        try:
            result = list(self.user_model.find_many(email=email))
            end_time = time.time()
            self.logger.info(
                "Query execution succeeded for filter_by_email",
                start_time=start_time,
                end_time=end_time,
                duration_ms=(end_time - start_time) * 1000,
                details={"email": email},
            )
            return result

        except Exception as exc:
            end_time = time.time()
            self.logger.error(
                "Query execution failed for filter_by_email",
                start_time=start_time,
                end_time=end_time,
                duration_ms=(end_time - start_time) * 1000,
                details={"email": email},
                error=str(exc),
                exc=exc,
            )
            raise exc

    def filter_by_auth_type_id(self, auth_type_id: int) -> List[User]:
        """Filter User records by auth_type_id."""
        start_time = time.time()

        try:
            result = list(self.user_model.find_many(auth_type_id=auth_type_id))
            end_time = time.time()
            self.logger.info(
                "Query execution succeeded for filter_by_auth_type_id",
                start_time=start_time,
                end_time=end_time,
                duration_ms=(end_time - start_time) * 1000,
                details={"auth_type_id": auth_type_id},
            )
            return result

        except Exception as exc:
            end_time = time.time()
            self.logger.error(
                "Query execution failed for filter_by_auth_type_id",
                start_time=start_time,
                end_time=end_time,
                duration_ms=(end_time - start_time) * 1000,
                details={"auth_type_id": auth_type_id},
                error=str(exc),
                exc=exc,
            )
            raise exc

    def filter_by_is_mfa_enabled(self, is_mfa_enabled: bool) -> List[User]:
        """Filter User records by is_mfa_enabled."""
        start_time = time.time()

        try:
            result = list(self.user_model.find_many(is_mfa_enabled=is_mfa_enabled))
            end_time = time.time()
            self.logger.info(
                "Query execution succeeded for filter_by_is_mfa_enabled",
                start_time=start_time,
                end_time=end_time,
                duration_ms=(end_time - start_time) * 1000,
                details={"is_mfa_enabled": is_mfa_enabled},
            )
            return result

        except Exception as exc:
            end_time = time.time()
            self.logger.error(
                "Query execution failed for filter_by_is_mfa_enabled",
                start_time=start_time,
                end_time=end_time,
                duration_ms=(end_time - start_time) * 1000,
                details={"is_mfa_enabled": is_mfa_enabled},
                error=str(exc),
                exc=exc,
            )
            raise exc

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "UserRepository"
