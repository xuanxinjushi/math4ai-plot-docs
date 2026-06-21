# Installation

Math4AI supports Linux x86_64 and Python 3.9+.

## Install from PyPI

```bash
pip install math4ai
```

Verify:

```bash
python -c "from math4ai import point_x_color; print(point_x_color)"
```

## Conda environment example

```bash
conda create -n math4ai python=3.12
conda activate math4ai
pip install math4ai
```

## Editable install (development)

If you work from source:

```bash
cd ~/math4ai-plot
pip install -e .
```

This installs the package in editable mode so local source changes are picked up immediately.

## Dependencies

Installed automatically:

- matplotlib >= 3.0.0
- numpy >= 1.18.0
