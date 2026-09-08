
import pytest
from dtos import ListDedupGroupsRequest

class TestListDedupGroupsRequest:

    def test_schema_valid(self) -> None:
        schema = ListDedupGroupsRequest.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = ListDedupGroupsRequest.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                ListDedupGroupsRequest.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestListDedupGroupsRequest"

