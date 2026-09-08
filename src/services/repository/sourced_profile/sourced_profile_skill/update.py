from exceptions import BadInputException
"""Update sourced_profile_skill repository service module."""

from datetime import datetime
from rivex import Dependency
from typing import Any, Optional

from abstractions import DTOLayer
from constants import Service
from dtos import UpdateSourcedProfileSkillServiceDTO
from dependencies import SourcedProfileSkillRepositoryDependency
from repositories import SourcedProfileSkillRepository
from models import SourcedProfileSkill
from .abstraction import ISourcedProfileSkillRepositoryService


class UpdateSourcedProfileSkillService(ISourcedProfileSkillRepositoryService):
    """Application service for update operation on sourced_profile_skill repository."""

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
        sourced_profile_skill_repository: SourcedProfileSkillRepository = Dependency(SourcedProfileSkillRepositoryDependency),
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
        self.sourced_profile_skill_repository = sourced_profile_skill_repository

    async def run(self, request: UpdateSourcedProfileSkillServiceDTO) -> DTOLayer:
        """Executes update business logic for sourced_profile_skill."""
        self.logger.info("Executing service run", service=self.name)

        if request.user_id is None or request.tenant_id is None:
            raise BadInputException("user_id and tenant_id are required")

        try:

            sourced_profile_skill: SourcedProfileSkill = SourcedProfileSkill.build(
            sourced_profile_id=request.sourced_profile_id,
            skill_id=request.skill_id,
            is_deleted=request.is_deleted,
            updated_at=datetime.now()
            )

            return self.sourced_profile_skill_repository.update(model=sourced_profile_skill)

        except Exception as exc:
            self.logger.error("Service execution failed", service=self.name, error=str(exc), exc=exc)
            raise exc

        finally:
            self.logger.info("Service execution completed", service=self.name)

    @property
    def name(self) -> str:
        """Returns the class name."""
        return Service.UPDATE_SOURCED_PROFILE_SKILL_SERVICE
