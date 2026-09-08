
import pytest
from dtos import RequisitionApprovalResponse

class TestRequisitionApprovalResponse:

    def test_schema_valid(self) -> None:
        schema = RequisitionApprovalResponse.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = RequisitionApprovalResponse.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                RequisitionApprovalResponse.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestRequisitionApprovalResponse"

