
from repositories.job.job_location import JobLocationRepository

class TestJobLocationRepository:

    def test_repository_instantiation(self) -> None:
        repo = JobLocationRepository()
        assert repo is not None
        assert repo.model_class is not None

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestJobLocationRepository"

