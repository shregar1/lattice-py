
import pytest
from dtos import UpdateESignatureStatusRequest

class TestUpdateESignatureStatusRequest:

    def test_schema_valid(self) -> None:
        schema = UpdateESignatureStatusRequest.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = UpdateESignatureStatusRequest.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                UpdateESignatureStatusRequest.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestUpdateESignatureStatusRequest"

