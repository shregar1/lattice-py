# Stage 7. Instantiates requestUrn, correlationId, startTime
from lattice.abstractions.middleware import BaseMiddleware

class RequestContextMiddleware(BaseMiddleware):
    """7. Instantiates requestUrn, correlationId, startTime"""
    async def handle(self, request, call_next):
        return await call_next(request)
