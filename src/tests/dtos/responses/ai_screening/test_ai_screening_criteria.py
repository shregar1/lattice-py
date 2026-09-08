
import pytest
from dtos import AIScreeningCriteriaResponse

class TestAIScreeningCriteriaResponse:

    def test_schema_valid(self) -> None:
        schema = AIScreeningCriteriaResponse.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = AIScreeningCriteriaResponse.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                AIScreeningCriteriaResponse.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestAIScreeningCriteriaResponse"

