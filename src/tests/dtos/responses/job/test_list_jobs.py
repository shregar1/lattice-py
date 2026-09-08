
import pytest
from dtos import ListJobsResponse

class TestListJobsResponse:

    def test_schema_valid(self) -> None:
        schema = ListJobsResponse.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = ListJobsResponse.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                ListJobsResponse.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestListJobsResponse"

