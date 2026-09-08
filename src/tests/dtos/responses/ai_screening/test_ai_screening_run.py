
import pytest
from dtos import AIScreeningRunResponse

class TestAIScreeningRunResponse:

    def test_schema_valid(self) -> None:
        schema = AIScreeningRunResponse.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = AIScreeningRunResponse.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                AIScreeningRunResponse.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestAIScreeningRunResponse"

