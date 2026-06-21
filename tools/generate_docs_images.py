import os
import shutil
import tempfile

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from PIL import Image, ImageChops

from math4ai import (
    Matrix,
    arrow,
    configure_math_fonts,
    customize_2d_grid,
    draw_affine_grid,
    draw_vec,
    finalize,
    point_x_color,
    render_mindmap,
)


ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(ROOT, "docs", "images")
MINDMAP_SAMPLE_JSON = os.path.join(ROOT, "tools", "mindmap-sample.json")


def ensure_out_dir():
    os.makedirs(OUT_DIR, exist_ok=True)


def trim_uniform_border(image_path, padding=8):
    """Trim uniform outer border (based on corner background color) with padding."""
    im = Image.open(image_path).convert("RGBA")
    bg_color = im.getpixel((0, 0))
    bg = Image.new("RGBA", im.size, bg_color)
    diff = ImageChops.difference(im, bg)
    bbox = diff.getbbox()
    if not bbox:
        return

    left, top, right, bottom = bbox
    left = max(0, left - padding)
    top = max(0, top - padding)
    right = min(im.size[0], right + padding)
    bottom = min(im.size[1], bottom + padding)
    cropped = im.crop((left, top, right, bottom))
    cropped.save(image_path)


def gen_scatter_image():
    fig, ax = plt.subplots(figsize=(5.5, 4.0))
    xs = [1, 2, 3, 4]
    ys = [1, 4, 9, 16]
    ax.scatter(xs, ys, s=80, color=point_x_color)
    ax.plot(xs, ys, color="#444", alpha=0.5)
    ax.set_title("Consistent point styling")
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    customize_2d_grid(ax)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT_DIR, "quickstart-scatter.png"), dpi=180)
    plt.close(fig)


def gen_matrix_image():
    fig, ax = plt.subplots(figsize=(6.5, 3.6))
    m = Matrix(4, 6, cell_size=0.75)
    m.highlight_diagonal(use_gradient=True)
    m.color_row(4, "#ffe7cc")
    m.color_col(1, "#d9ecff")
    m.draw(ax)
    finalize(ax, xlim=(-0.2, m.get_width() + 0.2), ylim=(-0.2, m.get_height() + 0.2))
    fig.tight_layout()
    fig.savefig(os.path.join(OUT_DIR, "matrix-highlight.png"), dpi=180)
    plt.close(fig)


def gen_vector_image():
    fig, ax = plt.subplots(figsize=(5.4, 5.0))
    ax.set_xlim(-3.5, 4.0)
    ax.set_ylim(-3.5, 4.0)
    ax.set_aspect("equal")

    draw_affine_grid(ax, origin=(0, 0), v1=(1.0, 0.2), v2=(-0.4, 1.0), n=5)
    draw_vec(ax, (2.2, 1.5), color="#1f77b4", label="v", offset=(0.1, 0.12))
    arrow(ax, (0, 0), (-1.5, 2.4), color="#ff7f0e")

    ax.set_title("Vectors on an affine grid")
    customize_2d_grid(ax)
    fig.tight_layout()
    fig.savefig(os.path.join(OUT_DIR, "vector-grid.png"), dpi=180)
    plt.close(fig)


def gen_mindmap_image():
    with tempfile.TemporaryDirectory() as tmp:
        script_path = os.path.join(tmp, "mindmap_example.py")
        with open(script_path, "w", encoding="utf-8") as f:
            f.write("# temporary mindmap caller\n")
        json_path = os.path.join(tmp, "mindmap.json")
        shutil.copyfile(MINDMAP_SAMPLE_JSON, json_path)

        render_mindmap(script_path)

        generated = os.path.join(tmp, "mindmap_example.png")
        target = os.path.join(OUT_DIR, "mindmap-sample.png")
        shutil.copyfile(generated, target)
        trim_uniform_border(target, padding=1)


def main():
    configure_math_fonts()
    ensure_out_dir()
    gen_scatter_image()
    gen_matrix_image()
    gen_vector_image()
    gen_mindmap_image()
    print(f"Generated docs images in: {OUT_DIR}")


if __name__ == "__main__":
    main()
