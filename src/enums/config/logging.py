"""logging enum module."""

from enum import Enum
from abstractions import EnumLayer
from constants import LoggingConfig


class LoggingConfigENUM(EnumLayer):
    CONFIG_PATH = LoggingConfig.CONFIG_PATH
    STDOUT = LoggingConfig.STDOUT
    CALLER_INFO = LoggingConfig.CALLER_INFO
    LEVEL = LoggingConfig.LEVEL
    STDOUT_FORMAT = LoggingConfig.STDOUT_FORMAT
    STDOUT_COLOR = LoggingConfig.STDOUT_COLOR
    SAMPLE_ONE_IN = LoggingConfig.SAMPLE_ONE_IN

    @property
    def name(self) -> str:
        """Returns the layer name."""
        return "LoggingConfigENUM"

