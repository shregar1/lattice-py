from typing import Final

from ..abstraction import IConfigurationConstant


class INotificationConfigurationConstant(IConfigurationConstant):

    TITLE: Final[str] = "Mono Notification"
    TIMEOUT_SECONDS: Final[int] = 10
    ICON_EMOJI: Final[str] = ":robot_face:"

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "INotificationConfigurationConstant"
