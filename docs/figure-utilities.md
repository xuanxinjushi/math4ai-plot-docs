# Figure utilities

Figure helpers live in `figure_utils.py`.

## Configure text rendering

## `configure_math_fonts`

```python
configure_math_fonts(font_size=14)
```

Sets matplotlib `rcParams` for math-heavy plots:

- `mathtext.fontset = "cm"`
- serif family with `STIXGeneral`

Call this near the start of scripts that use equations in labels.

## Grid styling

## `customize_3d_grid`

```python
customize_3d_grid(
    ax,
    grid_color="#FFFA0D",
    grid_linewidth=0.8,
    pane_alpha=0.1,
    pane_linewidth=0.5,
)
```

Applies custom pane and grid styling for 3D axes.

## `customize_2d_grid`

```python
customize_2d_grid(
    ax,
    grid_color="#f000B0",
    grid_linewidth=0.8,
    grid_alpha=0.5,
    face_color="#FFFAFD",
)
```

Applies a themed 2D background and major/minor grid style.

## Saving outputs

## `save_figure_to_script_dir`

```python
save_figure_to_script_dir(filename, dpi=300, bbox_inches="tight", caller_file=None)
```

Saves the active figure to the calling script directory.

## `save_figure`

```python
save_figure(
    caller_file=None,
    *,
    dpi=300,
    bbox_inches="tight",
    facecolor="white",
    edgecolor="none",
    pad_inches=0.03,
    close=True,
)
```

Saves as `<script_name>.png` beside the calling script.

This is the default pattern used in chapter figure pipelines.
