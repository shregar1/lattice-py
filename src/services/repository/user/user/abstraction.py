"""Base abstraction for user repository service."""

from .abstraction import IAtomicRepositoryService


class IUserRepositoryService(IAtomicRepositoryService):
    """Marker base for user repository service."""
    @property
    def name(self) -> str:
        """Returns the class name."""
        return "IUserRepositoryService"
