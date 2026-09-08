
from repositories.application.application_pipeline import ApplicationPipelineRepository

class TestApplicationPipelineRepository:

    def test_repository_instantiation(self) -> None:
        repo = ApplicationPipelineRepository()
        assert repo is not None
        assert repo.model_class is not None

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestApplicationPipelineRepository"

