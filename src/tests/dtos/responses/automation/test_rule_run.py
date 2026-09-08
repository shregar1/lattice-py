
import pytest
from dtos import RuleRunResponse

class TestRuleRunResponse:

    def test_schema_valid(self) -> None:
        schema = RuleRunResponse.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = RuleRunResponse.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                RuleRunResponse.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestRuleRunResponse"

