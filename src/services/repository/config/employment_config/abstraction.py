"""Base abstraction for employment_config repository service."""

from .abstraction import IAtomicRepositoryService


class IEmploymentConfigRepositoryService(IAtomicRepositoryService):
    """Marker base for employment_config repository service."""
    @property
    def name(self) -> str:
        """Returns the class name."""
        return "IEmploymentConfigRepositoryService"
