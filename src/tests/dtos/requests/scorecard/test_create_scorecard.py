
import pytest
from dtos import CreateScorecardRequest

class TestCreateScorecardRequest:

    def test_schema_valid(self) -> None:
        schema = CreateScorecardRequest.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = CreateScorecardRequest.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                CreateScorecardRequest.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestCreateScorecardRequest"

