
import pytest
from dtos import ListInterviewsResponse

class TestListInterviewsResponse:

    def test_schema_valid(self) -> None:
        schema = ListInterviewsResponse.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = ListInterviewsResponse.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                ListInterviewsResponse.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestListInterviewsResponse"

