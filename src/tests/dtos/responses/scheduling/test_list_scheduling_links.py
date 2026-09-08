
import pytest
from dtos import ListSchedulingLinksResponse

class TestListSchedulingLinksResponse:

    def test_schema_valid(self) -> None:
        schema = ListSchedulingLinksResponse.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = ListSchedulingLinksResponse.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                ListSchedulingLinksResponse.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestListSchedulingLinksResponse"

