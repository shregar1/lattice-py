
import pytest
from dtos import UpdateSavedReportRequest

class TestUpdateSavedReportRequest:

    def test_schema_valid(self) -> None:
        schema = UpdateSavedReportRequest.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = UpdateSavedReportRequest.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                UpdateSavedReportRequest.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestUpdateSavedReportRequest"

