
import pytest
from dtos import OfferResponse

class TestOfferResponse:

    def test_schema_valid(self) -> None:
        schema = OfferResponse.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = OfferResponse.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                OfferResponse.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestOfferResponse"

