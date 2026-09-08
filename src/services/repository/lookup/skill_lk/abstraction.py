"""Base abstraction for skill_lk repository service."""

from .abstraction import IAtomicRepositoryService


class ISkillLKRepositoryService(IAtomicRepositoryService):
    """Marker base for skill_lk repository service."""
    @property
    def name(self) -> str:
        """Returns the class name."""
        return "ISkillLKRepositoryService"
