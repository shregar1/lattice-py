"""jwt enum module."""

from enum import Enum
from abstractions import EnumLayer
from constants import JWT


class JWTENUM(EnumLayer):
    ACCESS = JWT.ACCESS
    REFRESH = JWT.REFRESH
    JTI = JWT.JTI
    HS256 = JWT.HS256
    HS384 = JWT.HS384
    HS512 = JWT.HS512
    RS256 = JWT.RS256

    @property
    def name(self) -> str:
        """Returns the layer name."""
        return "JWTENUM"

