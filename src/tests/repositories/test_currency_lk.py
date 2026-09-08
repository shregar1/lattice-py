
from repositories.lookup.currency_lk import CurrencyLKRepository

class TestCurrencyLKRepository:

    def test_repository_instantiation(self) -> None:
        repo = CurrencyLKRepository()
        assert repo is not None
        assert repo.model_class is not None

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestCurrencyLKRepository"

