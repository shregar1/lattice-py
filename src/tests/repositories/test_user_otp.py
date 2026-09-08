
from repositories.user.user_otp import UserOtpRepository

class TestUserOtpRepository:

    def test_repository_instantiation(self) -> None:
        repo = UserOtpRepository()
        assert repo is not None
        assert repo.model_class is not None

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestUserOtpRepository"

