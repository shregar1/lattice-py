"""status enum module."""

from enum import Enum
from abstractions import EnumLayer
from constants import ApiStatus


class ApiStatusENUM(EnumLayer):
    OK = ApiStatus.OK
    SUCCESS = ApiStatus.SUCCESS
    FAILED = ApiStatus.FAILED

    @property
    def name(self) -> str:
        """Returns the layer name."""
        return "ApiStatusENUM"

