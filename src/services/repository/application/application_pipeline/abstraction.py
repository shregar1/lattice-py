"""Base abstraction for application_pipeline repository service."""

from .abstraction import IAtomicRepositoryService


class IApplicationPipelineRepositoryService(IAtomicRepositoryService):
    """Marker base for application_pipeline repository service."""
    @property
    def name(self) -> str:
        """Returns the class name."""
        return "IApplicationPipelineRepositoryService"
