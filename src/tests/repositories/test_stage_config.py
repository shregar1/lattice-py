
from repositories.config.stage_config import StageConfigRepository

class TestStageConfigRepository:

    def test_repository_instantiation(self) -> None:
        repo = StageConfigRepository()
        assert repo is not None
        assert repo.model_class is not None

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestStageConfigRepository"

