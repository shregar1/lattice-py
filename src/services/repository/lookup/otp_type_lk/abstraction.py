"""Base abstraction for otp_type_lk repository service."""

from .abstraction import IAtomicRepositoryService


class IOtpTypeLKRepositoryService(IAtomicRepositoryService):
    """Marker base for otp_type_lk repository service."""
    @property
    def name(self) -> str:
        """Returns the class name."""
        return "IOtpTypeLKRepositoryService"
