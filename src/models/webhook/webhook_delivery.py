from datetime import datetime
from typing import Optional, Self
from uuid import UUID


from pydantic import HTTPUrl

from constants import DBColumn, DBTable, Model
from ..abstraction import IWebhookModel
from ..fields import ForeignKey, HTTPURLField, IntegerField, SmallIntegerField, TextField, TimestampTZField


class WebhookDelivery(IWebhookModel):
    """Record of a webhook HTTP delivery attempt."""

    __tablename__ = DBTable.WEBHOOK_DELIVERY

    endpoint_id: int = ForeignKey(f"{DBTable.WEBHOOK_ENDPOINT}.{DBColumn.ID}", nullable=False)
    endpoint_url: HTTPUrl = HTTPURLField(max_length=2048, nullable=False)
    event_type_id: int = ForeignKey(f"{DBTable.EVENT_TYPE_LK}.{DBColumn.ID}", nullable=False)
    envelope_id: Optional[int] = ForeignKey(f"{DBTable.ENVELOPE}.{DBColumn.ID}", nullable=True)
    payload_json: str = TextField(nullable=False)
    delivery_status_id: int = ForeignKey(
        f"{DBTable.WEBHOOK_DELIVERY_STATUS_LK}.{DBColumn.ID}",
        nullable=False,
    )
    http_status: int = SmallIntegerField(nullable=False)
    latency_ms: int = IntegerField(nullable=False)
    delivered_at: datetime = TimestampTZField(nullable=False)

    @classmethod
    def build(
        cls,
        urn: UUID,
        external_id: str,
        tenant_id: int,
        endpoint_id: int,
        endpoint_url: str,
        event_type_id: int,
        payload_json: str,
        delivery_status_id: int,
        http_status: int,
        latency_ms: int,
        delivered_at: datetime,
        created_at: datetime = datetime.now(),
        updated_at: Optional[datetime] = None,
        created_by: Optional[int] = None,
        updated_by: Optional[int] = None,
        is_deleted: bool = False,
        is_active: bool = True,
        envelope_id: Optional[int] = None,
    ) -> Self:
        """Construct a webhook delivery instance."""
        return WebhookDelivery(
            urn=urn,
            external_id=external_id,
            tenant_id=tenant_id,
            endpoint_id=endpoint_id,
            endpoint_url=endpoint_url,
            event_type_id=event_type_id,
            envelope_id=envelope_id,
            payload_json=payload_json,
            delivery_status_id=delivery_status_id,
            http_status=http_status,
            latency_ms=latency_ms,
            delivered_at=delivered_at,
            created_at=created_at,
            updated_at=updated_at,
            created_by=created_by,
            updated_by=updated_by,
            is_deleted=is_deleted,
            is_active=is_active,
        )

    @property
    def name(self) -> str:
        """Returns the model name constant."""
        return Model.WEBHOOK_DELIVERY
