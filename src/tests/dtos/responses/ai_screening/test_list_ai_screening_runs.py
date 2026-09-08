
import pytest
from dtos import ListAIScreeningRunsResponse

class TestListAIScreeningRunsResponse:

    def test_schema_valid(self) -> None:
        schema = ListAIScreeningRunsResponse.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = ListAIScreeningRunsResponse.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                ListAIScreeningRunsResponse.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestListAIScreeningRunsResponse"

