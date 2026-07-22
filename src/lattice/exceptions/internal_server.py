from lattice.exceptions.base import BaseException

class InternalServerException(BaseException):
    def __init__(self, message: str = "Internal server error", response_key: str = "INTERNALSERVEREXCEPTION"):
        super().__init__(message, 500, response_key)
