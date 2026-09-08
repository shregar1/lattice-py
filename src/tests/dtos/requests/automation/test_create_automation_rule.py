
import pytest
from dtos import CreateAutomationRuleRequest

class TestCreateAutomationRuleRequest:

    def test_schema_valid(self) -> None:
        schema = CreateAutomationRuleRequest.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = CreateAutomationRuleRequest.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                CreateAutomationRuleRequest.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestCreateAutomationRuleRequest"

