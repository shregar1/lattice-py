from orchestrator.api.v1.user.generate_mfa_session import GenerateMFASessionService


class TestGenerateMFASessionService:
    def test_service_instantiation(self) -> None:
        service = GenerateMFASessionService()
        assert service is not None
        assert (
            hasattr(service, "execute")
            or hasattr(service, "process")
            or hasattr(service, "run")
            or hasattr(service, "name")
        )

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestGenerateMFASessionService"

