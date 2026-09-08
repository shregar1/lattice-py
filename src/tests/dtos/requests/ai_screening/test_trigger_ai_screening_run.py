
import pytest
from dtos import TriggerAIScreeningRunRequest

class TestTriggerAIScreeningRunRequest:

    def test_schema_valid(self) -> None:
        schema = TriggerAIScreeningRunRequest.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = TriggerAIScreeningRunRequest.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                TriggerAIScreeningRunRequest.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestTriggerAIScreeningRunRequest"

