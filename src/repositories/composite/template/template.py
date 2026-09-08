"""Repository implementation for Template."""

import time
from typing import Any, List, Optional

from rivex import Dependency

from dependencies.model import (
    CompanyDependency,
    TemplateDependency,
    TenantDependency,
    UserDependency,
)
from dependencies.utility import LoggerUtilityDependency
from models import Company, Template, Tenant, User
from repositories.atomic import TemplateRepository as AtomicTemplateRepository
from utilities import Logger

from ..abstraction import ICompositeRepository


class TemplateRepository(AtomicTemplateRepository, ICompositeRepository):
    """Repository for Template; extends AtomicTemplateRepository."""

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
        model: type[Template] = Dependency(TemplateDependency),
        company_model: type[Company] = Dependency(CompanyDependency),
        tenant_model: type[Tenant] = Dependency(TenantDependency),
        user_model: type[User] = Dependency(UserDependency),
        *args: Any,
        **kwargs: Any,
    ) -> None:
        AtomicTemplateRepository.__init__(
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
        self.template_model = model
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
                self.template_model.exists(id=entity_id, tenant_id=tenant_id)
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

    def filter_by_tenant(self, tenant_id: int) -> List[Template]:
        """Filter Template records by tenant_id."""
        start_time = time.time()

        try:
            result = list(self.template_model.find_many(tenant_id=tenant_id))
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

    def filter_by_template_name(self, template_name: str) -> List[Template]:
        """Filter Template records by template_name."""
        start_time = time.time()

        try:
            result = list(self.template_model.find_many(template_name=template_name))
            end_time = time.time()
            self.logger.info(
                "Query execution succeeded for filter_by_template_name",
                start_time=start_time,
                end_time=end_time,
                duration_ms=(end_time - start_time) * 1000,
                details={"template_name": template_name},
            )
            return result

        except Exception as exc:
            end_time = time.time()
            self.logger.error(
                "Query execution failed for filter_by_template_name",
                start_time=start_time,
                end_time=end_time,
                duration_ms=(end_time - start_time) * 1000,
                details={"template_name": template_name},
                error=str(exc),
                exc=exc,
            )
            raise exc

    def filter_by_shared(self, shared: bool) -> List[Template]:
        """Filter Template records by shared."""
        start_time = time.time()

        try:
            result = list(self.template_model.find_many(shared=shared))
            end_time = time.time()
            self.logger.info(
                "Query execution succeeded for filter_by_shared",
                start_time=start_time,
                end_time=end_time,
                duration_ms=(end_time - start_time) * 1000,
                details={"shared": shared},
            )
            return result

        except Exception as exc:
            end_time = time.time()
            self.logger.error(
                "Query execution failed for filter_by_shared",
                start_time=start_time,
                end_time=end_time,
                duration_ms=(end_time - start_time) * 1000,
                details={"shared": shared},
                error=str(exc),
                exc=exc,
            )
            raise exc

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "TemplateRepository"
