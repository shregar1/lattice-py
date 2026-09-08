
import pytest
from dtos import SavedReportResponse

class TestSavedReportResponse:

    def test_schema_valid(self) -> None:
        schema = SavedReportResponse.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = SavedReportResponse.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                SavedReportResponse.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestSavedReportResponse"

