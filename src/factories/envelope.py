from typing import Tuple

from .abstraction import IFactory
from dtos import IResponseDTO



class EnvelopeFactory(IFactory[Tuple[IResponseDTO, int]]):

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "EnvelopeFactory"
