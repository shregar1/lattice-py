from exceptions import BadInputException
"""Create dedup_group repository service module."""

from datetime import datetime
from rivex import Dependency
from typing import Any, Optional

from abstractions import DTOLayer
from constants import Service
from dtos import CreateDedupGroupInputDTO
from dependencies import DedupGroupRepositoryDependency
from repositories import DedupGroupRepository
from models import DedupGroup
from .abstraction import IDedupGroupRepositoryService


class CreateDedupGroupService(IDedupGroupRepositoryService):
    """Application service for create operation on dedup_group repository."""

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
        dedup_group_repository: DedupGroupRepository = Dependency(DedupGroupRepositoryDependency),
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
        self.dedup_group_repository = dedup_group_repository

    async def run(self, request: CreateDedupGroupInputDTO) -> DTOLayer:
        """Executes create business logic for dedup_group."""
        self.logger.info("Executing service run", service=self.name)

        if request.user_id is None or request.tenant_id is None:
            raise BadInputException("user_id and tenant_id are required")

        try:

            dedup_group: DedupGroup = DedupGroup.build(
            confidence=request.confidence,
            is_resolved=request.is_resolved,
            reasons=request.reasons,
            is_deleted=request.is_deleted,
            is_active=request.is_active,
            created_at=datetime.now(),
            created_by=request.created_by,
            )

            return self.dedup_group_repository.create(model=dedup_group)

        except Exception as exc:
            self.logger.error("Service execution failed", service=self.name, error=str(exc), exc=exc)
            raise exc

        finally:
            self.logger.info("Service execution completed", service=self.name)

    @property
    def name(self) -> str:
        """Returns the class name."""
        return Service.CREATE_DEDUP_GROUP_SERVICE
