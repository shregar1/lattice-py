"""Repository implementation for Envelope."""

import time
from typing import Any, List, Optional

from rivex import Dependency

from dependencies.model import (
    CompanyDependency,
    EnvelopeDependency,
    TenantDependency,
    UserDependency,
)
from dependencies.utility import LoggerUtilityDependency
from models import Company, Envelope, Tenant, User
from repositories.atomic import EnvelopeRepository as AtomicEnvelopeRepository
from utilities import Logger

from ..abstraction import ICompositeRepository


class EnvelopeRepository(AtomicEnvelopeRepository, ICompositeRepository):
    """Repository for Envelope; extends AtomicEnvelopeRepository."""

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
        model: type[Envelope] = Dependency(EnvelopeDependency),
        company_model: type[Company] = Dependency(CompanyDependency),
        tenant_model: type[Tenant] = Dependency(TenantDependency),
        user_model: type[User] = Dependency(UserDependency),
        *args: Any,
        **kwargs: Any,
    ) -> None:
        AtomicEnvelopeRepository.__init__(
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
        self.envelope_model = model
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
                self.envelope_model.exists(id=entity_id, tenant_id=tenant_id)
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

    def filter_by_tenant(self, tenant_id: int) -> List[Envelope]:
        """Filter Envelope records by tenant_id."""
        start_time = time.time()

        try:
            result = list(self.envelope_model.find_many(tenant_id=tenant_id))
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

    def filter_by_status_id(self, status_id: int) -> List[Envelope]:
        """Filter Envelope records by status_id."""
        start_time = time.time()

        try:
            result = list(self.envelope_model.find_many(status_id=status_id))
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

    def filter_by_template_id(self, template_id: int) -> List[Envelope]:
        """Filter Envelope records by template_id."""
        start_time = time.time()

        try:
            result = list(self.envelope_model.find_many(template_id=template_id))
            end_time = time.time()
            self.logger.info(
                "Query execution succeeded for filter_by_template_id",
                start_time=start_time,
                end_time=end_time,
                duration_ms=(end_time - start_time) * 1000,
                details={"template_id": template_id},
            )
            return result

        except Exception as exc:
            end_time = time.time()
            self.logger.error(
                "Query execution failed for filter_by_template_id",
                start_time=start_time,
                end_time=end_time,
                duration_ms=(end_time - start_time) * 1000,
                details={"template_id": template_id},
                error=str(exc),
                exc=exc,
            )
            raise exc

    def filter_by_external_id(self, external_id: str) -> List[Envelope]:
        """Filter Envelope records by external_id."""
        start_time = time.time()

        try:
            result = list(self.envelope_model.find_many(external_id=external_id))
            end_time = time.time()
            self.logger.info(
                "Query execution succeeded for filter_by_external_id",
                start_time=start_time,
                end_time=end_time,
                duration_ms=(end_time - start_time) * 1000,
                details={"external_id": external_id},
            )
            return result

        except Exception as exc:
            end_time = time.time()
            self.logger.error(
                "Query execution failed for filter_by_external_id",
                start_time=start_time,
                end_time=end_time,
                duration_ms=(end_time - start_time) * 1000,
                details={"external_id": external_id},
                error=str(exc),
                exc=exc,
            )
            raise exc

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "EnvelopeRepository"
