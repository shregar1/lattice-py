
from repositories.lookup.job_role_level_lk import JobRoleLevelLKRepository

class TestJobRoleLevelLKRepository:

    def test_repository_instantiation(self) -> None:
        repo = JobRoleLevelLKRepository()
        assert repo is not None
        assert repo.model_class is not None

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestJobRoleLevelLKRepository"

