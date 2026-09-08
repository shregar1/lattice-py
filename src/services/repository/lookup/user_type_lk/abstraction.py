"""Base abstraction for user_type_lk repository service."""

from .abstraction import IAtomicRepositoryService


class IUserTypeLKRepositoryService(IAtomicRepositoryService):
    """Marker base for user_type_lk repository service."""
    @property
    def name(self) -> str:
        """Returns the class name."""
        return "IUserTypeLKRepositoryService"
