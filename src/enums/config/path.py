"""path enum module."""

from enum import Enum
from abstractions import EnumLayer
from constants import PathConfig


class PathConfigENUM(EnumLayer):
    CONFIG_PATH = PathConfig.CONFIG_PATH
    LOGS_DIR = PathConfig.LOGS_DIR
    MIGRATIONS_DIR = PathConfig.MIGRATIONS_DIR
    SCRIPTS_DIR = PathConfig.SCRIPTS_DIR
    MEDIA_DIR = PathConfig.MEDIA_DIR
    MEDIA_URL_PREFIX = PathConfig.MEDIA_URL_PREFIX

    @property
    def name(self) -> str:
        """Returns the layer name."""
        return "PathConfigENUM"

