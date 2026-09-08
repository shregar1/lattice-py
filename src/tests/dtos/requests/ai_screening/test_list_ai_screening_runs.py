
import pytest
from dtos import ListAIScreeningRunsRequest

class TestListAIScreeningRunsRequest:

    def test_schema_valid(self) -> None:
        schema = ListAIScreeningRunsRequest.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = ListAIScreeningRunsRequest.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                ListAIScreeningRunsRequest.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestListAIScreeningRunsRequest"

