from datetime import datetime
from typing import Optional, Self
from uuid import UUID


from pydantic import HTTPUrl

from constants import DBTable, Model
from ..abstraction import IWebhookModel
from ..fields import BooleanField, HTTPURLField, TextField


class WebhookEndpoint(IWebhookModel):
    """Outbound webhook subscription for envelope lifecycle events."""

    __tablename__ = DBTable.WEBHOOK_ENDPOINT

    url: HTTPUrl = HTTPURLField(max_length=2048, nullable=False)
    events: str = TextField(nullable=False)
    active: bool = BooleanField(default=True, nullable=False)

    @classmethod
    def build(
        cls,
        urn: UUID,
        external_id: str,
        tenant_id: int,
        url: str,
        events: str,
        active: bool = True,
        created_at: datetime = datetime.now(),
        updated_at: Optional[datetime] = None,
        created_by: Optional[int] = None,
        updated_by: Optional[int] = None,
        is_deleted: bool = False,
        is_active: bool = True,
    ) -> Self:
        """Construct a webhook endpoint instance."""
        return WebhookEndpoint(
            urn=urn,
            external_id=external_id,
            tenant_id=tenant_id,
            url=url,
            events=events,
            active=active,
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
        return Model.WEBHOOK_ENDPOINT
