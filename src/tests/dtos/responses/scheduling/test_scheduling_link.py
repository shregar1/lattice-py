
import pytest
from dtos import SchedulingLinkResponse

class TestSchedulingLinkResponse:

    def test_schema_valid(self) -> None:
        schema = SchedulingLinkResponse.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = SchedulingLinkResponse.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                SchedulingLinkResponse.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestSchedulingLinkResponse"

