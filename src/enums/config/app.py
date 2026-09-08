"""app enum module."""

from enum import Enum
from abstractions import EnumLayer
from constants import AppConfig


class AppConfigENUM(EnumLayer):
    CONFIG_PATH = AppConfig.CONFIG_PATH
    POWERED_BY = AppConfig.POWERED_BY
    HOST = AppConfig.HOST
    PORT = AppConfig.PORT
    RATE_LIMIT_MAX = AppConfig.RATE_LIMIT_MAX
    RATE_LIMIT_WINDOW_SECONDS = AppConfig.RATE_LIMIT_WINDOW_SECONDS
    REQUEST_TIMEOUT = AppConfig.REQUEST_TIMEOUT
    DEBUG = AppConfig.DEBUG

    @property
    def name(self) -> str:
        """Returns the layer name."""
        return "AppConfigENUM"

