
import pytest
from dtos import ListRuleRunsRequest

class TestListRuleRunsRequest:

    def test_schema_valid(self) -> None:
        schema = ListRuleRunsRequest.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = ListRuleRunsRequest.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                ListRuleRunsRequest.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestListRuleRunsRequest"

