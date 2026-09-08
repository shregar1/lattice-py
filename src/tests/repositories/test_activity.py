
from repositories.activity import ActivityRepository

class TestActivityRepository:

    def test_repository_instantiation(self) -> None:
        repo = ActivityRepository()
        assert repo is not None
        assert repo.model_class is not None

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestActivityRepository"

