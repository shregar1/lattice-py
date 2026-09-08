
import pytest
from dtos import UpdateRequisitionRequest

class TestUpdateRequisitionRequest:

    def test_schema_valid(self) -> None:
        schema = UpdateRequisitionRequest.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = UpdateRequisitionRequest.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                UpdateRequisitionRequest.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestUpdateRequisitionRequest"

