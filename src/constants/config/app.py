from typing import Final
from .abstraction import IConfigurationConstant


class AppConfig(IConfigurationConstant):

    CONFIG_PATH: Final[str] = "configs/app/config.json"
    NAME: Final[str] = "MONO"
    POWERED_BY: Final[str] = "vexarr"
    HOST: Final[str] = "0.0.0.0"
    PORT: Final[int] = 8000
    RATE_LIMIT_MAX: Final[int] = 100
    RATE_LIMIT_WINDOW_SECONDS: Final[int] = 60
    REQUEST_TIMEOUT: Final[int] = 30000
    DEBUG: Final[bool] = False

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "AppConfig"
