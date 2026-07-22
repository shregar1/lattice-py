class BaseException(Exception):
    """Base domain exception with status code and error key."""
    def __init__(self, message: str, status_code: int = 500, response_key: str = "INTERNAL_ERROR"):
        super().__init__(message)
        self.message = message
        self.status_code = status_code
        self.response_key = response_key
