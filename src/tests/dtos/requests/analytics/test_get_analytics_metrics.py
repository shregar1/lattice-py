
import pytest
from dtos import GetAnalyticsMetricsRequest

class TestGetAnalyticsMetricsRequest:

    def test_schema_valid(self) -> None:
        schema = GetAnalyticsMetricsRequest.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = GetAnalyticsMetricsRequest.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                GetAnalyticsMetricsRequest.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestGetAnalyticsMetricsRequest"

