
from repositories.e_signature import ESignatureRepository

class TestESignatureRepository:

    def test_repository_instantiation(self) -> None:
        repo = ESignatureRepository()
        assert repo is not None
        assert repo.model_class is not None

    def test_find_by_offer_callable(self) -> None:
        repo = ESignatureRepository()
        assert hasattr(repo, 'find_by_offer')
        assert callable(getattr(repo, 'find_by_offer'))

    def test_find_by_status_callable(self) -> None:
        repo = ESignatureRepository()
        assert hasattr(repo, 'find_by_status')
        assert callable(getattr(repo, 'find_by_status'))

    def test_find_signed_callable(self) -> None:
        repo = ESignatureRepository()
        assert hasattr(repo, 'find_signed')
        assert callable(getattr(repo, 'find_signed'))

    def test_find_pending_callable(self) -> None:
        repo = ESignatureRepository()
        assert hasattr(repo, 'find_pending')
        assert callable(getattr(repo, 'find_pending'))

    def test_count_signed_by_offer_callable(self) -> None:
        repo = ESignatureRepository()
        assert hasattr(repo, 'count_signed_by_offer')
        assert callable(getattr(repo, 'count_signed_by_offer'))

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestESignatureRepository"

