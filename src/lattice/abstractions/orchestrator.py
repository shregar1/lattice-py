# Lattice (Python Edition) — Orchestrator Abstraction
from abc import ABC
from typing import Callable, TypeVar, Any

T = TypeVar("T")

class BaseOrchestrator(ABC):
    """Base workflow orchestrator managing Unit of Work boundaries."""

    def __init__(self, unit_of_work: Any):
        self.unit_of_work = unit_of_work

    async def execute_in_transaction(self, work: Callable[[], Any], action_name: str) -> Any:
        """Executes a workflow within a Unit of Work transaction boundary."""
        async with self.unit_of_work.transaction():
            return await work()
