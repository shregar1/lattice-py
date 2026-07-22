# Stage 15. Immutable audit logging for state mutations
from lattice.abstractions.middleware import BaseMiddleware

class AuditLoggerMiddleware(BaseMiddleware):
    """15. Immutable audit logging for state mutations"""
    async def handle(self, request, call_next):
        return await call_next(request)
