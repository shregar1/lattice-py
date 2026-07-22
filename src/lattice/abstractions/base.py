# Lattice (Python Edition) — Abstractions
# Base abstractions for Models, Services, Controllers, and Repositories.

class BaseModel:
    """Base persistent entity model."""
    pass

class BaseRepository:
    """Base persistence abstraction for SQLAlchemy AsyncIO."""
    pass

class BaseService:
    """Base domain capability service."""
    pass

class BaseOrchestrator:
    """Base workflow orchestrator managing Unit of Work boundaries."""
    pass

class BaseController:
    """Base thin HTTP controller."""
    pass
