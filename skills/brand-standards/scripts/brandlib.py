"""Shared colour, accessibility, and image helpers for the style-guide-creator scripts.

Standard library only. Pillow is used when installed (raster formats other than
PNG, asset generation); a minimal pure-Python PNG decoder is the fallback so
logo analysis works on a bare Python install.
"""

from __future__ import annotations

import math
import re
import shutil
import struct
import subprocess
import zlib
from pathlib import Path

try:  # Optional dependency.
    from PIL import Image  # type: ignore

    HAVE_PIL = True
except ImportError:  # pragma: no cover - depends on environment
    Image = None
    HAVE_PIL = False


# --------------------------------------------------------------------------
# Colour parsing and conversion
# --------------------------------------------------------------------------

HEX_RE = re.compile(r"^#?([0-9a-fA-F]{3}|[0-9a-fA-F]{6})$")

NAMED_COLOURS = {
    "black": "#000000", "white": "#ffffff", "red": "#ff0000", "green": "#008000",
    "blue": "#0000ff", "yellow": "#ffff00", "orange": "#ffa500", "purple": "#800080",
    "gray": "#808080", "grey": "#808080", "navy": "#000080", "teal": "#008080",
    "maroon": "#800000", "olive": "#808000", "silver": "#c0c0c0", "lime": "#00ff00",
    "aqua": "#00ffff", "cyan": "#00ffff", "fuchsia": "#ff00ff", "magenta": "#ff00ff",
}


def normalize_hex(value: str) -> str:
    """Return a lowercase #rrggbb string, or raise ValueError."""
    value = value.strip()
    if value.lower() in NAMED_COLOURS:
        return NAMED_COLOURS[value.lower()]
    m = HEX_RE.match(value)
    if not m:
        raise ValueError(f"Not a hex colour: {value!r}")
    h = m.group(1).lower()
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    return "#" + h


def hex_to_rgb(value: str) -> tuple[int, int, int]:
    h = normalize_hex(value)[1:]
    return int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)


def rgb_to_hex(rgb) -> str:
    r, g, b = (max(0, min(255, int(round(c)))) for c in rgb[:3])
    return f"#{r:02x}{g:02x}{b:02x}"


def _srgb_to_linear(c: float) -> float:
    c /= 255.0
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def _linear_to_srgb(c: float) -> float:
    c = max(0.0, min(1.0, c))
    v = 12.92 * c if c <= 0.0031308 else 1.055 * (c ** (1 / 2.4)) - 0.055
    return v * 255.0


def relative_luminance(colour) -> float:
    """WCAG 2.x relative luminance for a hex string or (r, g, b) tuple."""
    r, g, b = hex_to_rgb(colour) if isinstance(colour, str) else colour[:3]
    # WCAG 2.x specifies 0.03928; the difference from 0.04045 is immaterial for 8-bit values.
    return 0.2126 * _srgb_to_linear(r) + 0.7152 * _srgb_to_linear(g) + 0.0722 * _srgb_to_linear(b)


def contrast_ratio(fg, bg) -> float:
    l1, l2 = relative_luminance(fg), relative_luminance(bg)
    hi, lo = max(l1, l2), min(l1, l2)
    return (hi + 0.05) / (lo + 0.05)


# WCAG 2.2 thresholds. "large" text = >= 24px regular or >= 18.66px (14pt) bold.
THRESHOLDS = {
    "body": 4.5,        # SC 1.4.3 AA, normal text
    "large": 3.0,       # SC 1.4.3 AA, large text
    "ui": 3.0,          # SC 1.4.11 AA, UI components and meaningful graphics
    "body-aaa": 7.0,    # SC 1.4.6 AAA, normal text
    "large-aaa": 4.5,   # SC 1.4.6 AAA, large text
    "decorative": 0.0,  # No requirement (incidental / logotype / pure decoration)
}


def wcag_report(fg, bg) -> dict:
    ratio = contrast_ratio(fg, bg)
    return {
        "ratio": round(ratio, 2),
        "aaBody": ratio >= 4.5,
        "aaLarge": ratio >= 3.0,
        "aaUi": ratio >= 3.0,
        "aaaBody": ratio >= 7.0,
        "aaaLarge": ratio >= 4.5,
        "rating": rating_label(ratio),
    }


def rating_label(ratio: float) -> str:
    if ratio >= 7.0:
        return "AAA"
    if ratio >= 4.5:
        return "AA"
    if ratio >= 3.0:
        return "AA Large / UI"
    return "Fail"


def rgb_to_oklab(rgb) -> tuple[float, float, float]:
    r, g, b = (_srgb_to_linear(c) for c in rgb[:3])
    l = 0.4122214708 * r + 0.5363325363 * g + 0.0514459929 * b
    m = 0.2119034982 * r + 0.6806995451 * g + 0.1073969566 * b
    s = 0.0883024619 * r + 0.2817188376 * g + 0.6299787005 * b
    l_, m_, s_ = (math.copysign(abs(v) ** (1 / 3), v) for v in (l, m, s))
    return (
        0.2104542553 * l_ + 0.7936177850 * m_ - 0.0040720468 * s_,
        1.9779984951 * l_ - 2.4285922050 * m_ + 0.4505937099 * s_,
        0.0259040371 * l_ + 0.7827717662 * m_ - 0.8086757660 * s_,
    )


def oklab_to_linear(lab) -> tuple[float, float, float]:
    L, a, b = lab
    l_ = L + 0.3963377774 * a + 0.2158037573 * b
    m_ = L - 0.1055613458 * a - 0.0638541728 * b
    s_ = L - 0.0894841775 * a - 1.2914855480 * b
    l, m, s = l_ ** 3, m_ ** 3, s_ ** 3
    return (
        4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s,
        -1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s,
        -0.0041960863 * l - 0.7034186147 * m + 1.7076147010 * s,
    )


def oklab_to_rgb(lab) -> tuple[float, float, float]:
    return tuple(_linear_to_srgb(c) for c in oklab_to_linear(lab))


def rgb_to_oklch(rgb) -> tuple[float, float, float]:
    L, a, b = rgb_to_oklab(rgb)
    C = math.hypot(a, b)
    H = math.degrees(math.atan2(b, a)) % 360
    return L, C, H


def oklch_to_lab(L, C, H):
    h = math.radians(H)
    return L, C * math.cos(h), C * math.sin(h)


def in_gamut(L, C, H, eps=1e-4) -> bool:
    return all(-eps <= c <= 1 + eps for c in oklab_to_linear(oklch_to_lab(L, C, H)))


def oklch_to_hex(L, C, H) -> str:
    """Convert OKLCH to hex, reducing chroma until the colour fits sRGB."""
    L = max(0.0, min(1.0, L))
    if not in_gamut(L, C, H):
        lo, hi = 0.0, C
        for _ in range(24):
            mid = (lo + hi) / 2
            if in_gamut(L, mid, H):
                lo = mid
            else:
                hi = mid
        C = lo
    return rgb_to_hex(oklab_to_rgb(oklch_to_lab(L, C, H)))


def delta_e_ok(c1, c2) -> float:
    """Euclidean distance in OKLab (~0.02 is a just-noticeable difference)."""
    a = rgb_to_oklab(hex_to_rgb(c1) if isinstance(c1, str) else c1)
    b = rgb_to_oklab(hex_to_rgb(c2) if isinstance(c2, str) else c2)
    return math.dist(a, b)


def rgb_to_hsl(rgb) -> tuple[int, int, int]:
    r, g, b = (c / 255 for c in rgb[:3])
    mx, mn = max(r, g, b), min(r, g, b)
    l = (mx + mn) / 2
    if mx == mn:
        return 0, 0, round(l * 100)
    d = mx - mn
    s = d / (2 - mx - mn) if l > 0.5 else d / (mx + mn)
    if mx == r:
        h = (g - b) / d + (6 if g < b else 0)
    elif mx == g:
        h = (b - r) / d + 2
    else:
        h = (r - g) / d + 4
    return round(h * 60) % 360, round(s * 100), round(l * 100)


def rgb_to_cmyk(rgb) -> tuple[int, int, int, int]:
    """Naive device-independent CMYK. Print values must be confirmed by a printer/ICC profile."""
    r, g, b = (c / 255 for c in rgb[:3])
    k = 1 - max(r, g, b)
    if k >= 1:
        return 0, 0, 0, 100
    c = (1 - r - k) / (1 - k)
    m = (1 - g - k) / (1 - k)
    y = (1 - b - k) / (1 - k)
    return tuple(round(v * 100) for v in (c, m, y, k))


def colour_formats(hex_value: str) -> dict:
    rgb = hex_to_rgb(hex_value)
    L, C, H = rgb_to_oklch(rgb)
    return {
        "hex": normalize_hex(hex_value),
        "rgb": f"rgb({rgb[0]} {rgb[1]} {rgb[2]})",
        "hsl": "hsl({} {}% {}%)".format(*rgb_to_hsl(rgb)),
        "oklch": f"oklch({L * 100:.1f}% {C:.3f} {H:.1f})",
        "cmyk": "C{} M{} Y{} K{}".format(*rgb_to_cmyk(rgb)),
    }


def hue_name(hex_value: str) -> str:
    """Rough human-readable colour family, used for default names and alt text."""
    L, C, H = rgb_to_oklch(hex_to_rgb(hex_value))
    if C < 0.03:
        if L > 0.93:
            return "white"
        if L < 0.22:
            return "black"
        return "grey"
    bands = [
        (20, "pink"), (45, "red"), (70, "orange"), (100, "amber"), (115, "yellow"),
        (135, "lime"), (165, "green"), (195, "teal"), (230, "cyan"), (265, "blue"),
        (300, "indigo"), (330, "violet"), (360, "pink"),
    ]
    name = next(n for limit, n in bands if H < limit)
    if L < 0.4:
        return "dark " + name
    if L > 0.85:
        return "light " + name
    return name


# --------------------------------------------------------------------------
# Colour-vision-deficiency simulation (Machado, Oliveira & Fernandes 2009, severity 1.0)
# --------------------------------------------------------------------------

CVD_MATRICES = {
    "protanopia": ((0.152286, 1.052583, -0.204868),
                   (0.114503, 0.786281, 0.099216),
                   (-0.003882, -0.048116, 1.051998)),
    "deuteranopia": ((0.367322, 0.860646, -0.227968),
                     (0.280085, 0.672501, 0.047413),
                     (-0.011820, 0.042940, 0.968881)),
    "tritanopia": ((1.255528, -0.076749, -0.178779),
                   (-0.078411, 0.930809, 0.147602),
                   (0.004733, 0.691367, 0.303900)),
}


def simulate_cvd(hex_value: str, kind: str) -> str:
    rgb = hex_to_rgb(hex_value)
    lin = [_srgb_to_linear(c) for c in rgb]
    if kind == "achromatopsia":
        y = 0.2126 * lin[0] + 0.7152 * lin[1] + 0.0722 * lin[2]
        out = (y, y, y)
    else:
        m = CVD_MATRICES[kind]
        out = tuple(sum(m[i][j] * lin[j] for j in range(3)) for i in range(3))
    return rgb_to_hex(tuple(_linear_to_srgb(c) for c in out))


CVD_KINDS = ("protanopia", "deuteranopia", "tritanopia", "achromatopsia")
# Achromatopsia is excluded from pairwise checks: equal-lightness hues always collide and the
# universal rule "never rely on colour alone" already covers it.
CVD_PAIR_KINDS = ("protanopia", "deuteranopia", "tritanopia")
# Below this OKLab distance two colours are likely to be confused; do not rely on hue alone.
CVD_CONFUSION_THRESHOLD = 0.08


def cvd_pair_report(colours: dict[str, str]) -> list[dict]:
    """For each pair of named colours, find CVD types under which they become hard to tell apart."""
    names = list(colours)
    issues = []
    for i, a in enumerate(names):
        for b in names[i + 1:]:
            normal = delta_e_ok(colours[a], colours[b])
            if normal < CVD_CONFUSION_THRESHOLD:
                issues.append({"pair": [a, b], "vision": "typical", "deltaE": round(normal, 3)})
                continue
            for kind in CVD_PAIR_KINDS:
                d = delta_e_ok(simulate_cvd(colours[a], kind), simulate_cvd(colours[b], kind))
                if d < CVD_CONFUSION_THRESHOLD:
                    issues.append({"pair": [a, b], "vision": kind, "deltaE": round(d, 3)})
    return issues


# --------------------------------------------------------------------------
# Image loading
# --------------------------------------------------------------------------

class ImageError(RuntimeError):
    pass


def _paeth(a, b, c):
    p = a + b - c
    pa, pb, pc = abs(p - a), abs(p - b), abs(p - c)
    if pa <= pb and pa <= pc:
        return a
    return b if pb <= pc else c


def decode_png(path: Path):
    """Minimal PNG decoder -> (width, height, list of RGBA tuples). Non-interlaced only."""
    data = path.read_bytes()
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        raise ImageError(f"{path} is not a PNG file")
    pos, idat, palette, trns = 8, bytearray(), None, None
    width = height = depth = ctype = interlace = None
    while pos < len(data):
        (length,) = struct.unpack(">I", data[pos:pos + 4])
        kind = data[pos + 4:pos + 8]
        chunk = data[pos + 8:pos + 8 + length]
        pos += 12 + length
        if kind == b"IHDR":
            width, height, depth, ctype, _, _, interlace = struct.unpack(">IIBBBBB", chunk)
        elif kind == b"PLTE":
            palette = [tuple(chunk[i:i + 3]) for i in range(0, len(chunk), 3)]
        elif kind == b"tRNS":
            trns = chunk
        elif kind == b"IDAT":
            idat += chunk
        elif kind == b"IEND":
            break
    if interlace:
        raise ImageError("Interlaced PNG needs Pillow: pip install pillow")
    channels = {0: 1, 2: 3, 3: 1, 4: 2, 6: 4}[ctype]
    bits_pp = channels * depth
    stride = (width * bits_pp + 7) // 8
    bpp = max(1, bits_pp // 8)
    raw = zlib.decompress(bytes(idat))
    rows, prev, i = [], bytearray(stride), 0
    for _ in range(height):
        ftype = raw[i]
        line = bytearray(raw[i + 1:i + 1 + stride])
        i += 1 + stride
        for x in range(stride):
            a = line[x - bpp] if x >= bpp else 0
            b = prev[x]
            c = prev[x - bpp] if x >= bpp else 0
            if ftype == 1:
                line[x] = (line[x] + a) & 255
            elif ftype == 2:
                line[x] = (line[x] + b) & 255
            elif ftype == 3:
                line[x] = (line[x] + ((a + b) >> 1)) & 255
            elif ftype == 4:
                line[x] = (line[x] + _paeth(a, b, c)) & 255
        rows.append(line)
        prev = line

    def samples(line):
        if depth == 8:
            return list(line)
        if depth == 16:
            return [line[k] for k in range(0, len(line), 2)]
        out, mask = [], (1 << depth) - 1
        for byte in line:
            for shift in range(8 - depth, -1, -depth):
                out.append((byte >> shift) & mask)
        return out

    scale = 255 // ((1 << depth) - 1) if depth < 8 else 1
    pixels = []
    for line in rows:
        s = samples(line)
        for x in range(width):
            if ctype == 6:
                pixels.append(tuple(s[x * 4:x * 4 + 4]))
            elif ctype == 2:
                r, g, b = s[x * 3:x * 3 + 3]
                alpha = 255
                if trns and len(trns) >= 6 and (r, g, b) == struct.unpack(">HHH", trns[:6]):
                    alpha = 0
                pixels.append((r, g, b, alpha))
            elif ctype == 3:
                idx = s[x]
                r, g, b = palette[idx]
                alpha = trns[idx] if trns and idx < len(trns) else 255
                pixels.append((r, g, b, alpha))
            elif ctype == 4:
                v, alpha = s[x * 2], s[x * 2 + 1]
                pixels.append((v, v, v, alpha))
            else:
                v = s[x] * scale
                pixels.append((v, v, v, 255))
    return width, height, pixels


def rasterize_svg(svg: Path, out_png: Path, size: int = 1024) -> bool:
    """Render an SVG to PNG with whatever renderer is available. Returns True on success."""
    try:
        import cairosvg  # type: ignore

        cairosvg.svg2png(url=str(svg), write_to=str(out_png), output_width=size)
        return out_png.exists()
    except Exception:
        pass
    candidates = [
        ["rsvg-convert", "-w", str(size), "-o", str(out_png), str(svg)],
        ["inkscape", str(svg), "--export-type=png", f"--export-filename={out_png}", f"--export-width={size}"],
        ["magick", "-background", "none", "-density", "300", str(svg), "-resize", f"{size}x", str(out_png)],
    ]
    for cmd in candidates:
        if shutil.which(cmd[0]):
            try:
                subprocess.run(cmd, check=True, capture_output=True, timeout=60)
                if out_png.exists():
                    return True
            except Exception:
                continue
    if shutil.which("qlmanage"):  # macOS Quick Look; renders onto an opaque background.
        try:
            subprocess.run(["qlmanage", "-t", "-s", str(size), "-o", str(out_png.parent), str(svg)],
                           check=True, capture_output=True, timeout=60)
            produced = out_png.parent / (svg.name + ".png")
            if produced.exists():
                produced.replace(out_png)
                return True
        except Exception:
            pass
    return False


def load_rgba(path: Path, max_side: int = 256):
    """Load an image as RGBA, downsampled so the longest side is <= max_side.

    Returns dict(width, height, original_width, original_height, pixels).
    """
    path = Path(path)
    if HAVE_PIL:
        with Image.open(path) as im:
            ow, oh = im.size
            im = im.convert("RGBA")
            im.thumbnail((max_side, max_side), Image.NEAREST)  # NEAREST keeps exact brand colours.
            return {"width": im.width, "height": im.height, "original_width": ow,
                    "original_height": oh, "pixels": list(im.getdata())}
    if path.suffix.lower() != ".png":
        raise ImageError(f"Reading {path.suffix} files needs Pillow: pip install pillow")
    w, h, px = decode_png(path)
    step = max(1, math.ceil(max(w, h) / max_side))
    sw, sh = len(range(0, w, step)), len(range(0, h, step))
    sampled = [px[y * w + x] for y in range(0, h, step) for x in range(0, w, step)]
    return {"width": sw, "height": sh, "original_width": w, "original_height": h, "pixels": sampled}


# --------------------------------------------------------------------------
# SVG inspection
# --------------------------------------------------------------------------

SVG_COLOUR_RE = re.compile(
    r"(?:fill|stroke|stop-color|color)\s*[:=]\s*[\"']?\s*(#[0-9a-fA-F]{3,6}\b|rgb\([^)]*\)|[a-zA-Z]+)")


def svg_colours(text: str) -> dict[str, int]:
    """Count colour declarations in an SVG (attributes, inline styles, <style> blocks)."""
    counts: dict[str, int] = {}
    for raw in SVG_COLOUR_RE.findall(text):
        raw = raw.strip()
        if raw.lower() in ("none", "transparent", "currentcolor", "inherit", "url"):
            continue
        try:
            if raw.lower().startswith("rgb("):
                nums = [float(v.strip().rstrip("%")) for v in re.split(r"[ ,/]+", raw[4:-1]) if v.strip()][:3]
                hx = rgb_to_hex(nums)
            else:
                hx = normalize_hex(raw)
        except (ValueError, IndexError):
            continue
        counts[hx] = counts.get(hx, 0) + 1
    return counts


def svg_info(text: str) -> dict:
    info: dict = {}
    vb = re.search(r"viewBox\s*=\s*[\"']([^\"']+)[\"']", text)
    if vb:
        parts = [float(p) for p in re.split(r"[ ,]+", vb.group(1).strip())]
        if len(parts) == 4:
            info["viewBox"] = parts
            info["width"], info["height"] = parts[2], parts[3]
    if "width" not in info:
        w = re.search(r"<svg[^>]*\swidth\s*=\s*[\"']([\d.]+)", text)
        h = re.search(r"<svg[^>]*\sheight\s*=\s*[\"']([\d.]+)", text)
        if w and h:
            info["width"], info["height"] = float(w.group(1)), float(h.group(1))
    info["hasText"] = "<text" in text
    info["fonts"] = sorted(set(re.findall(r"font-family\s*[:=]\s*[\"']?([^;\"'>]+)", text)))
    info["hasGradient"] = bool(re.search(r"<(linear|radial)Gradient", text))
    info["hasEmbeddedRaster"] = "data:image/" in text or bool(re.search(r"<image\b", text))
    info["hasTitle"] = "<title" in text
    info["hasRoleImg"] = 'role="img"' in text
    return info


def slugify(text: str) -> str:
    s = re.sub(r"[^a-zA-Z0-9]+", "-", text.strip().lower()).strip("-")
    return s or "brand"
