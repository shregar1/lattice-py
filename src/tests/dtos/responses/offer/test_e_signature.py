
import pytest
from dtos import ESignatureResponse

class TestESignatureResponse:

    def test_schema_valid(self) -> None:
        schema = ESignatureResponse.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = ESignatureResponse.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                ESignatureResponse.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestESignatureResponse"

