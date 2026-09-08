"""Base abstraction for sourced_profile_skill repository service."""

from .abstraction import IAtomicRepositoryService


class ISourcedProfileSkillRepositoryService(IAtomicRepositoryService):
    """Marker base for sourced_profile_skill repository service."""
    @property
    def name(self) -> str:
        """Returns the class name."""
        return "ISourcedProfileSkillRepositoryService"
