
import pytest
from dtos import ExecuteRuleRunRequest

class TestExecuteRuleRunRequest:

    def test_schema_valid(self) -> None:
        schema = ExecuteRuleRunRequest.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = ExecuteRuleRunRequest.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                ExecuteRuleRunRequest.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestExecuteRuleRunRequest"

