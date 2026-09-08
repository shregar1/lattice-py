from typing import Any, Self
from pydantic import field_validator, ValidationInfo

from .abstraction import IDTO
from utilities import ValidationUtility


class IRequestDTO(IDTO):
    @field_validator("*", mode="before")
    @classmethod
    def validate_urn_field(cls, v: Any, info: ValidationInfo) -> Any:
        if info.field_name == "urn" or (info.field_name and info.field_name.endswith("_urn")):
            return ValidationUtility.validate_urn(v, field_name=info.field_name)
        return v

    @classmethod
    def model_validate(cls, data: Any, **kwargs: Any) -> Self:
        if isinstance(data, dict):
            for key, val in data.items():
                if key == "urn" or key.endswith("_urn"):
                    ValidationUtility.validate_urn(val, field_name=key)
        elif hasattr(data, "__dict__"):
            for key, val in data.__dict__.items():
                if key == "urn" or key.endswith("_urn"):
                    ValidationUtility.validate_urn(val, field_name=key)

        return super().model_validate(data, **kwargs)

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "IRequestDTO"
