from typing import Dict, Any, Type

from ..abstraction import IFactory

from constants import Utility
from utilities import CryptoUtility
from utilities import EmailUtility
from utilities import HashingUtility
from utilities import JWTUtility
from utilities import Logger
from utilities import URNUtility
from utilities import RequestTimingUtility
from utilities import ResponseUtility
from utilities import SMSUtility
from utilities import ValidationUtility


class UtilityFactory(IFactory[Any]):
    _registry: Dict[str, Type[Any]] = {
        Utility.LOGGER: Logger,
        Utility.EMAIL: EmailUtility,
        Utility.SMS: SMSUtility,
        Utility.CRYPTO: CryptoUtility,
        Utility.HASHING: HashingUtility,
        Utility.JWT: JWTUtility,
        Utility.VALIDATION: ValidationUtility,
        Utility.RESPONSE: ResponseUtility,
        Utility.REQUEST_TIMING: RequestTimingUtility,
        Utility.URN: URNUtility,
    }

    def get(self, utility_name: str, **overrides: Any) -> Any:
        key = utility_name.lower()

        if utility_name == "parse_public_urn":
            return URNUtility.parse_public_urn(**overrides)

        if key not in self._registry:
            raise KeyError(
                f"Unknown utility name: '{utility_name}'. Available: {list(self._registry.keys())}"
            )
        utility_cls = self._registry[key]

        return utility_cls(**overrides)
