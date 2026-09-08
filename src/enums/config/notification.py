"""notification enum module."""

from enum import Enum
from abstractions import EnumLayer
from constants import SlackConfig
from constants import TeamsConfig


class SlackConfigENUM(EnumLayer):
    DEFAULT_CHANNEL = SlackConfig.DEFAULT_CHANNEL
    USERNAME = SlackConfig.USERNAME
    ICON_EMOJI = SlackConfig.ICON_EMOJI
    TIMEOUT_SECONDS = SlackConfig.TIMEOUT_SECONDS

    @property
    def name(self) -> str:
        """Returns the layer name."""
        return "SlackConfigENUM"


class TeamsConfigENUM(EnumLayer):
    TIMEOUT_SECONDS = TeamsConfig.TIMEOUT_SECONDS
    THEME_COLOR = TeamsConfig.THEME_COLOR
    TITLE = TeamsConfig.TITLE

    @property
    def name(self) -> str:
        """Returns the layer name."""
        return "TeamsConfigENUM"

