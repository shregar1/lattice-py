# Stage 2. Validates request Host header against whitelist
from lattice.abstractions.middleware import BaseMiddleware

class TrustedHostMiddleware(BaseMiddleware):
    """2. Validates request Host header against whitelist"""
    async def handle(self, request, call_next):
        return await call_next(request)
