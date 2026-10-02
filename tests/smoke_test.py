#!/usr/bin/env python3
"""End-to-end smoke test for the style-guide-creator scripts.

Runs init -> assets -> tokens -> render -> validate on each fixture logo, checks the
quality gate FAILS while chapters still hold TODO markers, fills the chapters with
placeholder prose, and checks the gate then PASSES.

Usage:
    python3 tests/smoke_test.py            # uses whichever python runs it
Pillow is optional; without it, PNG assets are skipped and the test still runs.
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "skills" / "brand-standards" / "scripts"
FIXTURES = ROOT / "tests" / "fixtures"
FILLER = ("This section is written for the people who use the brand every day. " * 12).strip()


def run(script, *args, expect=0):
    proc = subprocess.run([sys.executable, str(SCRIPTS / script), *map(str, args)], capture_output=True, text=True)
    if proc.returncode != expect:
        print(proc.stdout[-3000:], proc.stderr[-3000:], sep="\n")
        raise SystemExit(f"FAIL: {script} exited {proc.returncode}, expected {expect}")
    return proc.stdout


def fill_chapters(content: Path):
    for md in content.glob("*.md"):
        text = re.sub(r"TODO\([^\n]*\)", FILLER, md.read_text())
        md.write_text(text)


def check_fixture(logo: Path, tmp: Path):
    out = tmp / logo.name.replace(".", "-")
    summary = json.loads(run("init_guide.py", "--logo", logo, "--name", "Northwind Labs", "--out", out,
                             "--contact", "brand@example.org", "--platforms", "instagram,linkedin,youtube,web"))
    assert summary["seeds"], "no seed colours extracted"
    brand = out / "brand.json"
    run("make_assets.py", brand)
    run("generate_tokens.py", brand)
    run("render_guide.py", brand)
    gate = json.loads(run("validate_brand.py", brand, expect=1))
    assert any("TODO" in e for e in gate["errors"]), "gate should fail on TODO markers"
    fill_chapters(out / "content")
    run("render_guide.py", brand)
    gate = json.loads(run("validate_brand.py", brand, expect=0))
    html = (out / "style-guide.html").read_text()
    assert html.count("<section") == 20, "expected 20 chapters"
    assert "Pass ✓" in html and "<caption>" in html
    manifest = json.loads((out / "assets" / "manifest.json").read_text())
    print(f"ok  {logo.name}: seeds={summary['seeds']} files={len(manifest['files'])} warnings={len(gate['warnings'])}")


def main():
    # Library sanity checks against known WCAG values.
    sys.path.insert(0, str(SCRIPTS))
    import brandlib as bl
    assert abs(bl.contrast_ratio("#ffffff", "#000000") - 21.0) < 0.01
    assert abs(bl.contrast_ratio("#767676", "#ffffff") - 4.54) < 0.01
    assert bl.normalize_hex("#ABC") == "#aabbcc"
    assert bl.oklch_to_hex(*bl.rgb_to_oklch(bl.hex_to_rgb("#0f6e7a"))) == "#0f6e7a"
    print("ok  colour maths")
    # PDFs must not embed local file paths: links to local files are stripped from the print copy.
    import render_guide
    with tempfile.TemporaryDirectory() as tmp:
        page = Path(tmp) / "style-guide.html"
        page.write_text('<a href="assets/logo/x.png">x.png</a> <a href="https://example.org">web</a> <a href="#logo">logo</a>')
        copy = render_guide._print_copy(page).read_text()
        assert 'href="assets' not in copy and "x.png" in copy, "local links must become plain text"
        assert 'href="https://example.org"' in copy and 'href="#logo"' in copy, "web and in-page links must stay"
    print("ok  PDF print copy has no local file links")
    with tempfile.TemporaryDirectory() as tmp:
        logos = [FIXTURES / "sample-logo.svg", FIXTURES / "sample-logo.png"]
        if bl.HAVE_PIL:
            logos.append(FIXTURES / "sample-logo-opaque.jpg")
        for logo in logos:
            check_fixture(logo, Path(tmp))
    print("All smoke tests passed.")


if __name__ == "__main__":
    main()
