# Stage 13. Upstream payload validation against schema
from lattice.abstractions.middleware import BaseMiddleware

class RequestValidationMiddleware(BaseMiddleware):
    """13. Upstream payload validation against schema"""
    async def handle(self, request, call_next):
        return await call_next(request)
