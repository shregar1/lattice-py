from exceptions import BadInputException
"""Update saved_report repository service module."""

from datetime import datetime
from rivex import Dependency
from typing import Any, Optional

from abstractions import DTOLayer
from constants import Service
from dtos import UpdateSavedReportServiceDTO
from dependencies import SavedReportRepositoryDependency
from repositories import SavedReportRepository
from models import SavedReport
from .abstraction import ISavedReportRepositoryService


class UpdateSavedReportService(ISavedReportRepositoryService):
    """Application service for update operation on saved_report repository."""

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
        saved_report_repository: SavedReportRepository = Dependency(SavedReportRepositoryDependency),
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
        self.saved_report_repository = saved_report_repository

    async def run(self, request: UpdateSavedReportServiceDTO) -> DTOLayer:
        """Executes update business logic for saved_report."""
        self.logger.info("Executing service run", service=self.name)

        if request.user_id is None or request.tenant_id is None:
            raise BadInputException("user_id and tenant_id are required")

        try:

            saved_report: SavedReport = SavedReport.build(
            label=request.label,
            chart=request.chart,
            metric_id=request.metric_id,
            dimension_id=request.dimension_id,
            is_deleted=request.is_deleted,
            updated_at=datetime.now()
            )

            return self.saved_report_repository.update(model=saved_report)

        except Exception as exc:
            self.logger.error("Service execution failed", service=self.name, error=str(exc), exc=exc)
            raise exc

        finally:
            self.logger.info("Service execution completed", service=self.name)

    @property
    def name(self) -> str:
        """Returns the class name."""
        return Service.UPDATE_SAVED_REPORT_SERVICE
