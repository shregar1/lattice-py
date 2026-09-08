
from repositories.job.job_skill import JobSkillRepository

class TestJobSkillRepository:

    def test_repository_instantiation(self) -> None:
        repo = JobSkillRepository()
        assert repo is not None
        assert repo.model_class is not None

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestJobSkillRepository"

