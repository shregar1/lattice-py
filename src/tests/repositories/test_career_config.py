
from repositories.config.career_config import CareerConfigRepository

class TestCareerConfigRepository:

    def test_repository_instantiation(self) -> None:
        repo = CareerConfigRepository()
        assert repo is not None
        assert repo.model_class is not None

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestCareerConfigRepository"

