"""content_type enum module."""

from enum import Enum
from abstractions import EnumLayer
from constants import APIResponseContentType


class APIResponseContentTypeENUM(EnumLayer):
    APPLICATION_JSON = APIResponseContentType.APPLICATION_JSON
    APPLICATION_XML = APIResponseContentType.APPLICATION_XML
    APPLICATION_PDF = APIResponseContentType.APPLICATION_PDF
    APPLICATION_ZIP = APIResponseContentType.APPLICATION_ZIP
    APPLICATION_GZIP = APIResponseContentType.APPLICATION_GZIP
    APPLICATION_OCTET_STREAM = APIResponseContentType.APPLICATION_OCTET_STREAM
    APPLICATION_FORM_URLENCODED = APIResponseContentType.APPLICATION_FORM_URLENCODED
    APPLICATION_JAVASCRIPT = APIResponseContentType.APPLICATION_JAVASCRIPT
    APPLICATION_MSWORD = APIResponseContentType.APPLICATION_MSWORD
    APPLICATION_DOCX = APIResponseContentType.APPLICATION_DOCX
    APPLICATION_XLSX = APIResponseContentType.APPLICATION_XLSX
    APPLICATION_PPTX = APIResponseContentType.APPLICATION_PPTX
    TEXT_PLAIN = APIResponseContentType.TEXT_PLAIN
    TEXT_HTML = APIResponseContentType.TEXT_HTML
    TEXT_CSS = APIResponseContentType.TEXT_CSS
    TEXT_CSV = APIResponseContentType.TEXT_CSV
    TEXT_XML = APIResponseContentType.TEXT_XML
    TEXT_MARKDOWN = APIResponseContentType.TEXT_MARKDOWN
    TEXT_EVENT_STREAM = APIResponseContentType.TEXT_EVENT_STREAM
    MULTIPART_FORM_DATA = APIResponseContentType.MULTIPART_FORM_DATA
    MULTIPART_BYTERANGES = APIResponseContentType.MULTIPART_BYTERANGES
    IMAGE_PNG = APIResponseContentType.IMAGE_PNG
    IMAGE_JPEG = APIResponseContentType.IMAGE_JPEG
    IMAGE_GIF = APIResponseContentType.IMAGE_GIF
    IMAGE_SVG = APIResponseContentType.IMAGE_SVG
    IMAGE_WEBP = APIResponseContentType.IMAGE_WEBP
    IMAGE_ICO = APIResponseContentType.IMAGE_ICO
    AUDIO_MPEG = APIResponseContentType.AUDIO_MPEG
    AUDIO_WAV = APIResponseContentType.AUDIO_WAV
    VIDEO_MP4 = APIResponseContentType.VIDEO_MP4
    VIDEO_WEBM = APIResponseContentType.VIDEO_WEBM

    @property
    def name(self) -> str:
        """Returns the layer name."""
        return "APIResponseContentTypeENUM"

