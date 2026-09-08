from datetime import datetime
from typing import Optional
from pydantic import Field, field_validator

from constants import DBColumn
from .abstraction import IAtomicRepositoryServiceDTO


class IUpdateRepositoryServiceDTO(IAtomicRepositoryServiceDTO):
    """Marker base for update repository service DTOs."""

    id: Optional[int] = Field(default=None, description="Optional updated id")
    updated_at: datetime = Field(..., description="updated_at timestamp")
    updated_by: str = Field(..., description="updated_by user URN")

    @field_validator(DBColumn.ID, check_fields=False)
    @classmethod
    def validate_id(cls, v: Optional[int], info) -> Optional[int]:
        return cls.validation_utility.validate_id(v, field_name=info.field_name, required=False)

    @field_validator(DBColumn.UPDATED_AT, check_fields=False)
    @classmethod
    def validate_updated_at(cls, v: datetime, info) -> datetime:
        return cls.validation_utility.validate_datetime(v, field_name=info.field_name, required=True)

    @field_validator(DBColumn.UPDATED_BY, check_fields=False)
    @classmethod
    def validate_updated_by(cls, v: str, info) -> str:
        return cls.validation_utility.validate_string(v, field_name=info.field_name, required=True)

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "IUpdateRepositoryServiceDTO"
