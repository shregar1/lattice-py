from typing import Final
from .abstraction import IConfigurationConstant


class LoggingConfig(IConfigurationConstant):

    CONFIG_PATH: Final[str] = "configs/logging/config.json"
    STDOUT: Final[bool] = True
    CALLER_INFO: Final[bool] = True
    LEVEL: Final[str] = "info"
    STDOUT_FORMAT: Final[str] = "pretty"
    STDOUT_COLOR: Final[str] = "auto"
    SAMPLE_ONE_IN: Final[int] = 1

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "LoggingConfig"
