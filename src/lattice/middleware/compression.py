# Stage 5. Payload Gzip/Deflate compression
from lattice.abstractions.middleware import BaseMiddleware

class CompressionMiddleware(BaseMiddleware):
    """5. Payload Gzip/Deflate compression"""
    async def handle(self, request, call_next):
        return await call_next(request)
