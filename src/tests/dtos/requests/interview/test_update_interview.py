
import pytest
from dtos import UpdateInterviewRequest

class TestUpdateInterviewRequest:

    def test_schema_valid(self) -> None:
        schema = UpdateInterviewRequest.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = UpdateInterviewRequest.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                UpdateInterviewRequest.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestUpdateInterviewRequest"

