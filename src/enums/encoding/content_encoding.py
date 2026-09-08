"""content_encoding enum module."""

from enum import Enum
from abstractions import EnumLayer
from constants import ContentEncoding


class ContentEncodingENUM(EnumLayer):
    GZIP = ContentEncoding.GZIP
    DEFLATE = ContentEncoding.DEFLATE
    BR = ContentEncoding.BR
    IDENTITY = ContentEncoding.IDENTITY

    @property
    def name(self) -> str:
        """Returns the layer name."""
        return "ContentEncodingENUM"

