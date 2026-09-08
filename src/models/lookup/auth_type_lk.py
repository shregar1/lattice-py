from datetime import datetime
from typing import Optional, Self
from uuid import UUID

from constants import DBTable, Model
from ..abstraction import ICoreLookupModel


class AuthTypeLK(ICoreLookupModel):
    """Lookup values for authentication methods."""

    __tablename__ = DBTable.AUTH_TYPE_LK

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
        """Construct an auth type lookup instance."""
        return AuthTypeLK(
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
        return Model.AUTH_TYPE_LK
