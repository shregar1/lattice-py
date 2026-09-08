
import pytest
from dtos import ListJobsRequest

class TestListJobsRequest:

    def test_schema_valid(self) -> None:
        schema = ListJobsRequest.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = ListJobsRequest.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                ListJobsRequest.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestListJobsRequest"

