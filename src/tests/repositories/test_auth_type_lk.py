
from repositories.lookup.auth_type_lk import AuthTypeLKRepository

class TestAuthTypeLKRepository:

    def test_repository_instantiation(self) -> None:
        repo = AuthTypeLKRepository()
        assert repo is not None
        assert repo.model_class is not None

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestAuthTypeLKRepository"

