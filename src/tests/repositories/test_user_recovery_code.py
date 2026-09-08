
from repositories.user.user_recovery_code import UserRecoveryCodeRepository

class TestUserRecoveryCodeRepository:

    def test_repository_instantiation(self) -> None:
        repo = UserRecoveryCodeRepository()
        assert repo is not None
        assert repo.model_class is not None

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestUserRecoveryCodeRepository"

