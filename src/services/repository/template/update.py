from exceptions import BadInputException
"""Update template repository service module."""

from datetime import datetime
from rivex import Dependency
from typing import Any, Optional

from abstractions import DTOLayer
from constants import Service
from dtos import UpdateTemplateServiceDTO
from dependencies import TemplateRepositoryDependency
from repositories import TemplateRepository
from models import Template
from .abstraction import ITemplateRepositoryService


class UpdateTemplateService(ITemplateRepositoryService):
    """Application service for update operation on template repository."""

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
        template_repository: TemplateRepository = Dependency(TemplateRepositoryDependency),
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
        self.template_repository = template_repository

    async def run(self, request: UpdateTemplateServiceDTO) -> DTOLayer:
        """Executes update business logic for template."""
        self.logger.info("Executing service run", service=self.name)

        if request.user_id is None or request.tenant_id is None:
            raise BadInputException("user_id and tenant_id are required")

        try:

            template: Template = Template.build(
            label=request.label,
            subject=request.subject,
            body=request.body,
            is_system=request.is_system,
            template_type_id=request.template_type_id,
            is_deleted=request.is_deleted,
            updated_at=datetime.now()
            )

            return self.template_repository.update(model=template)

        except Exception as exc:
            self.logger.error("Service execution failed", service=self.name, error=str(exc), exc=exc)
            raise exc

        finally:
            self.logger.info("Service execution completed", service=self.name)

    @property
    def name(self) -> str:
        """Returns the class name."""
        return Service.UPDATE_TEMPLATE_SERVICE
