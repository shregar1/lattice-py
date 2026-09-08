"""Base abstraction for user_recovery_code repository service."""

from .abstraction import IAtomicRepositoryService


class IUserRecoveryCodeRepositoryService(IAtomicRepositoryService):
    """Marker base for user_recovery_code repository service."""
    @property
    def name(self) -> str:
        """Returns the class name."""
        return "IUserRecoveryCodeRepositoryService"
