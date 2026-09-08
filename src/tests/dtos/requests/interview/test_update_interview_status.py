
import pytest
from dtos import UpdateInterviewStatusRequest

class TestUpdateInterviewStatusRequest:

    def test_schema_valid(self) -> None:
        schema = UpdateInterviewStatusRequest.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = UpdateInterviewStatusRequest.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                UpdateInterviewStatusRequest.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestUpdateInterviewStatusRequest"

