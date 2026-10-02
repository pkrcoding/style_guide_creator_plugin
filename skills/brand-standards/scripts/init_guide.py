#!/usr/bin/env python3
"""Scaffold a style-guide workspace from a logo.

Creates:
  <out>/brand.json            single source of truth (palette, type, spacing, motion, social...)
  <out>/analysis/logo.json    logo analysis
  <out>/analysis/palette.json full palette build
  <out>/assets/source/        copies of the supplied logo (and symbol)
  <out>/content/NN-*.md       one skeleton per chapter with TODO( ) markers and data placeholders

Re-running never overwrites existing content/*.md files or brand.json unless --force is given,
so it is safe to resume.

Usage:
    init_guide.py --logo logo.svg --name "Northwind Labs" [--symbol mark.svg] [--out brand-guide]
                  [--seed "#hex:role:Name" ...] [--locale en-GB] [--platforms instagram,linkedin]
                  [--display-font "Name"] [--body-font "Name"] [--target "WCAG 2.2 AA"]
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import analyze_logo  # noqa: E402
import brandlib as bl  # noqa: E402
import build_palette  # noqa: E402
from guide_spec import CHAPTERS, TODO_MARKER  # noqa: E402

SYSTEM_SANS = "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
SYSTEM_MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"


def analyse(path: Path) -> dict:
    data: dict = {"file": str(path), "format": path.suffix.lower().lstrip(".")}
    if data["format"] == "svg":
        analyze_logo.analyse_svg(path, data)
    else:
        analyze_logo.analyse_raster(path, data)
    data["recommendations"] = analyze_logo.recommendations(data)
    return data


def default_seeds(analysis: dict) -> list[str]:
    colours = analysis.get("colours", [])
    chromatic = [c for c in colours if not c["isNeutral"]]
    neutrals = [c for c in colours if c["isNeutral"]]
    seeds = []
    roles = ["primary", "secondary", "accent"]
    for c in chromatic[:3]:
        seeds.append(f"{c['hex']}:{roles[len(seeds)]}:{c['name'].title()}")
    # A dark neutral used in the logo (e.g. navy/charcoal wordmark) becomes secondary when room.
    if len(seeds) < 2:
        for c in neutrals:
            if c["onWhite"]["ratio"] >= 7 and not c["hex"] in ("#000000",):
                seeds.append(f"{c['hex']}:{roles[len(seeds)]}:{c['name'].title()}")
                break
    if not seeds:
        seeds.append(f"{colours[0]['hex'] if colours else '#1f2937'}:primary:Primary")
    return seeds


def type_scale(base: int = 16):
    return [
        {"token": "display", "sizePx": 60, "lineHeight": 1.1, "weight": 700, "letterSpacing": "-0.02em", "family": "display", "usage": "Campaign headlines, hero banners (one per page)"},
        {"token": "h1", "sizePx": 48, "lineHeight": 1.15, "weight": 700, "letterSpacing": "-0.015em", "family": "display", "usage": "Page titles"},
        {"token": "h2", "sizePx": 36, "lineHeight": 1.2, "weight": 700, "letterSpacing": "-0.01em", "family": "display", "usage": "Section titles"},
        {"token": "h3", "sizePx": 28, "lineHeight": 1.25, "weight": 600, "letterSpacing": "0", "family": "display", "usage": "Sub-sections"},
        {"token": "h4", "sizePx": 22, "lineHeight": 1.3, "weight": 600, "letterSpacing": "0", "family": "body", "usage": "Card and component titles"},
        {"token": "body-lg", "sizePx": 20, "lineHeight": 1.5, "weight": 400, "letterSpacing": "0", "family": "body", "usage": "Introductions and lead paragraphs"},
        {"token": "body", "sizePx": base, "lineHeight": 1.5, "weight": 400, "letterSpacing": "0", "family": "body", "usage": "Default body text (never smaller on screen)"},
        {"token": "small", "sizePx": 14, "lineHeight": 1.5, "weight": 400, "letterSpacing": "0.01em", "family": "body", "usage": "Captions, metadata, legal (not for long passages)"},
        {"token": "label", "sizePx": 14, "lineHeight": 1.4, "weight": 600, "letterSpacing": "0.02em", "family": "body", "usage": "Buttons, form labels, tags"},
        {"token": "code", "sizePx": 15, "lineHeight": 1.5, "weight": 400, "letterSpacing": "0", "family": "mono", "usage": "Code, data, reference numbers"},
    ]


def build_brand(args, analysis, palette, logo_rel, symbol_rel):
    today = dt.date.today().isoformat()
    primary = palette["brand"][0]
    # Focus rings use the 4.5:1 steps (not the 3:1 minimum) so they stay visible next to tinted surfaces.
    focus = primary["accessible"]["textOnLight"] or {"hex": palette["neutral"]["scale"]["900"]}
    focus_dark = primary["accessible"]["textOnDark"] or {"hex": "#ffffff"}
    rec = analysis["recommendations"]
    assumptions = [
        "Brand colours were extracted from the logo; confirm exact values against the master artwork or existing specifications.",
        "CMYK values are mathematical conversions; confirm with your printer and choose Pantone matches from a physical swatch book.",
        "Social platform specifications were last reviewed on the date in the social chapter; verify before production.",
    ]
    if not args.display_font:
        assumptions.append("Typefaces are defaults pending a typography decision; replace with the organisation's licensed fonts if they exist.")
    return {
        "$schema": "style-guide-creator/brand@1",
        "meta": {
            "name": args.name,
            "slug": bl.slugify(args.name),
            "version": "1.0.0",
            "lastUpdated": today,
            "owner": args.owner or "Brand and Marketing team",
            "contact": args.contact or "TODO(contact email for brand questions)",
            "accessibilityTarget": args.target,
            "locale": args.locale,
            "languages": [args.locale],
            "reviewCadence": "Every 12 months, and after any rebrand or platform change",
            "assumptions": assumptions,
        },
        "foundations": {
            "mission": "", "vision": "", "values": [], "positioning": "", "personality": [],
            "audiences": [], "tagline": "", "boilerplate": {"short": "", "medium": "", "long": ""},
            "industry": args.industry or "",
        },
        "logo": {
            "master": logo_rel,
            "symbol": symbol_rel,
            "type": "",
            "description": "",
            "altText": f"{args.name} logo",
            "orientation": analysis.get("orientation"),
            "aspectRatio": analysis.get("contentAspectRatio"),
            "clearSpace": {"fraction": 0.25, "rule": "Keep clear space equal to 25% of the logo's height on all sides (refine to a named element of the logo, e.g. the height of the symbol)."},
            "minSize": {"digitalPx": rec["suggestedMinSize"]["digitalWidthPx"],
                        "printMm": rec["suggestedMinSize"]["printWidthMm"],
                        "symbolDigitalPx": 24, "symbolPrintMm": 8},
            "monoStyle": "auto",
            "fullColourExceptions": [],
            "misuse": [],
            "analysis": "analysis/logo.json",
        },
        "color": palette,
        "typography": {
            "families": [
                {"role": "display", "name": args.display_font or "Inter", "fallback": SYSTEM_SANS,
                 "source": "Google Fonts" if not args.display_font else "", "license": "SIL Open Font License 1.1" if not args.display_font else "",
                 "url": "https://fonts.google.com/specimen/Inter" if not args.display_font else "", "weights": [400, 600, 700]},
                {"role": "body", "name": args.body_font or args.display_font or "Inter", "fallback": SYSTEM_SANS,
                 "source": "Google Fonts" if not (args.body_font or args.display_font) else "", "license": "SIL Open Font License 1.1" if not (args.body_font or args.display_font) else "",
                 "url": "https://fonts.google.com/specimen/Inter" if not (args.body_font or args.display_font) else "", "weights": [400, 600, 700]},
                {"role": "mono", "name": "JetBrains Mono", "fallback": SYSTEM_MONO, "source": "Google Fonts",
                 "license": "SIL Open Font License 1.1", "url": "https://fonts.google.com/specimen/JetBrains+Mono", "weights": [400, 600]},
            ],
            "baseSizePx": 16,
            "scaleRatio": "1.25 (major third), rounded",
            "measure": "45-75 characters per line (aim for 66)",
            "scale": type_scale(),
        },
        "spacing": {"basePx": 4, "scale": {"0": 0, "1": 4, "2": 8, "3": 12, "4": 16, "5": 24, "6": 32, "7": 40, "8": 48, "9": 64, "10": 80, "11": 96, "12": 128}},
        "grid": {
            "maxContentWidthPx": 1280,
            "breakpoints": [
                {"id": "mobile", "minPx": 0, "columns": 4, "gutterPx": 16, "marginPx": 16},
                {"id": "tablet", "minPx": 768, "columns": 8, "gutterPx": 24, "marginPx": 32},
                {"id": "desktop", "minPx": 1024, "columns": 12, "gutterPx": 24, "marginPx": 48},
                {"id": "wide", "minPx": 1440, "columns": 12, "gutterPx": 32, "marginPx": 80},
            ],
        },
        "radius": {"none": 0, "sm": 4, "md": 8, "lg": 12, "xl": 24, "pill": 9999},
        "elevation": {
            "0": "none",
            "1": "0 1px 2px rgb(0 0 0 / 0.08), 0 1px 1px rgb(0 0 0 / 0.04)",
            "2": "0 4px 8px rgb(0 0 0 / 0.08), 0 2px 4px rgb(0 0 0 / 0.04)",
            "3": "0 12px 24px rgb(0 0 0 / 0.10), 0 4px 8px rgb(0 0 0 / 0.05)",
        },
        "motion": {
            "durations": {"instant": "0ms", "fast": "120ms", "base": "200ms", "slow": "320ms", "deliberate": "500ms"},
            "easing": {"standard": "cubic-bezier(0.2, 0, 0, 1)", "enter": "cubic-bezier(0, 0, 0, 1)", "exit": "cubic-bezier(0.3, 0, 1, 1)"},
            "reducedMotion": "When prefers-reduced-motion is set, replace movement with fades of 120ms or less, and stop parallax, auto-advancing carousels and looping animation.",
        },
        "focus": {"colorOnLight": focus["hex"], "colorOnDark": focus_dark["hex"], "widthPx": 3, "offsetPx": 2, "style": "solid",
                  "onBrand": build_palette.focus_on_brand(palette)},
        "social": {
            "handles": {},
            "platforms": args.platforms.split(",") if args.platforms else ["instagram", "facebook", "linkedin", "x", "youtube", "tiktok", "web"],
            "avatarBackground": "primary",
            "coverBackground": "primary",
            "hashtags": {"brand": [], "campaign": []},
            "contentPillars": [],
        },
        "content": {"dir": "content"},
    }


def chapter_skeleton(stem, title, owner, placeholders, brief):
    body = [f"# {title}", "", f"<!-- Owner skill: {owner}. Brief: {brief} -->", "",
            f"{TODO_MARKER}{brief})", ""]
    for p in placeholders:
        body += [p, ""]
    return "\n".join(body)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--logo", type=Path, required=True)
    ap.add_argument("--name", required=True, help="Organisation name as it should appear in the guide")
    ap.add_argument("--symbol", type=Path, help="Optional symbol/monogram for avatars and favicons")
    ap.add_argument("--out", type=Path, default=Path("brand-guide"))
    ap.add_argument("--seed", action="append", help="Override colours: HEX[:ROLE[:NAME]] (first = primary)")
    ap.add_argument("--locale", default="en-GB")
    ap.add_argument("--target", default="WCAG 2.2 AA")
    ap.add_argument("--platforms")
    ap.add_argument("--display-font")
    ap.add_argument("--body-font")
    ap.add_argument("--industry")
    ap.add_argument("--owner")
    ap.add_argument("--contact")
    ap.add_argument("--force", action="store_true", help="Overwrite brand.json and chapter files")
    args = ap.parse_args(argv)

    if not args.logo.exists():
        print(f"error: logo {args.logo} not found", file=sys.stderr)
        return 2
    out = args.out
    for d in ("analysis", "assets/source", "content"):
        (out / d).mkdir(parents=True, exist_ok=True)
    logo_dest = out / "assets" / "source" / f"logo{args.logo.suffix.lower()}"
    if args.logo.resolve() != logo_dest.resolve():
        shutil.copyfile(args.logo, logo_dest)
    symbol_rel = None
    if args.symbol:
        sym_dest = out / "assets" / "source" / f"symbol{args.symbol.suffix.lower()}"
        if args.symbol.resolve() != sym_dest.resolve():
            shutil.copyfile(args.symbol, sym_dest)
        symbol_rel = str(sym_dest.relative_to(out))

    try:
        analysis = analyse(logo_dest)
    except bl.ImageError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    analysis["file"] = str(logo_dest.relative_to(out))  # Relative: no local usernames or temp paths in outputs.
    (out / "analysis" / "logo.json").write_text(json.dumps(analysis, indent=2) + "\n")
    seeds = args.seed or default_seeds(analysis)
    palette = build_palette.build(seeds)
    (out / "analysis" / "palette.json").write_text(json.dumps(palette, indent=2, ensure_ascii=False) + "\n")

    brand_path = out / "brand.json"
    if brand_path.exists() and not args.force:
        print(f"note: {brand_path} exists; left unchanged (use --force to regenerate)", file=sys.stderr)
    else:
        brand = build_brand(args, analysis, palette, str(logo_dest.relative_to(out)), symbol_rel)
        brand_path.write_text(json.dumps(brand, indent=2, ensure_ascii=False) + "\n")

    created = []
    for stem, title, owner, placeholders, brief in CHAPTERS:
        path = out / "content" / f"{stem}.md"
        if path.exists() and not args.force:
            continue
        path.write_text(chapter_skeleton(stem, title, owner, placeholders, brief), encoding="utf-8")
        created.append(path.name)

    summary = {
        "workspace": str(out),
        "brand": str(brand_path),
        "seeds": seeds,
        "orientation": analysis.get("orientation"),
        "logoColours": [c["hex"] for c in analysis.get("colours", [])],
        "recommendations": analysis["recommendations"],
        "paletteNotes": palette["notes"],
        "chaptersCreated": created,
    }
    print(json.dumps(summary, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
