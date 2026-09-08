
from orchestrator.api.v1.sourcing.resolve_dedup_group_record import ResolveDedupGroupRecordService

class TestResolveDedupGroupRecordService:

    def test_service_instantiation(self) -> None:
        service = ResolveDedupGroupRecordService()
        assert service is not None
        assert hasattr(service, 'execute') or hasattr(service, 'process') or hasattr(service, 'run') or hasattr(service, 'name')

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestResolveDedupGroupRecordService"

