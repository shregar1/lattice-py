from datetime import datetime
from typing import Optional
from pydantic import Field, field_validator

from constants import DBColumn
from .abstraction import IAtomicRepositoryServiceDTO


class IDeleteRepositoryServiceDTO(IAtomicRepositoryServiceDTO):
    """Marker base for delete repository service DTOs."""

    id: int = Field(..., description="ID of the record to delete")
    is_hard_delete: bool = Field(default=False, description="Whether to perform hard deletion")
    updated_at: datetime = Field(..., description="updated_at timestamp")
    updated_by: str = Field(..., description="updated_by user URN")

    @field_validator(DBColumn.ID, check_fields=False)
    @classmethod
    def validate_id(cls, v: int, info) -> int:
        """
        Method to ....
        """
        return cls.validation_utility.validate_id(v, field_name=info.field_name)

    @field_validator("is_hard_delete", check_fields=False)
    @classmethod
    def validate_is_hard_delete(cls, v: bool, info) -> bool:
        """
        Method to ....
        """
        return cls.validation_utility.validate_bool(v, field_name=info.field_name, required=False)

    @field_validator(DBColumn.UPDATED_AT, check_fields=False)
    @classmethod
    def validate_updated_at(cls, v: datetime, info) -> datetime:
        """
        Method to ....
        """
        return cls.validation_utility.validate_datetime(v, field_name=info.field_name, required=True)

    @field_validator(DBColumn.UPDATED_BY, check_fields=False)
    @classmethod
    def validate_updated_by(cls, v: str, info) -> str:
        """
        Method to ....
        """
        return cls.validation_utility.validate_string(v, field_name=info.field_name, required=True)

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "IDeleteRepositoryServiceDTO"
