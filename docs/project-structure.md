# Project structure

Repository layout of `math4ai-plot`:

| Path | Role |
|---|---|
| `__init__.py` | Public API exports and package version |
| `colors.py` | Shared color constants |
| `matrix_vis.py` | Matrix class and matrix annotation helpers |
| `vector_vis.py` | Vector, arrow, and affine grid helpers |
| `figure_utils.py` | Save helpers and grid/font customization |
| `icon_utils.py` | Built-in icon drawing functions |
| `mindmap.py` | JSON-driven mindmap renderer |
| `setup.py` | Package metadata and dependencies |
| `dev.md` | Developer and release instructions |
| `packaging/` | Encryption, loader extension, release wheel scripts |

## Packaging folders

- `packaging/encrypt/`: builds encrypted payload archive
- `packaging/dploader/`: C extension for loading encrypted modules
- `packaging/release/`: wheel assembly and cibuildwheel config

## Public API source of truth

Public imports are defined by `__init__.py` and `__all__`.
Any new function intended for users should be exported there.
