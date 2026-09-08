from exceptions import BadInputException
"""Create e_signature repository service module."""

from datetime import datetime
from rivex import Dependency
from typing import Any, Optional

from abstractions import DTOLayer
from constants import Service
from dtos import CreateESignatureInputDTO
from dependencies import ESignatureRepositoryDependency
from repositories import ESignatureRepository
from models import ESignature
from .abstraction import IESignatureRepositoryService


class CreateESignatureService(IESignatureRepositoryService):
    """Application service for create operation on e_signature repository."""

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
        e_signature_repository: ESignatureRepository = Dependency(ESignatureRepositoryDependency),
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
        self.e_signature_repository = e_signature_repository

    async def run(self, request: CreateESignatureInputDTO) -> DTOLayer:
        """Executes create business logic for e_signature."""
        self.logger.info("Executing service run", service=self.name)

        if request.user_id is None or request.tenant_id is None:
            raise BadInputException("user_id and tenant_id are required")

        try:

            e_signature: ESignature = ESignature.build(
            signer=request.signer,
            sent_at=request.sent_at,
            signed_at=request.signed_at,
            offer_id=request.offer_id,
            status_id=request.status_id,
            is_deleted=request.is_deleted,
            is_active=request.is_active,
            created_at=datetime.now(),
            created_by=request.created_by,
            )

            return self.e_signature_repository.create(model=e_signature)

        except Exception as exc:
            self.logger.error("Service execution failed", service=self.name, error=str(exc), exc=exc)
            raise exc

        finally:
            self.logger.info("Service execution completed", service=self.name)

    @property
    def name(self) -> str:
        """Returns the class name."""
        return Service.CREATE_E_SIGNATURE_SERVICE
