from exceptions import BadInputException
"""Update candidate_tag repository service module."""

from datetime import datetime
from rivex import Dependency
from typing import Any, Optional

from abstractions import DTOLayer
from constants import Service
from dtos import UpdateCandidateTagServiceDTO
from dependencies import CandidateTagRepositoryDependency
from repositories import CandidateTagRepository
from models import CandidateTag
from .abstraction import ICandidateTagRepositoryService


class UpdateCandidateTagService(ICandidateTagRepositoryService):
    """Application service for update operation on candidate_tag repository."""

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
        candidate_tag_repository: CandidateTagRepository = Dependency(CandidateTagRepositoryDependency),
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
        self.candidate_tag_repository = candidate_tag_repository

    async def run(self, request: UpdateCandidateTagServiceDTO) -> DTOLayer:
        """Executes update business logic for candidate_tag."""
        self.logger.info("Executing service run", service=self.name)

        if request.user_id is None or request.tenant_id is None:
            raise BadInputException("user_id and tenant_id are required")

        try:

            candidate_tag: CandidateTag = CandidateTag.build(
            label=request.label,
            candidate_id=request.candidate_id,
            is_deleted=request.is_deleted,
            updated_at=datetime.now()
            )

            return self.candidate_tag_repository.update(model=candidate_tag)

        except Exception as exc:
            self.logger.error("Service execution failed", service=self.name, error=str(exc), exc=exc)
            raise exc

        finally:
            self.logger.info("Service execution completed", service=self.name)

    @property
    def name(self) -> str:
        """Returns the class name."""
        return Service.UPDATE_CANDIDATE_TAG_SERVICE
