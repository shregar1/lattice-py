"""Authentication controller module for API v1."""

from .abstraction import IAuthController
from auth.login import LoginAuthController
from auth.logout import LogoutAuthController
from auth.register import RegisterAuthController
