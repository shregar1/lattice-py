from datetime import datetime
from typing import Optional, Self
from uuid import UUID

from constants import DBTable, Model
from ..abstraction import ILookupModel


class StatusLK(ILookupModel):
    """Lookup values for contract lifecycle status."""

    __tablename__ = DBTable.STATUS_LK

    @classmethod
    def build(
        cls,
        urn: UUID,
        code: str,
        label: str,
        description: str,
        created_at: datetime = datetime.now(),
        updated_at: Optional[datetime] = None,
        is_deleted: bool = False,
        is_active: bool = True,
    ) -> Self:
        """Construct a contract status lookup instance."""
        return StatusLK(
            urn=urn,
            code=code,
            label=label,
            description=description,
            created_at=created_at,
            updated_at=updated_at,
            is_deleted=is_deleted,
            is_active=is_active,
        )

    @property
    def name(self) -> str:
        """Returns the model name constant."""
        return Model.STATUS_LK
