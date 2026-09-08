
from orchestrator.api.v1.sourcing.list_sourced_profiles import ListSourcedProfilesService

class TestListSourcedProfilesService:

    def test_service_instantiation(self) -> None:
        service = ListSourcedProfilesService()
        assert service is not None
        assert hasattr(service, 'execute') or hasattr(service, 'process') or hasattr(service, 'run') or hasattr(service, 'name')

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestListSourcedProfilesService"

