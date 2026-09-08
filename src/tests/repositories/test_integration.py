
from repositories.integration import IntegrationRepository

class TestIntegrationRepository:

    def test_repository_instantiation(self) -> None:
        repo = IntegrationRepository()
        assert repo is not None
        assert repo.model_class is not None

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestIntegrationRepository"

