
from repositories.offer import OfferRepository

class TestOfferRepository:

    def test_repository_instantiation(self) -> None:
        repo = OfferRepository()
        assert repo is not None
        assert repo.model_class is not None

    def test_find_by_application_callable(self) -> None:
        repo = OfferRepository()
        assert hasattr(repo, 'find_by_application')
        assert callable(getattr(repo, 'find_by_application'))

    def test_find_by_status_callable(self) -> None:
        repo = OfferRepository()
        assert hasattr(repo, 'find_by_status')
        assert callable(getattr(repo, 'find_by_status'))

    def test_find_by_role_level_callable(self) -> None:
        repo = OfferRepository()
        assert hasattr(repo, 'find_by_role_level')
        assert callable(getattr(repo, 'find_by_role_level'))

    def test_find_by_template_callable(self) -> None:
        repo = OfferRepository()
        assert hasattr(repo, 'find_by_template')
        assert callable(getattr(repo, 'find_by_template'))

    def test_find_by_currency_callable(self) -> None:
        repo = OfferRepository()
        assert hasattr(repo, 'find_by_currency')
        assert callable(getattr(repo, 'find_by_currency'))

    def test_find_high_salary_callable(self) -> None:
        repo = OfferRepository()
        assert hasattr(repo, 'find_high_salary')
        assert callable(getattr(repo, 'find_high_salary'))

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestOfferRepository"

