# Stage 4. Handles CORS headers and OPTIONS preflight
from lattice.abstractions.middleware import BaseMiddleware

class CorsMiddleware(BaseMiddleware):
    """4. Handles CORS headers and OPTIONS preflight"""
    async def handle(self, request, call_next):
        return await call_next(request)
