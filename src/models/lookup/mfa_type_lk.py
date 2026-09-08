from datetime import datetime
from typing import Optional, Self
from uuid import UUID

from constants import DBTable, Model
from ..abstraction import ICoreLookupModel


class MFATypeLK(ICoreLookupModel):
    """Lookup values for multi-factor authentication methods."""

    __tablename__ = DBTable.MFA_TYPE_LK

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
        """Construct an MFA type lookup instance."""
        return MFATypeLK(
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
        return Model.MFA_TYPE_LK
