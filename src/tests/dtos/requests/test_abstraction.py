
import pytest
from dtos import IRequestDTO

class TestIRequestDTO:

    def test_schema_valid(self) -> None:
        schema = IRequestDTO.model_json_schema()
        assert isinstance(schema, dict)

    def test_instantiation_contract(self) -> None:
        required = IRequestDTO.model_json_schema().get('required', [])

        if required:
            with pytest.raises(Exception):
                IRequestDTO.model_validate({})

    @property
    def name(self) -> str:
        """Returns the class name."""

        return "TestName.TestIRequestDTO"

