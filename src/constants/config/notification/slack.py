from typing import Final
from .abstraction import INotificationConfigurationConstant


class SlackConfig(INotificationConfigurationConstant):

    CONFIG_PATH: Final[str] = "configs/notification/slack/config.json"
    WEBHOOK_URL: Final[str] = ""
    DEFAULT_CHANNEL: Final[str] = "#general"
    USERNAME: Final[str] = "mono"
    ICON_EMOJI: Final[str] = ""
    TIMEOUT_SECONDS: Final[int] = 5
    IS_CONFIGURED: Final[bool] = False

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "SlackConfig"
