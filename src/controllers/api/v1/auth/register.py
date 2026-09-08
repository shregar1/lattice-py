"""Register auth controller for API v1."""

from rivex import post, Request
from typing import Any, Dict, List

from constants import APIPath
from constants import APISummary
from constants import APITag
from constants import Controller
from .abstraction import IAuthController
from utilities import timer


class RegisterAuthController(IAuthController):
    """Controller handling user registration requests."""

    path: str = APIPath.AUTH_REGISTER
    tags: List[str] = [APITag.AUTHENTICATE]


    @post(path=path, tags=tags, summary=APISummary.USER_REGISTRATION)
    @timer("controller")
    async def register(self, request: Request) -> Dict[str, Any]:
        """Register a new user account."""
        self.bind_request(request)

        return {
            "message": "Registration successful",
        }

    @property
    def name(self) -> str:
        """Returns the class name."""
        return Controller.REGISTER_AUTH
