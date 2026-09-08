from datetime import datetime
from typing import Optional, Self
from uuid import UUID

from constants import DBTable, Model
from ..abstraction import ICoreLookupModel


class UserTypeLK(ICoreLookupModel):
    """Lookup values for workspace user roles."""

    __tablename__ = DBTable.USER_TYPE_LK

    @classmethod
    def build(
        cls,
        urn: UUID,
        code: str,
        description: str,
        created_at: datetime = datetime.now(),
        updated_at: Optional[datetime] = None,
        is_deleted: bool = False,
    ) -> Self:
        """Construct a user type lookup instance."""
        return UserTypeLK(
            urn=urn,
            code=code,
            description=description,
            created_at=created_at,
            updated_at=updated_at or created_at,
            is_deleted=is_deleted,
        )

    @property
    def name(self) -> str:
        """Returns the model name constant."""
        return Model.USER_TYPE_LK
