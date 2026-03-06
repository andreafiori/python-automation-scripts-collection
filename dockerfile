FROM python:3.12-slim AS base
WORKDIR /app
COPY pyproject.toml .
COPY src ./src
RUN pip install --upgrade pip && pip install .

FROM base AS test
COPY tests ./tests
RUN pip install pytest
CMD ["pytest"]