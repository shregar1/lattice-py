"""Base abstraction for requisition_approval repository service."""

from .abstraction import IAtomicRepositoryService


class IRequisitionApprovalRepositoryService(IAtomicRepositoryService):
    """Marker base for requisition_approval repository service."""
    @property
    def name(self) -> str:
        """Returns the class name."""
        return "IRequisitionApprovalRepositoryService"
