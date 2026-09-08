
import pytest
from dtos import ScorecardAttributeRequest

class TestScorecardAttributeRequest:

    def test_schema_valid(self) -> None:
        schema = ScorecardAttributeRequest.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = ScorecardAttributeRequest.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                ScorecardAttributeRequest.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestScorecardAttributeRequest"

