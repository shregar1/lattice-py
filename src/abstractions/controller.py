"""HTTP controller abstraction that wraps with envelope responses."""

from abc import ABC, abstractmethod
from rivex import Controller, Request
from typing import Any, Optional, Dict, List, Tuple

from .abstraction import ILayer
from dtos import IResponseDTO


class ControllerLayer(Controller, ILayer, ABC):
    """
    Base class for HTTP controllers.

    Controllers return a response built from an ``IResponseDTO`` envelope.

    Attributes:
        path: Mount path segment used by the routing layer.
        tags: OpenAPI tags associated with the controller's endpoints.
    """

    path: str = ""
    tags: List[str] = []

    def __init__(
        self,
        urn: Optional[str] = None,
        user_id: Optional[int] = None,
        user_urn: Optional[str] = None,
        tenant_id: Optional[int] = None,
        tenant_urn: Optional[str] = None,
        api_name: Optional[str] = None,
        ip_address: Optional[str] = None,
        user_agent: Optional[str] = None,
        logger: Optional[Any] = None,
        *args: Any,
        **kwargs: Any,
    ) -> None:
        """Initializes the controller with request-scoped context."""

        ILayer.__init__(
            self,
            urn=urn,
            tenant_id=tenant_id,
            tenant_urn=tenant_urn,
            user_id=user_id,
            user_urn=user_urn,
            api_name=api_name,
            ip_address=ip_address,
            user_agent=user_agent,
            logger=logger,
            *args,
            **kwargs,
        )

        self.urn=urn
        self.tenant_id=tenant_id
        self.tenant_urn=tenant_urn
        self.user_id=user_id
        self.user_urn=user_urn
        self.api_name=api_name
        self.ip_address=ip_address
        self.user_agent=user_agent
        self.logger=logger

    @classmethod
    def path(cls) -> str:
        """Returns the base URL path the controller is mounted at."""
        return cls.path

    @classmethod
    def tags(cls) -> str:
        """
        Method to ....
        """
        return cls.path

    def bind_request(self, request: Request, *, api_name: Optional[str] = None) -> None:
        """
        Copies request metadata from a ``Request`` into the controller's context.

        Args:
            request: The incoming request whose ``state`` and ``path``
                attributes carry request id, tenant id, user id, ip and agent.
            api_name: Override for the API name; defaults to the request path.
        """
        self.bind_request_context(
            urn=getattr(request.state, "urn", None),
            tenant_urn=getattr(request.state, "tenant_urn", None),
            user_urn=getattr(request.state, "user_urn", None),
            api_name=(api_name or getattr(request, "api_name", None)),
            ip_address=getattr(request.state, "ip_address", None),
            user_agent=getattr(request.state, "user_agent", None),
        )

    @staticmethod
    def ok(
        envelope: IResponseDTO,
        status_code: int,
        extra_headers: List[Tuple[str, str]] | None = None,
    ) -> Dict[str, Any]:
        """
        Wraps a response envelope with the standard HTTP envelope payload.

        Args:
            envelope: Success or failure envelope returned by the handler.
            status_code: HTTP status code to associate with the response.
            extra_headers: Optional additional response headers.


        returns:
            A dict that serializes as the HTTP response body.
        """
        pass

    @property
    @abstractmethod
    def name(self) -> str:
        """Returns the layer name that every subclass must define."""
        pass
