
import pytest
from dtos import DedupGroupCandidateResponse

class TestDedupGroupCandidateResponse:

    def test_schema_valid(self) -> None:
        schema = DedupGroupCandidateResponse.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = DedupGroupCandidateResponse.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                DedupGroupCandidateResponse.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestDedupGroupCandidateResponse"

