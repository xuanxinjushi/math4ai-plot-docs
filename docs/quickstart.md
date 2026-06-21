# Quick start

This page shows practical first steps with the public API.

## 1. Save a simple figure beside your script

```python
import matplotlib.pyplot as plt
from math4ai import point_x_color, save_figure_to_script_dir

fig, ax = plt.subplots()
ax.scatter([1, 2, 3], [1, 4, 9], color=point_x_color)
save_figure_to_script_dir("example.png", caller_file=__file__)
```

## 2. Draw vectors

```python
import matplotlib.pyplot as plt
from math4ai import draw_vec, arrow

fig, ax = plt.subplots(figsize=(5, 5))
ax.set_xlim(-1, 4)
ax.set_ylim(-1, 4)
ax.set_aspect("equal")

draw_vec(ax, (2.5, 1.5), color="tab:blue", label="v")
arrow(ax, (0, 0), (1.2, 2.8), color="tab:red")

plt.show()
```

## 3. Draw and highlight a matrix

```python
import matplotlib.pyplot as plt
from math4ai import Matrix, finalize

fig, ax = plt.subplots(figsize=(6, 4))

m = Matrix(4, 5, cell_size=0.8)
m.highlight_diagonal(use_gradient=True)
m.draw(ax)

finalize(ax)
plt.show()
```

## 4. Render a mindmap from JSON

Create `mindmap.json` beside your script, then:

```python
from math4ai import render_mindmap

if __name__ == "__main__":
    render_mindmap(__file__)
```

The output file is saved next to your script, using the script name as PNG.
