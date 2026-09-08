from typing import Final
from .abstraction import IAPIConstant


class ApiResponseKey(IAPIConstant):

    TRANSACTION_URN: Final[str] = "transactionURN"
    STATUS: Final[str] = "status"
    RESPONSE_MESSAGE: Final[str] = "responseMessage"
    RESPONSE_KEY: Final[str] = "responseKey"
    ERRORS: Final[str] = "errors"
    TIMESTAMP: Final[str] = "timestamp"
    METADATA: Final[str] = "metadata"
    DATA: Final[str] = "data"
    REFERENCE_URN: Final[str] = "referenceURN"

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "ApiResponseKey"
