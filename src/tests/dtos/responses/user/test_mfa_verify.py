import pytest
from dtos import MFAVerifyResponse


class TestMFAVerifyResponse:
    def test_schema_valid(self) -> None:
        schema = MFAVerifyResponse.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = MFAVerifyResponse.model_json_schema().get("required", [])

        if required:
            with pytest.raises(Exception):
                MFAVerifyResponse.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestMFAVerifyResponse"

