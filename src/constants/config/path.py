from typing import Final
from .abstraction import IConfigurationConstant


class PathConfig(IConfigurationConstant):

    CONFIG_PATH: Final[str] = "configs/path/config.json"
    LOGS_DIR: Final[str] = "logs"
    MIGRATIONS_DIR: Final[str] = "migrations"
    SCRIPTS_DIR: Final[str] = "scripts"
    MEDIA_DIR: Final[str] = "uploads"
    MEDIA_URL_PREFIX: Final[str] = "/media"

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "PathConfig"
