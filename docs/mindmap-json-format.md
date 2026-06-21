# Mindmap JSON format

This page describes the `mindmap.json` schema consumed by:

```python
render_mindmap(__file__)
```

The JSON file must be in the same directory as the calling script.

Example render produced from this format:

![Mindmap JSON render example](images/mindmap-sample.png)

## Top-level schema

```json
{
  "canvas": { ... },
  "nodes": [ ... ],
  "extra_links": [ ... ]
}
```

- `canvas`: optional object
- `nodes`: optional array (normally required for useful output)
- `extra_links`: optional array

If `canvas`, `nodes`, or `extra_links` are missing, defaults are used where possible.

## canvas

Controls figure and text defaults.

| Key | Type | Default | Notes |
|---|---|---|---|
| `figsize` | `[number, number]` | `[12.0, 7.5]` | Passed to `plt.subplots(figsize=...)` |
| `xlim` | `[number, number]` | `[0.0, 14.5]` | Axes x-range |
| `ylim` | `[number, number]` | `[1.5, 10.5]` | Axes y-range |
| `font_size` | number | `13` | Default label font size for non-branch nodes |
| `autofit` | boolean | `false` | Auto-fit `xlim/ylim` to rendered content |
| `autofit_pad_x` | number | `0.28` | Horizontal padding used when `autofit=true` |
| `autofit_pad_y` | number | `0.20` | Vertical padding used when `autofit=true` |
| `autofit_include_text` | boolean | `true` | Include labels when computing auto-fit bounds |

## nodes

Each entry in `nodes` is a node object:

| Key | Type | Required | Default | Notes |
|---|---|---|---|---|
| `id` | string | yes | none | Unique node id |
| `label` | string | yes | none | Text label |
| `pos` | `[number, number]` | yes | none | Node anchor position `(x, y)` |
| `parent` | string | no | none | Parent node id for tree edge drawing |
| `color` | string | no | inherited from parent | Used for edge and branch box colors |
| `is_branch` | boolean | no | `false` | Branch title style when true |
| `icon` | string | no | none | Icon name resolved to draw function |
| `icon_size` | number | no | depends on icon | Size passed to draw function |
| `text_position` | string | no | `"right"` | One of `"right"`, `"left"`, `"top"`, `"bottom"` |
| `text_gap` | number | no | auto | Extra horizontal label gap on top of icon-size-based margin |
| `text_gap_y` | number | no | auto | Extra vertical label gap on top of icon-size-based margin |
| `text_margin_x` | number | no | auto | Explicit horizontal text margin (overrides auto) |
| `text_margin_y` | number | no | auto | Explicit vertical text margin (overrides auto) |
| `ha` | string | no | `"center"` for branches | Branch label horizontal alignment |
| `va` | string | no | `"center"` for branches | Branch label vertical alignment |
| `bg` | string | no | `color` | Branch label box background |

### Auto text layout

For non-branch nodes, text spacing is automatically computed from `icon_size` and icon visual footprint.
This avoids common overlap issues when icons have very different geometry.

When needed, you can fine-tune per node with `text_gap`, `text_gap_y`, `text_margin_x`, and `text_margin_y`.

### Branch node behavior

If `is_branch` is true, label is rendered as a bold rounded box. For branch nodes:

- icon is ignored
- `bg` overrides box color
- text alignment uses `ha` and `va` if provided

### Non-branch node behavior

For regular nodes:

- icon is drawn if `icon` is set
- label is placed around icon according to `text_position`
- text is rendered on a white semi-transparent rounded background

## extra_links

`extra_links` draws additional Bezier links beyond parent-child edges.

Each link object:

| Key | Type | Required | Default | Notes |
|---|---|---|---|---|
| `from` | string | yes | none | Source node id |
| `to` | string | yes | none | Target node id |
| `color` | string | no | source node color | Curve color |
| `lw` | number | no | `1.8` | Line width |
| `style` | string | no | `"-"` | Matplotlib linestyle |

## Icon resolution

For node icon `"name"`, renderer resolves draw function in this order:

1. `custom_icons["name"]`
2. `custom_icons["draw_name_icon"]`
3. local `draw_name_icon` function in caller script
4. built-in `math4ai.icon_utils.draw_name_icon`

If icon resolution fails, a warning is printed.

## Complete example

```json
{
  "canvas": {
    "figsize": [13.0, 8.0],
    "xlim": [0.0, 16.0],
    "ylim": [1.0, 11.0],
    "font_size": 12
  },
  "nodes": [
    {
      "id": "root",
      "label": "Mathematics for AI",
      "pos": [8.0, 9.5],
      "color": "#1d4ed8",
      "is_branch": true,
      "bg": "#1e40af"
    },
    {
      "id": "la",
      "parent": "root",
      "label": "Linear algebra",
      "pos": [4.8, 7.2],
      "icon": "svd",
      "text_position": "right"
    },
    {
      "id": "prob",
      "parent": "root",
      "label": "Probability",
      "pos": [11.0, 7.2],
      "color": "#0f766e",
      "icon": "bayes",
      "icon_size": 0.55,
      "text_position": "top"
    }
  ],
  "extra_links": [
    {
      "from": "la",
      "to": "prob",
      "color": "#64748b",
      "lw": 1.6,
      "style": "--"
    }
  ]
}
```

## Validation checklist

- Every non-root `parent` id exists in `nodes`
- Every `extra_links.from` and `extra_links.to` id exists
- Every `pos` has exactly two numeric values
- Every icon string matches a built-in icon or custom icon function
