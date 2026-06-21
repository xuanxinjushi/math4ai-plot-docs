# Python API overview

Main package import:

```python
import math4ai
```

Most users import specific symbols:

```python
from math4ai import Matrix, draw_vec, save_figure, render_mindmap
```

## API groups

## 1. Color constants

- `plane_color`
- `point_x_color`
- `foot_x_bar_color`
- `distance_line_color`
- `normal_vector_color`
- `right_angle_indicator_color`

See [Colors](colors.md).

## 2. Matrix visualization

Class:

- `Matrix`

Functions:

- `draw_dashed_row`, `draw_dashed_col`
- `draw_column_indices`, `draw_row_indices`
- `draw_piercing_row`, `draw_piercing_col`
- `draw_brace`, `draw_curved_label`
- `color_row_col`, `finalize`

See [Matrix visualization](matrix-visualization.md).

## 3. Vector visualization

- `draw_affine_grid`
- `draw_vec`
- `arrow`

See [Vector visualization](vector-visualization.md).

## 4. Figure utilities

- `configure_math_fonts`
- `customize_3d_grid`
- `customize_2d_grid`
- `save_figure_to_script_dir`
- `save_figure`

See [Figure utilities](figure-utilities.md).

## 5. Mindmaps and icons

- `render_mindmap`
- icon drawing functions from `icon_utils.py`

See [Mindmaps](mindmaps.md) and [Icons reference](icons-reference.md).
