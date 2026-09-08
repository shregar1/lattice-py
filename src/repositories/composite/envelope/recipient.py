"""Repository implementation for Recipient."""

import time
from typing import Any, List, Optional

from rivex import Dependency

from dependencies.model import (
    CompanyDependency,
    EnvelopeDependency,
    RecipientDependency,
    TenantDependency,
    UserDependency,
)
from dependencies.utility import LoggerUtilityDependency
from models import Company, Envelope, Recipient, Tenant, User
from repositories.atomic import RecipientRepository as AtomicRecipientRepository
from utilities import Logger

from ..abstraction import ICompositeRepository


class RecipientRepository(AtomicRecipientRepository, ICompositeRepository):
    """Repository for Recipient; extends AtomicRecipientRepository."""

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
        model: type[Recipient] = Dependency(RecipientDependency),
        company_model: type[Company] = Dependency(CompanyDependency),
        envelope_model: type[Envelope] = Dependency(EnvelopeDependency),
        tenant_model: type[Tenant] = Dependency(TenantDependency),
        user_model: type[User] = Dependency(UserDependency),
        *args: Any,
        **kwargs: Any,
    ) -> None:
        AtomicRecipientRepository.__init__(
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
        self.recipient_model = model
        self.company_model = company_model
        self.envelope_model = envelope_model
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
            record: Optional[Recipient] = self.recipient_model.find_one(id=entity_id)
            if record is None:
                result = False
            else:
                parent: Optional[Envelope] = self.envelope_model.find_one(
                    id=getattr(record, "envelope_id")
                )
                if parent is None or getattr(parent, "tenant_id") != tenant_id:
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

    def filter_by_envelope_id(self, envelope_id: int) -> List[Recipient]:
        """Filter Recipient records by envelope_id."""
        start_time = time.time()

        try:
            result = list(self.recipient_model.find_many(envelope_id=envelope_id))
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
        return "RecipientRepository"
