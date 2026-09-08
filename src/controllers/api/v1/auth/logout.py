"""Logout auth controller for API v1."""

from rivex import post, Request
from typing import Any, Dict, List

from .abstraction import IAuthController

from constants import APIPath
from constants import APISummary
from constants import APITag
from constants import Controller

from utilities import RequestTimingUtility


class LogoutAuthController(IAuthController):
    """Controller handling user logout requests."""

    path: str = APIPath.AUTH_LOGOUT
    tags: List[str] = [APITag.AUTHENTICATE]
    timer: List[str] = RequestTimingUtility()

    @post(path=path, tags=tags, summary=APISummary.USER_LOGOUT)
    @timer("controller")
    async def logout(self, request: Request) -> Dict[str, Any]:
        """Invalidate user session/token and log out."""
        self.bind_request(request)

        return {
            "message": "Logout successful",
        }

    @property
    def name(self) -> str:
        """Returns the class name."""
        return Controller.LOGOUT_AUTH
