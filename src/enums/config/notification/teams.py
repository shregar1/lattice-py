"""teams enum module."""

from enum import Enum
from abstractions import EnumLayer
from constants import TeamsConfig


class TeamsConfigENUM(EnumLayer):
    CONFIG_PATH = TeamsConfig.CONFIG_PATH
    WEBHOOK_URL = TeamsConfig.WEBHOOK_URL
    THEME_COLOR = TeamsConfig.THEME_COLOR
    DEFAULT_CHANNEL = TeamsConfig.DEFAULT_CHANNEL
    USERNAME = TeamsConfig.USERNAME
    ICON_EMOJI = TeamsConfig.ICON_EMOJI
    TIMEOUT_SECONDS = TeamsConfig.TIMEOUT_SECONDS
    IS_CONFIGURED = TeamsConfig.IS_CONFIGURED

    @property
    def name(self) -> str:
        """Returns the layer name."""
        return "TeamsConfigENUM"

