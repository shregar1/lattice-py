from repositories.lookup.mfa_type_lk import MFATypeLKRepository


class TestMFATypeLKRepository:
    def test_repository_instantiation(self) -> None:
        repo = MFATypeLKRepository()
        assert repo is not None
        assert repo.model_class is not None

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestMFATypeLKRepository"

