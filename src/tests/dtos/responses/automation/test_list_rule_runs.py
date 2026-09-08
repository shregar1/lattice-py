
import pytest
from dtos import ListRuleRunsResponse

class TestListRuleRunsResponse:

    def test_schema_valid(self) -> None:
        schema = ListRuleRunsResponse.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = ListRuleRunsResponse.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                ListRuleRunsResponse.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestListRuleRunsResponse"

