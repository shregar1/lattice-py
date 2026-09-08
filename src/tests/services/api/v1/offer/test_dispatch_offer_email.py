
from orchestrator.api.v1.offer.dispatch_offer_email import DispatchOfferEmailService

class TestDispatchOfferEmailService:

    def test_service_instantiation(self) -> None:
        service = DispatchOfferEmailService()
        assert service is not None
        assert hasattr(service, 'execute') or hasattr(service, 'process') or hasattr(service, 'run') or hasattr(service, 'name')

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestDispatchOfferEmailService"

