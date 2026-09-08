"""Repository implementation for UserOtp."""

import time
from typing import Any, List, Optional

from rivex import Dependency

from dependencies.model import (
    CompanyDependency,
    TenantDependency,
    UserDependency,
    UserOtpDependency,
)
from dependencies.utility import LoggerUtilityDependency
from models import Company, Tenant, User, UserOtp
from repositories.atomic import UserOtpRepository as AtomicUserOtpRepository
from utilities import Logger

from ..abstraction import ICompositeRepository


class UserOtpRepository(AtomicUserOtpRepository, ICompositeRepository):
    """Repository for UserOtp; extends AtomicUserOtpRepository."""

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
        model: type[UserOtp] = Dependency(UserOtpDependency),
        company_model: type[Company] = Dependency(CompanyDependency),
        tenant_model: type[Tenant] = Dependency(TenantDependency),
        user_model: type[User] = Dependency(UserDependency),
        *args: Any,
        **kwargs: Any,
    ) -> None:
        AtomicUserOtpRepository.__init__(
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
        self.user_otp_model = model
        self.company_model = company_model
        self.tenant_model = tenant_model
        self.user_model = user_model

    def exists_by_id_user_and_tenant(
        self,
        entity_id: int,
        user_id: int,
        tenant_id: int,
    ) -> bool:
        """Prevents IDOR: record owned by user and caller is a company member."""
        start_time = time.time()

        try:
            result = (
                self.user_otp_model.exists(id=entity_id, user_id=user_id)
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

    def filter_by_user_id(self, user_id: int) -> List[UserOtp]:
        """Filter UserOtp records by user_id."""
        start_time = time.time()

        try:
            result = list(self.user_otp_model.find_many(user_id=user_id))
            end_time = time.time()
            self.logger.info(
                "Query execution succeeded for filter_by_user_id",
                start_time=start_time,
                end_time=end_time,
                duration_ms=(end_time - start_time) * 1000,
                details={"user_id": user_id},
            )
            return result

        except Exception as exc:
            end_time = time.time()
            self.logger.error(
                "Query execution failed for filter_by_user_id",
                start_time=start_time,
                end_time=end_time,
                duration_ms=(end_time - start_time) * 1000,
                details={"user_id": user_id},
                error=str(exc),
                exc=exc,
            )
            raise exc

    def filter_by_otp_type_id(self, otp_type_id: int) -> List[UserOtp]:
        """Filter UserOtp records by otp_type_id."""
        start_time = time.time()

        try:
            result = list(self.user_otp_model.find_many(otp_type_id=otp_type_id))
            end_time = time.time()
            self.logger.info(
                "Query execution succeeded for filter_by_otp_type_id",
                start_time=start_time,
                end_time=end_time,
                duration_ms=(end_time - start_time) * 1000,
                details={"otp_type_id": otp_type_id},
            )
            return result

        except Exception as exc:
            end_time = time.time()
            self.logger.error(
                "Query execution failed for filter_by_otp_type_id",
                start_time=start_time,
                end_time=end_time,
                duration_ms=(end_time - start_time) * 1000,
                details={"otp_type_id": otp_type_id},
                error=str(exc),
                exc=exc,
            )
            raise exc

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "UserOtpRepository"
