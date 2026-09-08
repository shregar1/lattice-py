"""Encryption algorithms and parameters constants."""

from typing import Final

from .abstraction import IConstant


class Encryption(IConstant):

    AES_256_GCM: Final[str] = "AES-256-GCM"
    AES_256_CBC: Final[str] = "AES-256-CBC"
    AES_128_GCM: Final[str] = "AES-128-GCM"
    AES_128_CBC: Final[str] = "AES-128-CBC"
    CHACHA20_POLY1305: Final[str] = "ChaCha20-Poly1305"
    RSA_OAEP: Final[str] = "RSA-OAEP"
    FERNET: Final[str] = "Fernet"

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "Encryption"
