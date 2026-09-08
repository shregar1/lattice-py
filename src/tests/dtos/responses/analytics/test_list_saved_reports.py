
import pytest
from dtos import ListSavedReportsResponse

class TestListSavedReportsResponse:

    def test_schema_valid(self) -> None:
        schema = ListSavedReportsResponse.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = ListSavedReportsResponse.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                ListSavedReportsResponse.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestListSavedReportsResponse"

