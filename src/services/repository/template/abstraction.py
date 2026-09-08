"""Base abstraction for template repository service."""

from .abstraction import IAtomicRepositoryService


class ITemplateRepositoryService(IAtomicRepositoryService):
    """Marker base for template repository service."""
    @property
    def name(self) -> str:
        """Returns the class name."""
        return "ITemplateRepositoryService"
