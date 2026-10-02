#!/usr/bin/env python3
"""Quality gate for a generated style guide. Exit 1 if any error is found.

Checks:
  brand.json   required fields; every colour pairing recomputed against WCAG 2.2
               thresholds; focus indicator contrast; semantic token contrast in
               light and dark themes; body text size and line height; font licences.
  content/     every chapter present; no TODO( ) markers; known placeholders only;
               image alt text; heading order; descriptive link text; thin chapters.
  assets/      manifest present; asset warnings surfaced; platform specs freshness.
  HTML         lang, title, skip link, alt attributes, single h1, heading order,
               duplicate ids, stale output.
  audit        analysis/accessibility-audit.md saved, with no open Critical/Serious rows.

Writes analysis/validation-report.md and prints a JSON summary.

Usage:
    validate_brand.py path/to/brand.json
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import brandlib as bl  # noqa: E402
import generate_tokens  # noqa: E402
from guide_spec import CHAPTER_STEMS, CHAPTERS, PLACEHOLDERS, TODO_MARKER  # noqa: E402

PLATFORMS_FILE = HERE.parent.parent / "social-media-kit" / "references" / "social-platforms.json"
VAGUE_LINKS = {"here", "click here", "read more", "more", "link", "this", "this link", "learn more"}
MIN_WORDS = 80


class Report:
    def __init__(self):
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self.passes: list[str] = []

    def error(self, msg):
        self.errors.append(msg)

    def warn(self, msg):
        self.warnings.append(msg)

    def ok(self, msg):
        self.passes.append(msg)


def get(d, path, default=None):
    for key in path.split("."):
        if not isinstance(d, dict) or key not in d:
            return default
        d = d[key]
    return d


def check_brand(brand: dict, root: Path, r: Report):
    for path in ("meta.name", "meta.version", "meta.lastUpdated", "meta.accessibilityTarget", "meta.contact",
                 "logo.master", "logo.altText", "logo.clearSpace.rule", "logo.minSize.digitalPx"):
        v = get(brand, path)
        if v in (None, "", []):
            r.error(f"brand.json: '{path}' is missing")
        elif isinstance(v, str) and TODO_MARKER in v:
            r.error(f"brand.json: '{path}' still contains a TODO marker")
    master = get(brand, "logo.master")
    if master and not (root / master).exists():
        r.error(f"brand.json: logo.master file '{master}' not found")
    alt = (get(brand, "logo.altText") or "").strip().lower()
    if alt in ("logo", "image", "img", "picture"):
        r.error("brand.json: logo.altText must name the organisation (e.g. 'Acme logo')")

    colours = get(brand, "color.brand") or []
    if not colours:
        r.error("brand.json: color.brand is empty")
    for c in colours:
        try:
            bl.normalize_hex(c["hex"])
        except (KeyError, ValueError):
            r.error(f"brand.json: invalid colour {c}")

    # Pairings: recompute from hex values, never trust stored ratios.
    pairings = get(brand, "color.pairings") or []
    if not pairings:
        r.error("brand.json: color.pairings is empty; approved colour combinations are required")
    failed = 0
    for p in pairings:
        need = bl.THRESHOLDS.get(p.get("use"), 4.5)
        ratio = bl.contrast_ratio(p["fg"], p["bg"])
        if ratio < need:
            failed += 1
            r.error(f"Contrast: '{p.get('label')}' {p['fg']} on {p['bg']} is {ratio:.2f}:1, needs {need}:1 for '{p.get('use')}'")
    if pairings and not failed:
        r.ok(f"All {len(pairings)} colour pairings meet their WCAG 2.2 thresholds")

    # Focus indicator.
    sem = generate_tokens.semantic_aliases(brand)
    for theme, key in (("light", "colorOnLight"), ("dark", "colorOnDark")):
        colour = get(brand, f"focus.{key}")
        surface = sem[theme]["surface-default"]
        if not colour:
            r.error(f"brand.json: focus.{key} missing")
        elif bl.contrast_ratio(colour, surface) < 3.0:
            r.error(f"Focus: {theme} focus colour {colour} is {bl.contrast_ratio(colour, surface):.2f}:1 on {surface}; needs 3:1 (SC 1.4.11)")
    on_brand = get(brand, "focus.onBrand") or {}
    if not on_brand:
        r.warn("Focus: focus.onBrand missing; rebuild with build_palette.py --brand to get focus colours for brand-coloured sections")
    for cid, spec in on_brand.items():
        for surface in spec.get("surfaces", []):
            ratio = bl.contrast_ratio(spec["focus"], surface)
            if ratio < 3.0:
                r.error(f"Focus: on '{cid}' surfaces the focus colour {spec['focus']} is {ratio:.2f}:1 on {surface}; needs 3:1")
    if (get(brand, "focus.widthPx") or 0) < 2:
        r.error("Focus: focus.widthPx must be at least 2")

    # Semantic tokens in both themes.
    sem_fail = 0
    for theme in ("light", "dark"):
        s = sem[theme]
        for k, v in s.items():
            if k.startswith("focus-on-") and k != "focus-on-brand":
                continue  # Checked per brand surface via focus.onBrand above.
            need = 4.5 if k in ("text-default", "text-muted", "text-link") or k.endswith("-fg") else 3.0 if k in ("border-strong", "focus", "focus-on-brand") else None
            bg = s["surface-brand"] if k == "focus-on-brand" else s[k.replace("-fg", "-bg")] if k.endswith("-fg") else s["surface-default"]
            if need and bl.contrast_ratio(v, bg) < need:
                sem_fail += 1
                r.error(f"Tokens ({theme}): {k} {v} on {bg} is {bl.contrast_ratio(v, bg):.2f}:1, needs {need}:1")
    if not sem_fail:
        r.ok("Semantic text, link, border and focus tokens pass in light and dark themes")

    # Typography.
    fams = {f.get("role"): f for f in get(brand, "typography.families") or []}
    for role in ("display", "body"):
        if role not in fams:
            r.error(f"Typography: no '{role}' family defined")
    for f in fams.values():
        if not f.get("fallback"):
            r.error(f"Typography: '{f.get('name')}' has no fallback font stack")
        if not f.get("license"):
            r.warn(f"Typography: licence for '{f.get('name')}' not recorded; confirm it covers web, print, apps and social use")
    scale = {t["token"]: t for t in get(brand, "typography.scale") or []}
    body = scale.get("body")
    if not body:
        r.error("Typography: no 'body' token in the type scale")
    else:
        if body["sizePx"] < 16:
            r.error(f"Typography: body text is {body['sizePx']}px; use at least 16px on screen")
        if body["lineHeight"] < 1.5:
            r.error(f"Typography: body line height is {body['lineHeight']}; use at least 1.5")
    for t in scale.values():
        if t["sizePx"] < 12:
            r.error(f"Typography: '{t['token']}' is {t['sizePx']}px; nothing below 12px")
        elif t["sizePx"] < 14:
            r.warn(f"Typography: '{t['token']}' is {t['sizePx']}px; keep to non-essential text")

    cvd = get(brand, "color.cvd") or []
    if cvd:
        r.warn(f"Colour vision: {len(cvd)} colour pair(s) may be confused; the colour chapter must say how meaning is also shown (labels, icons, patterns)")
    if not get(brand, "social.platforms"):
        r.warn("Social: no platforms listed in social.platforms")


def check_content(brand: dict, root: Path, r: Report):
    cdir = root / get(brand, "content.dir", "content")
    expected = {stem: (title, placeholders) for stem, title, _, placeholders, _ in CHAPTERS}
    for stem in CHAPTER_STEMS:
        if not (cdir / f"{stem}.md").exists():
            r.error(f"Content: chapter {stem}.md is missing")
    for path in sorted(cdir.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        name = path.name
        if TODO_MARKER in text:
            r.error(f"Content: {name} still has {text.count(TODO_MARKER)} TODO( ) marker(s)")
        for ph in re.findall(r"\{\{[^}]+\}\}", text):
            if ph not in PLACEHOLDERS:
                r.error(f"Content: {name} uses unknown placeholder {ph}")
        if path.stem in expected:
            for ph in expected[path.stem][1]:
                if ph not in text:
                    r.warn(f"Content: {name} no longer includes {ph}")
        for alt in re.findall(r"!\[([^\]]*)\]\(", text):
            if not alt.strip():
                r.error(f"Content: {name} has an image with empty alt text (use descriptive alt, or mark decorative images in HTML)")
        prev = 0
        for line in re.sub(r"```.*?```", "", text, flags=re.S).splitlines():
            m = re.match(r"^(#{1,6})\s", line)
            if m:
                level = len(m.group(1))
                if prev and level > prev + 1:
                    r.error(f"Content: {name} skips a heading level ('{line.strip()}')")
                prev = level
        for label in re.findall(r"(?<!!)\[([^\]]+)\]\(", text):
            if label.strip().lower() in VAGUE_LINKS:
                r.warn(f"Content: {name} has non-descriptive link text '{label}'")
        prose = re.sub(r"<!--.*?-->|\{\{[^}]+\}\}|```.*?```", "", text, flags=re.S)
        words = len(re.findall(r"\b\w+\b", prose))
        if words < MIN_WORDS and TODO_MARKER not in text:
            r.warn(f"Content: {name} has only {words} words; check it covers its brief")
        for caps in re.findall(r"\b(?:[A-Z]{2,}\s+){5,}[A-Z]{2,}\b", prose):
            r.warn(f"Content: {name} has a long all-caps run ('{caps[:40]}…'); all caps is harder to read")


def check_repeated_headings(brand: dict, root: Path, r: Report):
    """Warn when the same sub-heading text appears in 3+ chapters (ambiguous in a heading list)."""
    cdir = root / get(brand, "content.dir", "content")
    seen: dict = {}
    for path in sorted(cdir.glob("*.md")):
        for h in re.findall(r"^#{2,3}\s+(.+?)\s*$", path.read_text(encoding="utf-8"), flags=re.M):
            seen.setdefault(h.strip().lower(), set()).add(path.name)
    for heading, files in seen.items():
        if len(files) >= 3:
            r.warn(f"Content: the heading '{heading}' appears in {len(files)} chapters; make each specific (e.g. 'Logo {heading}')")


def check_assets(root: Path, r: Report):
    mf = root / "assets" / "manifest.json"
    if not mf.exists():
        r.warn("Assets: assets/manifest.json missing; run make_assets.py")
        return
    m = json.loads(mf.read_text())
    r.ok(f"Assets: {len(m.get('files', []))} files in the asset kit")
    for w in m.get("warnings", []):
        r.warn(f"Assets: {w}")
    for s in m.get("skipped", []):
        r.warn(f"Assets skipped: {s}")
    missing = [f["path"] for f in m.get("files", []) if not (root / f["path"]).exists()]
    if missing:
        r.error(f"Assets: {len(missing)} file(s) in the manifest are missing, e.g. {missing[0]}")
    if PLATFORMS_FILE.exists():
        reviewed = json.loads(PLATFORMS_FILE.read_text()).get("lastReviewed")
        try:
            age = (dt.date.today() - dt.date.fromisoformat(reviewed)).days
            if age > 180:
                r.warn(f"Social: platform specs were last reviewed {age} days ago ({reviewed}); verify sizes before publishing")
        except (TypeError, ValueError):
            pass


def check_audit(root: Path, r: Report):
    audit = root / "analysis" / "accessibility-audit.md"
    if not audit.exists():
        r.warn("Audit: analysis/accessibility-audit.md not found; run the accessibility-audit skill in audit mode and save its findings")
        return
    text = audit.read_text(encoding="utf-8")
    # If the file has a Resolution section, judge only that (the original report stays below it as a record).
    if "## Resolution" in text:
        text = text.split("## Resolution", 1)[1].split("\n## ", 1)[0]
    open_blockers = [l for l in text.splitlines() if l.startswith("|") and re.search(r"\|\s*(Critical|Serious)\b", l)
                     and not any(w in l.lower() for w in ("fixed", "resolved", "closed"))]
    if open_blockers:
        r.warn(f"Audit: {len(open_blockers)} Critical/Serious finding row(s) not marked fixed in accessibility-audit.md; confirm they are resolved")
    else:
        r.ok("Audit: accessibility audit saved with no open Critical or Serious findings")


def check_html(brand_path: Path, root: Path, r: Report):
    page = root / "style-guide.html"
    if not page.exists():
        r.warn("HTML: style-guide.html not rendered yet; run render_guide.py")
        return
    html = page.read_text(encoding="utf-8")
    if not re.search(r'<html[^>]*\slang="[^"]+"', html):
        r.error("HTML: <html> has no lang attribute")
    if not re.search(r"<title>[^<]+</title>", html):
        r.error("HTML: missing <title>")
    if 'class="skip-link"' not in html:
        r.error("HTML: missing skip link")
    imgs = re.findall(r"<img\b[^>]*>", html)
    no_alt = [i for i in imgs if not re.search(r'\salt="', i)]
    if no_alt:
        r.error(f"HTML: {len(no_alt)} image(s) without an alt attribute")
    # Header logos sit beside an h1 that names the organisation, so their empty alt is intentional.
    empty_alt = [i for i in imgs if re.search(r'\salt=""', i) and not re.search(r'class="logo-(light|dark)"', i)]
    if empty_alt:
        r.warn(f"HTML: {len(empty_alt)} image(s) with empty alt; confirm they are decorative")
    if len(re.findall(r"<h1\b", html)) != 1:
        r.error("HTML: there must be exactly one <h1>")
    levels = [int(x) for x in re.findall(r"<h([1-6])\b", html)]
    for a, b in zip(levels, levels[1:]):
        if b > a + 1:
            r.error(f"HTML: heading level jumps from h{a} to h{b}")
            break
    ids = re.findall(r'\sid="([^"]+)"', html)
    dupes = {i for i in ids if ids.count(i) > 1}
    if dupes:
        r.error(f"HTML: duplicate ids {sorted(dupes)[:5]}")
    cdir = root / "content"
    newest = max([brand_path.stat().st_mtime] + [p.stat().st_mtime for p in cdir.glob("*.md")])
    if page.stat().st_mtime < newest:
        r.error("HTML: style-guide.html is older than brand.json or content; re-run render_guide.py")
    if not (r.errors and any(e.startswith("HTML") for e in r.errors)):
        r.ok("HTML: lang, title, skip link, alt attributes, headings and ids pass automated checks")


def write_report(root: Path, brand: dict, r: Report) -> Path:
    out = root / "analysis" / "validation-report.md"
    out.parent.mkdir(exist_ok=True)
    status = "PASS" if not r.errors else "FAIL"
    lines = [f"# Validation report: {get(brand, 'meta.name', '')}", "",
             f"**Result: {status}** — {len(r.errors)} error(s), {len(r.warnings)} warning(s). "
             f"Generated {dt.datetime.now().isoformat(timespec='minutes')}.", "",
             "Automated checks cannot confirm everything. Also complete the manual checks in the accessibility-audit skill "
             "(screen reader pass, keyboard pass, 200%/400% zoom, logo legibility at minimum size, real content review).", ""]
    for title, items in (("Errors (must fix)", r.errors), ("Warnings (review)", r.warnings), ("Passed", r.passes)):
        lines += [f"## {title}", ""] + ([f"- {i}" for i in items] or ["- None"]) + [""]
    out.write_text("\n".join(lines), encoding="utf-8")
    return out


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("brand", type=Path)
    args = ap.parse_args(argv)
    brand_path = args.brand.resolve()
    root = brand_path.parent
    brand = json.loads(brand_path.read_text())
    r = Report()
    check_brand(brand, root, r)
    check_content(brand, root, r)
    check_repeated_headings(brand, root, r)
    check_assets(root, r)
    check_html(brand_path, root, r)
    check_audit(root, r)
    report = write_report(root, brand, r)
    print(json.dumps({"status": "PASS" if not r.errors else "FAIL", "errors": r.errors,
                      "warnings": r.warnings, "passed": r.passes, "report": str(report)}, indent=2, ensure_ascii=False))
    return 1 if r.errors else 0


if __name__ == "__main__":
    sys.exit(main())
