from lattice.exceptions.base import BaseException

class ConflictException(BaseException):
    def __init__(self, message: str = "Resource conflict", response_key: str = "CONFLICTEXCEPTION"):
        super().__init__(message, 409, response_key)
