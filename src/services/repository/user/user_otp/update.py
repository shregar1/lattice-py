from exceptions import BadInputException
"""Update user_otp repository service module."""

from datetime import datetime
from rivex import Dependency
from typing import Any, Optional

from abstractions import DTOLayer
from constants import Service
from dtos import UpdateUserOtpServiceDTO
from dependencies import UserOtpRepositoryDependency
from repositories import UserOtpRepository
from models import UserOtp
from .abstraction import IUserOtpRepositoryService


class UpdateUserOtpService(IUserOtpRepositoryService):
    """Application service for update operation on user_otp repository."""

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

    async def run(self, request: UpdateUserOtpServiceDTO) -> DTOLayer:
        """Executes update business logic for user_otp."""
        self.logger.info("Executing service run", service=self.name)

        if request.user_id is None or request.tenant_id is None:
            raise BadInputException("user_id and tenant_id are required")

        try:

            user_otp: UserOtp = UserOtp.build(
            otp_hash=request.otp_hash,
            expires_at=request.expires_at,
            attempts=request.attempts,
            verified_at=request.verified_at,
            otp_type_id=request.otp_type_id,
            is_deleted=request.is_deleted,
            updated_at=datetime.now()
            )

            return self.user_otp_repository.update(model=user_otp)

        except Exception as exc:
            self.logger.error("Service execution failed", service=self.name, error=str(exc), exc=exc)
            raise exc

        finally:
            self.logger.info("Service execution completed", service=self.name)

    @property
    def name(self) -> str:
        """Returns the class name."""
        return Service.UPDATE_USER_OTP_SERVICE
