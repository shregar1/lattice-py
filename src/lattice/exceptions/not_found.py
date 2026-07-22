from lattice.exceptions.base import BaseException

class NotFoundException(BaseException):
    def __init__(self, message: str = "Resource not found", response_key: str = "NOTFOUNDEXCEPTION"):
        super().__init__(message, 404, response_key)
