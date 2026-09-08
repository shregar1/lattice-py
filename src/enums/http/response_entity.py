"""response_entity enum module."""

from enum import Enum
from abstractions import EnumLayer
from constants import ResponseEntity


class ResponseEntityENUM(EnumLayer):
    STATUS = ResponseEntity.STATUS
    BODY = ResponseEntity.BODY
    HEADERS = ResponseEntity.HEADERS

    @property
    def name(self) -> str:
        """Returns the layer name."""
        return "ResponseEntityENUM"

