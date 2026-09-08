
from repositories.config.employment_config import EmploymentConfigRepository

class TestEmploymentConfigRepository:

    def test_repository_instantiation(self) -> None:
        repo = EmploymentConfigRepository()
        assert repo is not None
        assert repo.model_class is not None

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestEmploymentConfigRepository"

