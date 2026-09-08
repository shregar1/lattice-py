
from repositories.lookup.activity_type_lk import ActivityTypeLKRepository

class TestActivityTypeLKRepository:

    def test_repository_instantiation(self) -> None:
        repo = ActivityTypeLKRepository()
        assert repo is not None
        assert repo.model_class is not None

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestActivityTypeLKRepository"

