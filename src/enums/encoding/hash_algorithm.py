"""hash_algorithm enum module."""

from enum import Enum
from abstractions import EnumLayer
from constants import HashAlgorithm


class HashAlgorithmENUM(EnumLayer):
    SHA256 = HashAlgorithm.SHA256
    SHA512 = HashAlgorithm.SHA512
    SHA1 = HashAlgorithm.SHA1
    MD5 = HashAlgorithm.MD5
    BCRYPT = HashAlgorithm.BCRYPT
    ARGON2 = HashAlgorithm.ARGON2

    @property
    def name(self) -> str:
        """Returns the layer name."""
        return "HashAlgorithmENUM"

