from typing import Final
from .abstraction import EncodingKey


class Encoding(EncodingKey):
    UTF_8: Final[str] = "utf-8"
    UTF_16: Final[str] = "utf-16"
    UTF_32: Final[str] = "utf-32"
    ASCII: Final[str] = "ascii"
    LATIN_1: Final[str] = "latin-1"
    ISO_8859_1: Final[str] = "iso-8859-1"
    BASE64: Final[str] = "base64"
    HEX: Final[str] = "hex"

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "Encoding"
