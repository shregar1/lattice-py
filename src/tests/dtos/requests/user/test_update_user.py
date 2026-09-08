
import pytest
from dtos import UpdateUserRequest

class TestUpdateUserRequest:

    def test_schema_valid(self) -> None:
        schema = UpdateUserRequest.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = UpdateUserRequest.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                UpdateUserRequest.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestUpdateUserRequest"

