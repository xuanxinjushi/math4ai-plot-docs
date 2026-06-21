# Mindmaps

Mindmap rendering is provided by:

```python
from math4ai import render_mindmap
```

## Entry point

```python
render_mindmap(caller_file, custom_icons=None)
```

- `caller_file`: usually `__file__`
- `custom_icons`: optional dict that maps icon names to drawing functions

The renderer reads `mindmap.json` from the same directory as `caller_file`.

## Minimal usage

```python
from math4ai import render_mindmap

if __name__ == "__main__":
    render_mindmap(__file__)
```

Rendered example:

![Rendered mindmap example](images/mindmap-sample.png)

This image is generated from [tools/mindmap-sample.json](../tools/mindmap-sample.json).

## JSON structure

Typical top-level keys:

- `canvas`
- `nodes`
- `extra_links`

For the complete schema and field-by-field reference, see [Mindmap JSON format](mindmap-json-format.md).

Minimal example:

```json
{
  "canvas": {
    "figsize": [12.0, 7.5],
    "xlim": [0.0, 14.5],
    "ylim": [1.5, 10.5],
    "font_size": 13
  },
  "nodes": [
    {"id": "root", "label": "Math4AI", "pos": [7.0, 9.0], "color": "#2563eb", "is_branch": true},
    {"id": "la", "parent": "root", "label": "Linear Algebra", "pos": [4.0, 6.5], "icon": "svd"}
  ],
  "extra_links": []
}
```

## Local custom icons

Renderer lookup order for icon `name`:

1. `custom_icons["name"]`
2. `custom_icons["draw_name_icon"]`
3. local function `draw_name_icon` in caller script
4. built-in `math4ai.icon_utils.draw_name_icon`

That allows chapter-specific icons without forking the library.
