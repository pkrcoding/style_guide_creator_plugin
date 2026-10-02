"""Draw the three fictional sample logos used in examples/.

Usage: python3 make_sample_logos.py <out-dir>
Needs Pillow and fontTools, and macOS system fonts (Avenir Next, SF Rounded, Palatino).
Outputs: northwind-logo.svg, northwind-symbol.svg (outlined vector), harbourside-logo.png
(transparent raster), pip-and-pine-logo.jpg (single colour on cream).
"""
from fontTools.ttLib import TTCollection, TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from PIL import Image, ImageDraw, ImageFont
import math, sys
OUT = sys.argv[1]

def text_path(font, text, x, y, size, tracking=0):
    """Outline text as one SVG path; (x, y) is the baseline origin."""
    gs, cmap, hmtx = font.getGlyphSet(), font.getBestCmap(), font["hmtx"]
    upm = font["head"].unitsPerEm
    s = size / upm
    pen = SVGPathPen(gs)
    cx = x
    for ch in text:
        g = cmap[ord(ch)]
        gs[g].draw(TransformPen(pen, (s, 0, 0, -s, cx, y)))
        cx += hmtx[g][0] * s + tracking
    return pen.getCommands(), cx

# ---------- Northwind Labs (SVG combination mark + symbol)
avenir = TTCollection("/System/Library/Fonts/Avenir Next.ttc")
bold = next(f for f in avenir.fonts if f["name"].getDebugName(4) == "Avenir Next Bold")
demi = next(f for f in avenir.fonts if f["name"].getDebugName(4) == "Avenir Next Demi Bold")
symbol = '''<circle cx="64" cy="64" r="60" fill="#0F6E7A"/>
  <path d="M30 92 L64 30 L98 92 Z" fill="#F2A541"/>
  <path d="M46 92 L64 60 L82 92 Z" fill="#0F6E7A"/>'''
word, end1 = text_path(bold, "Northwind", 150, 78, 64)
labs, end2 = text_path(demi, "LABS", end1 + 18, 78, 30, tracking=6)
W = math.ceil(end2 + 8)
open(f"{OUT}/northwind-logo.svg", "w").write(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} 128" role="img" aria-labelledby="t">
  <title id="t">Northwind Labs</title>
  {symbol}
  <path d="{word}" fill="#1B2A3A"/>
  <path d="{labs}" fill="#0F6E7A"/>
</svg>
''')
open(f"{OUT}/northwind-symbol.svg", "w").write(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128 128" role="img" aria-labelledby="t">
  <title id="t">Northwind Labs symbol</title>
  {symbol}
</svg>
''')

# ---------- Harbourside Community Trust (transparent PNG)
def rounded(size, weight):
    f = ImageFont.truetype("/System/Library/Fonts/SFNSRounded.ttf", size)
    try:
        f.set_variation_by_axes([weight])
    except Exception:
        pass
    return f
SC = 4  # supersample
im = Image.new("RGBA", (1500 * SC, 420 * SC), (0, 0, 0, 0))
d = ImageDraw.Draw(im)
cx, cy, r = 210 * SC, 210 * SC, 180 * SC
d.ellipse((cx - r, cy - r, cx + r, cy + r), fill="#1D4E89")
sun_r = 78 * SC
d.pieslice((cx - sun_r, cy - sun_r - 10 * SC, cx + sun_r, cy + sun_r - 10 * SC), 180, 360, fill="#F26B5B")
# three waves as filled bands between two sine curves (clean edges)
for i, col in enumerate(["#FFFFFF", "#9CC8E8", "#FFFFFF"]):
    y0 = cy + (20 + i * 46) * SC
    xs = range(int(cx - r), int(cx + r) + SC, SC)
    top = [(x, y0 - 8 * SC + math.sin((x - cx) / (34 * SC)) * 12 * SC) for x in xs]
    bot = [(x, y0 + 8 * SC + math.sin((x - cx) / (34 * SC)) * 12 * SC) for x in reversed(xs)]
    d.polygon(top + bot, fill=col)
# clip waves to circle
mask = Image.new("L", im.size, 0)
ImageDraw.Draw(mask).ellipse((cx - r, cy - r, cx + r, cy + r), fill=255)
mask.paste(255, (430 * SC, 0, im.width, im.height))
im.putalpha(Image.composite(im.getchannel("A"), Image.new("L", im.size, 0), mask))
d = ImageDraw.Draw(im)
d.text((440 * SC, 95 * SC), "Harbourside", font=rounded(150 * SC, 700), fill="#1D4E89")
d.text((446 * SC, 262 * SC), "Community Trust", font=rounded(84 * SC, 500), fill="#F26B5B")
bbox = im.getchannel("A").getbbox()
im = im.crop((bbox[0] - 20 * SC, bbox[1] - 20 * SC, bbox[2] + 20 * SC, bbox[3] + 20 * SC))
im = im.resize((im.width // SC, im.height // SC), Image.LANCZOS)
im.save(f"{OUT}/harbourside-logo.png")

# ---------- Pip & Pine Bakery (single colour on cream, JPG)
SC = 3
N = 1200 * SC
im = Image.new("RGB", (N, N), "#FBF3E4")
d = ImageDraw.Draw(im)
ink = "#5B3A29"
c = N // 2
for rr, w in ((470, 16), (430, 6)):
    R = rr * SC
    d.ellipse((c - R, c - R, c + R, c + R), outline=ink, width=w * SC)
# pine tree: stacked triangles + trunk
for i, (top, half, bottom) in enumerate(((250, 90, 420), (330, 130, 520), (420, 170, 620))):
    d.polygon([(c, top * SC), (c - half * SC, bottom * SC), (c + half * SC, bottom * SC)], fill=ink)
d.rectangle((c - 22 * SC, 620 * SC, c + 22 * SC, 680 * SC), fill=ink)
# a "pip" (seed) beside the tree
d.ellipse((c + 205 * SC, 575 * SC, c + 245 * SC, 635 * SC), fill=ink)
serif = ImageFont.truetype("/System/Library/Fonts/Palatino.ttc", 118 * SC, index=2)
small = ImageFont.truetype("/System/Library/Fonts/Palatino.ttc", 62 * SC, index=0)
for txt, font, y in (("PIP & PINE", serif, 712), ("BAKERY", small, 885)):
    tw = d.textlength(txt, font=font) + (len(txt) - 1) * (8 * SC if font is small else 0)
    x = c - tw / 2
    for ch in txt:
        d.text((x, y * SC), ch, font=font, fill=ink)
        x += d.textlength(ch, font=font) + (8 * SC if font is small else 0)
im = im.resize((1200, 1200), Image.LANCZOS)
im.save(f"{OUT}/pip-and-pine-logo.jpg", quality=92)
print("ok")
