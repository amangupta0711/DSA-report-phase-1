"""Renders each demo section's real output as a terminal-style PNG into ../screenshots/."""
import io, contextlib, os
from PIL import Image, ImageDraw, ImageFont
import demo
FONT = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf", 18)
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "screenshots")
names = {"1": "01_knapsack", "2": "02_lcs", "3": "03_resource_allocation",
         "4": "04_subset_sum", "5": "05_graph_coloring"}
for k, fn in demo.PARTS.items():
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf): fn()
    lines = ["$ python demo.py " + k] + buf.getvalue().strip("\n").split("\n")
    w = max(len(l) for l in lines) * 11 + 50
    h = len(lines) * 26 + 50
    img = Image.new("RGB", (w, h), (30, 30, 36)); d = ImageDraw.Draw(img)
    d.ellipse((15, 12, 27, 24), fill=(255, 95, 86)); d.ellipse((35, 12, 47, 24), fill=(255, 189, 46)); d.ellipse((55, 12, 67, 24), fill=(39, 201, 63))
    y = 36
    for i, l in enumerate(lines):
        col = (120, 220, 120) if i == 0 else (235, 235, 235)
        if l.startswith("=") : col = (100, 100, 110)
        elif l[:2].strip()[:1].isdigit() and ". " in l[:4]: col = (255, 200, 90)
        elif "Best" in l or "Maximum" in l or "Minimum" in l or "LCS length" in l: col = (130, 200, 255)
        d.text((20, y), l, font=FONT, fill=col); y += 26
    img.save(os.path.join(OUT, names[k] + ".png"))
    print("saved", names[k])
