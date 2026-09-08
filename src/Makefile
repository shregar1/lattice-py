.PHONY: install dev run test lint typecheck ci env

PYTHON ?= .venv/bin/python
PROJECT_SLUG := mono-backend
PROJECT_NAME := mono-backend

env:
	@if [ ! -f .env ]; then cp .env.example .env && echo "Created .env from .env.example"; else echo ".env already exists"; fi

install: env
	pip install -e ".[dev]"

dev:
	PYTHONPATH=. $(PYTHON) main.py

run:
	PYTHONPATH=. $(PYTHON) main.py

test:
	PYTHONPATH=. $(PYTHON) -m pytest tests -q

lint:
	ruff check .

typecheck:
	$(PYTHON) -m compileall -q abstractions controllers services repositories dtos utilities constants configurations errors dependencies

ci: lint typecheck test
