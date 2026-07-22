from datetime import datetime
from dataclasses import dataclass, field
from typing import Optional

@dataclass
class BaseModel:
    """Base persistent entity model."""
    id: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
