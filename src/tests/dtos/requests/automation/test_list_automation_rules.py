
import pytest
from dtos import ListAutomationRulesRequest

class TestListAutomationRulesRequest:

    def test_schema_valid(self) -> None:
        schema = ListAutomationRulesRequest.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = ListAutomationRulesRequest.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                ListAutomationRulesRequest.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestListAutomationRulesRequest"

