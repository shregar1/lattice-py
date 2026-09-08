
import pytest
from dtos import ListCandidatesRequest

class TestListCandidatesRequest:

    def test_schema_valid(self) -> None:
        schema = ListCandidatesRequest.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = ListCandidatesRequest.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                ListCandidatesRequest.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestListCandidatesRequest"

