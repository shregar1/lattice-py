
import pytest
from dtos import OtpResponse

class TestOtpResponse:

    def test_schema_valid(self) -> None:
        schema = OtpResponse.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = OtpResponse.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                OtpResponse.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestOtpResponse"

