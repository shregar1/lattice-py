"""Base abstraction for candidate_upload repository service."""

from .abstraction import IAtomicRepositoryService


class ICandidateUploadRepositoryService(IAtomicRepositoryService):
    """Marker base for candidate_upload repository service."""
    @property
    def name(self) -> str:
        """Returns the class name."""
        return "ICandidateUploadRepositoryService"
