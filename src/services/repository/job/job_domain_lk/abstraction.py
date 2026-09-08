"""Base abstraction for job_domain_lk repository service."""

from .abstraction import IAtomicRepositoryService


class IJobDomainLKRepositoryService(IAtomicRepositoryService):
    """Marker base for job_domain_lk repository service."""
    @property
    def name(self) -> str:
        """Returns the class name."""
        return "IJobDomainLKRepositoryService"
