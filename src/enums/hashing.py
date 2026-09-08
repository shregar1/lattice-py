"""hashing enum module."""

from enum import Enum
from abstractions import EnumLayer
from constants import Hashing


class HashingENUM(EnumLayer):
    ARGON2 = Hashing.ARGON2
    BCRYPT = Hashing.BCRYPT

    @property
    def name(self) -> str:
        """Returns the layer name."""
        return "HashingENUM"

