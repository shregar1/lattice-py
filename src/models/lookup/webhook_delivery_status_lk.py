from datetime import datetime
from typing import Optional, Self
from uuid import UUID

from constants import DBTable, Model
from ..abstraction import ILookupModel


class WebhookDeliveryStatusLK(ILookupModel):
    """Lookup values for webhook delivery outcome."""

    __tablename__ = DBTable.WEBHOOK_DELIVERY_STATUS_LK

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
        """Construct a webhook delivery status lookup instance."""
        return WebhookDeliveryStatusLK(
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
        return Model.WEBHOOK_DELIVERY_STATUS_LK
