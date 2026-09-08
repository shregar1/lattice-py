from exceptions import BadInputException
"""Update candidate_upload repository service module."""

from datetime import datetime
from rivex import Dependency
from typing import Any, Optional

from abstractions import DTOLayer
from constants import Service
from dtos import UpdateCandidateUploadServiceDTO
from dependencies import CandidateUploadRepositoryDependency
from repositories import CandidateUploadRepository
from models import CandidateUpload
from .abstraction import ICandidateUploadRepositoryService


class UpdateCandidateUploadService(ICandidateUploadRepositoryService):
    """Application service for update operation on candidate_upload repository."""

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
        candidate_upload_repository: CandidateUploadRepository = Dependency(CandidateUploadRepositoryDependency),
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
        self.candidate_upload_repository = candidate_upload_repository

    async def run(self, request: UpdateCandidateUploadServiceDTO) -> DTOLayer:
        """Executes update business logic for candidate_upload."""
        self.logger.info("Executing service run", service=self.name)

        if request.user_id is None or request.tenant_id is None:
            raise BadInputException("user_id and tenant_id are required")

        try:

            candidate_upload: CandidateUpload = CandidateUpload.build(
            file_name=request.file_name,
            file_size_bytes=request.file_size_bytes,
            url=request.url,
            content_type=request.content_type,
            candidate_id=request.candidate_id,
            upload_type_id=request.upload_type_id,
            uploaded_by_id=request.uploaded_by_id,
            is_deleted=request.is_deleted,
            updated_at=datetime.now()
            )

            return self.candidate_upload_repository.update(model=candidate_upload)

        except Exception as exc:
            self.logger.error("Service execution failed", service=self.name, error=str(exc), exc=exc)
            raise exc

        finally:
            self.logger.info("Service execution completed", service=self.name)

    @property
    def name(self) -> str:
        """Returns the class name."""
        return Service.UPDATE_CANDIDATE_UPLOAD_SERVICE
