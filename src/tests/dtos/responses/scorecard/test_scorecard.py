
import pytest
from dtos import ScorecardResponse

class TestScorecardResponse:

    def test_schema_valid(self) -> None:
        schema = ScorecardResponse.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = ScorecardResponse.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                ScorecardResponse.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestScorecardResponse"

