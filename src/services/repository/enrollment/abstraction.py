"""Base abstraction for enrollment repository service."""

from .abstraction import IAtomicRepositoryService


class IEnrollmentRepositoryService(IAtomicRepositoryService):
    """Marker base for enrollment repository service."""
    @property
    def name(self) -> str:
        """Returns the class name."""
        return "IEnrollmentRepositoryService"
