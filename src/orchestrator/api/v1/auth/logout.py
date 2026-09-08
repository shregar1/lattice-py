"""Logout auth orchestrator for API v1."""

from typing import Any
from abstractions import DTOLayer
from constants import Orchestrator
from .abstraction import IAuthOrchestrator


class LogoutAuthOrchestrator(IAuthOrchestrator):
    """Orchestration service for user logout workflow."""

    async def execute(self, request: DTOLayer) -> DTOLayer:
        """Execute user logout workflow."""
        return request

    @property
    def name(self) -> str:
        """Returns the class name."""
        return Orchestrator.LOGOUT_AUTH
