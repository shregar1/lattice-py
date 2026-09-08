from exceptions import BadInputException
from constants import DBColumn
"""Delete user_otp repository service module."""

from datetime import datetime
from rivex import Dependency
from typing import Any, Optional

from abstractions import DTOLayer
from constants import Service
from dtos import DeleteUserOtpServiceDTO
from dependencies import UserOtpRepositoryDependency
from repositories import UserOtpRepository
from .abstraction import IUserOtpRepositoryService


class DeleteUserOtpService(IUserOtpRepositoryService):
    """Application service for delete operation on user_otp repository."""

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
        user_otp_repository: UserOtpRepository = Dependency(UserOtpRepositoryDependency),
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
        self.user_otp_repository = user_otp_repository

    async def run(self, request: DeleteUserOtpServiceDTO) -> DTOLayer:
        """Executes delete business logic for record."""
        self.logger.info("Executing service run", service=self.name)

        if request.user_id is None or request.tenant_id is None:
            raise BadInputException("user_id and tenant_id are required")

        try:
            if request.id:
                if request.is_hard_delete:
                    return self.user_otp_repository.hard_delete(id=request.id)
                return self.user_otp_repository.soft_delete(id=request.id)
            return request
        except Exception as exc:
            self.logger.error("Service execution failed", service=self.name, error=str(exc), exc=exc)
            raise exc

        finally:
            self.logger.info("Service execution completed", service=self.name)

    @property
    def name(self) -> str:
        """Returns the class name."""
        return Service.DELETE_USER_OTP_SERVICE
