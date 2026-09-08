
from repositories.lookup.location_lk import LocationLKRepository

class TestLocationLKRepository:

    def test_repository_instantiation(self) -> None:
        repo = LocationLKRepository()
        assert repo is not None
        assert repo.model_class is not None

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestLocationLKRepository"

