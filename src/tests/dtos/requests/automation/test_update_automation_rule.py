
import pytest
from dtos import UpdateAutomationRuleRequest

class TestUpdateAutomationRuleRequest:

    def test_schema_valid(self) -> None:
        schema = UpdateAutomationRuleRequest.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = UpdateAutomationRuleRequest.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                UpdateAutomationRuleRequest.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestUpdateAutomationRuleRequest"

