from lattice.exceptions.base import BaseException

class TimeoutException(BaseException):
    def __init__(self, message: str = "Request timeout", response_key: str = "TIMEOUTEXCEPTION"):
        super().__init__(message, 504, response_key)
