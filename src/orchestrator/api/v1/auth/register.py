"""Register auth orchestrator for API v1."""

from typing import Any
from abstractions import DTOLayer
from constants import Orchestrator
from .abstraction import IAuthOrchestrator


class RegisterAuthOrchestrator(IAuthOrchestrator):
    """Orchestration service for user registration workflow."""

    async def execute(self, request: DTOLayer) -> DTOLayer:
        """Execute user registration workflow."""
        return request

    @property
    def name(self) -> str:
        """Returns the class name."""
        return Orchestrator.REGISTER_AUTH
