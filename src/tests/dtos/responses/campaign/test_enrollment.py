
import pytest
from dtos import EnrollmentResponse

class TestEnrollmentResponse:

    def test_schema_valid(self) -> None:
        schema = EnrollmentResponse.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = EnrollmentResponse.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                EnrollmentResponse.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestEnrollmentResponse"

