
import pytest
from dtos import ListDedupGroupsResponse

class TestListDedupGroupsResponse:

    def test_schema_valid(self) -> None:
        schema = ListDedupGroupsResponse.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = ListDedupGroupsResponse.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                ListDedupGroupsResponse.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestListDedupGroupsResponse"

