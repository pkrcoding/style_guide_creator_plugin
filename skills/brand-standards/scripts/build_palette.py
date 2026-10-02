#!/usr/bin/env python3
"""Build an accessible brand colour system from seed colours (usually from the logo).

For every seed it generates an 11-step tonal scale (50-950) in OKLCH with the
exact brand colour pinned to its nearest step, then picks the steps that meet
WCAG 2.2 for text and UI on light and dark surfaces. It adds a tinted neutral
scale, semantic colours (success, warning, error, info) checked against the
brand hues, recommended pairings with contrast ratios, and a
colour-vision-deficiency (CVD) confusion report.

Usage:
    build_palette.py --seed "#0f6e7a:primary:Northwind Teal" --seed "#f2a541:accent:Lantern Gold" [--out palette.json]
    build_palette.py --seed ... --brand brand-guide/brand.json   # rebuild brand.json "color" in place

With --brand, manual fields on each colour (pantone, usage, ...) and color.proportions are kept
when the colour id still exists, and focus colours are refreshed.

Seed format: HEX[:ROLE[:NAME]]. The first seed is the primary colour by default.
ROLE is one of primary, secondary, accent, tertiary.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import brandlib as bl  # noqa: E402

STEPS = ["50", "100", "200", "300", "400", "500", "600", "700", "800", "900", "950"]
LIGHTNESS = [0.975, 0.945, 0.89, 0.81, 0.71, 0.62, 0.53, 0.45, 0.37, 0.29, 0.21]
CHROMA_FACTOR = [0.12, 0.25, 0.45, 0.7, 0.9, 1.0, 0.95, 0.85, 0.72, 0.58, 0.45]
SEMANTIC_HUES = {"success": 150.0, "warning": 75.0, "error": 27.0, "info": 250.0}
SEMANTIC_CHROMA = 0.16
WHITE, BLACK = "#ffffff", "#000000"


def make_scale(hex_seed: str | None, hue: float, chroma: float, pin: bool = True):
    scale = {s: bl.oklch_to_hex(L, chroma * f, hue) for s, L, f in zip(STEPS, LIGHTNESS, CHROMA_FACTOR)}
    pinned = None
    if hex_seed and pin:
        L = bl.rgb_to_oklch(bl.hex_to_rgb(hex_seed))[0]
        pinned = min(STEPS, key=lambda s: abs(LIGHTNESS[STEPS.index(s)] - L))
        scale[pinned] = bl.normalize_hex(hex_seed)
    return scale, pinned


def first_step(scale: dict, bg: str, threshold: float, from_light: bool = True):
    """Lightest (or darkest) step meeting the threshold against bg."""
    order = STEPS if from_light else list(reversed(STEPS))
    for s in order:
        if bl.contrast_ratio(scale[s], bg) >= threshold:
            return {"step": s, "hex": scale[s], "ratio": round(bl.contrast_ratio(scale[s], bg), 2)}
    return None


def solid_with_white_text(scale: dict):
    for s in STEPS:
        if bl.contrast_ratio(WHITE, scale[s]) >= 4.5:
            return {"step": s, "hex": scale[s], "ratio": round(bl.contrast_ratio(WHITE, scale[s]), 2)}
    return None


def step_details(scale: dict, neutral_dark: str):
    out = {}
    for s, hx in scale.items():
        on_white = bl.contrast_ratio(hx, WHITE)
        on_dark = bl.contrast_ratio(hx, neutral_dark)
        out[s] = {
            "hex": hx,
            "oklch": bl.colour_formats(hx)["oklch"],
            "contrastWithWhite": round(on_white, 2),
            "contrastWithBlack": round(bl.contrast_ratio(hx, BLACK), 2),
            "textColour": WHITE if bl.contrast_ratio(WHITE, hx) >= bl.contrast_ratio(neutral_dark, hx) else neutral_dark,
        }
    return out


def parse_seed(raw: str, index: int):
    parts = raw.split(":")
    hx = bl.normalize_hex(parts[0])
    default_roles = ["primary", "secondary", "accent", "tertiary"]
    role = parts[1].strip().lower() if len(parts) > 1 and parts[1].strip() else default_roles[min(index, 3)]
    name = parts[2].strip() if len(parts) > 2 and parts[2].strip() else f"{bl.hue_name(hx).title()}"
    return hx, role, name


def build(seeds: list[str], neutral_chroma: float = 0.012):
    notes: list[str] = []
    parsed = [parse_seed(s, i) for i, s in enumerate(seeds)]
    primary_hex = parsed[0][0]
    pL, pC, pH = bl.rgb_to_oklch(bl.hex_to_rgb(primary_hex))
    if pC < 0.03:
        notes.append("Primary colour is neutral (black/grey/white). Consider an accent colour for links, focus and highlights.")

    # Neutral scale tinted towards the primary hue (pure grey if primary is neutral).
    neutral_scale, _ = make_scale(None, pH, neutral_chroma if pC >= 0.03 else 0.0, pin=False)
    neutral_scale["950"] = bl.oklch_to_hex(0.17, neutral_chroma if pC >= 0.03 else 0.0, pH)
    dark_surface = neutral_scale["950"]

    brand = []
    used_ids: set[str] = set()
    for hx, role, name in parsed:
        L, C, H = bl.rgb_to_oklch(bl.hex_to_rgb(hx))
        scale, pinned = make_scale(hx, H, max(C, 0.02) / max(CHROMA_FACTOR[STEPS.index(
            min(STEPS, key=lambda s: abs(LIGHTNESS[STEPS.index(s)] - L)))], 0.1))
        cid = role if role not in used_ids else f"{role}-{len(used_ids)}"
        used_ids.add(cid)
        entry = {
            "id": cid,
            "name": name,
            "role": role,
            **bl.colour_formats(hx),
            "pinnedStep": pinned,
            "scale": scale,
            "steps": step_details(scale, dark_surface),
            "accessible": {
                "textOnLight": first_step(scale, WHITE, 4.5),
                "uiOnLight": first_step(scale, WHITE, 3.0),
                "textOnDark": first_step(scale, dark_surface, 4.5, from_light=False),
                "uiOnDark": first_step(scale, dark_surface, 3.0, from_light=False),
                "solidWithWhiteText": solid_with_white_text(scale),
            },
            "original": {
                "onWhite": bl.wcag_report(hx, WHITE),
                "onBlack": bl.wcag_report(hx, BLACK),
                "withWhiteText": bl.wcag_report(WHITE, hx),
            },
        }
        if entry["original"]["onWhite"]["ratio"] < 3.0:
            notes.append(f"{name} ({hx}) is {entry['original']['onWhite']['ratio']}:1 on white: decorative or large-area use only on light backgrounds. Use step {entry['accessible']['textOnLight']['step'] if entry['accessible']['textOnLight'] else 'n/a'} for text.")
        brand.append(entry)

    semantic = []
    brand_hues = [(b["name"], bl.rgb_to_oklch(bl.hex_to_rgb(b["hex"]))) for b in brand]
    for sid, hue in SEMANTIC_HUES.items():
        for bname, (bL, bC, bH) in brand_hues:
            diff = min(abs(bH - hue), 360 - abs(bH - hue))
            if bC >= 0.06 and diff < 20:
                notes.append(f"Brand colour '{bname}' is close in hue to the '{sid}' state colour. Never signal {sid} by colour alone; pair it with an icon and text, and keep brand {bname} out of {sid} messaging.")
        scale, _ = make_scale(None, hue, SEMANTIC_CHROMA, pin=False)
        semantic.append({
            "id": sid,
            "scale": scale,
            "tokens": {
                "fg": first_step(scale, WHITE, 4.5),
                "bg": {"step": "50", "hex": scale["50"]},
                "border": first_step(scale, WHITE, 3.0),
                "solid": solid_with_white_text(scale),
                "fgOnDark": first_step(scale, dark_surface, 4.5, from_light=False),
            },
        })

    pairings = recommended_pairings(brand, neutral_scale, semantic, dark_surface)
    cvd_set = {b["name"]: b["hex"] for b in brand if bl.rgb_to_oklch(bl.hex_to_rgb(b["hex"]))[1] >= 0.03}
    cvd_set.update({s["id"].title(): s["tokens"]["fg"]["hex"] for s in semantic if s["tokens"]["fg"]})
    cvd = bl.cvd_pair_report(cvd_set)
    grouped: dict = {}
    for issue in cvd:
        grouped.setdefault(tuple(issue["pair"]), []).append(issue["vision"])
    for (a, b), visions in grouped.items():
        notes.append(f"{a} and {b} may be confused ({', '.join(visions)}). Add labels, icons, patterns or a lightness difference wherever they carry meaning together.")

    return {
        "brand": brand,
        "neutral": {"id": "neutral", "scale": neutral_scale, "steps": step_details(neutral_scale, dark_surface),
                    "accessible": {
                        "body": {"step": "900", "hex": neutral_scale["900"], "ratio": round(bl.contrast_ratio(neutral_scale["900"], WHITE), 2)},
                        "secondaryText": first_step(neutral_scale, WHITE, 4.5),
                        "border": first_step(neutral_scale, WHITE, 3.0),
                        "decorativeBorder": {"step": "200", "hex": neutral_scale["200"]},
                    }},
        "semantic": semantic,
        "surfaces": {"light": WHITE, "dark": dark_surface},
        "proportions": default_proportions(brand),
        "pairings": pairings,
        "cvd": cvd,
        "notes": notes,
    }


def default_proportions(brand):
    roles = [b["id"] for b in brand]
    props = {"neutral": 60, roles[0]: 30}
    rest = roles[1:]
    for r in rest:
        props[r] = round(10 / len(rest), 1)
    if not rest:
        props[roles[0]] = 40
    return props


def _pair(fg, bg, fg_token, bg_token, use, label):
    ratio = bl.contrast_ratio(fg, bg)
    required = bl.THRESHOLDS[use]
    return {"fg": fg, "bg": bg, "fgToken": fg_token, "bgToken": bg_token, "use": use, "label": label,
            "ratio": round(ratio, 2), "required": required, "pass": ratio >= required,
            "rating": bl.rating_label(ratio)}


def recommended_pairings(brand, neutral, semantic, dark):
    p = []
    n_body = {"step": "900", "hex": neutral["900"]}
    n_sec = first_step(neutral, WHITE, 4.5)
    p.append(_pair(n_body["hex"], WHITE, f"neutral-{n_body['step']}", "white", "body", "Body text on light background"))
    if n_sec:
        p.append(_pair(n_sec["hex"], WHITE, f"neutral-{n_sec['step']}", "white", "body", "Secondary text / captions on light background"))
    p.append(_pair(neutral["50"], dark, "neutral-50", "neutral-950", "body", "Body text on dark background"))
    for b in brand:
        acc = b["accessible"]
        if acc["textOnLight"]:
            s = acc["textOnLight"]
            p.append(_pair(s["hex"], WHITE, f"{b['id']}-{s['step']}", "white", "body", f"{b['name']} text and links on light background"))
        if acc["solidWithWhiteText"]:
            s = acc["solidWithWhiteText"]
            p.append(_pair(WHITE, s["hex"], "white", f"{b['id']}-{s['step']}", "body", f"White text on {b['name']} buttons and banners"))
        if acc["textOnDark"]:
            s = acc["textOnDark"]
            p.append(_pair(s["hex"], dark, f"{b['id']}-{s['step']}", "neutral-950", "body", f"{b['name']} text and links on dark background"))
        orig_white = bl.contrast_ratio(b["hex"], WHITE)
        use = "body" if orig_white >= 4.5 else "large" if orig_white >= 3.0 else "decorative"
        p.append(_pair(b["hex"], WHITE, b["id"], "white", use,
                       f"Exact {b['name']} on white ({'any text' if use == 'body' else 'large text / UI only' if use == 'large' else 'decorative only - not for text or meaningful graphics'})"))
        on_brand = WHITE if bl.contrast_ratio(WHITE, b["hex"]) >= bl.contrast_ratio(neutral["950"], b["hex"]) else neutral["950"]
        r = bl.contrast_ratio(on_brand, b["hex"])
        use = "body" if r >= 4.5 else "large" if r >= 3.0 else "decorative"
        p.append(_pair(on_brand, b["hex"], "white" if on_brand == WHITE else "neutral-950", b["id"], use,
                       f"Text on exact {b['name']} background"))
    for s in semantic:
        t = s["tokens"]
        if t["fg"]:
            p.append(_pair(t["fg"]["hex"], t["bg"]["hex"], f"{s['id']}-{t['fg']['step']}", f"{s['id']}-50", "body", f"{s['id'].title()} message text on tinted background"))
    return p


GENERATED_KEYS = {"id", "name", "role", "hex", "rgb", "hsl", "oklch", "cmyk", "pinnedStep", "scale", "steps", "accessible", "original"}


def focus_on_brand(palette: dict) -> dict:
    """Focus ring colour to use inside sections filled with each brand colour (white or darkest neutral)."""
    dark = palette["neutral"]["scale"]["950"]
    out = {}
    for c in palette["brand"]:
        surfaces = [c["hex"]] + ([c["accessible"]["solidWithWhiteText"]["hex"]] if c["accessible"].get("solidWithWhiteText") else [])
        best = max((WHITE, dark), key=lambda f: min(bl.contrast_ratio(f, s) for s in surfaces))
        out[c["id"]] = {"surfaces": surfaces, "focus": best,
                        "ratio": round(min(bl.contrast_ratio(best, s) for s in surfaces), 2)}
    return out


def apply_custom_pairings(palette: dict, custom: list, excluded: list):
    """Keep human-approved pairings (recomputed) and drop excluded generated ones by label."""
    pairs = [p for p in palette["pairings"] if p["label"] not in set(excluded)]
    for c in custom:
        fg, bg = bl.normalize_hex(c["fg"]), bl.normalize_hex(c["bg"])
        use = c.get("use", "body")
        ratio = bl.contrast_ratio(fg, bg)
        pairs.append({"fg": fg, "bg": bg, "fgToken": c.get("fgToken", fg), "bgToken": c.get("bgToken", bg),
                      "use": use, "label": c.get("label", f"{fg} on {bg}"), "ratio": round(ratio, 2),
                      "required": bl.THRESHOLDS[use], "pass": ratio >= bl.THRESHOLDS[use],
                      "rating": bl.rating_label(ratio), "custom": True})
    palette["pairings"] = pairs
    palette["customPairings"] = custom
    palette["excludedPairings"] = excluded


def merge_into_brand(brand_path: Path, palette: dict):
    brand = json.loads(brand_path.read_text())
    old = brand.get("color", {})
    old_by_id = {c["id"]: c for c in old.get("brand", [])}
    for c in palette["brand"]:
        for k, v in old_by_id.get(c["id"], {}).items():
            if k not in GENERATED_KEYS:
                c[k] = v  # Keep manual additions such as pantone or usage notes.
    if old.get("proportions") and set(old["proportions"]) <= {c["id"] for c in palette["brand"]} | {"neutral"}:
        palette["proportions"] = old["proportions"]
    apply_custom_pairings(palette, old.get("customPairings", []), old.get("excludedPairings", []))
    brand["color"] = palette
    acc = palette["brand"][0]["accessible"]
    brand.setdefault("focus", {})
    if acc.get("textOnLight"):
        brand["focus"]["colorOnLight"] = acc["textOnLight"]["hex"]
    if acc.get("textOnDark"):
        brand["focus"]["colorOnDark"] = acc["textOnDark"]["hex"]
    brand["focus"]["onBrand"] = focus_on_brand(palette)
    brand_path.write_text(json.dumps(brand, indent=2, ensure_ascii=False) + "\n")


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--seed", action="append", required=True, help="HEX[:ROLE[:NAME]], repeatable; first is primary")
    ap.add_argument("--neutral-chroma", type=float, default=0.012, help="Tint strength of the neutral scale (0 = pure grey)")
    ap.add_argument("--out", type=Path)
    ap.add_argument("--brand", type=Path, help="Update the 'color' section of this brand.json in place")
    args = ap.parse_args(argv)
    try:
        result = build(args.seed, args.neutral_chroma)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    if args.brand:
        merge_into_brand(args.brand, result)
    text = json.dumps(result, indent=2, ensure_ascii=False)
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(text + "\n")
    print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
