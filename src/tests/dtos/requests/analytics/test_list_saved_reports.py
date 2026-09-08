
import pytest
from dtos import ListSavedReportsRequest

class TestListSavedReportsRequest:

    def test_schema_valid(self) -> None:
        schema = ListSavedReportsRequest.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = ListSavedReportsRequest.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                ListSavedReportsRequest.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestListSavedReportsRequest"

