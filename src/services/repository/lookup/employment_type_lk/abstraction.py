"""Base abstraction for employment_type_lk repository service."""

from .abstraction import IAtomicRepositoryService


class IEmploymentTypeLKRepositoryService(IAtomicRepositoryService):
    """Marker base for employment_type_lk repository service."""
    @property
    def name(self) -> str:
        """Returns the class name."""
        return "IEmploymentTypeLKRepositoryService"
