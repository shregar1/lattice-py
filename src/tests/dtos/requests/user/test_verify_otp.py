
import pytest
from dtos import VerifyOtpRequest

class TestVerifyOtpRequest:

    def test_schema_valid(self) -> None:
        schema = VerifyOtpRequest.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = VerifyOtpRequest.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                VerifyOtpRequest.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestVerifyOtpRequest"

