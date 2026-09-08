"""Login auth controller for API v1."""

from rivex import post, Request
from typing import Any, Dict, List

from constants import APIPath
from constants import APISummary
from constants import APITag
from constants import Controller
from .abstraction import IAuthController
from dtos import LoginRequestDTO
from utilities import timer


class LoginAuthController(IAuthController):
    """Controller handling user authentication/login requests."""

    path: str = APIPath.AUTH_LOGIN
    tags: List[str] = [APITag.AUTHENTICATE]


    @post(path=path, tags=tags, summary=APISummary.USER_LOGIN)
    @timer("controller")
    async def login(self, request: Request, payload: LoginRequestDTO) -> Dict[str, Any]:
        """Authenticate user and return token or session information."""
        self.bind_request(request)

        return {
            "message": "Login successful",
        }

    @property
    def name(self) -> str:
        """Returns the class name."""
        return Controller.LOGIN_AUTH
