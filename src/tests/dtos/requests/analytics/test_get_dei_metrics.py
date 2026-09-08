
import pytest
from dtos import GetDeiMetricsRequest

class TestGetDeiMetricsRequest:

    def test_schema_valid(self) -> None:
        schema = GetDeiMetricsRequest.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = GetDeiMetricsRequest.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                GetDeiMetricsRequest.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestGetDeiMetricsRequest"

