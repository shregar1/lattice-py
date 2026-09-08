from exceptions import BadInputException
"""Create interview_kit repository service module."""

from datetime import datetime
from rivex import Dependency
from typing import Any, Optional

from abstractions import DTOLayer
from constants import Service
from dtos import CreateInterviewKitServiceDTO
from dependencies import InterviewKitRepositoryDependency
from repositories import InterviewKitRepository
from .abstraction import InterviewKit
from .abstraction import IInterviewKitRepositoryService


class CreateInterviewKitService(IInterviewKitRepositoryService):
    """Application service for create operation on interview_kit repository."""

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
        interview_kit_repository: InterviewKitRepository = Dependency(InterviewKitRepositoryDependency),
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
        self.interview_kit_repository = interview_kit_repository

    async def run(self, request: CreateInterviewKitServiceDTO) -> DTOLayer:
        """Executes create business logic for interview_kit."""
        self.logger.info("Executing service run", service=self.name)

        if request.user_id is None or request.tenant_id is None:
            raise BadInputException("user_id and tenant_id are required")

        try:

            interview_kit: InterviewKit = InterviewKit.build(
            title=request.title,
            interview_type_id=request.interview_type_id,
            domain_id=request.domain_id,
            is_deleted=request.is_deleted,
            is_active=request.is_active,
            created_at=datetime.now(),
            created_by=request.created_by,
            )

            return self.interview_kit_repository.create(model=interview_kit)

        except Exception as exc:
            self.logger.error("Service execution failed", service=self.name, error=str(exc), exc=exc)
            raise exc

        finally:
            self.logger.info("Service execution completed", service=self.name)

    @property
    def name(self) -> str:
        """Returns the class name."""
        return Service.CREATE_INTERVIEW_KIT_SERVICE
