import pytest
from dtos import MFAVerifyRequest


class TestMFAVerifyRequest:
    def test_schema_valid(self) -> None:
        schema = MFAVerifyRequest.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = MFAVerifyRequest.model_json_schema().get("required", [])

        if required:
            with pytest.raises(Exception):
                MFAVerifyRequest.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestMFAVerifyRequest"

