
import pytest
from dtos import LoginRequest

class TestLoginRequest:

    def test_schema_valid(self) -> None:
        schema = LoginRequest.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = LoginRequest.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                LoginRequest.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestLoginRequest"

