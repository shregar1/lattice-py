"""Base abstraction for requisition repository service."""

from .abstraction import IAtomicRepositoryService


class IRequisitionRepositoryService(IAtomicRepositoryService):
    """Marker base for requisition repository service."""
    @property
    def name(self) -> str:
        """Returns the class name."""
        return "IRequisitionRepositoryService"
