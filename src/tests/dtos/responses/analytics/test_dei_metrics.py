
import pytest
from dtos import DeiMetricsResponse

class TestDeiMetricsResponse:

    def test_schema_valid(self) -> None:
        schema = DeiMetricsResponse.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = DeiMetricsResponse.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                DeiMetricsResponse.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestDeiMetricsResponse"

