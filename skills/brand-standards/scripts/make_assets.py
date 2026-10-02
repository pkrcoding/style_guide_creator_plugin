#!/usr/bin/env python3
"""Generate the brand asset kit from brand.json.

Produces (under <guide>/assets/):
  logo/       full-colour, mono-dark, mono-light (reversed) and clear-space versions
              (SVG variants when the master is SVG; PNG when Pillow is installed)
  logo/backgrounds/  logo-on-background test tiles with pass/fail contrast
  favicons/   favicon.ico (16/32/48), PNG icons, apple-touch-icon, maskable icon,
              site.webmanifest and an HTML <head> snippet
  social/<platform>/  avatars, covers and banners sized per platform, plus
              editable SVG templates with a separate safe-zone guide layer
  manifest.json      every file produced, its purpose, alt text and any warnings

Without Pillow, only SVG outputs are produced and manifest.json lists what was skipped.

Usage:
    make_assets.py path/to/brand.json [--platforms instagram,linkedin,...]
"""

from __future__ import annotations

import argparse
import base64
import json
import re
import shutil
import sys
import tempfile
from pathlib import Path
from xml.sax.saxutils import escape

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import analyze_logo  # noqa: E402
import brandlib as bl  # noqa: E402

PLATFORMS_FILE = HERE.parent.parent / "social-media-kit" / "references" / "social-platforms.json"
DEFAULT_PLATFORMS = ["instagram", "facebook", "linkedin", "x", "youtube", "tiktok", "web"]

if bl.HAVE_PIL:
    from PIL import Image, ImageDraw  # type: ignore


class Kit:
    def __init__(self, brand_path: Path, platforms: list[str] | None):
        self.brand_path = brand_path
        self.root = brand_path.parent
        self.brand = json.loads(brand_path.read_text())
        self.out = self.root / "assets"
        self.manifest: dict = {"files": [], "warnings": [], "skipped": []}
        meta = self.brand.get("meta", {})
        self.name = meta.get("name", "Brand")
        logo = self.brand.get("logo", {})
        self.master = self.root / logo["master"]
        self.symbol = self.root / logo["symbol"] if logo.get("symbol") else None
        self.clear = float(logo.get("clearSpace", {}).get("fraction", 0.25))
        self.alt = logo.get("altText") or f"{self.name} logo"
        self.mono_style = logo.get("monoStyle", "auto")  # auto | knockout | solid
        # Backgrounds (hex or colour id) where a person approved full colour below 3:1 (logo exemption).
        self.exceptions = {self._resolve_ref(r) for r in logo.get("fullColourExceptions", [])}
        self.has_knockout = False
        colour = self.brand.get("color", {})
        brand_colours = colour.get("brand", [])
        if not brand_colours:
            raise SystemExit("error: brand.json has no color.brand entries; run build_palette.py first")
        self.primary = brand_colours[0]["hex"]
        neutral = colour.get("neutral", {}).get("scale", {})
        self.dark = colour.get("surfaces", {}).get("dark") or neutral.get("950", "#111111")
        self.light = "#ffffff"
        self.tint = neutral.get("50", "#f5f5f5")
        social = self.brand.get("social", {})
        self.platform_ids = platforms or social.get("platforms") or DEFAULT_PLATFORMS
        self.social_bg = self._resolve(social.get("coverBackground", "primary"))
        self.avatar_bg = self._resolve(social.get("avatarBackground", "primary"))
        families = self.brand.get("typography", {}).get("families", [])
        display = next((f for f in families if f.get("role") == "display"), families[0] if families else {})
        self.display_font = f"'{display.get('name', 'sans-serif')}', {display.get('fallback', 'sans-serif')}"
        body = next((f for f in families if f.get("role") == "body"), display)
        self.body_font = f"'{body.get('name', 'sans-serif')}', {body.get('fallback', 'sans-serif')}"
        self.logo_colours = self._logo_colours(self.master)
        self.aspect = self._aspect(self.master)
        self.symbol_aspect = self._aspect(self.symbol) if self.symbol else self.aspect
        self.symbol_colours = self._logo_colours(self.symbol) if self.symbol else self.logo_colours

    # ------------------------------------------------------------------ helpers
    def _resolve_ref(self, ref: str) -> str:
        if ref.startswith("#"):
            return bl.normalize_hex(ref)
        for c in self.brand.get("color", {}).get("brand", []):
            if c["id"] == ref:
                return c["hex"]
        return {"white": "#ffffff", "black": "#000000"}.get(ref, ref)

    def label(self, hex_value: str) -> str:
        """Human name for a colour: the brand colour name when it matches, else a plain description."""
        hex_value = bl.normalize_hex(hex_value)
        for c in self.brand["color"]["brand"]:
            if bl.delta_e_ok(c["hex"], hex_value) < 0.03:
                return c["name"]
        if hex_value == "#ffffff":
            return "white"
        if bl.delta_e_ok(hex_value, self.dark) < 0.03:
            return "dark neutral"
        if bl.delta_e_ok(hex_value, self.tint) < 0.03:
            return "light neutral"
        return bl.hue_name(hex_value)

    def _resolve(self, ref: str) -> str:
        if ref.startswith("#"):
            return bl.normalize_hex(ref)
        for c in self.brand["color"]["brand"]:
            if c["id"] == ref:
                return c["hex"]
        return {"white": "#ffffff", "dark": self.dark, "light": self.tint}.get(ref, self.primary)

    def _aspect(self, path: Path) -> float:
        data: dict = {}
        try:
            (analyze_logo.analyse_svg if path.suffix.lower() == ".svg" else analyze_logo.analyse_raster)(path, data)
        except bl.ImageError:
            return 1.0
        return float(data.get("contentAspectRatio") or 1.0)

    def _logo_colours(self, path: Path | None) -> list[dict]:
        if not path:
            return []
        data: dict = {}
        if path.suffix.lower() == ".svg":
            analyze_logo.analyse_svg(path, data)
        else:
            analyze_logo.analyse_raster(path, data)
        return data.get("colours", [])

    def record(self, path: Path, purpose: str, **extra):
        self.manifest["files"].append({"path": str(path.relative_to(self.root)), "purpose": purpose, **extra})

    def variant_for(self, bg: str, colours: list[dict]) -> tuple[str, float]:
        """Choose the logo variant that stays >= 3:1 against bg (WCAG 1.4.11 best practice for logos)."""
        full = self.full_colour_ratio(bg, colours)
        if full >= 3.0 or bl.normalize_hex(bg) in self.exceptions:
            return "full-colour", full
        light, dark = bl.contrast_ratio("#ffffff", bg), bl.contrast_ratio(self.dark, bg)
        return ("mono-light", light) if light >= dark else ("mono-dark", dark)

    @staticmethod
    def full_colour_ratio(bg: str, colours: list[dict]) -> float:
        """Lowest contrast between bg and the logo colours that actually touch the background.

        Colours enclosed by other colours (e.g. a shape inside a disc) never meet the background.
        """
        edge = [c["hex"] for c in colours if c.get("touchesBackground", True) and c.get("share", 1) >= 0.03]
        edge = edge or [c["hex"] for c in colours] or ["#000000"]
        return min(bl.contrast_ratio(c, bg) for c in edge)

    def mono_name(self, name: str, variants: dict | None = None) -> str:
        """Variant name actually used once monoStyle is applied (for alt text)."""
        if name.startswith("mono") and self.mono_style in ("auto", "knockout") and self.has_knockout:
            return f"{name}-knockout"
        return name

    def pick(self, variants: dict, name: str):
        """Return the image for a variant, honouring logo.monoStyle for single-colour versions."""
        if name.startswith("mono") and self.mono_style in ("auto", "knockout") and f"{name}-knockout" in variants:
            return variants[f"{name}-knockout"]
        return variants[name]

    # ------------------------------------------------------------------ SVG
    @staticmethod
    def svg_recolour(text: str, mapping: dict) -> str:
        """Replace each declared colour (any case, 3- or 6-digit form) using mapping {hex: new}."""
        out = text
        for hx, new in mapping.items():
            forms = {hx, hx.upper(), hx[:1] + hx[1:].upper()}
            if hx[1] == hx[2] and hx[3] == hx[4] and hx[5] == hx[6]:
                short = "#" + hx[1] + hx[3] + hx[5]
                forms |= {short, short.upper()}
            for form in forms:
                out = re.sub(re.escape(form) + r"(?![0-9a-fA-F])", new, out)
        return out

    def svg_knockout(self, text: str, knock: set, ink: str) -> str | None:
        """True vector knockout: knock-colour shapes become holes via an SVG luminance mask."""
        m_open = re.search(r"<svg\b[^>]*>", text)
        m_close = text.rfind("</svg>")
        vb = re.search(r'viewBox\s*=\s*["\']([^"\']+)["\']', text)
        if not (m_open and m_close > 0 and vb):
            return None
        inner = text[m_open.end():m_close]
        inner_mask = re.sub(r"<(title|desc)\b.*?</\1>", "", inner, flags=re.S)
        inner_mask = re.sub(r'\sid="[^"]*"', "", inner_mask)
        colours = bl.svg_colours(text)
        mask = self.svg_recolour(inner_mask, {hx: ("#000000" if hx in knock else "#ffffff") for hx in colours})
        art = self.svg_recolour(inner, {hx: ink for hx in colours})
        x, y, w, h = re.split(r"[ ,]+", vb.group(1).strip())
        return (text[:m_open.end()] +
                f'\n  <defs><mask id="sgc-knockout" maskUnits="userSpaceOnUse" x="{x}" y="{y}" width="{w}" height="{h}">{mask}</mask></defs>'
                f'\n  <g mask="url(#sgc-knockout)">{art}</g>\n</svg>\n')

    def svg_variants(self, src: Path, stem: str, colours: list[dict]):
        text = src.read_text(encoding="utf-8")
        dest = self.out / "logo"
        shutil.copyfile(src, dest / f"{stem}-full-colour.svg")
        self.record(dest / f"{stem}-full-colour.svg", f"{stem} logo, full colour (vector master)", alt=self.variant_alt(stem, "full-colour"))
        declared = bl.svg_colours(text)
        # Only knock out light colours that sit inside the mark, never free-standing ones (e.g. a tagline).
        knock = {hx for hx in self.knockout_set(colours)
                 if not next((c.get("touchesBackground") for c in colours if c["hex"] == hx), False)}
        knock = {hx for hx in declared if any(bl.delta_e_ok(hx, k) < 0.03 for k in knock)}
        for variant, colour in (("mono-dark", self.dark), ("mono-light", "#ffffff")):
            path = dest / f"{stem}-{variant}.svg"
            path.write_text(self.svg_recolour(text, {hx: colour for hx in declared}), encoding="utf-8")
            self.record(path, f"{stem} logo, single colour, solid {'(reversed, for dark backgrounds)' if variant == 'mono-light' else '(for light backgrounds)'}", alt=self.variant_alt(stem, variant))
            if knock:
                ko = self.svg_knockout(text, knock, colour)
                if ko:
                    path = dest / f"{stem}-{variant}-knockout.svg"
                    path.write_text(ko, encoding="utf-8")
                    self.record(path, f"{stem} logo, single colour with inner shapes knocked out {'(reversed, for dark backgrounds)' if variant == 'mono-light' else '(for light backgrounds)'}", alt=self.variant_alt(stem, f"{variant}-knockout"))

    # ------------------------------------------------------------------ raster
    def load_master(self, src: Path):
        if src.suffix.lower() == ".svg":
            tmp = Path(tempfile.mkdtemp()) / "master.png"
            if not bl.rasterize_svg(src, tmp, 2048):
                self.manifest["warnings"].append(f"Could not rasterise {src.name}; PNG assets skipped. Install cairosvg or librsvg.")
                return None
            im = Image.open(tmp).convert("RGBA")
        else:
            im = Image.open(src).convert("RGBA")
        im = self.remove_background(im)
        bbox = im.getchannel("A").point(lambda a: 255 if a > 8 else 0).getbbox()
        return im.crop(bbox) if bbox else im

    @staticmethod
    def remove_background(im):
        alpha = im.getchannel("A")
        if alpha.getextrema()[0] < 250:
            return im  # Already transparent.
        w, h = im.size
        px = im.load()
        border = [px[x, 0] for x in range(w)] + [px[x, h - 1] for x in range(w)]
        border += [px[0, y] for y in range(h)] + [px[w - 1, y] for y in range(h)]
        counts: dict = {}
        for p in border:
            counts[(p[0] >> 4, p[1] >> 4, p[2] >> 4)] = counts.get((p[0] >> 4, p[1] >> 4, p[2] >> 4), 0) + 1
        key, n = max(counts.items(), key=lambda kv: kv[1])
        if n / len(border) < 0.6:
            return im  # Complex background: leave as is.
        sel = [p for p in border if (p[0] >> 4, p[1] >> 4, p[2] >> 4) == key]
        bg = tuple(sum(p[i] for p in sel) / len(sel) for i in range(3))
        out = im.copy()
        op = out.load()
        for y in range(h):
            for x in range(w):
                r, g, b, a = op[x, y]
                d = ((r - bg[0]) ** 2 + (g - bg[1]) ** 2 + (b - bg[2]) ** 2) ** 0.5
                if d < 24:
                    op[x, y] = (r, g, b, 0)
                elif d < 64:  # Soft edge for anti-aliased pixels.
                    op[x, y] = (r, g, b, int(a * (d - 24) / 40))
        return out

    @staticmethod
    def recolour(im, hex_value: str):
        solid = Image.new("RGBA", im.size, bl.hex_to_rgb(hex_value) + (255,))
        solid.putalpha(im.getchannel("A"))
        return solid

    @staticmethod
    def fit(im, max_w: int, max_h: int):
        scale = min(max_w / im.width, max_h / im.height)
        return im.resize((max(1, round(im.width * scale)), max(1, round(im.height * scale))), Image.LANCZOS)

    def compose(self, logo, size, bg_hex, box_frac=None, box=None, shape="square"):
        """Place logo centred in size on a solid background, inside box (x0,y0,x1,y1) or a centred fraction."""
        w, h = size
        canvas = Image.new("RGBA", size, bl.hex_to_rgb(bg_hex) + (255,))
        if box is None:
            fw, fh = box_frac
            box = ((1 - fw) / 2 * w, (1 - fh) / 2 * h, (1 + fw) / 2 * w, (1 + fh) / 2 * h)
        x0, y0, x1, y1 = box
        placed = self.fit(logo, int(x1 - x0), int(y1 - y0))
        canvas.alpha_composite(placed, (int(x0 + (x1 - x0 - placed.width) / 2), int(y0 + (y1 - y0 - placed.height) / 2)))
        return canvas

    def knockout_set(self, colours: list[dict]) -> list[str]:
        """Lighter logo colours to knock out (make transparent) in single-colour versions."""
        if len(colours) < 2:
            return []
        lights = {c["hex"]: bl.rgb_to_oklch(bl.hex_to_rgb(c["hex"]))[0] for c in colours}
        darkest = min(lights.values())
        return [hx for hx, L in lights.items() if L - darkest > 0.25]

    def knockout(self, im, colours: list[dict], knock: list[str], ink: str):
        """Recolour to ink and turn enclosed light shapes into holes.

        Pixels nearest a knockout colour are grouped into connected shapes. A shape is knocked out
        only if it is mostly enclosed by ink; free-standing shapes (e.g. a lighter tagline) that
        mostly border the background stay as ink so no part of the logo disappears.
        """
        palette = [bl.hex_to_rgb(c["hex"]) for c in colours]
        knock_rgb = {bl.hex_to_rgb(k) for k in knock}
        ink_rgb = bl.hex_to_rgb(ink)
        w, h = im.size
        src = im.load()
        is_knock = bytearray(w * h)
        alpha = bytearray(w * h)
        for y in range(h):
            for x in range(w):
                r, g, b, a = src[x, y]
                alpha[y * w + x] = a
                if a:
                    nearest = min(palette, key=lambda p: (p[0] - r) ** 2 + (p[1] - g) ** 2 + (p[2] - b) ** 2)
                    is_knock[y * w + x] = nearest in knock_rgb
        hole = bytearray(w * h)
        seen = bytearray(w * h)
        for start in range(w * h):
            if not is_knock[start] or seen[start]:
                continue
            stack, comp, boundary, exterior = [start], [], 0, 0
            seen[start] = 1
            while stack:
                i = stack.pop()
                comp.append(i)
                x, y = i % w, i // w
                edge = False
                touches_bg = False
                for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                    if not (0 <= nx < w and 0 <= ny < h):
                        edge = touches_bg = True
                        continue
                    j = ny * w + nx
                    if is_knock[j]:
                        if not seen[j]:
                            seen[j] = 1
                            stack.append(j)
                    else:
                        edge = True
                        if alpha[j] < 32:
                            touches_bg = True
                boundary += edge
                exterior += touches_bg
            if boundary and exterior / boundary < 0.25:
                for i in comp:
                    hole[i] = 1
        out = Image.new("RGBA", im.size, (0, 0, 0, 0))
        dst = out.load()
        for i in range(w * h):
            if alpha[i] and not hole[i]:
                dst[i % w, i // w] = ink_rgb + (alpha[i],)
        return out

    VARIANT_WORDS = {
        "full-colour": "full colour",
        "mono-dark": "single colour, dark",
        "mono-light": "single colour, white (reversed)",
        "mono-dark-knockout": "single colour, dark, with cut-out details",
        "mono-light-knockout": "single colour, white (reversed), with cut-out details",
    }

    def variant_alt(self, stem: str, variant: str) -> str:
        """Alt text that names the organisation and says which version this is."""
        subject = f"{self.name} symbol" if stem == "symbol" else self.alt
        return f"{subject}, {self.VARIANT_WORDS.get(variant, variant.replace('-', ' '))}"

    def raster_logos(self, master, stem: str, colours: list[dict]):
        dest = self.out / "logo"
        variants = {"full-colour": master, "mono-dark": self.recolour(master, self.dark),
                    "mono-light": self.recolour(master, "#ffffff")}
        knock = self.knockout_set(colours)
        if knock:
            self.has_knockout = True
            variants["mono-dark-knockout"] = self.knockout(master, colours, knock, self.dark)
            variants["mono-light-knockout"] = self.knockout(master, colours, knock, "#ffffff")
            self.manifest["warnings"].append(
                f"{stem} logo has several colours. Plain single-colour versions merge overlapping shapes; "
                f"knockout versions turn enclosed shapes in {knock} into holes instead. Inspect both, keep the one that preserves "
                "the logo's detail, and ask the designer for official single-colour artwork if neither does.")
        for name, im in variants.items():
            path = dest / f"{stem}-{name}.png"
            self.fit(im, 2000, 2000).save(path)
            self.record(path, f"{stem} logo, {name.replace('-', ' ')} (PNG, transparent)", alt=self.variant_alt(stem, name))
            pad = round(im.height * self.clear)
            padded = Image.new("RGBA", (im.width + 2 * pad, im.height + 2 * pad), (0, 0, 0, 0))
            padded.alpha_composite(im, (pad, pad))
            path = dest / f"{stem}-{name}-clearspace.png"
            self.fit(padded, 2000, 2000).save(path)
            self.record(path, f"{stem} logo, {name.replace('-', ' ')}, with minimum clear space built in", alt=self.variant_alt(stem, name))
        return variants

    def background_tests(self, variants):
        dest = self.out / "logo" / "backgrounds"
        dest.mkdir(parents=True, exist_ok=True)
        tests = [("white", "#ffffff"), ("light-neutral", self.tint), ("primary", self.primary), ("dark", self.dark)]
        tests += [(c["id"], c["hex"]) for c in self.brand["color"]["brand"][1:]]
        results = []
        for label, bg in tests:
            variant, ratio = self.variant_for(bg, self.logo_colours)
            full_ratio = self.full_colour_ratio(bg, self.logo_colours)
            tile = self.compose(self.pick(variants, variant), (800, 400), bg, box_frac=(0.7, 0.5))
            path = dest / f"logo-on-{label}.png"
            tile.convert("RGB").save(path)
            results.append({"background": label, "hex": bg, "recommendedVariant": variant,
                            "contrast": round(ratio, 2), "fullColourContrast": round(full_ratio, 2),
                            "fullColourAllowed": full_ratio >= 3.0 or bg in self.exceptions,
                            "approvedException": full_ratio < 3.0 and bg in self.exceptions,
                            "file": str(path.relative_to(self.root))})
            self.record(path, f"Logo ({variant}) on {label} background", alt=f"{self.variant_alt('primary', self.mono_name(variant))} on a {self.label(bg)} background")
        self.manifest["backgroundTests"] = results

    def favicons(self, icon_src):
        dest = self.out / "favicons"
        dest.mkdir(parents=True, exist_ok=True)
        # Solid brand tile: transparent icons vanish on dark browser tabs and fine detail blurs at 16px.
        tile = self.avatar_bg
        variant, _ = self.variant_for(tile, self.symbol_colours)
        sq_t = self.compose(self.pick(icon_src, variant), (512, 512), tile, box_frac=(0.8, 0.8))
        sq_t.save(dest / "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)])
        self.record(dest / "favicon.ico", "Browser favicon (16, 32, 48 px) on a solid brand tile")
        for s in (16, 32, 48, 192, 512):
            p = dest / f"icon-{s}.png"
            sq_t.resize((s, s), Image.LANCZOS).save(p)
            self.record(p, f"App/browser icon {s}x{s}", alt=f"{self.name} icon")
        bg_variant, _ = self.variant_for(self.primary, self.symbol_colours)
        apple = self.compose(self.pick(icon_src, bg_variant), (180, 180), self.primary, box_frac=(0.72, 0.72))
        apple.convert("RGB").save(dest / "apple-touch-icon.png")
        self.record(dest / "apple-touch-icon.png", "Apple touch icon 180x180 (opaque)")
        # Maskable icons: keep content inside the central 80% circle -> ~56% box.
        mask = self.compose(self.pick(icon_src, bg_variant), (512, 512), self.primary, box_frac=(0.56, 0.56))
        mask.convert("RGB").save(dest / "icon-maskable-512.png")
        self.record(dest / "icon-maskable-512.png", "Android maskable icon 512x512 (content inside safe circle)")
        manifest = {
            "name": self.name.strip(), "short_name": self.short_name(),
            "icons": [
                {"src": "icon-192.png", "sizes": "192x192", "type": "image/png"},
                {"src": "icon-512.png", "sizes": "512x512", "type": "image/png"},
                {"src": "icon-maskable-512.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable"},
            ],
            "theme_color": self.primary, "background_color": "#ffffff", "display": "standalone",
        }
        (dest / "site.webmanifest").write_text(json.dumps(manifest, indent=2) + "\n")
        self.record(dest / "site.webmanifest", "Web app manifest")
        (dest / "head-snippet.html").write_text(
            '<link rel="icon" href="/favicon.ico" sizes="48x48">\n'
            '<link rel="icon" href="/icon-192.png" type="image/png" sizes="192x192">\n'
            '<link rel="apple-touch-icon" href="/apple-touch-icon.png">\n'
            '<link rel="manifest" href="/site.webmanifest">\n'
            f'<meta name="theme-color" content="{self.primary}">\n')
        self.record(dest / "head-snippet.html", "HTML <head> tags for favicons")

    def short_name(self) -> str:
        """App short name: whole words only, at most 12 characters (home-screen label limit)."""
        out = ""
        for word in self.name.split():
            if len((out + " " + word).strip()) > 12:
                break
            out = (out + " " + word).strip()
        return out or self.name.split()[0][:12]

    # ------------------------------------------------------------------ social
    def platforms(self):
        data = json.loads(PLATFORMS_FILE.read_text())
        self.manifest["platformSpecsReviewed"] = data["lastReviewed"]
        known = {p["id"]: p for p in data["platforms"]}
        for pid in self.platform_ids:
            if pid not in known:
                self.manifest["warnings"].append(f"Unknown platform '{pid}' (known: {', '.join(known)})")
                continue
            yield known[pid]

    def safe_box(self, fmt):
        w, h = fmt["width"], fmt["height"]
        sz = fmt.get("safeZone") or {"top": 0.08, "right": 0.08, "bottom": 0.08, "left": 0.08}
        return (sz["left"] * w, sz["top"] * h, w - sz["right"] * w, h - sz["bottom"] * h)

    PHONE_WIDTH = 360  # CSS px a cover is shown at on a small phone.

    def layout(self, fmt, aspect: float, symbol_aspect: float):
        """Where the logo (and template text) go. Shared by PNG previews and SVG templates.

        Returns dict(use_symbol, box=(x0,y0,x1,y1), text=bool, note).
        """
        w, h = fmt["width"], fmt["height"]
        x0, y0, x1, y1 = self.safe_box(fmt)
        cw, ch = x1 - x0, y1 - y0
        if fmt["kind"] == "avatar":
            frac = 0.62 if fmt.get("displayShape") == "circle" else 0.74
            return {"use_symbol": True, "box": ((1 - frac) / 2 * w, (1 - frac) / 2 * h, (1 + frac) / 2 * w, (1 + frac) / 2 * h),
                    "text": False, "note": "Logo sized to sit inside the circular crop." if fmt.get("displayShape") == "circle" else ""}
        if fmt["kind"] == "cover":
            min_px = float(self.brand["logo"].get("minSize", {}).get("digitalPx", 0) or 0)
            needed = min(min_px * w / self.PHONE_WIDTH, cw * 0.95)  # Upload px so the logo stays >= min size on phones.
            for frac in (0.6, 0.8, 0.95):
                fitted = min(cw * frac, ch * frac * aspect)
                if fitted >= needed:
                    lw, lh = fitted, fitted / aspect
                    return {"use_symbol": False, "text": False, "note": fmt.get("note", ""),
                            "box": (x0 + (cw - lw) / 2, y0 + (ch - lh) / 2, x0 + (cw + lw) / 2, y0 + (ch + lh) / 2)}
            lh = ch * 0.8
            lw = min(cw, lh * symbol_aspect)
            return {"use_symbol": self.symbol is not None, "text": False,
                    "note": ("Full logo would be below its minimum size on phones, so the symbol is used. " if self.symbol else
                             "Warning: the full logo is below its minimum size on phones; supply a symbol. ") + fmt.get("note", ""),
                    "box": (x0 + (cw - lw) / 2, y0 + (ch - lh) / 2, x0 + (cw + lw) / 2, y0 + (ch + lh) / 2)}
        # Posts, stories, thumbnails, link images: headline top-left, logo bottom-left.
        lh = max(ch * 0.12, 1)
        lw = min(cw * 0.4, lh * aspect)
        lh = lw / aspect
        return {"use_symbol": False, "text": True, "note": fmt.get("note", ""), "box": (x0, y1 - lh, x0 + lw, y1)}

    @staticmethod
    def text_sizes(fmt):
        base = min(fmt["width"], fmt["height"])
        return max(32, round(base * 0.08)), max(24, round(base * 0.05))

    def social(self, logo_variants, symbol_variants):
        orientation = "wide-horizontal" if self._is_wide(self.symbol or self.master) else "ok"
        if orientation == "wide-horizontal" and not self.symbol:
            self.manifest["warnings"].append(
                "Logo is wide and no symbol/monogram was supplied: avatars will be hard to read. "
                "Supply logo.symbol in brand.json (or a stacked lock-up) and re-run.")
        for platform in self.platforms():
            dest = self.out / "social" / platform["id"]
            dest.mkdir(parents=True, exist_ok=True)
            for fmt in platform["formats"]:
                stem = dest / f"{platform['id']}-{fmt['id']}-{fmt['width']}x{fmt['height']}"
                self.svg_template(platform, fmt, stem.with_suffix(".svg"))
                self.guides_svg(fmt, Path(str(stem) + "-guides.svg"))
                if not logo_variants:
                    continue
                spec = self.layout(fmt, self.aspect, self.symbol_aspect)
                bg = self.avatar_bg if fmt["kind"] == "avatar" else self.social_bg
                use_symbol = spec["use_symbol"]
                colours = self.symbol_colours if use_symbol else self.logo_colours
                variant, ratio = self.variant_for(bg, colours)
                source = symbol_variants if use_symbol else logo_variants
                im = self.compose(self.pick(source, variant), (fmt["width"], fmt["height"]), bg, box=spec["box"])
                note = spec["note"]
                png = stem.with_suffix(".png")
                im.convert("RGB").save(png, optimize=True)
                purpose = f"{platform['name']} {fmt['label']} ({fmt['width']}x{fmt['height']})"
                if spec["text"]:
                    purpose += " layout preview; add the headline using the SVG template"
                subject = self.variant_alt("symbol" if use_symbol and self.symbol else "primary", self.mono_name(variant))
                self.record(png, purpose,
                            alt=f"{subject} on a {self.label(bg)} background", logoVariant=variant,
                            logoContrast=round(ratio, 2), note=note)

    def _is_wide(self, path: Path) -> bool:
        data: dict = {}
        try:
            (analyze_logo.analyse_svg if path.suffix.lower() == ".svg" else analyze_logo.analyse_raster)(path, data)
        except bl.ImageError:
            return False
        return data.get("orientation") == "wide-horizontal"

    def _logo_href(self, svg_path: Path, src: Path | None = None) -> str:
        """Embed the logo so the SVG template is self-contained (falls back to a relative link)."""
        src = src or self.master
        mime = {"svg": "image/svg+xml", "png": "image/png", "jpg": "image/jpeg", "jpeg": "image/jpeg", "webp": "image/webp"}
        kind = mime.get(src.suffix.lower().lstrip("."))
        if kind and src.stat().st_size < 2_000_000:
            return f"data:{kind};base64,{base64.b64encode(src.read_bytes()).decode()}"
        return str(Path(*[".."] * len(svg_path.parent.relative_to(self.root).parts)) / src.relative_to(self.root))

    def svg_template(self, platform, fmt, path: Path):
        w, h = fmt["width"], fmt["height"]
        x0, y0, x1, y1 = self.safe_box(fmt)
        bg = self.avatar_bg if fmt["kind"] == "avatar" else self.social_bg
        text_colour = "#ffffff" if bl.contrast_ratio("#ffffff", bg) >= bl.contrast_ratio(self.dark, bg) else self.dark
        ratio = bl.contrast_ratio(text_colour, bg)
        href = self._logo_href(path)
        sw, sh = x1 - x0, y1 - y0
        spec = self.layout(fmt, self.aspect, self.symbol_aspect)
        if spec["use_symbol"] and self.symbol:
            href = self._logo_href(path, self.symbol)
        bx0, by0, bx1, by1 = spec["box"]
        align = "xMinYMax" if spec["text"] else "xMidYMid"
        logo_el = (f'<image href="{href}" x="{bx0:.0f}" y="{by0:.0f}" width="{bx1 - bx0:.0f}" height="{by1 - by0:.0f}" '
                   f'preserveAspectRatio="{align} meet"/>')
        text_el = ""
        if spec["text"]:
            fs, fs2 = self.text_sizes(fmt)
            text_el = (f'<text x="{x0:.0f}" y="{y0 + fs:.0f}" font-family="{escape(self.display_font)}" font-size="{fs}" '
                       f'font-weight="700" fill="{text_colour}">Headline: one idea, few words</text>'
                       f'<text x="{x0:.0f}" y="{y0 + fs * 1.4 + fs2 * 1.2:.0f}" font-family="{escape(self.body_font)}" font-size="{fs2}" '
                       f'fill="{text_colour}">Supporting line (contrast {ratio:.1f}:1)</text>')
        svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc">
  <title id="title">{escape(self.name)} {escape(platform["name"])} {escape(fmt["label"])} template</title>
  <desc id="desc">Template {w}x{h}px. Keep text and logos inside the dashed safe zone. Text colour {text_colour} on {bg} = {ratio:.1f}:1. Delete the "guides" group before export.</desc>
  <rect id="background" width="{w}" height="{h}" fill="{bg}"/>
  <g id="artwork">{logo_el}{text_el}</g>
  <g id="guides" fill="none" stroke="#ff00aa" stroke-width="{max(2, w // 400)}" stroke-dasharray="12 8">
    <rect x="{x0:.0f}" y="{y0:.0f}" width="{sw:.0f}" height="{sh:.0f}"/>
    {f'<circle cx="{w / 2}" cy="{h / 2}" r="{w / 2}"/>' if fmt.get("displayShape") == "circle" else ""}
  </g>
</svg>
'''
        path.write_text(svg, encoding="utf-8")
        self.record(path, f"Editable template: {platform['name']} {fmt['label']}", note=fmt.get("note", ""))

    def guides_svg(self, fmt, path: Path):
        w, h = fmt["width"], fmt["height"]
        x0, y0, x1, y1 = self.safe_box(fmt)
        circle = f'<circle cx="{w / 2}" cy="{h / 2}" r="{w / 2}" fill="none" stroke="#ff00aa" stroke-width="3"/>' if fmt.get("displayShape") == "circle" else ""
        path.write_text(
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="Safe zone overlay">'
            f'<path fill="#ff00aa" fill-opacity="0.18" fill-rule="evenodd" d="M0 0H{w}V{h}H0Z M{x0:.0f} {y0:.0f}V{y1:.0f}H{x1:.0f}V{y0:.0f}Z"/>'
            f'<rect x="{x0:.0f}" y="{y0:.0f}" width="{x1 - x0:.0f}" height="{y1 - y0:.0f}" fill="none" stroke="#ff00aa" stroke-width="3" stroke-dasharray="12 8"/>'
            f'{circle}</svg>\n', encoding="utf-8")

    # ------------------------------------------------------------------ run
    def run(self):
        (self.out / "logo").mkdir(parents=True, exist_ok=True)
        if self.master.suffix.lower() == ".svg":
            self.svg_variants(self.master, "primary", self.logo_colours)
            if self.symbol and self.symbol.suffix.lower() == ".svg":
                self.svg_variants(self.symbol, "symbol", self.symbol_colours)
        else:
            dest = self.out / "logo" / f"primary-original{self.master.suffix.lower()}"
            shutil.copyfile(self.master, dest)
            self.record(dest, "Original logo file as supplied", alt=self.alt)
        logo_variants = symbol_variants = None
        if bl.HAVE_PIL:
            master = self.load_master(self.master)
            if master is not None:
                logo_variants = self.raster_logos(master, "primary", self.logo_colours)
                symbol_variants = logo_variants
                if self.symbol:
                    sym = self.load_master(self.symbol)
                    if sym is not None:
                        symbol_variants = self.raster_logos(sym, "symbol", self.symbol_colours)
                self.background_tests(logo_variants)
                self.favicons(symbol_variants)
        else:
            self.manifest["skipped"].append("PNG logo variants, background tests, favicons and social PNGs need Pillow: pip install pillow")
        self.social(logo_variants, symbol_variants)
        (self.out / "manifest.json").write_text(json.dumps(self.manifest, indent=2) + "\n")
        return self.manifest


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("brand", type=Path)
    ap.add_argument("--platforms", help="Comma-separated platform ids (default: brand.json social.platforms)")
    args = ap.parse_args(argv)
    kit = Kit(args.brand.resolve(), args.platforms.split(",") if args.platforms else None)
    manifest = kit.run()
    print(json.dumps({"files": len(manifest["files"]), "warnings": manifest["warnings"],
                      "skipped": manifest["skipped"], "manifest": str(kit.out / "manifest.json")}, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
