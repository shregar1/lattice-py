from typing import Final

from .abstraction import IConstant


class Hashing(IConstant):

    ARGON2: Final[str] = "argon2"
    BCRYPT: Final[str] = "bcrypt"
    HMAC_SHA256: Final[str] = "sha256"
    HMAC_SHA512: Final[str] = "sha512"
    HMAC_MD5: Final[str] = "md5"

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "Hashing"
