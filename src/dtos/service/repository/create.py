from datetime import datetime
from typing import Optional
from pydantic import Field, field_validator

from constants import DBColumn
from .abstraction import IAtomicRepositoryServiceDTO


class ICreateRepositoryServiceDTO(IAtomicRepositoryServiceDTO):
    """Marker base for create repository service DTOs."""

    urn: Optional[str] = Field(default=None, description="Optional record URN")
    created_at: datetime = Field(..., description="created_at timestamp")
    created_by: str = Field(..., description="created_by user URN")

    @field_validator(DBColumn.URN, check_fields=False)
    @classmethod
    def validate_urn(cls, v: Optional[str], info) -> Optional[str]:
        """
        Method to ....
        """
        return cls.validation_utility.validate_urn(v, field_name=info.field_name, required=False)

    @field_validator(DBColumn.CREATED_AT, check_fields=False)
    @classmethod
    def validate_created_at(cls, v: datetime, info) -> datetime:
        """
        Method to ....
        """
        return cls.validation_utility.validate_datetime(v, field_name=info.field_name, required=True)

    @field_validator(DBColumn.CREATED_BY, check_fields=False)
    @classmethod
    def validate_created_by(cls, v: str, info) -> str:
        """
        Method to ....
        """
        return cls.validation_utility.validate_string(v, field_name=info.field_name, required=True)

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "ICreateRepositoryServiceDTO"
