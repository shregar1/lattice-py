
import pytest
from dtos import AutomationRuleResponse

class TestAutomationRuleResponse:

    def test_schema_valid(self) -> None:
        schema = AutomationRuleResponse.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = AutomationRuleResponse.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                AutomationRuleResponse.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestAutomationRuleResponse"

