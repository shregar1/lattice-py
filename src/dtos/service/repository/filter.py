from typing import Optional
from pydantic import Field, field_validator

from constants import DBColumn
from .abstraction import IAtomicRepositoryServiceDTO


class IFilterRepositoryServiceDTO(IAtomicRepositoryServiceDTO):
    """Marker base for filter repository service DTOs."""

    id: Optional[int] = Field(default=None, description="Optional id filter parameter")
    urn: Optional[str] = Field(default=None, description="Optional urn filter parameter")

    @field_validator(DBColumn.ID, check_fields=False)
    @classmethod
    def validate_id(cls, v: Optional[int], info) -> Optional[int]:
        """
        Method to ....
        """
        return cls.validation_utility.validate_id(v, field_name=info.field_name, required=False)

    @field_validator(DBColumn.URN, check_fields=False)
    @classmethod
    def validate_urn(cls, v: Optional[str], info) -> Optional[str]:
        """
        Method to ....
        """
        return cls.validation_utility.validate_urn(v, field_name=info.field_name, required=False)

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "IFilterRepositoryServiceDTO"
