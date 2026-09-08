
import pytest
from dtos import BookSchedulingLinkRequest

class TestBookSchedulingLinkRequest:

    def test_schema_valid(self) -> None:
        schema = BookSchedulingLinkRequest.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = BookSchedulingLinkRequest.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                BookSchedulingLinkRequest.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestBookSchedulingLinkRequest"

