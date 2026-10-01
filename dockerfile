FROM python:3.12-slim AS base

WORKDIR /app

COPY pyproject.toml .
COPY src ./src

RUN pip install --no-cache-dir --upgrade pip
&& pip install --no-cache-dir .

FROM base AS test

COPY tests ./tests

RUN pip install --no-cache-dir pytest

CMD ["pytest"]