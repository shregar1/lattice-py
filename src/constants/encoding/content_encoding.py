from typing import Final
from .abstraction import EncodingKey


class ContentEncoding(EncodingKey):
    GZIP: Final[str] = "gzip"
    DEFLATE: Final[str] = "deflate"
    BR: Final[str] = "br"
    IDENTITY: Final[str] = "identity"

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "ContentEncoding"
