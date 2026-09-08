from typing import Optional
from pydantic import Field, field_validator
from rivex import Dependency

from constants import DBColumn
from dependencies import ValidationUtilityDependency
from .abstraction import IServiceDTO
from utilities import ValidationUtility


class IAtomicRepositoryServiceDTO(IServiceDTO):
    """Marker base for repository service DTOs."""

    validation_utility: ValidationUtility = Dependency(ValidationUtilityDependency)

    user_id: int = Field(..., description="user_id parameter")
    tenant_id: int = Field(..., description="tenant_id parameter")

    is_deleted: Optional[bool] = Field(default=None, description="Deleted status metadata")
    is_active: Optional[bool] = Field(default=None, description="Active status metadata")

    @field_validator(DBColumn.USER_ID, DBColumn.TENANT_ID, check_fields=False)
    @classmethod
    def validate_user_tenant_id(cls, v: int, info) -> int:
        return cls.validation_utility.validate_id(v, field_name=info.field_name, required=True)

    @field_validator(DBColumn.IS_DELETED, check_fields=False)
    @classmethod
    def validate_is_deleted(cls, v: Optional[bool], info) -> Optional[bool]:
        return cls.validation_utility.validate_bool(v, field_name=info.field_name, required=False)

    @field_validator(DBColumn.IS_ACTIVE, check_fields=False)
    @classmethod
    def validate_is_active(cls, v: Optional[bool], info) -> Optional[bool]:
        return cls.validation_utility.validate_bool(v, field_name=info.field_name, required=False)

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "IAtomicRepositoryServiceDTO"
