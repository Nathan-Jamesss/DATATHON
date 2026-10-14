"""Make white-background versions of the logos (the originals are light-on-black). Usage: python make_light_logos.py <assets_dir>"""
import sys, os
from PIL import Image

A = sys.argv[1]
for name in ("logo-dsc", "logo-vitap", "logo-iiec"):
    im = Image.open(os.path.join(A, name + ".png")).convert("RGB")
    px = im.load(); w, h = im.size
    out = Image.new("RGBA", (w, h))
    op = out.load()
    for y in range(h):
        for x in range(w):
            r, g, b = px[x, y]
            mx, mn = max(r, g, b), min(r, g, b)
            if mx < 12:
                op[x, y] = (0, 0, 0, 0); continue
            a = mx / 255.0
            sat = (mx - mn) / mx
            if sat < 0.30:           # white / grey artwork -> black ink
                op[x, y] = (0, 0, 0, min(255, int(a * 255 * 1.1)))
            elif name == 'logo-iiec':  # solid dark red, like the original lettering
                f = 175.0 / mx
                op[x, y] = (min(255, int(r * f)), min(255, int(g * f)), min(255, int(b * f)), min(255, int(mx * 5)))
                continue
            else:                    # coloured artwork (pink brains, red IIEC) -> keep colour, un-premultiply
                al = min(1.0, a * 1.6)
                f = 255.0 / mx
                op[x, y] = (min(255, int(r * f)), min(255, int(g * f)), min(255, int(b * f)), int(al * 255))
    out.save(os.path.join(A, name + "-light.png"), optimize=True)
    print(name, out.size)
