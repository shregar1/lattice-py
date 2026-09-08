"""Base abstraction for saved_report repository service."""

from .abstraction import IAtomicRepositoryService


class ISavedReportRepositoryService(IAtomicRepositoryService):
    """Marker base for saved_report repository service."""
    @property
    def name(self) -> str:
        """Returns the class name."""
        return "ISavedReportRepositoryService"
