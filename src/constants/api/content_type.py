"""API content type constants."""

from typing import Final
from .abstraction import IAPIConstant


class APIResponseContentType(IAPIConstant):

    # Application Content Types
    APPLICATION_JSON: Final[str] = "application/json"
    APPLICATION_XML: Final[str] = "application/xml"
    APPLICATION_PDF: Final[str] = "application/pdf"
    APPLICATION_ZIP: Final[str] = "application/zip"
    APPLICATION_GZIP: Final[str] = "application/gzip"
    APPLICATION_OCTET_STREAM: Final[str] = "application/octet-stream"
    APPLICATION_FORM_URLENCODED: Final[str] = "application/x-www-form-urlencoded"
    APPLICATION_JAVASCRIPT: Final[str] = "application/javascript"
    APPLICATION_MSWORD: Final[str] = "application/msword"
    APPLICATION_DOCX: Final[str] = (
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )
    APPLICATION_XLSX: Final[str] = (
        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    APPLICATION_PPTX: Final[str] = (
        "application/vnd.openxmlformats-officedocument.presentationml.presentation"
    )

    # Text Content Types
    TEXT_PLAIN: Final[str] = "text/plain"
    TEXT_HTML: Final[str] = "text/html"
    TEXT_CSS: Final[str] = "text/css"
    TEXT_CSV: Final[str] = "text/csv"
    TEXT_XML: Final[str] = "text/xml"
    TEXT_MARKDOWN: Final[str] = "text/markdown"
    TEXT_EVENT_STREAM: Final[str] = "text/event-stream"

    # Multipart Content Types
    MULTIPART_FORM_DATA: Final[str] = "multipart/form-data"
    MULTIPART_BYTERANGES: Final[str] = "multipart/byteranges"

    # Image Content Types
    IMAGE_PNG: Final[str] = "image/png"
    IMAGE_JPEG: Final[str] = "image/jpeg"
    IMAGE_GIF: Final[str] = "image/gif"
    IMAGE_SVG: Final[str] = "image/svg+xml"
    IMAGE_WEBP: Final[str] = "image/webp"
    IMAGE_ICO: Final[str] = "image/x-icon"

    # Audio & Video Content Types
    AUDIO_MPEG: Final[str] = "audio/mpeg"
    AUDIO_WAV: Final[str] = "audio/wav"
    VIDEO_MP4: Final[str] = "video/mp4"
    VIDEO_WEBM: Final[str] = "video/webm"

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "APIResponseContentType"
