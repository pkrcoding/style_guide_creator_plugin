# Changelog

## 1.1.0 — 2026-10-02

Fixes found by running the plugin end to end on three sample logos (see `examples/`).

### Added
- `examples/`: three complete generated guides (SVG, PNG and logo-only JPG inputs) with PDFs, tokens, assets and audit records.
- Print-ready PDF: A4 cover and contents pages, page numbers, chapters on new pages, colours preserved, always the light theme, tagged with bookmarks.
- True vector (SVG mask) knockout logos.
- `logo.fullColourExceptions` for signed-off logotype contrast exceptions.
- `focus.onBrand` and `--focus-on-<colour>` tokens: a focus-ring colour for each brand surface.
- `color.customPairings` / `color.excludedPairings`, kept across palette rebuilds.
- Gate checks: per-surface focus contrast, saved accessibility audit, repeated generic headings.

### Fixed
- Logo background rules now count only colours that touch the background (enclosed shapes no longer block full colour on white).
- Logo colour extraction ignores anti-aliasing and JPEG fringe blends, and keeps thin real shapes (analysis at 512px).
- Knockouts never delete free-standing lighter elements, such as a tagline.
- Favicons on a solid brand tile (visible in dark tabs).
- Cover logos sized to stay above minimum size on phones, falling back to the symbol.
- PNG previews and SVG templates share one layout; template text scales with the canvas and uses the body typeface.
- Facebook cover safe zone widened for mobile cropping; LinkedIn company cover updated to 1512×256.
- Descriptive alt text for every logo variant and avatar; brand colour names in alt text.
- Every table has a caption; only scrolling tables are tab stops; callouts are notes, not unnamed landmarks; the PDF has no figure tags without alt text.
- The web app short name is cut at a word boundary.

## 1.0.0 — 2026-10-02

### Added
- `create-style-guide` orchestrator: logo-only input with optional extras, producing 20 chapters, an asset kit, design tokens, and HTML/Markdown/PDF output.
- Specialist skills: logo-analysis, color-system, typography, visual-language, voice-and-tone, social-media-kit, brand-applications, accessibility-audit, brand-standards.
- Agents: brand-strategist, visual-identity-designer, social-media-designer, accessibility-auditor.
- Scripts: logo analysis, OKLCH palette builder with WCAG 2.2 pairings and CVD checks, contrast checker, asset generator (logo variants, knockouts, background tests, favicons, social kit for 13 platforms), token exporter (DTCG, CSS, SCSS, Tailwind v3/v4), renderer, and validation gate.
- End-to-end smoke test.
