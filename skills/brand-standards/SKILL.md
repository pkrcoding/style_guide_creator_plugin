---
name: brand-standards
description: Shared standards for every role building a style guide with this plugin — the brand.json contract, workspace layout, accessibility baseline (WCAG 2.2 AA thresholds), writing standard for guide chapters, data placeholders, and the scripts (logo analysis, palette builder, contrast/CVD checker, asset generator, token exporter, renderer, quality gate). Load before analysing a logo, editing brand.json, writing any chapter, or running any style-guide script.
---

# Brand standards

Every role in this plugin follows these rules. They keep the guide, the design tokens and the asset kit consistent and accessible.

## Workspace layout

```
<out>/
  brand.json                 single source of truth (data)
  content/NN-*.md            20 chapters (words + data placeholders)
  analysis/logo.json         logo measurements
  analysis/palette.json      full palette build
  analysis/validation-report.md
  assets/source/             logo (and symbol) as supplied
  assets/logo/               variants, clear-space versions, background tests
  assets/favicons/           favicon.ico, icons, apple-touch, maskable, manifest, <head> snippet
  assets/social/<platform>/  PNG previews, editable SVG templates, safe-zone overlays
  assets/manifest.json       every asset with purpose, alt text, warnings
  tokens/                    tokens.json (DTCG), tokens.css, _tokens.scss, tailwind.preset.js, tailwind-theme.css
  style-guide.html / .md / .pdf
```

## Scripts

All scripts are in `${CLAUDE_PLUGIN_ROOT}/skills/brand-standards/scripts/` (same as `${CLAUDE_SKILL_DIR}/scripts/` from this skill). They need Python 3.9+ only. **Pillow** (`pip install pillow`) is optional: it adds JPG/WebP input, PNG asset generation, favicons and previews. If `python3 -c "import PIL"` fails and the user agrees, install it in a virtual environment. Never install packages globally without asking.

| Script | Purpose |
|---|---|
| `init_guide.py --logo L --name N --out D [...]` | Analyse the logo, build the palette, write `brand.json` and chapter skeletons. Safe to re-run: it never overwrites without `--force` |
| `analyze_logo.py LOGO` | Colours with share of area, background type, bounding box, orientation, contrast on white and black, CVD risks, minimum-size suggestion, SVG details |
| `build_palette.py --seed HEX:ROLE:NAME ... [--brand brand.json]` | 50–950 tonal scales (OKLCH), neutrals, semantic colours, accessible steps, pairings, CVD report. `--brand` updates `brand.json` in place |
| `contrast_check.py FG BG ... / --matrix / --cvd [--use body\|large\|ui]` | Ad-hoc WCAG and colour-vision checks. Exits 1 on failure with `--use` |
| `make_assets.py brand.json [--platforms ...]` | Logo variants, background tests, favicons, social avatars, covers, templates, manifest |
| `generate_tokens.py brand.json` | Exports design tokens and checks that semantic tokens pass in light and dark themes |
| `render_guide.py brand.json [--pdf]` | Renders HTML and Markdown, plus with `--pdf` a print-ready A4 PDF (cover, contents, page numbers, light theme, tagged, with bookmarks) via headless Chrome/Edge |
| `validate_brand.py brand.json` | Quality gate: exits 1 on any error and writes `analysis/validation-report.md` |

Run scripts with absolute paths. Read their JSON output. Do not re-derive numbers by hand that a script already computed.

## brand.json contract

See `references/brand-schema.md` for every field. Rules:

- **Only the lead edits `brand.json`.** Section agents propose changes in their handoff. This avoids conflicting parallel writes.
- Colours are always lowercase `#rrggbb`. Never hand-edit `scale`, `steps`, `accessible` or `pairings`: rebuild them with `build_palette.py --brand`. Manual fields (`pantone`, `usage`), `proportions`, `customPairings` and `excludedPairings` survive a rebuild. Add extra approved combinations through `customPairings`, never by editing `pairings`.
- Every pairing has a `use` of `body` (4.5:1), `large` (3:1), `ui` (3:1) or `decorative` (no requirement, never for text or meaning). The gate recomputes every ratio from the hex values.
- Unknown facts go in `meta.assumptions`, never presented as truth.

## Accessibility baseline

`references/accessibility-baseline.md` is the non-negotiable minimum for everything the guide recommends. The short version:

- Text contrast is at least 4.5:1, or 3:1 for large text (24px+, or 18.66px+ bold). UI components, focus indicators, and meaningful graphics and chart marks are at least 3:1.
- Never use colour alone to convey meaning. Pair it with text, icons, patterns or position.
- Body text is at least 16px on screen, line height at least 1.5, and lines 45–75 characters long. Body copy is left-aligned (right-aligned for RTL) and never justified. Avoid long runs of all caps or italics.
- Focus is always visible: at least 2px, at least 3:1, and never removed.
- Targets are at least 24×24 CSS px (44×44 recommended for touch).
- Motion respects `prefers-reduced-motion`. No more than three flashes per second, and a pause control for anything that moves for more than five seconds.
- Every meaningful image has alt text, video has accurate captions, and audio has transcripts.
- Social: alt text on every image, captions on every video, CamelCase hashtags, emoji used sparingly and at the end of a sentence, and no "fancy" Unicode letters.

If the user picks AAA, use 7:1 / 4.5:1 thresholds and state it in chapter 13.

## Writing the guide

Follow `references/writing-the-guide.md` for every chapter: structure, tone, placeholders, Do/Don't callouts, image alt text, and what never to invent. The quality gate enforces part of it (no `TODO(` markers, known placeholders only, alt text, heading order, descriptive links, minimum depth). The rest is your professional responsibility.

## Handoff contract (section agents → lead)

Return a short Markdown handoff of no more than 300 words:

1. **Files written:** absolute paths.
2. **Proposed `brand.json` changes:** exact JSON path and value. For example, `foundations.values` = `[...]`, `logo.misuse` = `[...]`, `social.hashtags.brand` = `[...]`.
3. **Assumptions** you made, to add to `meta.assumptions`.
4. **Open issues** the lead must decide or tell the user.
