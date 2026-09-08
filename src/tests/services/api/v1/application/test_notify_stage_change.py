
from orchestrator.api.v1.application.notify_stage_change import NotifyStageChangeService

class TestNotifyStageChangeService:

    def test_service_instantiation(self) -> None:
        service = NotifyStageChangeService()
        assert service is not None
        assert hasattr(service, 'execute') or hasattr(service, 'process') or hasattr(service, 'run') or hasattr(service, 'name')

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestNotifyStageChangeService"

