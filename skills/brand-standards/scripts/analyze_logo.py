#!/usr/bin/env python3
"""Analyse a logo file and report measurable facts for the style guide.

Reports: format, dimensions, aspect ratio and orientation, background type,
content bounding box and built-in padding, dominant colours (with HEX/RGB/HSL/
OKLCH/CMYK, share of logo area, and WCAG contrast against white and black),
recommended backgrounds, colour-vision-deficiency risks, and SVG details
(fonts, gradients, embedded rasters, accessibility title).

Usage:
    analyze_logo.py path/to/logo.(svg|png|jpg|webp) [--out analysis.json]

Exit codes: 0 success, 2 bad input.
"""

from __future__ import annotations

import argparse
import json
import random
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import brandlib as bl  # noqa: E402


def _quantize(pixels, alpha_min=200):
    """Bucket opaque pixels to 5 bits/channel -> {(r,g,b): count} using bucket means."""
    sums: dict = {}
    for r, g, b, a in pixels:
        if a < alpha_min:
            continue
        key = (r >> 3, g >> 3, b >> 3)
        s = sums.setdefault(key, [0, 0, 0, 0])
        s[0] += r
        s[1] += g
        s[2] += b
        s[3] += 1
    return {(s[0] / s[3], s[1] / s[3], s[2] / s[3]): s[3] for s in sums.values()}


def _kmeans(weighted: dict, k: int, iters: int = 20, seed: int = 7):
    """Weighted k-means in OKLab over quantised colours. Returns [(lab, weight)]."""
    pts = [(bl.rgb_to_oklab(rgb), w) for rgb, w in weighted.items()]
    if not pts:
        return []
    k = min(k, len(pts))
    rng = random.Random(seed)
    # k-means++ initialisation, weighted by pixel count.
    centres = [max(pts, key=lambda p: p[1])[0]]
    while len(centres) < k:
        d2 = [min(sum((a - b) ** 2 for a, b in zip(p, c)) for c in centres) * w for p, w in pts]
        total = sum(d2)
        if total == 0:
            break
        r, acc = rng.random() * total, 0.0
        for (p, _), d in zip(pts, d2):
            acc += d
            if acc >= r:
                centres.append(p)
                break
    for _ in range(iters):
        groups = [[0.0, 0.0, 0.0, 0.0] for _ in centres]
        for p, w in pts:
            j = min(range(len(centres)), key=lambda i: sum((a - b) ** 2 for a, b in zip(p, centres[i])))
            g = groups[j]
            g[0] += p[0] * w
            g[1] += p[1] * w
            g[2] += p[2] * w
            g[3] += w
        new = [(g[0] / g[3], g[1] / g[3], g[2] / g[3]) if g[3] else c for g, c in zip(groups, centres)]
        if new == centres:
            break
        centres = new
    weights = [0.0] * len(centres)
    for p, w in pts:
        j = min(range(len(centres)), key=lambda i: sum((a - b) ** 2 for a, b in zip(p, centres[i])))
        weights[j] += w
    return [(c, w) for c, w in zip(centres, weights) if w > 0]


def _merge(clusters, threshold=0.06):
    clusters = sorted(clusters, key=lambda c: -c[1])
    merged = True
    while merged:
        merged = False
        for i in range(len(clusters)):
            for j in range(i + 1, len(clusters)):
                (a, wa), (b, wb) = clusters[i], clusters[j]
                if sum((x - y) ** 2 for x, y in zip(a, b)) ** 0.5 < threshold:
                    w = wa + wb
                    c = tuple((x * wa + y * wb) / w for x, y in zip(a, b))
                    clusters[i] = (c, w)
                    del clusters[j]
                    merged = True
                    break
            if merged:
                break
    return clusters


def _background(img):
    """Detect transparent or solid background colour from alpha and border pixels."""
    w, h, px = img["width"], img["height"], img["pixels"]
    transparent = sum(1 for p in px if p[3] < 16)
    if transparent / len(px) > 0.02:
        return {"type": "transparent", "hex": None}
    border = [px[x] for x in range(w)] + [px[(h - 1) * w + x] for x in range(w)]
    border += [px[y * w] for y in range(h)] + [px[y * w + w - 1] for y in range(h)]
    counts: dict = {}
    for r, g, b, _ in border:
        key = (r >> 4, g >> 4, b >> 4)
        counts.setdefault(key, []).append((r, g, b))
    best = max(counts.values(), key=len)
    if len(best) / len(border) < 0.6:
        return {"type": "complex", "hex": None,
                "note": "Border is not a single colour (photo, gradient or full-bleed artwork). Provide a version on a transparent background."}
    mean = tuple(sum(c[i] for c in best) / len(best) for i in range(3))
    return {"type": "solid", "hex": bl.rgb_to_hex(mean)}


def _foreground(img, bg):
    px = img["pixels"]
    if bg["type"] == "solid":
        bg_lab = bl.rgb_to_oklab(bl.hex_to_rgb(bg["hex"]))
        out = []
        for p in px:
            d = sum((a - b) ** 2 for a, b in zip(bl.rgb_to_oklab(p), bg_lab)) ** 0.5
            out.append(p if d > 0.05 else (p[0], p[1], p[2], 0))
        return out
    return px


def _bbox(img, fg):
    w, h = img["width"], img["height"]
    xs, ys = [], []
    for i, p in enumerate(fg):
        if p[3] >= 32:
            xs.append(i % w)
            ys.append(i // w)
    if not xs:
        return None
    x0, x1, y0, y1 = min(xs), max(xs) + 1, min(ys), max(ys) + 1
    return {
        "x": round(x0 / w, 4), "y": round(y0 / h, 4),
        "width": round((x1 - x0) / w, 4), "height": round((y1 - y0) / h, 4),
        "paddingFraction": {"left": round(x0 / w, 3), "right": round((w - x1) / w, 3),
                            "top": round(y0 / h, 3), "bottom": round((h - y1) / h, 3)},
    }


EDGE_THRESHOLD = 0.10  # Share of the outer edge a colour needs before it counts as touching the background.


def _is_blend(lab, others, max_dist=0.035):
    """True if lab lies on the mix line between two other colours (anti-aliasing / JPEG fringe)."""
    for i, a in enumerate(others):
        for b in others[i + 1:]:
            ab = [y - x for x, y in zip(a, b)]
            denom = sum(v * v for v in ab)
            if denom == 0:
                continue
            t = sum((l - x) * v for l, x, v in zip(lab, a, ab)) / denom
            if 0.05 < t < 0.95:
                point = [x + t * v for x, v in zip(a, ab)]
                if sum((l - q) ** 2 for l, q in zip(lab, point)) ** 0.5 < max_dist:
                    return True
    return False


def _interior_ratios(img, fg, labs):
    """For each cluster, the share of its pixels whose four neighbours are the same cluster.

    Real shapes are solid (high ratio); anti-aliasing fringes are 1-2px rings (low ratio).
    """
    w, h = img["width"], img["height"]
    assign = []
    for p in fg:
        if p[3] < 200:
            assign.append(-1)
            continue
        lab = bl.rgb_to_oklab(p)
        assign.append(min(range(len(labs)), key=lambda i: sum((a - b) ** 2 for a, b in zip(lab, labs[i]))))
    total = [0] * len(labs)
    inner = [0] * len(labs)
    for i, a in enumerate(assign):
        if a < 0:
            continue
        total[a] += 1
        x, y = i % w, i // w
        if 0 < x < w - 1 and 0 < y < h - 1 and all(assign[j] == a for j in (i - 1, i + 1, i - w, i + w)):
            inner[a] += 1
    return [inner[i] / total[i] if total[i] else 0 for i in range(len(labs))]


def _edge_shares(img, fg, hexes):
    """Share of the logo's outer edge taken by each colour (pixels next to the background).

    Colours fully enclosed by other colours (e.g. a shape inside a disc) get ~0 and never
    sit against the background, so they do not decide which backgrounds the logo can use.
    """
    w, h = img["width"], img["height"]
    labs = {hx: bl.rgb_to_oklab(bl.hex_to_rgb(hx)) for hx in hexes}
    counts = {hx: 0 for hx in hexes}
    for i, p in enumerate(fg):
        if p[3] < 200:
            continue
        x, y = i % w, i // w
        touch = False
        for dx, dy in ((2, 0), (-2, 0), (0, 2), (0, -2)):  # Distance 2 skips the anti-aliased ring.
            nx, ny = x + dx, y + dy
            if not (0 <= nx < w and 0 <= ny < h) or fg[ny * w + nx][3] < 32:
                touch = True
                break
        if touch:
            lab = bl.rgb_to_oklab(p)
            dist = {k: sum((a - b) ** 2 for a, b in zip(v, lab)) ** 0.5 for k, v in labs.items()}
            nearest = min(dist, key=dist.get)
            if dist[nearest] < 0.06:  # Ignore anti-aliased blends; they belong to no colour.
                counts[nearest] += 1
    total = sum(counts.values()) or 1
    return {hx: n / total for hx, n in counts.items()}


def _orientation(ratio):
    if ratio >= 2.5:
        return "wide-horizontal"
    if ratio >= 1.25:
        return "horizontal"
    if ratio > 0.8:
        return "square"
    return "vertical"


def describe_colour(hx, share=None):
    entry = {"name": bl.hue_name(hx), **bl.colour_formats(hx)}
    if share is not None:
        entry["share"] = round(share, 4)
    L, C, H = bl.rgb_to_oklch(bl.hex_to_rgb(hx))
    entry["isNeutral"] = C < 0.03
    entry["onWhite"] = bl.wcag_report(hx, "#ffffff")
    entry["onBlack"] = bl.wcag_report(hx, "#000000")
    return entry


def analyse_raster(path: Path, analysis: dict):
    img = bl.load_rgba(path, max_side=512)
    analysis["dimensions"] = {"width": img["original_width"], "height": img["original_height"]}
    bg = _background(img)
    analysis["background"] = bg
    fg = _foreground(img, bg)
    bbox = _bbox(img, fg)
    analysis["contentBox"] = bbox
    if bbox:
        cw = bbox["width"] * img["original_width"]
        ch = bbox["height"] * img["original_height"]
        ratio = cw / ch if ch else 1
        analysis["contentAspectRatio"] = round(ratio, 3)
        analysis["orientation"] = _orientation(ratio)
    weighted = _quantize(fg)
    total = sum(weighted.values()) or 1
    clusters = _merge(_kmeans(weighted, k=8))
    colours = []
    ordered = sorted(clusters, key=lambda c: -c[1])
    interior = _interior_ratios(img, fg, [lab for lab, _ in ordered])
    kept_labs = [bl.rgb_to_oklab(bl.hex_to_rgb(bg["hex"]))] if bg["type"] == "solid" else []
    for idx, (lab, w) in enumerate(ordered):
        share = w / total
        if share < 0.015:  # Anti-aliasing fringes and noise.
            continue
        if share < 0.08 and interior[idx] < 0.35 and _is_blend(lab, kept_labs):
            continue  # Thin edge blend between two real colours (or a colour and the background).
        kept_labs.append(lab)
        colours.append(describe_colour(bl.rgb_to_hex(bl.oklab_to_rgb(lab)), share))
    if colours:
        total_kept = sum(c["share"] for c in colours)
        for c in colours:
            c["share"] = round(c["share"] / total_kept, 4)
    edges = _edge_shares(img, fg, [c["hex"] for c in colours])
    for c in colours:
        c["edgeShare"] = round(edges.get(c["hex"], 0), 4)
        c["touchesBackground"] = c["edgeShare"] >= EDGE_THRESHOLD
    analysis["colours"] = colours
    analysis["resolutionWarning"] = (
        max(img["original_width"], img["original_height"]) < 1000
        and "Raster logo is under 1000px on its longest side; request a vector (SVG/EPS/PDF) or a larger master file."
    ) or None
    hues = [c for c in colours if not c["isNeutral"]]
    analysis["possibleGradient"] = len(hues) >= 4 and len({round(float(c["oklch"].split()[2].rstrip(")")) / 30) for c in hues}) <= 2


def analyse_svg(path: Path, analysis: dict):
    text = path.read_text(encoding="utf-8", errors="replace")
    info = bl.svg_info(text)
    analysis["svg"] = info
    if "width" in info and info["height"]:
        ratio = info["width"] / info["height"]
        analysis["dimensions"] = {"width": info["width"], "height": info["height"], "units": "svg user units"}
        analysis["contentAspectRatio"] = round(ratio, 3)
        analysis["orientation"] = _orientation(ratio)
    counts = bl.svg_colours(text)
    total = sum(counts.values()) or 1
    analysis["declaredColours"] = [
        describe_colour(hx, n / total) | {"declarations": n}
        for hx, n in sorted(counts.items(), key=lambda kv: -kv[1])
    ]
    # Rasterise for pixel-accurate colour shares and bounding box when a renderer exists.
    with tempfile.TemporaryDirectory() as tmp:
        png = Path(tmp) / "render.png"
        if bl.rasterize_svg(path, png):
            raster: dict = {}
            try:
                analyse_raster(png, raster)
                analysis["rendered"] = {k: raster[k] for k in ("background", "contentBox", "colours") if k in raster}
                if raster.get("contentAspectRatio"):
                    analysis["contentAspectRatio"] = raster["contentAspectRatio"]
                    analysis["orientation"] = raster["orientation"]
            except bl.ImageError as exc:
                analysis["renderNote"] = str(exc)
        else:
            analysis["renderNote"] = ("No SVG renderer found (cairosvg, rsvg-convert, inkscape, magick, qlmanage); "
                                      "colour shares are by declaration count, not area.")
    declared = analysis["declaredColours"]
    rendered = analysis.get("rendered", {}).get("colours")
    if declared and rendered:
        # Declared colours are exact; the render only supplies area shares. Rendered clusters
        # that match no declared colour are anti-aliasing or renderer background, so drop them.
        shares = {c["hex"]: 0.0 for c in declared}
        edges = {c["hex"]: 0.0 for c in declared}
        for rc in rendered:
            nearest = min(declared, key=lambda d: bl.delta_e_ok(d["hex"], rc["hex"]))
            if bl.delta_e_ok(nearest["hex"], rc["hex"]) < 0.08:
                shares[nearest["hex"]] += rc["share"]
                edges[nearest["hex"]] += rc.get("edgeShare", 0)
        total_share = sum(shares.values()) or 1
        total_edge = sum(edges.values()) or 1
        colours = []
        for hx, sh in sorted(shares.items(), key=lambda kv: -kv[1]):
            if sh > 0:
                c = describe_colour(hx, sh / total_share)
                c["edgeShare"] = round(edges[hx] / total_edge, 4)
                c["touchesBackground"] = c["edgeShare"] >= EDGE_THRESHOLD
                colours.append(c)
        analysis["colours"] = colours or declared
    else:
        analysis["colours"] = declared or rendered or []


def recommendations(analysis: dict) -> dict:
    colours = analysis.get("colours", [])
    rec: dict = {}
    if colours:
        # Only colours that touch the background decide which backgrounds the logo can sit on.
        edge = [c for c in colours if c.get("touchesBackground", True)] or colours
        min_white = min(c["onWhite"]["ratio"] for c in edge)
        min_black = min(c["onBlack"]["ratio"] for c in edge)
        rec["fullColourOnWhite"] = min_white >= 3.0
        rec["fullColourOnBlack"] = min_black >= 3.0
        rec["lowestContrastOnWhite"] = round(min_white, 2)
        rec["lowestContrastOnBlack"] = round(min_black, 2)
        notes = []
        if min_white < 3.0:
            weak = [c["hex"] for c in edge if c["onWhite"]["ratio"] < 3.0]
            notes.append(f"Logo colours {weak} are below 3:1 on white. Use a dark or brand-colour background for the full-colour logo, or use the mono version on light backgrounds.")
        if min_black < 3.0:
            weak = [c["hex"] for c in edge if c["onBlack"]["ratio"] < 3.0]
            notes.append(f"Logo colours {weak} are below 3:1 on black. Use the reversed (white) logo on dark backgrounds.")
        rec["notes"] = notes
        chromatic = {c["hex"]: c["hex"] for c in colours if not c["isNeutral"]}
        rec["cvdRisks"] = bl.cvd_pair_report(chromatic) if len(chromatic) > 1 else []
        rec["seedColours"] = [c["hex"] for c in colours if not c["isNeutral"]][:3] or [colours[0]["hex"]]
    orient = analysis.get("orientation")
    rec["needsSymbolForAvatars"] = orient == "wide-horizontal"
    if orient == "wide-horizontal":
        rec["avatarNote"] = ("Wide logo: it will be illegible inside circular social avatars. "
                             "Use the symbol/monogram alone, or create a stacked lock-up for square formats.")
    # Minimum size: wider marks need more width to keep the height legible.
    ratio = analysis.get("contentAspectRatio") or 1
    min_height_px = 24 if ratio < 2.5 else 20
    rec["suggestedMinSize"] = {
        "digitalWidthPx": max(24, round(min_height_px * ratio)),
        "printWidthMm": max(10, round(min_height_px * ratio * 0.2646 * 1.3)),
        "rationale": "Starting point only: confirm by viewing the logo at this size and checking the smallest detail and any text stay legible.",
    }
    return rec


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("logo", type=Path)
    ap.add_argument("--out", type=Path, help="Write JSON here as well as stdout")
    args = ap.parse_args(argv)
    if not args.logo.exists():
        print(f"error: {args.logo} not found", file=sys.stderr)
        return 2
    analysis: dict = {"file": str(args.logo), "format": args.logo.suffix.lower().lstrip("."),
                      "pillowAvailable": bl.HAVE_PIL}
    try:
        if analysis["format"] == "svg":
            analyse_svg(args.logo, analysis)
        else:
            analyse_raster(args.logo, analysis)
    except bl.ImageError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    analysis["recommendations"] = recommendations(analysis)
    text = json.dumps(analysis, indent=2)
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(text + "\n")
    print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
