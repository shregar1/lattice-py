from lattice.exceptions.base import BaseException

class UnauthorizedException(BaseException):
    def __init__(self, message: str = "Unauthorized access", response_key: str = "UNAUTHORIZEDEXCEPTION"):
        super().__init__(message, 403, response_key)
