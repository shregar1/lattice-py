"""webhook composite repositories."""

from .webhook_endpoint import WebhookEndpointRepository
from .webhook_delivery import WebhookDeliveryRepository

__all__ = [
    "WebhookDeliveryRepository",
    "WebhookEndpointRepository",
]
