
import pytest
from dtos import ListScorecardsRequest

class TestListScorecardsRequest:

    def test_schema_valid(self) -> None:
        schema = ListScorecardsRequest.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = ListScorecardsRequest.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                ListScorecardsRequest.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestListScorecardsRequest"

