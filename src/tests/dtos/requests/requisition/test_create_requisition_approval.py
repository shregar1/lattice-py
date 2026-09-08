
import pytest
from dtos import CreateRequisitionApprovalRequest

class TestCreateRequisitionApprovalRequest:

    def test_schema_valid(self) -> None:
        schema = CreateRequisitionApprovalRequest.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = CreateRequisitionApprovalRequest.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                CreateRequisitionApprovalRequest.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestCreateRequisitionApprovalRequest"

