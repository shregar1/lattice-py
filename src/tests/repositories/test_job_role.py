
from repositories.job.job_role import JobRoleRepository

class TestJobRoleRepository:

    def test_repository_instantiation(self) -> None:
        repo = JobRoleRepository()
        assert repo is not None
        assert repo.model_class is not None

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestJobRoleRepository"

