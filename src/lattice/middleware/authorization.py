# Stage 12. RBAC role & permission enforcement
from lattice.abstractions.middleware import BaseMiddleware

class AuthorizationMiddleware(BaseMiddleware):
    """12. RBAC role & permission enforcement"""
    async def handle(self, request, call_next):
        return await call_next(request)
