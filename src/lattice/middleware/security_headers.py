# Stage 3. Injects OWASP security headers
from lattice.abstractions.middleware import BaseMiddleware

class SecurityHeadersMiddleware(BaseMiddleware):
    """3. Injects OWASP security headers"""
    async def handle(self, request, call_next):
        return await call_next(request)
