"""Base abstraction for auth_type_lk repository service."""

from .abstraction import IAtomicRepositoryService


class IAuthTypeLKRepositoryService(IAtomicRepositoryService):
    """Marker base for auth_type_lk repository service."""
    @property
    def name(self) -> str:
        """Returns the class name."""
        return "IAuthTypeLKRepositoryService"
