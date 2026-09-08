
from repositories.saved_report import SavedReportRepository

class TestSavedReportRepository:

    def test_repository_instantiation(self) -> None:
        repo = SavedReportRepository()
        assert repo is not None
        assert repo.model_class is not None

    def test_find_by_tenant_callable(self) -> None:
        repo = SavedReportRepository()
        assert hasattr(repo, 'find_by_tenant')
        assert callable(getattr(repo, 'find_by_tenant'))

    def test_find_by_chart_type_callable(self) -> None:
        repo = SavedReportRepository()
        assert hasattr(repo, 'find_by_chart_type')
        assert callable(getattr(repo, 'find_by_chart_type'))

    def test_find_by_metric_callable(self) -> None:
        repo = SavedReportRepository()
        assert hasattr(repo, 'find_by_metric')
        assert callable(getattr(repo, 'find_by_metric'))

    def test_search_by_name_callable(self) -> None:
        repo = SavedReportRepository()
        assert hasattr(repo, 'search_by_name')
        assert callable(getattr(repo, 'search_by_name'))

    def test_count_by_tenant_callable(self) -> None:
        repo = SavedReportRepository()
        assert hasattr(repo, 'count_by_tenant')
        assert callable(getattr(repo, 'count_by_tenant'))

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestSavedReportRepository"

