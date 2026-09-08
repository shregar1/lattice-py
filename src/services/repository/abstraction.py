"""Base abstraction for repository-layer services."""

from .abstraction import IService


class IAtomicRepositoryService(IService):
    """Marker base for repository-backed application services."""
    @property
    def name(self) -> str:
        """Returns the class name."""
        return "IAtomicRepositoryService"
