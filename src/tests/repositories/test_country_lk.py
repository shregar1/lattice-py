
from repositories.lookup.country_lk import CountryLKRepository

class TestCountryLKRepository:

    def test_repository_instantiation(self) -> None:
        repo = CountryLKRepository()
        assert repo is not None
        assert repo.model_class is not None

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestCountryLKRepository"

