
import pytest
from dtos import CreateCandidateUploadRequest

class TestCreateCandidateUploadRequest:

    def test_schema_valid(self) -> None:
        schema = CreateCandidateUploadRequest.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = CreateCandidateUploadRequest.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                CreateCandidateUploadRequest.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestCreateCandidateUploadRequest"

