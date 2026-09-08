from constants import Configuration
from .abstraction import INotificationConfigurationDTO
from rivex import Dependency
from typing import Any, Optional, Dict, List, Tuple, Self, Optional
from dependencies import LoggerUtilityDependency
from exceptions import LoadConfigurationException
from utilities import Logger


class WebhookConfigurationDTO(INotificationConfigurationDTO):
    webhook_url: Optional[str]
    timeout_seconds: int
    theme_color: str
    title: str
    is_configured: bool

    @classmethod
    def build(
        cls,
        webhook_url: str,
        timeout_seconds: int,
        theme_color: str,
        title: str,
        is_configured: bool,
    ) -> Self:
        """
        Method to ....
        """
        return cls(
            webhook_url=webhook_url,
            timeout_seconds=timeout_seconds,
            theme_color=theme_color,
            title=title,
            is_configured=is_configured,
        )

    @property
    def name(self) -> str:
        """Returns the class name."""
        return Configuration.WEBHOOK
