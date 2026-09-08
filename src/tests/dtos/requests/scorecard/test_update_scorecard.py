
import pytest
from dtos import UpdateScorecardRequest

class TestUpdateScorecardRequest:

    def test_schema_valid(self) -> None:
        schema = UpdateScorecardRequest.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = UpdateScorecardRequest.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                UpdateScorecardRequest.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestUpdateScorecardRequest"

