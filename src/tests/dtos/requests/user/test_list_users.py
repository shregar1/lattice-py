
import pytest
from dtos import ListUsersRequest

class TestListUsersRequest:

    def test_schema_valid(self) -> None:
        schema = ListUsersRequest.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = ListUsersRequest.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                ListUsersRequest.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestListUsersRequest"

