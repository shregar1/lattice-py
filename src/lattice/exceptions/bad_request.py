from lattice.exceptions.base import BaseException

class BadRequestException(BaseException):
    def __init__(self, message: str = "Bad request", response_key: str = "BADREQUESTEXCEPTION"):
        super().__init__(message, 400, response_key)
