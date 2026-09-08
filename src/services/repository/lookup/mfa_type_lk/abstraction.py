"""Base abstraction for mfa_type_lk repository service."""

from .abstraction import IAtomicRepositoryService


class IMfaTypeLKRepositoryService(IAtomicRepositoryService):
    """Marker base for mfa_type_lk repository service."""
    @property
    def name(self) -> str:
        """Returns the class name."""
        return "IMfaTypeLKRepositoryService"
