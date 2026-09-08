"""Orchestrator dependency layer constants."""

from .abstraction import ILayerConstant


class OrchestratorDependency(ILayerConstant):

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "OrchestratorDependency"
