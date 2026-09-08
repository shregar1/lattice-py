
import pytest
from dtos import LoginResponse

class TestLoginResponse:

    def test_schema_valid(self) -> None:
        schema = LoginResponse.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = LoginResponse.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                LoginResponse.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestLoginResponse"

