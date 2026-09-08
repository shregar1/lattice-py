"""Webhook domain atomic repositories."""

from .webhook_delivery import WebhookDeliveryRepository
from .webhook_endpoint import WebhookEndpointRepository

__all__ = [
    "WebhookDeliveryRepository",
    "WebhookEndpointRepository",
]
