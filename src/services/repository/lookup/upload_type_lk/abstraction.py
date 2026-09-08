"""Base abstraction for upload_type_lk repository service."""

from .abstraction import IAtomicRepositoryService


class IUploadTypeLKRepositoryService(IAtomicRepositoryService):
    """Marker base for upload_type_lk repository service."""
    @property
    def name(self) -> str:
        """Returns the class name."""
        return "IUploadTypeLKRepositoryService"
