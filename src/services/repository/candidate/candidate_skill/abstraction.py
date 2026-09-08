"""Base abstraction for candidate_skill repository service."""

from .abstraction import IAtomicRepositoryService


class ICandidateSkillRepositoryService(IAtomicRepositoryService):
    """Marker base for candidate_skill repository service."""
    @property
    def name(self) -> str:
        """Returns the class name."""
        return "ICandidateSkillRepositoryService"
