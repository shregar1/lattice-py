from exceptions import BadInputException
"""Create board_posting repository service module."""

from datetime import datetime
from rivex import Dependency
from typing import Any, Optional

from abstractions import DTOLayer
from constants import Service
from dtos import CreateBoardPostingServiceDTO
from dependencies import CompositeBoardPostingRepositoryDependency, BoardPostingRepositoryDependency
from repositories import BoardPostingRepository
from models import BoardPosting
from .abstraction import IBoardPostingRepositoryService


class CreateBoardPostingService(IBoardPostingRepositoryService):
    """Application service for create operation on board_posting repository."""

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
        board_posting_repository: BoardPostingRepository = Dependency(BoardPostingRepositoryDependency),
                composite_board_posting_repository: CompositeBoardPostingRepository = Dependency(CompositeBoardPostingRepositoryDependency),
        *args: Any,
        **kwargs: Any,
    ) -> None:

        self.composite_board_posting_repository = composite_board_posting_repository
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
        self.board_posting_repository = board_posting_repository

    async def run(self, request: CreateBoardPostingServiceDTO) -> DTOLayer:
        """Executes create business logic for board_posting."""
        self.logger.info("Executing service run", service=self.name)

        if request.user_id is None or request.tenant_id is None:
            raise BadInputException("user_id and tenant_id are required")

        try:
            if request.id is not None:
                if not self.composite_board_posting_repository.exists_by_id_user_and_tenant(
                    board_posting_id=request.id,
                    user_id=request.user_id,
                    tenant_id=request.tenant_id,
                ):
                    raise BadInputException("Forbidden or resource does not exist for current user and tenant")

            board_posting: BoardPosting = BoardPosting.build(
            board=request.board,
            url=request.url,
            posted_at=request.posted_at,
            job_id=request.job_id,
            status_id=request.status_id,
            is_deleted=request.is_deleted,
            is_active=request.is_active,
            created_at=datetime.now(),
            created_by=request.created_by,
            )

            return self.board_posting_repository.create(model=board_posting)

        except Exception as exc:
            self.logger.error("Service execution failed", service=self.name, error=str(exc), exc=exc)
            raise exc

        finally:
            self.logger.info("Service execution completed", service=self.name)

    @property
    def name(self) -> str:
        """Returns the class name."""
        return Service.CREATE_BOARD_POSTING_SERVICE
