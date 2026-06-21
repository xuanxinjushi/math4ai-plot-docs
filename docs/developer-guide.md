# Developer guide

This page summarizes development and release workflows for `math4ai-plot`.

## Platform support

- Linux x86_64
- CPython 3.9-3.13
- No official macOS or Windows release wheels

## Day-to-day development

Use editable install from source:

```bash
conda activate usao
cd ~/math4ai-plot
pip install -e .
```

Run figure scripts in the downstream content repo and iterate.

## Release wheel model

Math4AI release wheels package encrypted module payloads:

- plaintext dev sources live in repository root
- `packaging/encrypt/dp_maker.py` encrypts modules into `math4ai.dp`
- `packaging/dploader/` provides a C extension loader
- release wheel tree keeps only minimal bootstrap Python files

## Build local wheel

```bash
conda activate usao
cd ~/math4ai-plot
pip install pyzipper
PYTHON="$(which python)" bash packaging/release/make_wheel.sh
```

Result example:

- `dist/math4ai-0.1.0-cp312-cp312-linux_x86_64.whl`

## Wheel audit

```bash
unzip -l dist/math4ai-*.whl | grep '\.py$'
```

Expected Python files are minimal bootstrap stubs (`__init__.py`, `_dp_loader.py`).

## CIBW release

```bash
pip install cibuildwheel pyzipper
cibuildwheel --config-file packaging/release/pyproject.cibw.toml --output-dir dist
```

## Publish

```bash
twine check dist/math4ai-*.whl
twine upload dist/math4ai-*.whl
```

Use TestPyPI first when validating a new pipeline.
