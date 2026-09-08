from typing import Self

from .abstraction import INotificationConfigurationDTO
from constants import Configuration


class SlackConfigurationDTO(INotificationConfigurationDTO):
    webhook_url: str
    default_channel: str
    username: str
    icon_emoji: str
    timeout_seconds: int
    is_configured: bool

    @classmethod
    def build(
        cls,
        webhook_url: str,
        default_channel: str,
        username: str,
        icon_emoji: str,
        timeout_seconds: int,
        is_configured: bool,
    ) -> Self:
        """
        Method to ....
        """
        return cls(
            webhook_url=webhook_url,
            default_channel=default_channel,
            username=username,
            icon_emoji=icon_emoji,
            timeout_seconds=timeout_seconds,
            is_configured=is_configured,
        )

    @property
    def name(self) -> str:
        """Returns the class name."""
        return Configuration.SLACK
