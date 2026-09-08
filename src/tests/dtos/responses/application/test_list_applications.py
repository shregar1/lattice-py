
import pytest
from dtos import ListApplicationsResponse

class TestListApplicationsResponse:

    def test_schema_valid(self) -> None:
        schema = ListApplicationsResponse.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = ListApplicationsResponse.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                ListApplicationsResponse.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestListApplicationsResponse"

