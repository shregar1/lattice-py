# Stage 11. Multi-tenant header & boundary resolution
from lattice.abstractions.middleware import BaseMiddleware

class TenantResolutionMiddleware(BaseMiddleware):
    """11. Multi-tenant header & boundary resolution"""
    async def handle(self, request, call_next):
        return await call_next(request)
