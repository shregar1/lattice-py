"""Base abstraction for template_type_lk repository service."""

from .abstraction import IAtomicRepositoryService


class ITemplateTypeLKRepositoryService(IAtomicRepositoryService):
    """Marker base for template_type_lk repository service."""
    @property
    def name(self) -> str:
        """Returns the class name."""
        return "ITemplateTypeLKRepositoryService"
