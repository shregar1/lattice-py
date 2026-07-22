from lattice.exceptions.base import BaseException

class ForbiddenException(BaseException):
    def __init__(self, message: str = "Forbidden", response_key: str = "FORBIDDENEXCEPTION"):
        super().__init__(message, 403, response_key)
