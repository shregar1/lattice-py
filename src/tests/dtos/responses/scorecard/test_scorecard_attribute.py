
import pytest
from dtos import ScorecardAttributeResponse

class TestScorecardAttributeResponse:

    def test_schema_valid(self) -> None:
        schema = ScorecardAttributeResponse.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = ScorecardAttributeResponse.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                ScorecardAttributeResponse.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestScorecardAttributeResponse"

