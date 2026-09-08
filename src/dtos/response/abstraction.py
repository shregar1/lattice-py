from abc import abstractmethod
from datetime import datetime, timezone
from pydantic import Field
from typing import Any, Dict, List, Optional, Self

from constants import ApiResponseKey
from constants import ApiStatus
from ..abstraction import IDTO
from dtos import ErrorDTO
from dtos import MetaDataDTO


class IResponseDTO(IDTO):
    transaction_urn: str = Field(alias=ApiResponseKey.TRANSACTION_URN)
    status: str = Field(alias=ApiResponseKey.STATUS)
    response_message: str = Field(alias=ApiResponseKey.RESPONSE_MESSAGE)
    response_key: str = Field(alias=ApiResponseKey.RESPONSE_KEY)
    data: Dict[str, Any] | List[Any] = Field(alias=ApiResponseKey.DATA, default_factory=dict)
    errors: List[ErrorDTO] = Field(alias=ApiResponseKey.ERRORS, default_factory=list)
    metadata: Optional[MetaDataDTO] = Field(alias=ApiResponseKey.METADATA, default=None)
    timestamp: datetime = Field(
        alias=ApiResponseKey.TIMESTAMP, default_factory=lambda: datetime.now(timezone.utc)
    )
    reference_urn: Optional[str] = Field(alias=ApiResponseKey.REFERENCE_URN, default=None)

    @classmethod
    def build(
        cls,
        transaction_urn: str,
        response_message: str,
        response_key: str,
        status: str = ApiStatus.SUCCESS,
        data: Optional[IDTO] = None,
        errors: List[ErrorDTO] = None,
        metadata: MetaDataDTO = None,
        timestamp: datetime = datetime.now(timezone.utc),
        reference_urn: Optional[str] = None,
    ) -> Self:

        if isinstance(data, IDTO):
            data = data.model_dump()
        else:
            data = {}

        return cls(
            transaction_urn=transaction_urn,
            status=status,
            response_message=response_message,
            response_key=response_key,
            data=data,
            errors=errors,
            metadata=metadata,
            timestamp=timestamp,
            reference_urn=reference_urn,
        )

    @property
    @abstractmethod
    def name(self) -> str:
        """Returns the layer name that every subclass must define."""
        pass
