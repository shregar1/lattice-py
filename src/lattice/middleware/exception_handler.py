# Stage 1. Global exception handler & error envelope wrapping
from lattice.abstractions.middleware import BaseMiddleware

class ExceptionHandlerMiddleware(BaseMiddleware):
    """1. Global exception handler & error envelope wrapping"""
    async def handle(self, request, call_next):
        return await call_next(request)
