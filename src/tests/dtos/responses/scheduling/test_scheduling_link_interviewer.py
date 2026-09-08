
import pytest
from dtos import SchedulingLinkInterviewerResponse

class TestSchedulingLinkInterviewerResponse:

    def test_schema_valid(self) -> None:
        schema = SchedulingLinkInterviewerResponse.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = SchedulingLinkInterviewerResponse.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                SchedulingLinkInterviewerResponse.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestSchedulingLinkInterviewerResponse"

