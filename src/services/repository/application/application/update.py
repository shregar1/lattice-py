"""Update application repository service module."""

from datetime import datetime
from rivex import Dependency
from typing import Any, Optional

from abstractions import DTOLayer
from constants import Service

from dtos import UpdateApplicationServiceDTO
from dependencies import CompositeApplicationRepositoryDependency, ApplicationRepositoryDependency, CandidateRepositoryDependency
from exceptions import BadInputException, ForbiddenException
from repositories import ApplicationRepository, CandidateRepository
from models import Application
from .abstraction import IApplicationRepositoryService


class UpdateApplicationService(IApplicationRepositoryService):
    """Application service for update operation on application repository."""

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
        application_repository: ApplicationRepository = Dependency(ApplicationRepositoryDependency),
        candidate_repository: CandidateRepository = Dependency(CandidateRepositoryDependency),
                composite_application_repository: CompositeApplicationRepository = Dependency(CompositeApplicationRepositoryDependency),
        *args: Any,
        **kwargs: Any,
    ) -> None:

        self.composite_application_repository = composite_application_repository
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
        self.application_repository = application_repository
        self.candidate_repository = candidate_repository

    async def run(self, request: UpdateApplicationServiceDTO) -> DTOLayer:
        """Executes update business logic for application."""
        self.logger.info("Executing service run", service=self.name)

        if request.user_id is None or request.tenant_id is None:
            raise BadInputException("user_id and tenant_id are required")

        try:
            if request.id is not None:
                if not self.composite_application_repository.exists_by_id_user_and_tenant(
                    application_id=request.id,
                    user_id=request.user_id,
                    tenant_id=request.tenant_id,
                ):
                    raise BadInputException("Forbidden or resource does not exist for current user and tenant")
            # Single-query JOIN IDOR Check across Application -> Candidate
            if request.id and not self.application_repository.exists_by_id_candidate_user_and_tenant(
                application_id=request.id,
                user_id=request.user_id,
                tenant_id=request.tenant_id,
            ):
                raise ForbiddenException("User does not have permission to modify this application resource.")

            application: Application = Application.build(
                rating=request.rating,
                source=request.source,
                archive_reason=request.archive_reason,
                applied_at=request.applied_at,
                stage_entered_at=request.stage_entered_at,
                candidate_id=request.candidate_id,
                job_id=request.job_id,
                stage_id=request.stage_id,
                is_deleted=request.is_deleted,
                updated_at=datetime.now()
            )

            return self.application_repository.update(model=application)

        except Exception as exc:
            self.logger.error("Service execution failed", service=self.name, error=str(exc), exc=exc)
            raise exc

        finally:
            self.logger.info("Service execution completed", service=self.name)

    @property
    def name(self) -> str:
        """Returns the class name."""
        return Service.UPDATE_APPLICATION_SERVICE
