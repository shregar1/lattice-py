from .abstraction import INotificationConfigurationDTO
from .slack import SlackConfigurationDTO
from .teams import TeamsConfigurationDTO
from .webhook import WebhookConfigurationDTO

__all__ = [
    "INotificationConfigurationDTO",
    "SlackConfigurationDTO",
    "TeamsConfigurationDTO",
    "WebhookConfigurationDTO",
]
