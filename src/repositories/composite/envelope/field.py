"""Repository implementation for Field."""

import time
from typing import Any, List, Optional

from rivex import Dependency

from dependencies.model import (
    CompanyDependency,
    EnvelopeDependency,
    FieldDependency,
    TemplateDependency,
    TenantDependency,
    UserDependency,
)
from dependencies.utility import LoggerUtilityDependency
from models import Company, Envelope, Field, Template, Tenant, User
from repositories.atomic import FieldRepository as AtomicFieldRepository
from utilities import Logger

from ..abstraction import ICompositeRepository


class FieldRepository(AtomicFieldRepository, ICompositeRepository):
    """Repository for Field; extends AtomicFieldRepository."""

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
        model: type[Field] = Dependency(FieldDependency),
        company_model: type[Company] = Dependency(CompanyDependency),
        envelope_model: type[Envelope] = Dependency(EnvelopeDependency),
        template_model: type[Template] = Dependency(TemplateDependency),
        tenant_model: type[Tenant] = Dependency(TenantDependency),
        user_model: type[User] = Dependency(UserDependency),
        *args: Any,
        **kwargs: Any,
    ) -> None:
        AtomicFieldRepository.__init__(
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
        self.field_model = model
        self.company_model = company_model
        self.envelope_model = envelope_model
        self.template_model = template_model
        self.tenant_model = tenant_model
        self.user_model = user_model

    def exists_by_id_user_and_tenant(
        self,
        entity_id: int,
        user_id: int,
        tenant_id: int,
    ) -> bool:
        """Prevents IDOR: parent tenant match and caller is a company member."""
        start_time = time.time()

        try:
            record: Optional[Field] = self.field_model.find_one(id=entity_id)
            if record is None:
                result = False
            else:
                parent_tenant_id: Optional[int] = None
                envelope_id = getattr(record, "envelope_id", None)
                template_id = getattr(record, "template_id", None)
                if envelope_id is not None:
                    parent: Optional[Envelope] = self.envelope_model.find_one(id=envelope_id)
                    parent_tenant_id = (
                        getattr(parent, "tenant_id", None) if parent is not None else None
                    )
                elif template_id is not None:
                    template_parent: Optional[Template] = self.template_model.find_one(
                        id=template_id
                    )
                    parent_tenant_id = (
                        getattr(template_parent, "tenant_id", None)
                        if template_parent is not None
                        else None
                    )
                if parent_tenant_id != tenant_id:
                    result = False
                else:
                    result = self.company_model.exists(user_id=user_id, tenant_id=tenant_id)
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

    def filter_by_envelope_id(self, envelope_id: int) -> List[Field]:
        """Filter Field records by envelope_id."""
        start_time = time.time()

        try:
            result = list(self.field_model.find_many(envelope_id=envelope_id))
            end_time = time.time()
            self.logger.info(
                "Query execution succeeded for filter_by_envelope_id",
                start_time=start_time,
                end_time=end_time,
                duration_ms=(end_time - start_time) * 1000,
                details={"envelope_id": envelope_id},
            )
            return result

        except Exception as exc:
            end_time = time.time()
            self.logger.error(
                "Query execution failed for filter_by_envelope_id",
                start_time=start_time,
                end_time=end_time,
                duration_ms=(end_time - start_time) * 1000,
                details={"envelope_id": envelope_id},
                error=str(exc),
                exc=exc,
            )
            raise exc

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "FieldRepository"
