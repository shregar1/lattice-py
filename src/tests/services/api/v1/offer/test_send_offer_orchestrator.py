
from orchestrator.api.v1.offer.send_offer_orchestrator import SendOfferOrchestratorService

class TestSendOfferOrchestratorService:

    def test_service_instantiation(self) -> None:
        service = SendOfferOrchestratorService()
        assert service is not None
        assert hasattr(service, 'execute') or hasattr(service, 'process') or hasattr(service, 'run') or hasattr(service, 'name')

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestSendOfferOrchestratorService"

