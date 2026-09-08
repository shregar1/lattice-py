
import pytest
from dtos import CreateSavedReportRequest

class TestCreateSavedReportRequest:

    def test_schema_valid(self) -> None:
        schema = CreateSavedReportRequest.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = CreateSavedReportRequest.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                CreateSavedReportRequest.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestCreateSavedReportRequest"

