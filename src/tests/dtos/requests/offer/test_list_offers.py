
import pytest
from dtos import ListOffersRequest

class TestListOffersRequest:

    def test_schema_valid(self) -> None:
        schema = ListOffersRequest.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = ListOffersRequest.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                ListOffersRequest.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestListOffersRequest"

