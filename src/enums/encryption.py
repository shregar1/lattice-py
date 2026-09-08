"""encryption enum module."""

from enum import Enum
from abstractions import EnumLayer
from constants import Encryption


class EncryptionENUM(EnumLayer):
    AES_256_GCM = Encryption.AES_256_GCM
    AES_256_CBC = Encryption.AES_256_CBC
    AES_128_GCM = Encryption.AES_128_GCM
    AES_128_CBC = Encryption.AES_128_CBC
    CHACHA20_POLY1305 = Encryption.CHACHA20_POLY1305
    RSA_OAEP = Encryption.RSA_OAEP
    FERNET = Encryption.FERNET

    @property
    def name(self) -> str:
        """Returns the layer name."""
        return "EncryptionENUM"

