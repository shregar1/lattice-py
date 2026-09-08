
from repositories.lookup.otp_type_lk import OtpTypeLKRepository

class TestOtpTypeLKRepository:

    def test_repository_instantiation(self) -> None:
        repo = OtpTypeLKRepository()
        assert repo is not None
        assert repo.model_class is not None

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestOtpTypeLKRepository"

