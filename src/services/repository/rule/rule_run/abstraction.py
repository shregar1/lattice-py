"""Base abstraction for rule_run repository service."""

from .abstraction import IAtomicRepositoryService


class IRuleRunRepositoryService(IAtomicRepositoryService):
    """Marker base for rule_run repository service."""
    @property
    def name(self) -> str:
        """Returns the class name."""
        return "IRuleRunRepositoryService"
