from exceptions import BadInputException
"""Update application_pipeline repository service module."""

from datetime import datetime
from rivex import Dependency
from typing import Any, Optional

from abstractions import DTOLayer
from constants import Service
from dtos import UpdateApplicationPipelineServiceDTO
from dependencies import CompositeApplicationPipelineRepositoryDependency, ApplicationPipelineRepositoryDependency
from repositories import ApplicationPipelineRepository
from models import ApplicationPipeline
from .abstraction import IApplicationPipelineRepositoryService


class UpdateApplicationPipelineService(IApplicationPipelineRepositoryService):
    """Application service for update operation on application_pipeline repository."""

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
        application_pipeline_repository: ApplicationPipelineRepository = Dependency(ApplicationPipelineRepositoryDependency),
                composite_application_pipeline_repository: CompositeApplicationPipelineRepository = Dependency(CompositeApplicationPipelineRepositoryDependency),
        *args: Any,
        **kwargs: Any,
    ) -> None:

        self.composite_application_pipeline_repository = composite_application_pipeline_repository
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
        self.application_pipeline_repository = application_pipeline_repository

    async def run(self, request: UpdateApplicationPipelineServiceDTO) -> DTOLayer:
        """Executes update business logic for application_pipeline."""
        self.logger.info("Executing service run", service=self.name)

        if request.user_id is None or request.tenant_id is None:
            raise BadInputException("user_id and tenant_id are required")

        try:
            if request.id is not None:
                if not self.composite_application_pipeline_repository.exists_by_id_user_and_tenant(
                    pipeline_id=request.id,
                    user_id=request.user_id,
                    tenant_id=request.tenant_id,
                ):
                    raise BadInputException("Forbidden or resource does not exist for current user and tenant")

            application_pipeline: ApplicationPipeline = ApplicationPipeline.build(
            at=request.at,
            application_id=request.application_id,
            from_stage_id=request.from_stage_id,
            to_stage_id=request.to_stage_id,
            user_id=request.user_id,
            is_deleted=request.is_deleted,
            updated_at=datetime.now()
            )

            return self.application_pipeline_repository.update(model=application_pipeline)

        except Exception as exc:
            self.logger.error("Service execution failed", service=self.name, error=str(exc), exc=exc)
            raise exc

        finally:
            self.logger.info("Service execution completed", service=self.name)

    @property
    def name(self) -> str:
        """Returns the class name."""
        return Service.UPDATE_APPLICATION_PIPELINE_SERVICE
