
import pytest
from dtos import ListScorecardsResponse

class TestListScorecardsResponse:

    def test_schema_valid(self) -> None:
        schema = ListScorecardsResponse.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = ListScorecardsResponse.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                ListScorecardsResponse.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestListScorecardsResponse"

