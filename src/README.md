# mono-backend

> mono-backend

A Rivex-based backend service built from the layered architectural template.

- **Author:**  &lt;&gt;
- **License:** MIT
- **Year:** 2026

## Quick start

```bash
cp .env.example .env
# edit .env (database url, jwt secrets, etc.)
make dev   # http://127.0.0.1:8000
```

The `cp .env.example .env` step is part of the scaffold workflow — the generator
copies `.env.example` to `.env` automatically on first run, but the committed
template is `.env.example` (keep secrets out of source control).

## Layered architecture

```
controllers/     HTTP + WebSocket handlers (entry points)
services/        Business logic (use cases)
repositories/    Data access (ORM)
abstractions/    Ports — interfaces every layer implements
models/          ORMX persistence models
dtos/            Request / response schemas
mappers/         ORM ↔ DTO transformations
middlewares/     Request / response middleware
errors/          Domain errors with HTTP status mapping
constants/       API paths, log codes, platform defaults
configurations/  Runtime configuration singletons
configs/         JSON defaults + pydantic-settings
utilities/       Cross-cutting helpers
migrations/      ORM SQL migrations
tests/           pytest suites
```

Each concrete type in `controllers/`, `services/`, `repositories/`, etc. implements the matching interface in `abstractions/`.

## Example slice: items

`controllers/`, `services/`, `repositories/`, `models/`, `dtos/`, and `mappers/` for the `items` resource show the canonical pattern end-to-end. Copy and rename to add new slices.

## Environment

See `.env.example` for the full list of supported variables.

## Project metadata

Runtime code reads live metadata from `pyproject.toml` via `configs.project_metadata()`:

```python
from configs import project_metadata

print(project_metadata())
# {'name': 'mono-backend-backend', 'version': '0.1.0', 'description': 'mono-backend'}
```
