# Colors

Math4AI exposes shared color constants for consistent styling across scripts.

## Constants

```python
from math4ai import (
    plane_color,
    point_x_color,
    foot_x_bar_color,
    distance_line_color,
    normal_vector_color,
    right_angle_indicator_color,
)
```

Current defaults:

| Name | Value |
|---|---|
| `plane_color` | `"blue"` |
| `point_x_color` | `"red"` |
| `foot_x_bar_color` | `"green"` |
| `distance_line_color` | `"black"` |
| `normal_vector_color` | `"purple"` |
| `right_angle_indicator_color` | `"gray"` |

## Example

```python
import matplotlib.pyplot as plt
from math4ai import point_x_color, distance_line_color

fig, ax = plt.subplots()
ax.scatter([0, 1], [0, 1], color=point_x_color)
ax.plot([0, 1], [0, 1], color=distance_line_color)
```
