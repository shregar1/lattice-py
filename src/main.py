from dotenv import load_dotenv

import os
import nest_asyncio

from pathlib import Path
from rivex import CORSMiddleware, Dependency, Rivex, StaticFiles

from configurations import AppConfiguration
from dependencies import LoggerUtilityDependency
from middlewares import (
    ContentTypeValidationMiddleware,
    TracingMiddleware,
    SizeLimitMiddleware,
    RequestContextMiddleware,
    SecurityHeadersMiddleware,
    RequestValidationMiddleware,
    ApiKeyLeakRule,
    ProhibitedIntegerIdRule,
    SanitizePiiDataRule,
    SanitizeXssSqlInjectionRule,
)
from utilities import Logger

nest_asyncio.apply()
logger: Logger = Dependency(LoggerUtilityDependency)

logger.info("Loading configurations")
config: AppConfiguration = AppConfiguration.load()
logger.info("Configurations loaded")

logger.info("Loading environment variables")
load_dotenv()
APP_NAME = os.environ.get("PROJECT_NAME")
SERVICE_NAME = os.environ.get("SERVICE_NAME")
SERVICE_VERSION = os.environ.get("SERVICE_VERSION")
DESCRIPTION = os.environ.get("DESCRIPTION")
POWERED_BY = os.environ.get("POWERED_BY")
ADMIN_ENABLED = os.environ.get("ADMIN_ENABLED")
ADMIN_URL = os.environ.get("ADMIN_URL")
ADMIN_TOKEN = os.environ.get("ADMIN_TOKEN")
PROJECT_ROOT = Path(os.environ.get("PROJECT_ROOT")).resolve()
ADMIN_CODEGEN_ENABLED = os.environ.get("ADMIN_CODEGEN_ENABLED")
logger.info("Environment variables loaded")

logger.info("Initializing Rivex APP")
app = Rivex(
    title=APP_NAME,
    version=SERVICE_VERSION,
    description=DESCRIPTION,
    app_name=APP_NAME,
    powered_by=POWERED_BY,
    admin_url=ADMIN_URL if ADMIN_ENABLED else None,
    admin_token=ADMIN_TOKEN,
)
app.project_root = PROJECT_ROOT
logger.info("Rivex APP initialized")

logger.info("Adding middlewares")
app.add_middleware(
    CORSMiddleware,
    allow_origins=[config.settings.app.cors_origin],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)
app.add_middleware(
    RequestContextMiddleware,
    service_name=SERVICE_NAME,
    service_version=SERVICE_VERSION
)
app.add_middleware(SecurityHeadersMiddleware)
app.add_middleware(TracingMiddleware)
app.add_middleware(ContentTypeValidationMiddleware)
app.add_middleware(SizeLimitMiddleware, max_bytes=2000000)
validation_middleware = (
    RequestValidationMiddleware.builder()
    .with_rule(ProhibitedIntegerIdRule())
    .with_rule(ApiKeyLeakRule(exclude_paths=["/api/v1/auth/api-keys*", "/api/v1/keys/*"]))
    .with_rule(SanitizeXssSqlInjectionRule())
    .with_rule(SanitizePiiDataRule())
    .build()
)
app.add_middleware(RequestValidationMiddleware, rules=validation_middleware.rules)
logger.info("Middlewares added")

logger.info("Including routers")
app.include_router()
logger.info("Routers included")

logger.info("Mounting static files")
config.path.media_dir.mkdir(parents=True, exist_ok=True)
app.mount(config.path.media_url_prefix, StaticFiles(directory=str(config.path.media_dir)))
logger.info("Static files mounted")

if __name__ == "__main__":
    app.run(host=config.settings.app.host, port=config.settings.app.port)
