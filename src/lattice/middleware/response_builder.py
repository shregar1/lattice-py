# Stage 14. Response payload envelope builder
from lattice.abstractions.middleware import BaseMiddleware

class ResponseBuilderMiddleware(BaseMiddleware):
    """14. Response payload envelope builder"""
    async def handle(self, request, call_next):
        return await call_next(request)
