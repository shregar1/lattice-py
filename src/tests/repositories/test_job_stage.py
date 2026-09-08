
from repositories.job.job_stage import JobStageRepository

class TestJobStageRepository:

    def test_repository_instantiation(self) -> None:
        repo = JobStageRepository()
        assert repo is not None
        assert repo.model_class is not None

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestJobStageRepository"

