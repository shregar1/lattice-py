
import pytest
from dtos import CreateRequisitionRequest

class TestCreateRequisitionRequest:

    def test_schema_valid(self) -> None:
        schema = CreateRequisitionRequest.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = CreateRequisitionRequest.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                CreateRequisitionRequest.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestCreateRequisitionRequest"

