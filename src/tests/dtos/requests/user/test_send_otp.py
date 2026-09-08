
import pytest
from dtos import SendOtpRequest

class TestSendOtpRequest:

    def test_schema_valid(self) -> None:
        schema = SendOtpRequest.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = SendOtpRequest.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                SendOtpRequest.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestSendOtpRequest"

