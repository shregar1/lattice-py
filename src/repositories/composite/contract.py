"""Repository implementation for Contract."""

import time
from typing import Any, List, Optional

from rivex import Dependency

from dependencies.model import (
    CompanyDependency,
    ContractDependency,
    TenantDependency,
    UserDependency,
)
from dependencies.utility import LoggerUtilityDependency
from models import Company, Contract, Tenant, User
from repositories.atomic import ContractRepository as AtomicContractRepository
from utilities import Logger

from .abstraction import ICompositeRepository


class ContractRepository(AtomicContractRepository, ICompositeRepository):
    """Repository for Contract; extends AtomicContractRepository."""

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
        model: type[Contract] = Dependency(ContractDependency),
        company_model: type[Company] = Dependency(CompanyDependency),
        tenant_model: type[Tenant] = Dependency(TenantDependency),
        user_model: type[User] = Dependency(UserDependency),
        *args: Any,
        **kwargs: Any,
    ) -> None:
        AtomicContractRepository.__init__(
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
        self.contract_model = model
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
                self.contract_model.exists(id=entity_id, tenant_id=tenant_id)
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

    def filter_by_tenant(self, tenant_id: int) -> List[Contract]:
        """Filter Contract records by tenant_id."""
        start_time = time.time()

        try:
            result = list(self.contract_model.find_many(tenant_id=tenant_id))
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

    def filter_by_employer_id(self, employer_id: int) -> List[Contract]:
        """Filter Contract records by employer_id."""
        start_time = time.time()

        try:
            result = list(self.contract_model.find_many(employer_id=employer_id))
            end_time = time.time()
            self.logger.info(
                "Query execution succeeded for filter_by_employer_id",
                start_time=start_time,
                end_time=end_time,
                duration_ms=(end_time - start_time) * 1000,
                details={"employer_id": employer_id},
            )
            return result

        except Exception as exc:
            end_time = time.time()
            self.logger.error(
                "Query execution failed for filter_by_employer_id",
                start_time=start_time,
                end_time=end_time,
                duration_ms=(end_time - start_time) * 1000,
                details={"employer_id": employer_id},
                error=str(exc),
                exc=exc,
            )
            raise exc

    def filter_by_contractor_id(self, contractor_id: int) -> List[Contract]:
        """Filter Contract records by contractor_id."""
        start_time = time.time()

        try:
            result = list(self.contract_model.find_many(contractor_id=contractor_id))
            end_time = time.time()
            self.logger.info(
                "Query execution succeeded for filter_by_contractor_id",
                start_time=start_time,
                end_time=end_time,
                duration_ms=(end_time - start_time) * 1000,
                details={"contractor_id": contractor_id},
            )
            return result

        except Exception as exc:
            end_time = time.time()
            self.logger.error(
                "Query execution failed for filter_by_contractor_id",
                start_time=start_time,
                end_time=end_time,
                duration_ms=(end_time - start_time) * 1000,
                details={"contractor_id": contractor_id},
                error=str(exc),
                exc=exc,
            )
            raise exc

    def filter_by_candidate_id(self, candidate_id: int) -> List[Contract]:
        """Filter Contract records by candidate_id."""
        start_time = time.time()

        try:
            result = list(self.contract_model.find_many(candidate_id=candidate_id))
            end_time = time.time()
            self.logger.info(
                "Query execution succeeded for filter_by_candidate_id",
                start_time=start_time,
                end_time=end_time,
                duration_ms=(end_time - start_time) * 1000,
                details={"candidate_id": candidate_id},
            )
            return result

        except Exception as exc:
            end_time = time.time()
            self.logger.error(
                "Query execution failed for filter_by_candidate_id",
                start_time=start_time,
                end_time=end_time,
                duration_ms=(end_time - start_time) * 1000,
                details={"candidate_id": candidate_id},
                error=str(exc),
                exc=exc,
            )
            raise exc

    def filter_by_invite_id(self, invite_id: int) -> List[Contract]:
        """Filter Contract records by invite_id."""
        start_time = time.time()

        try:
            result = list(self.contract_model.find_many(invite_id=invite_id))
            end_time = time.time()
            self.logger.info(
                "Query execution succeeded for filter_by_invite_id",
                start_time=start_time,
                end_time=end_time,
                duration_ms=(end_time - start_time) * 1000,
                details={"invite_id": invite_id},
            )
            return result

        except Exception as exc:
            end_time = time.time()
            self.logger.error(
                "Query execution failed for filter_by_invite_id",
                start_time=start_time,
                end_time=end_time,
                duration_ms=(end_time - start_time) * 1000,
                details={"invite_id": invite_id},
                error=str(exc),
                exc=exc,
            )
            raise exc

    def filter_by_status_id(self, status_id: int) -> List[Contract]:
        """Filter Contract records by status_id."""
        start_time = time.time()

        try:
            result = list(self.contract_model.find_many(status_id=status_id))
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

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "ContractRepository"
