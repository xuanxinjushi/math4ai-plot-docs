# Vector visualization

Vector helpers live in `vector_vis.py`.

## Functions

## `draw_affine_grid`

```python
draw_affine_grid(ax, origin, v1, v2, n=8, color="gray", alpha=0.4)
```

Draws a lattice of lines through `origin` using basis directions `v1` and `v2`.

## `draw_vec`

```python
draw_vec(ax, v, color, label=None, offset=(0, 0), origin=(0, 0), lw=2.5, mutation_scale=18)
```

Draws a vector arrow from `origin` to endpoint `v`.

## `arrow`

```python
arrow(ax, p, q, color, lw=2, mutation_scale=15)
```

Draws an arrow from point `p` to point `q`.

## Example

```python
import matplotlib.pyplot as plt
from math4ai import draw_affine_grid, draw_vec, arrow

fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-4, 4)
ax.set_ylim(-4, 4)
ax.set_aspect("equal")

draw_affine_grid(ax, origin=(0, 0), v1=(1.0, 0.2), v2=(-0.3, 1.0), n=6)
draw_vec(ax, (2.2, 1.3), color="tab:blue", label="v", offset=(0.1, 0.1))
arrow(ax, (0, 0), (-1.4, 2.1), color="tab:orange")

plt.show()
```
