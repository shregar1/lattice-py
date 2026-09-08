
from repositories.lookup.job_domain_lk import JobDomainLKRepository

class TestJobDomainLKRepository:

    def test_repository_instantiation(self) -> None:
        repo = JobDomainLKRepository()
        assert repo is not None
        assert repo.model_class is not None

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestJobDomainLKRepository"

