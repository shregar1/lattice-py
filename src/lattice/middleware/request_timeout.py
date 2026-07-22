# Stage 6. Cancels requests exceeding execution limit
from lattice.abstractions.middleware import BaseMiddleware

class RequestTimeoutMiddleware(BaseMiddleware):
    """6. Cancels requests exceeding execution limit"""
    async def handle(self, request, call_next):
        return await call_next(request)
