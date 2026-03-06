# Python automation scripts collection

![Python](https://img.shields.io/badge/python-3.13.3-blue?logo=python)
![License](https://img.shields.io/badge/license-MIT-green)
![Tests](https://img.shields.io/badge/tests-passing-brightgreen)

A curated set of reusable Python scripts that automate common development and operational tasks.
Each script is designed to be lightweight, well‑documented, and easy to integrate into CI pipelines or local workflows.

## Requirements

* Python version: 3.13.3
* Pytest

## Create virtual env

python -m venv .venv

Activate:

Windows:
.venv\Scripts\activate

MacOS/Linux
source .venv/bin/activate

## Install dependencies

pip install -e .
pip install pytest

## Docker support

Alternatively, you can use Docker:

docker build --target test -t myapp-test .
docker run --rm myapp-test

## Run tests

pytest

or

.venv/bin/python -m pytest
