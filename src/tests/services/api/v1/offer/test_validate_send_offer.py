
from orchestrator.api.v1.offer.validate_send_offer import ValidateSendOfferService

class TestValidateSendOfferService:

    def test_service_instantiation(self) -> None:
        service = ValidateSendOfferService()
        assert service is not None
        assert hasattr(service, 'execute') or hasattr(service, 'process') or hasattr(service, 'run') or hasattr(service, 'name')

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestValidateSendOfferService"

