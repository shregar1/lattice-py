from typing import Final
from .abstraction import EncodingKey


class HashAlgorithm(EncodingKey):
    SHA256: Final[str] = "sha256"
    SHA512: Final[str] = "sha512"
    SHA1: Final[str] = "sha1"
    MD5: Final[str] = "md5"
    BCRYPT: Final[str] = "bcrypt"
    ARGON2: Final[str] = "argon2"

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "HashAlgorithm"
