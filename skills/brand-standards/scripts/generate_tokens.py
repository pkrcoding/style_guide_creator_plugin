#!/usr/bin/env python3
"""Export design tokens from brand.json.

Writes to <guide>/tokens/:
  tokens.json          W3C Design Tokens Community Group format ($type/$value)
  tokens.css           CSS custom properties, with light and dark semantic themes
  _tokens.scss         Sass variables
  tailwind.preset.js   Tailwind CSS v3 preset (theme.extend)
  tailwind-theme.css   Tailwind CSS v4 @theme block

Semantic aliases (text, surface, border, focus, link, state colours) are chosen so
every text alias meets WCAG 2.2 AA (4.5:1) and every border/focus alias meets 3:1
on its surface, in both light and dark themes.

Usage:
    generate_tokens.py path/to/brand.json
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import brandlib as bl  # noqa: E402
from build_palette import first_step  # noqa: E402


def semantic_aliases(brand: dict) -> dict:
    """Return {"light": {...}, "dark": {...}} semantic colour aliases as hex values."""
    c = brand["color"]
    n = c["neutral"]["scale"]
    dark = c.get("surfaces", {}).get("dark", n["950"])
    primary = c["brand"][0]
    acc = primary["accessible"]
    focus = brand.get("focus", {})

    def pick(found, fallback):
        return found["hex"] if found else fallback

    light = {
        "text-default": n["900"] if bl.contrast_ratio(n["900"], "#ffffff") >= 7.0 else pick(first_step(n, "#ffffff", 7.0), n["950"]),
        "text-muted": pick(first_step(n, "#ffffff", 4.5), n["700"]),
        "text-inverse": n["50"],
        "text-link": pick(acc.get("textOnLight"), n["900"]),
        "text-on-brand": "#ffffff",
        "surface-default": "#ffffff",
        "surface-subtle": n["50"],
        "surface-inverse": dark,
        "surface-brand": pick(acc.get("solidWithWhiteText"), n["900"]),
        "border-subtle": n["200"],
        "border-strong": pick(first_step(n, "#ffffff", 3.0), n["500"]),
        "focus": focus.get("colorOnLight") or pick(acc.get("uiOnLight"), n["900"]),
        "focus-on-brand": focus.get("onBrand", {}).get(primary["id"], {}).get("focus", "#ffffff"),
    }
    dark_set = {
        "text-default": n["50"],
        "text-muted": pick(first_step(n, dark, 4.5, from_light=False), n["300"]),
        "text-inverse": n["900"],
        "text-link": pick(acc.get("textOnDark"), n["50"]),
        "text-on-brand": "#ffffff",
        "surface-default": dark,
        "surface-subtle": n["900"],
        "surface-inverse": n["50"],
        "surface-brand": pick(acc.get("solidWithWhiteText"), n["800"]),
        "border-subtle": n["800"],
        "border-strong": pick(first_step(n, dark, 3.0, from_light=False), n["500"]),
        "focus": focus.get("colorOnDark") or pick(acc.get("uiOnDark"), n["50"]),
        "focus-on-brand": focus.get("onBrand", {}).get(primary["id"], {}).get("focus", "#ffffff"),
    }
    # One focus colour per brand surface: e.g. white inside dark teal, near-black inside coral.
    for cid, spec in focus.get("onBrand", {}).items():
        light[f"focus-on-{cid}"] = spec["focus"]
        dark_set[f"focus-on-{cid}"] = spec["focus"]
    for s in c.get("semantic", []):
        t = s["tokens"]
        light[f"{s['id']}-fg"] = pick(t.get("fg"), n["900"])
        light[f"{s['id']}-bg"] = t["bg"]["hex"]
        light[f"{s['id']}-border"] = pick(t.get("border"), n["500"])
        dark_set[f"{s['id']}-fg"] = pick(t.get("fgOnDark"), n["50"])
        dark_set[f"{s['id']}-bg"] = s["scale"]["950"]
        dark_set[f"{s['id']}-border"] = pick(t.get("fgOnDark"), n["400"])
    return {"light": light, "dark": dark_set}


def collect(brand: dict) -> dict:
    """Flatten brand.json into {group: {name: (type, value)}}."""
    c = brand["color"]
    colours: dict = {"white": "#ffffff", "black": "#000000"}
    for b in c["brand"]:
        colours[b["id"]] = b["hex"]
        for step, hx in b["scale"].items():
            colours[f"{b['id']}-{step}"] = hx
    for step, hx in c["neutral"]["scale"].items():
        colours[f"neutral-{step}"] = hx
    for s in c.get("semantic", []):
        for step, hx in s["scale"].items():
            colours[f"{s['id']}-{step}"] = hx
    t = brand["typography"]
    fams = {f["role"]: f"'{f['name']}', {f['fallback']}" if f.get("name") else f["fallback"] for f in t["families"]}
    return {
        "colours": colours,
        "semantic": semantic_aliases(brand),
        "fontFamily": fams,
        "type": t["scale"],
        "space": {k: v for k, v in brand["spacing"]["scale"].items()},
        "radius": brand.get("radius", {}),
        "shadow": brand.get("elevation", {}),
        "duration": brand.get("motion", {}).get("durations", {}),
        "easing": brand.get("motion", {}).get("easing", {}),
        "breakpoints": {bp["id"]: bp["minPx"] for bp in brand.get("grid", {}).get("breakpoints", [])},
        "focus": brand.get("focus", {}),
    }


def px(v):
    return f"{v}px" if isinstance(v, (int, float)) and v != 0 else str(v) if not isinstance(v, (int, float)) else "0"


def to_dtcg(d: dict) -> dict:
    out: dict = {"color": {}, "semantic": {"light": {}, "dark": {}}, "font": {"family": {}}, "type": {},
                 "space": {}, "radius": {}, "shadow": {}, "motion": {"duration": {}, "easing": {}}, "breakpoint": {}}
    for k, v in d["colours"].items():
        out["color"][k] = {"$type": "color", "$value": v}
    for theme in ("light", "dark"):
        for k, v in d["semantic"][theme].items():
            out["semantic"][theme][k] = {"$type": "color", "$value": v}
    for k, v in d["fontFamily"].items():
        out["font"]["family"][k] = {"$type": "fontFamily", "$value": v}
    for t in d["type"]:
        out["type"][t["token"]] = {"$type": "typography", "$value": {
            "fontFamily": f"{{font.family.{t['family']}}}", "fontSize": f"{t['sizePx'] / 16:g}rem",
            "fontWeight": t["weight"], "lineHeight": t["lineHeight"], "letterSpacing": t["letterSpacing"]},
            "$description": t.get("usage", "")}
    for k, v in d["space"].items():
        out["space"][k] = {"$type": "dimension", "$value": px(v)}
    for k, v in d["radius"].items():
        out["radius"][k] = {"$type": "dimension", "$value": px(v)}
    for k, v in d["shadow"].items():
        out["shadow"][k] = {"$type": "shadow", "$value": v}
    for k, v in d["duration"].items():
        out["motion"]["duration"][k] = {"$type": "duration", "$value": v}
    for k, v in d["easing"].items():
        out["motion"]["easing"][k] = {"$type": "cubicBezier", "$value": v}
    for k, v in d["breakpoints"].items():
        out["breakpoint"][k] = {"$type": "dimension", "$value": px(v)}
    return out


def css_vars(d: dict) -> list[str]:
    lines = [f"  --color-{k}: {v};" for k, v in d["colours"].items()]
    lines += [f"  --font-{k}: {v};" for k, v in d["fontFamily"].items()]
    for t in d["type"]:
        lines.append(f"  --text-{t['token']}: {t['sizePx'] / 16:g}rem;")
        lines.append(f"  --leading-{t['token']}: {t['lineHeight']};")
        lines.append(f"  --weight-{t['token']}: {t['weight']};")
        lines.append(f"  --tracking-{t['token']}: {t['letterSpacing']};")
    lines += [f"  --space-{k}: {px(v)};" for k, v in d["space"].items()]
    lines += [f"  --radius-{k}: {px(v)};" for k, v in d["radius"].items()]
    lines += [f"  --shadow-{k}: {v};" for k, v in d["shadow"].items()]
    lines += [f"  --duration-{k}: {v};" for k, v in d["duration"].items()]
    lines += [f"  --ease-{k}: {v};" for k, v in d["easing"].items()]
    f = d["focus"]
    lines += [f"  --focus-width: {f.get('widthPx', 3)}px;", f"  --focus-offset: {f.get('offsetPx', 2)}px;"]
    return lines


def css_file(d: dict) -> str:
    sem = d["semantic"]
    surface_rules = "\n".join(
        f'[data-surface="{k[len("focus-on-"):]}"] :focus-visible {{ outline-color: var(--{k}); }}'
        for k in sem["light"] if k.startswith("focus-on-") and k != "focus-on-brand")
    light = "\n".join(f"  --{k}: {v};" for k, v in sem["light"].items())
    dark = "\n".join(f"  --{k}: {v};" for k, v in sem["dark"].items())
    return f"""/* Generated by style-guide-creator from brand.json. Do not edit by hand. */
:root {{
{chr(10).join(css_vars(d))}
}}

/* Semantic colours: light theme (default) */
:root, [data-theme="light"] {{
{light}
}}

/* Semantic colours: dark theme */
@media (prefers-color-scheme: dark) {{
  :root:not([data-theme="light"]) {{
{chr(10).join('  ' + l for l in dark.splitlines())}
  }}
}}
[data-theme="dark"] {{
{dark}
}}

/* Accessible defaults */
:focus-visible {{
  outline: var(--focus-width) solid var(--focus);
  outline-offset: var(--focus-offset);
}}
/* Inside brand-coloured sections, the ring switches to a colour that contrasts with the fill */
.surface-brand :focus-visible, [data-surface="brand"] :focus-visible {{
  outline-color: var(--focus-on-brand);
}}
{surface_rules}
@media (prefers-reduced-motion: reduce) {{
  *, *::before, *::after {{
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }}
}}
"""


def scss_file(d: dict) -> str:
    out = ["// Generated by style-guide-creator from brand.json. Do not edit by hand."]
    for line in css_vars(d):
        name, value = line.strip().rstrip(";").split(": ", 1)
        out.append(f"${name[2:]}: {value};")
    for theme in ("light", "dark"):
        for k, v in d["semantic"][theme].items():
            out.append(f"${theme}-{k}: {v};")
    return "\n".join(out) + "\n"


def tailwind_v3(d: dict) -> str:
    colours: dict = {}
    for k, v in d["colours"].items():
        if "-" in k and k.rsplit("-", 1)[1].isdigit():
            group, step = k.rsplit("-", 1)
            colours.setdefault(group, {})[step] = v
        elif k in ("white", "black"):
            continue
        else:
            colours.setdefault(k, {})["DEFAULT"] = v
    for k in d["semantic"]["light"]:
        colours[k] = f"var(--{k})"
    preset = {
        "theme": {"extend": {
            "colors": colours,
            "fontFamily": {k: [v] for k, v in d["fontFamily"].items()},
            "fontSize": {t["token"]: [f"{t['sizePx'] / 16:g}rem", {"lineHeight": str(t["lineHeight"]),
                         "letterSpacing": t["letterSpacing"], "fontWeight": str(t["weight"])}] for t in d["type"]},
            "spacing": {k: px(v) for k, v in d["space"].items()},
            "borderRadius": {k: px(v) for k, v in d["radius"].items()},
            "boxShadow": {k: v for k, v in d["shadow"].items()},
            "transitionDuration": {k: v for k, v in d["duration"].items()},
            "transitionTimingFunction": {k: v for k, v in d["easing"].items()},
            "screens": {k: px(v) for k, v in d["breakpoints"].items() if v},
        }},
    }
    return ("// Generated by style-guide-creator. Tailwind CSS v3 preset: presets: [require('./tailwind.preset.js')]\n"
            "// Semantic colours read CSS variables, so also include tokens.css.\n"
            f"module.exports = {json.dumps(preset, indent=2)};\n")


def tailwind_v4(d: dict) -> str:
    lines = ["/* Generated by style-guide-creator. Tailwind CSS v4: @import \"./tailwind-theme.css\"; */", "@theme {"]
    lines += [f"  --color-{k}: {v};" for k, v in d["colours"].items()]
    lines += [f"  --font-{k}: {v};" for k, v in d["fontFamily"].items()]
    for t in d["type"]:
        lines.append(f"  --text-{t['token']}: {t['sizePx'] / 16:g}rem;")
        lines.append(f"  --text-{t['token']}--line-height: {t['lineHeight']};")
    lines += [f"  --radius-{k}: {px(v)};" for k, v in d["radius"].items()]
    lines += [f"  --shadow-{k}: {v};" for k, v in d["shadow"].items() if v != "none"]
    lines += [f"  --ease-{k}: {v};" for k, v in d["easing"].items()]
    lines += [f"  --breakpoint-{k}: {px(v)};" for k, v in d["breakpoints"].items() if v]
    lines.append("}")
    return "\n".join(lines) + "\n"


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("brand", type=Path)
    args = ap.parse_args(argv)
    brand = json.loads(args.brand.read_text())
    d = collect(brand)
    out = args.brand.parent / "tokens"
    out.mkdir(exist_ok=True)
    files = {
        "tokens.json": json.dumps(to_dtcg(d), indent=2) + "\n",
        "tokens.css": css_file(d),
        "_tokens.scss": scss_file(d),
        "tailwind.preset.js": tailwind_v3(d),
        "tailwind-theme.css": tailwind_v4(d),
    }
    for name, text in files.items():
        (out / name).write_text(text, encoding="utf-8")
    # Self-check: every semantic text alias must meet 4.5:1 and borders/focus 3:1 on their surface.
    problems = []
    for theme, surface_key in (("light", "surface-default"), ("dark", "surface-default")):
        sem = d["semantic"][theme]
        surface = sem[surface_key]
        for k, v in sem.items():
            need = 4.5 if k.startswith("text-") and k not in ("text-inverse", "text-on-brand") else 3.0 if k in ("border-strong", "focus") else None
            if need and bl.contrast_ratio(v, surface) < need:
                problems.append(f"{theme}: {k} {v} on {surface} = {bl.contrast_ratio(v, surface):.2f}:1 (needs {need})")
    print(json.dumps({"written": [str(out / f) for f in files], "problems": problems}, indent=2))
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
