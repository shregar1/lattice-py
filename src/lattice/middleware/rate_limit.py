# Stage 9. Sliding-window rate limiter
from lattice.abstractions.middleware import BaseMiddleware

class RateLimitMiddleware(BaseMiddleware):
    """9. Sliding-window rate limiter"""
    async def handle(self, request, call_next):
        return await call_next(request)
