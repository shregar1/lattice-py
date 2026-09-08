"""key enum module."""

from enum import Enum
from abstractions import EnumLayer
from constants import ApiResponseKey


class ApiResponseKeyENUM(EnumLayer):
    TRANSACTION_URN = ApiResponseKey.TRANSACTION_URN
    STATUS = ApiResponseKey.STATUS
    RESPONSE_MESSAGE = ApiResponseKey.RESPONSE_MESSAGE
    RESPONSE_KEY = ApiResponseKey.RESPONSE_KEY
    ERRORS = ApiResponseKey.ERRORS
    TIMESTAMP = ApiResponseKey.TIMESTAMP
    METADATA = ApiResponseKey.METADATA
    DATA = ApiResponseKey.DATA
    REFERENCE_URN = ApiResponseKey.REFERENCE_URN

    @property
    def name(self) -> str:
        """Returns the layer name."""
        return "ApiResponseKeyENUM"

