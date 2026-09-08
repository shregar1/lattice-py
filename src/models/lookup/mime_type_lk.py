from datetime import datetime
from typing import Optional, Self
from uuid import UUID



from constants import DBTable, Model
from ..abstraction import ILookupModel
from ..fields import Field


class MimeTypeLK(ILookupModel):
    """Lookup values for export/content MIME types."""

    __tablename__ = DBTable.MIME_TYPE_LK

    code: str = Field(max_length=128, unique=True, nullable=False)

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
        """Construct a MIME type lookup instance."""
        return MimeTypeLK(
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
        return Model.MIME_TYPE_LK
