from exceptions import BadInputException
"""Update dedup_group_candidate repository service module."""

from datetime import datetime
from rivex import Dependency
from typing import Any, Optional

from abstractions import DTOLayer
from constants import Service
from dtos import UpdateDedupGroupCandidateInputDTO
from dependencies import DedupGroupCandidateRepositoryDependency
from repositories import DedupGroupCandidateRepository
from models import DedupGroupCandidate
from .abstraction import IDedupGroupCandidateRepositoryService


class UpdateDedupGroupCandidateService(IDedupGroupCandidateRepositoryService):
    """Application service for update operation on dedup_group_candidate repository."""

    def __init__(
        self,
        urn: Optional[str] = None,
        user_id: Optional[int] = None,
        user_urn: Optional[str] = None,
        tenant_id: Optional[int] = None,
        tenant_urn: Optional[str] = None,
        api_name: Optional[str] = None,
        ip_address: Optional[str] = None,
        user_agent: Optional[str] = None,
        dedup_group_candidate_repository: DedupGroupCandidateRepository = Dependency(DedupGroupCandidateRepositoryDependency),
        *args: Any,
        **kwargs: Any,
    ) -> None:

        super().__init__(
            urn=urn,
            user_urn=user_urn,
            user_id=user_id,
            tenant_urn=tenant_urn,
            tenant_id=tenant_id,
            api_name=api_name,
            ip_address=ip_address,
            user_agent=user_agent,
            *args,
            **kwargs,
        )
        self.dedup_group_candidate_repository = dedup_group_candidate_repository

    async def run(self, request: UpdateDedupGroupCandidateServiceDTO) -> DTOLayer:
        """Executes update business logic for dedup_group_candidate."""
        self.logger.info("Executing service run", service=self.name)

        if request.user_id is None or request.tenant_id is None:
            raise BadInputException("user_id and tenant_id are required")

        try:

            dedup_group_candidate: DedupGroupCandidate = DedupGroupCandidate.build(
            candidate_id=request.candidate_id,
            dedup_group_id=request.dedup_group_id,
            is_deleted=request.is_deleted,
            updated_at=datetime.now()
            )

            return self.dedup_group_candidate_repository.update(model=dedup_group_candidate)

        except Exception as exc:
            self.logger.error("Service execution failed", service=self.name, error=str(exc), exc=exc)
            raise exc

        finally:
            self.logger.info("Service execution completed", service=self.name)

    @property
    def name(self) -> str:
        """Returns the class name."""
        return Service.UPDATE_DEDUP_GROUP_CANDIDATE_SERVICE
