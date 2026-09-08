"""Base abstraction for e_signature repository service."""

from .abstraction import IAtomicRepositoryService


class IESignatureRepositoryService(IAtomicRepositoryService):
    """Marker base for e_signature repository service."""
    @property
    def name(self) -> str:
        """Returns the class name."""
        return "IESignatureRepositoryService"
