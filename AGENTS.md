# [AGENTS.md](http://AGENTS.md)

Guidance for AI coding agents (and human collaborators) working in this repository. Follow these rules unless the user explicitly overrides them.

## What this repository is

A monorepo of small, independent Python projects that automate development and operational tasks. Projects do not share state: each one owns its dependencies, tests, and Dockerfile.

## Repository layout

```text
automation/
├── apps/           # Finished, user-facing tools (production-ready)
│   ├── excel-report/
│   ├── website-monitor/
│   ├── pdf-organizer/
│   └── network-checker/
├── packages/       # Shared internal libraries (filesystem, logging, config)
│   ├── filesystem/
│   ├── logging/
│   └── config/
└── experiments/    # Prototypes and spikes (not production-ready)
    ├── selenium-test/
    ├── playwright-test/
    └── ai-experiments/
```

Placement rules:

- Complete, tested tools → `apps/`
- Code shared by two or more apps → `packages/`
- Prototypes, spikes, technology evaluations → `experiments/`

Never promote a project out of `experiments/` without asking: it requires
tests, a README, and a review of the definition of done.

## Environment and commands

Python 3.13+ with [uv](https://github.com/astral-sh/uv) as package manager.

```bash
uv venv                             # create virtual environment
source .venv/bin/activate           # Windows: .venv\Scripts\activate
uv pip install -e .                 # install a project in editable mode

pytest                              # run all tests
pytest apps/excel-report            # test one project
pytest packages/filesystem          # test one package
```

Always run the tests of the project you touched — and of any `packages/` dependents — before declaring a task complete.

## Conventions

- One project = one folder under `apps/`, `packages/`, or `experiments/`, with its own `pyproject.toml`.
- Shared code lives in `packages/`; apps import packages, never other apps.
- Keep dependencies minimal and pinned in each project's `pyproject.toml`.
- Public functions get type hints and a short docstring.
- Tests live in a `tests/` folder inside the project, run with `pytest`.
- Every `apps/` project has a `README.md` (what it does, how to run it) and, when containerized, a `Dockerfile`.

## Definition of done

A change is complete only when:

- All unit tests pass for the project (and its dependents, if a package changed)
- Code coverage is acceptable (no new code without at least happy-path tests)
- Docker usability is preserved — the project's image still builds and runs
- Project configuration (`pyproject.toml`, linting, tooling) is up to date
- No regressions in unrelated projects

## Things to avoid

- Cross-importing between apps — extract shared logic into `packages/` instead.
- Adding top-level dependencies or configuration that affects all projects.
- Deleting or rewriting `experiments/` content without explicit instruction.
- Committing without running the affected test suite.

## Inspiration

- [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/)
