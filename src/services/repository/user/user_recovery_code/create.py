from exceptions import BadInputException
"""Create user_recovery_code repository service module."""

from datetime import datetime
from rivex import Dependency
from typing import Any, Optional

from abstractions import DTOLayer
from constants import Service
from dtos import CreateUserRecoveryCodeServiceDTO
from dependencies import UserRecoveryCodeRepositoryDependency
from repositories import UserRecoveryCodeRepository
from models import UserRecoveryCode
from .abstraction import IUserRecoveryCodeRepositoryService


class CreateUserRecoveryCodeService(IUserRecoveryCodeRepositoryService):
    """Application service for create operation on user_recovery_code repository."""

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
        user_recovery_code_repository: UserRecoveryCodeRepository = Dependency(UserRecoveryCodeRepositoryDependency),
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
        self.user_recovery_code_repository = user_recovery_code_repository

    async def run(self, request: CreateUserRecoveryCodeServiceDTO) -> DTOLayer:
        """Executes create business logic for user_recovery_code."""
        self.logger.info("Executing service run", service=self.name)

        if request.user_id is None or request.tenant_id is None:
            raise BadInputException("user_id and tenant_id are required")

        try:

            user_recovery_code: UserRecoveryCode = UserRecoveryCode.build(
            code_hash=request.code_hash,
            is_used=request.is_used,
            is_deleted=request.is_deleted,
            is_active=request.is_active,
            created_at=datetime.now(),
            created_by=request.created_by,
            )

            return self.user_recovery_code_repository.create(model=user_recovery_code)

        except Exception as exc:
            self.logger.error("Service execution failed", service=self.name, error=str(exc), exc=exc)
            raise exc

        finally:
            self.logger.info("Service execution completed", service=self.name)

    @property
    def name(self) -> str:
        """Returns the class name."""
        return Service.CREATE_USER_RECOVERY_CODE_SERVICE
