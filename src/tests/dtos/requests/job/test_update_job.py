
import pytest
from dtos import UpdateJobRequest

class TestUpdateJobRequest:

    def test_schema_valid(self) -> None:
        schema = UpdateJobRequest.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = UpdateJobRequest.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                UpdateJobRequest.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestUpdateJobRequest"

