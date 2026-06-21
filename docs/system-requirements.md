# System requirements

## Runtime

- OS: Linux x86_64
- Python: 3.9+
- Recommended Python: 3.12

## Python dependencies

- matplotlib >= 3.0.0
- numpy >= 1.18.0

These are installed automatically when installing `math4ai`.

## Verification commands

```bash
python -c "import math4ai; print(math4ai.__version__)"
python -c "from math4ai import Matrix, draw_vec, render_mindmap; print('OK')"
```
