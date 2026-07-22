# Stage 8. Structured JSON logging of HTTP requests
from lattice.abstractions.middleware import BaseMiddleware

class RequestLoggerMiddleware(BaseMiddleware):
    """8. Structured JSON logging of HTTP requests"""
    async def handle(self, request, call_next):
        return await call_next(request)
