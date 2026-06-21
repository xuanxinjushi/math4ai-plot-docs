# Matrix visualization

Matrix utilities live in `matrix_vis.py` and are exported at package top level.

## Matrix class

```python
from math4ai import Matrix
```

Constructor:

```python
Matrix(
    n,
    d,
    x_offset=0.0,
    y_offset=0.0,
    cell_size=1.0,
    cell_color="#eeeeee",
    highlight_color="#2ca02c",
    edge_color="white",
    edge_width=1.5,
    zorder=2,
)
```

- `n`: number of rows
- `d`: number of columns
- indices for helper methods are 1-based

## Common methods

- Position and size:
  - `set_position(x_offset, y_offset)`
  - `set_size(cell_size)`
- Highlighting:
  - `highlight(cells, use_gradient=False, gradient_colormap="viridis")`
  - `highlight_diagonal(...)`
  - `highlight_anti_diagonal(...)`
  - `highlight_symmetric(...)` (square matrices)
- Coloring:
  - `color_row(row, color)`
  - `color_col(col, color)`
- Geometry helpers:
  - `cell_center(i, j)`
  - `get_width()`, `get_height()`
- Render:
  - `draw(ax)`

## Helper functions

- `draw_dashed_row(ax, matrix, i, ...)`
- `draw_dashed_col(ax, matrix, j, ...)`
- `draw_column_indices(ax, matrix, ...)`
- `draw_row_indices(ax, matrix, ...)`
- `draw_piercing_row(ax, matrix, row, ...)`
- `draw_piercing_col(ax, matrix, col, ...)`
- `draw_brace(ax, start, end, text=None, ...)`
- `draw_curved_label(ax, text, x1, y1, x2, y2, ...)`
- `color_row_col(matrix, row=None, col=None, row_color=None, col_color=None)`
- `finalize(ax, equal_aspect=True)`

## Example

```python
import matplotlib.pyplot as plt
from math4ai import Matrix, draw_dashed_row, draw_dashed_col, finalize

fig, ax = plt.subplots(figsize=(7, 4))
m = Matrix(4, 6, cell_size=0.8, x_offset=0.2, y_offset=0.2)
m.highlight([(1, 2), (2, 3), (3, 4)], use_gradient=True)
m.color_row(4, "#ffe7cc")
m.color_col(1, "#d9ecff")
m.draw(ax)

draw_dashed_row(ax, m, 2, color="black", alpha=0.5)
draw_dashed_col(ax, m, 5, color="black", alpha=0.5)

finalize(ax)
plt.show()
```
