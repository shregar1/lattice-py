from typing import Final
from .abstraction import INotificationConfigurationConstant


class TeamsConfig(INotificationConfigurationConstant):

    CONFIG_PATH: Final[str] = "configs/notification/teams/config.json"
    WEBHOOK_URL: Final[str] = ""
    THEME_COLOR: Final[str] = "0076D7"
    DEFAULT_CHANNEL: Final[str] = "#general"
    USERNAME: Final[str] = "mono"
    ICON_EMOJI: Final[str] = ""
    TIMEOUT_SECONDS: Final[int] = 5
    IS_CONFIGURED: Final[bool] = False

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "TeamsConfig"
