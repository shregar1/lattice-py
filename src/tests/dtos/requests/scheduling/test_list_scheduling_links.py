
import pytest
from dtos import ListSchedulingLinksRequest

class TestListSchedulingLinksRequest:

    def test_schema_valid(self) -> None:
        schema = ListSchedulingLinksRequest.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = ListSchedulingLinksRequest.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                ListSchedulingLinksRequest.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestListSchedulingLinksRequest"

