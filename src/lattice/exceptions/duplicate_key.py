from lattice.exceptions.base import BaseException

class DuplicateKeyException(BaseException):
    def __init__(self, message: str = "Duplicate key error", response_key: str = "DUPLICATEKEYEXCEPTION"):
        super().__init__(message, 409, response_key)
