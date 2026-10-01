# Python Automation Projects

![Python](https://img.shields.io/badge/python-3.13.3-blue?logo=python)
![Tests](https://img.shields.io/badge/tests-passing-brightgreen)
![License](https://img.shields.io/badge/license-MIT-green)

A collection of small, independent Python projects that automate common
development and operational tasks.

Every project is self-contained: it owns its dependencies, tests, and
Dockerfile, and can be run standalone, embedded in a larger pipeline, or
plugged into CI.

## Repository layout

```text
automation/
├── apps/           # Finished, user-facing tools
│   ├── excel-report/
│   ├── website-monitor/
│   ├── pdf-organizer/
│   └── network-checker/
├── packages/       # Shared internal libraries used by apps
│   ├── filesystem/
│   ├── logging/
│   └── config/
└── experiments/    # Prototypes and spikes (not production-ready)
    ├── selenium-test/
    ├── playwright-test/
    └── ai-experiments/
```


| Path           | Purpose                                                       | Stability                   |
| -------------- | ------------------------------------------------------------- | --------------------------- |
| `apps/`        | Complete automation tools with tests and Docker support       | Production-ready            |
| `packages/`    | Shared libraries (filesystem, logging, config) reused by apps | Production-ready            |
| `experiments/` | Prototypes, spikes, technology evaluations                    | Experimental, no guarantees |


## Apps


| Project           | Description                                            |
| ----------------- | ------------------------------------------------------ |
| `excel-report`    | Generates Excel reports from raw data sources          |
| `website-monitor` | Periodically checks websites and alerts on failures    |
| `pdf-organizer`   | Renames, sorts, and merges PDF files by rules          |
| `network-checker` | Runs connectivity and latency checks on hosts/services |


Each app has its own `README.md` with usage details.

## Requirements

- [Python 3.13+](https://www.python.org/)
- [uv](https://github.com/astral-sh/uv) — recommended package manager (fallback to `pip` described below)

## Quick start with uv (recommended)

Install uv:

```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Create and activate an environment, then install a project in editable mode:

```bash
uv venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
uv pip install -e .
# or, for a shared package: uv pip install -e packages/filesystem
```

## Alternative: venv + pip

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -e .
pip install pytest
```

## Run a project

```bash
python -m apps.website-monitor        # run as a module
# or
python apps/website-monitor/main.py   # run the entry point directly
```

## Run tests

All projects:

```bash
pytest
```

A single project, with coverage report:

```bash
pytest apps/excel-report
pytest packages/filesystem --cov=filesystem --cov-report=term-missing
```

Or without activating the virtual environment:

```bash
.venv/bin/python -m pytest
```

## Docker

Every app ships a `Dockerfile` and can be built and run in isolation:

```bash
docker build -t website-monitor ./apps/website-monitor
docker run --rm website-monitor
```

Some apps also provide a `docker-compose.yml` for multi-service setups  
(e.g. monitoring with a database or notification service).

## Adding a new project

1. Create a folder under `apps/` (or `experiments/` for prototypes).
2. Add a `pyproject.toml` declaring the project and its dependencies.
3. Add a `README.md` describing what it does and how to run it.
4. Add tests under `tests/` — `pytest` must pass before the project counts as done.
5. Add a `Dockerfile` if the project should be runnable in a container.

## License

Released under the [MIT License](LICENSE).

## Inspiration

- [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/)
