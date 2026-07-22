from abc import ABC

class BaseOrchestrator(ABC):
    """Base workflow orchestrator managing Unit of Work boundaries."""
    def __init__(self, unit_of_work):
        self.unit_of_work = unit_of_work
