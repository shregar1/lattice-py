"""Repository implementation for ProjectTemplate."""

import time
from typing import Any, List, Optional

from rivex import Dependency

from dependencies.model import (
    CompanyDependency,
    ProjectDependency,
    ProjectTemplateDependency,
    TenantDependency,
    UserDependency,
)
from dependencies.utility import LoggerUtilityDependency
from models import Company, Project, ProjectTemplate, Tenant, User
from repositories.atomic import ProjectTemplateRepository as AtomicProjectTemplateRepository
from utilities import Logger

from ..abstraction import ICompositeRepository


class ProjectTemplateRepository(AtomicProjectTemplateRepository, ICompositeRepository):
    """Repository for ProjectTemplate; extends AtomicProjectTemplateRepository."""

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
        model: type[ProjectTemplate] = Dependency(ProjectTemplateDependency),
        company_model: type[Company] = Dependency(CompanyDependency),
        project_model: type[Project] = Dependency(ProjectDependency),
        tenant_model: type[Tenant] = Dependency(TenantDependency),
        user_model: type[User] = Dependency(UserDependency),
        *args: Any,
        **kwargs: Any,
    ) -> None:
        AtomicProjectTemplateRepository.__init__(
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
        self.project_template_model = model
        self.company_model = company_model
        self.project_model = project_model
        self.tenant_model = tenant_model
        self.user_model = user_model

    def exists_by_id_user_and_tenant(
        self,
        entity_id: int,
        user_id: int,
        tenant_id: int,
    ) -> bool:
        """Prevents IDOR: parent project tenant match and caller is a company member."""
        start_time = time.time()

        try:
            record: Optional[ProjectTemplate] = self.project_template_model.find_one(id=entity_id)
            if record is None:
                result = False
            else:
                parent: Optional[Project] = self.project_model.find_one(
                    id=getattr(record, "project_id")
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

    def filter_by_project_id(self, project_id: int) -> List[ProjectTemplate]:
        """Filter ProjectTemplate records by project_id."""
        start_time = time.time()

        try:
            result = list(self.project_template_model.find_many(project_id=project_id))
            end_time = time.time()
            self.logger.info(
                "Query execution succeeded for filter_by_project_id",
                start_time=start_time,
                end_time=end_time,
                duration_ms=(end_time - start_time) * 1000,
                details={"project_id": project_id},
            )
            return result

        except Exception as exc:
            end_time = time.time()
            self.logger.error(
                "Query execution failed for filter_by_project_id",
                start_time=start_time,
                end_time=end_time,
                duration_ms=(end_time - start_time) * 1000,
                details={"project_id": project_id},
                error=str(exc),
                exc=exc,
            )
            raise exc

    def filter_by_template_id(self, template_id: int) -> List[ProjectTemplate]:
        """Filter ProjectTemplate records by template_id."""
        start_time = time.time()

        try:
            result = list(self.project_template_model.find_many(template_id=template_id))
            end_time = time.time()
            self.logger.info(
                "Query execution succeeded for filter_by_template_id",
                start_time=start_time,
                end_time=end_time,
                duration_ms=(end_time - start_time) * 1000,
                details={"template_id": template_id},
            )
            return result

        except Exception as exc:
            end_time = time.time()
            self.logger.error(
                "Query execution failed for filter_by_template_id",
                start_time=start_time,
                end_time=end_time,
                duration_ms=(end_time - start_time) * 1000,
                details={"template_id": template_id},
                error=str(exc),
                exc=exc,
            )
            raise exc

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "ProjectTemplateRepository"
