
from repositories.campaign.campaign import CampaignRepository

class TestCampaignRepository:

    def test_repository_instantiation(self) -> None:
        repo = CampaignRepository()
        assert repo is not None
        assert repo.model_class is not None

    def test_find_by_tenant_callable(self) -> None:
        repo = CampaignRepository()
        assert hasattr(repo, 'find_by_tenant')
        assert callable(getattr(repo, 'find_by_tenant'))

    def test_find_active_callable(self) -> None:
        repo = CampaignRepository()
        assert hasattr(repo, 'find_active')
        assert callable(getattr(repo, 'find_active'))

    def test_find_by_owner_callable(self) -> None:
        repo = CampaignRepository()
        assert hasattr(repo, 'find_by_owner')
        assert callable(getattr(repo, 'find_by_owner'))

    def test_search_by_name_callable(self) -> None:
        repo = CampaignRepository()
        assert hasattr(repo, 'search_by_name')
        assert callable(getattr(repo, 'search_by_name'))

    def test_count_active_by_tenant_callable(self) -> None:
        repo = CampaignRepository()
        assert hasattr(repo, 'count_active_by_tenant')
        assert callable(getattr(repo, 'count_active_by_tenant'))

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestCampaignRepository"

