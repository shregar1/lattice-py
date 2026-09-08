from controllers.health.db import HealthDbController
from controllers.health.liveness import HealthLivenessController

ALL_CONTROLLERS: Tuple[type, ...] = (HealthLivenessController, HealthDbController)

__all__ = ['ALL_CONTROLLERS', 'HealthDbController', 'HealthLivenessController']