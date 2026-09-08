"""Base abstraction for automation_rule repository service."""

from .abstraction import IAtomicRepositoryService


class IAutomationRuleRepositoryService(IAtomicRepositoryService):
    """Marker base for automation_rule repository service."""
    @property
    def name(self) -> str:
        """Returns the class name."""
        return "IAutomationRuleRepositoryService"
