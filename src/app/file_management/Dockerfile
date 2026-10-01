FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
	PYTHONUNBUFFERED=1

WORKDIR /app

COPY pyproject.toml .
COPY src/ ./src

RUN python -m pip install --no-cache-dir --upgrade pip setuptools \
	&& python -m pip install --no-cache-dir . \
	&& groupadd --system app \
	&& useradd --system --gid app --create-home app \
	&& chown -R app:app /app

USER app