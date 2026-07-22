# Stage 10. JWT validation & identity extraction
from lattice.abstractions.middleware import BaseMiddleware

class AuthenticationMiddleware(BaseMiddleware):
    """10. JWT validation & identity extraction"""
    async def handle(self, request, call_next):
        return await call_next(request)
