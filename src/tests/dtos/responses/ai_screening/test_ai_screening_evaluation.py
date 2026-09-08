
import pytest
from dtos import AIScreeningEvaluationResponse

class TestAIScreeningEvaluationResponse:

    def test_schema_valid(self) -> None:
        schema = AIScreeningEvaluationResponse.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = AIScreeningEvaluationResponse.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                AIScreeningEvaluationResponse.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestAIScreeningEvaluationResponse"

