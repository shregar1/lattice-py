"""Repository implementation for Invite."""

import time
from typing import Any, List, Optional

from rivex import Dependency

from dependencies.model import (
    CompanyDependency,
    InviteDependency,
    TenantDependency,
    UserDependency,
)
from dependencies.utility import LoggerUtilityDependency
from models import Company, Invite, Tenant, User
from repositories.atomic import InviteRepository as AtomicInviteRepository
from utilities import Logger

from .abstraction import ICompositeRepository


class InviteRepository(AtomicInviteRepository, ICompositeRepository):
    """Repository for Invite; extends AtomicInviteRepository."""

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
        model: type[Invite] = Dependency(InviteDependency),
        company_model: type[Company] = Dependency(CompanyDependency),
        tenant_model: type[Tenant] = Dependency(TenantDependency),
        user_model: type[User] = Dependency(UserDependency),
        *args: Any,
        **kwargs: Any,
    ) -> None:
        AtomicInviteRepository.__init__(
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
        self.invite_model = model
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
                self.invite_model.exists(id=entity_id, tenant_id=tenant_id)
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

    def filter_by_tenant(self, tenant_id: int) -> List[Invite]:
        """Filter Invite records by tenant_id."""
        start_time = time.time()

        try:
            result = list(self.invite_model.find_many(tenant_id=tenant_id))
            end_time = time.time()
            self.logger.info(
                "Query execution succeeded for filter_by_tenant",
                start_time=start_time,
                end_time=end_time,
                duration_ms=(end_time - start_time) * 1000,
                details={"tenant_id": tenant_id},
            )
            return result

        except Exception as exc:
            end_time = time.time()
            self.logger.error(
                "Query execution failed for filter_by_tenant",
                start_time=start_time,
                end_time=end_time,
                duration_ms=(end_time - start_time) * 1000,
                details={"tenant_id": tenant_id},
                error=str(exc),
                exc=exc,
            )
            raise exc

    def filter_by_email(self, email: str) -> List[Invite]:
        """Filter Invite records by email."""
        start_time = time.time()

        try:
            result = list(self.invite_model.find_many(email=email))
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

    def filter_by_contact_id(self, contact_id: int) -> List[Invite]:
        """Filter Invite records by contact_id."""
        start_time = time.time()

        try:
            result = list(self.invite_model.find_many(contact_id=contact_id))
            end_time = time.time()
            self.logger.info(
                "Query execution succeeded for filter_by_contact_id",
                start_time=start_time,
                end_time=end_time,
                duration_ms=(end_time - start_time) * 1000,
                details={"contact_id": contact_id},
            )
            return result

        except Exception as exc:
            end_time = time.time()
            self.logger.error(
                "Query execution failed for filter_by_contact_id",
                start_time=start_time,
                end_time=end_time,
                duration_ms=(end_time - start_time) * 1000,
                details={"contact_id": contact_id},
                error=str(exc),
                exc=exc,
            )
            raise exc

    def filter_by_status_id(self, status_id: int) -> List[Invite]:
        """Filter Invite records by status_id."""
        start_time = time.time()

        try:
            result = list(self.invite_model.find_many(status_id=status_id))
            end_time = time.time()
            self.logger.info(
                "Query execution succeeded for filter_by_status_id",
                start_time=start_time,
                end_time=end_time,
                duration_ms=(end_time - start_time) * 1000,
                details={"status_id": status_id},
            )
            return result

        except Exception as exc:
            end_time = time.time()
            self.logger.error(
                "Query execution failed for filter_by_status_id",
                start_time=start_time,
                end_time=end_time,
                duration_ms=(end_time - start_time) * 1000,
                details={"status_id": status_id},
                error=str(exc),
                exc=exc,
            )
            raise exc

    def filter_by_invite_type_id(self, invite_type_id: int) -> List[Invite]:
        """Filter Invite records by invite_type_id."""
        start_time = time.time()

        try:
            result = list(self.invite_model.find_many(invite_type_id=invite_type_id))
            end_time = time.time()
            self.logger.info(
                "Query execution succeeded for filter_by_invite_type_id",
                start_time=start_time,
                end_time=end_time,
                duration_ms=(end_time - start_time) * 1000,
                details={"invite_type_id": invite_type_id},
            )
            return result

        except Exception as exc:
            end_time = time.time()
            self.logger.error(
                "Query execution failed for filter_by_invite_type_id",
                start_time=start_time,
                end_time=end_time,
                duration_ms=(end_time - start_time) * 1000,
                details={"invite_type_id": invite_type_id},
                error=str(exc),
                exc=exc,
            )
            raise exc

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "InviteRepository"
