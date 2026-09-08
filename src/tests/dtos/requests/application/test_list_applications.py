
import pytest
from dtos import ListApplicationsRequest

class TestListApplicationsRequest:

    def test_schema_valid(self) -> None:
        schema = ListApplicationsRequest.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = ListApplicationsRequest.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                ListApplicationsRequest.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestListApplicationsRequest"

