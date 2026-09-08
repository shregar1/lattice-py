"""encoding enum module."""

from enum import Enum
from abstractions import EnumLayer
from constants import Encoding


class EncodingENUM(EnumLayer):
    UTF_8 = Encoding.UTF_8
    UTF_16 = Encoding.UTF_16
    UTF_32 = Encoding.UTF_32
    ASCII = Encoding.ASCII
    LATIN_1 = Encoding.LATIN_1
    ISO_8859_1 = Encoding.ISO_8859_1
    BASE64 = Encoding.BASE64
    HEX = Encoding.HEX

    @property
    def name(self) -> str:
        """Returns the layer name."""
        return "EncodingENUM"

