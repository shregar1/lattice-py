
import pytest
from dtos import AnalyticsMetricsResponse

class TestAnalyticsMetricsResponse:

    def test_schema_valid(self) -> None:
        schema = AnalyticsMetricsResponse.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = AnalyticsMetricsResponse.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                AnalyticsMetricsResponse.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestAnalyticsMetricsResponse"

