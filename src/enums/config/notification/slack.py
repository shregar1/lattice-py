"""slack enum module."""

from enum import Enum
from abstractions import EnumLayer
from constants import SlackConfig


class SlackConfigENUM(EnumLayer):
    CONFIG_PATH = SlackConfig.CONFIG_PATH
    WEBHOOK_URL = SlackConfig.WEBHOOK_URL
    DEFAULT_CHANNEL = SlackConfig.DEFAULT_CHANNEL
    USERNAME = SlackConfig.USERNAME
    ICON_EMOJI = SlackConfig.ICON_EMOJI
    TIMEOUT_SECONDS = SlackConfig.TIMEOUT_SECONDS
    IS_CONFIGURED = SlackConfig.IS_CONFIGURED

    @property
    def name(self) -> str:
        """Returns the layer name."""
        return "SlackConfigENUM"

