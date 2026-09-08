
import pytest
from dtos import UserResponse

class TestUserResponse:

    def test_schema_valid(self) -> None:
        schema = UserResponse.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = UserResponse.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                UserResponse.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestUserResponse"

