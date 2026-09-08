from typing import Final
from abstractions import IConstant


class Page(IConstant):

    SIZE: Final[int] = 20
    MAX_SIZE: Final[int] = 100

    @property
    def name(self) -> str:
        """Returns the class name."""
        return "Page"
