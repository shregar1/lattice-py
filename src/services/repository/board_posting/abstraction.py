"""Base abstraction for board_posting repository service."""

from .abstraction import IAtomicRepositoryService


class IBoardPostingRepositoryService(IAtomicRepositoryService):
    """Marker base for board_posting repository service."""
    @property
    def name(self) -> str:
        """Returns the class name."""
        return "IBoardPostingRepositoryService"
