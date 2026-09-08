"""Base abstraction for user_otp repository service."""

from .abstraction import IAtomicRepositoryService


class IUserOtpRepositoryService(IAtomicRepositoryService):
    """Marker base for user_otp repository service."""
    @property
    def name(self) -> str:
        """Returns the class name."""
        return "IUserOtpRepositoryService"
