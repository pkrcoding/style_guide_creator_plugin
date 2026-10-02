# Validation report: Northwind Labs

**Result: PASS** — 0 error(s), 3 warning(s). Generated 2026-10-02T16:25.

Automated checks cannot confirm everything. Also complete the manual checks in the accessibility-audit skill (screen reader pass, keyboard pass, 200%/400% zoom, logo legibility at minimum size, real content review).

## Errors (must fix)

- None

## Warnings (review)

- Colour vision: 8 colour pair(s) may be confused; the colour chapter must say how meaning is also shown (labels, icons, patterns)
- Assets: primary logo has several colours. Plain single-colour versions merge overlapping shapes; knockout versions turn enclosed shapes in ['#f2a541'] into holes instead. Inspect both, keep the one that preserves the logo's detail, and ask the designer for official single-colour artwork if neither does.
- Assets: symbol logo has several colours. Plain single-colour versions merge overlapping shapes; knockout versions turn enclosed shapes in ['#f2a541'] into holes instead. Inspect both, keep the one that preserves the logo's detail, and ask the designer for official single-colour artwork if neither does.

## Passed

- All 28 colour pairings meet their WCAG 2.2 thresholds
- Semantic text, link, border and focus tokens pass in light and dark themes
- Assets: 92 files in the asset kit
- HTML: lang, title, skip link, alt attributes, headings and ids pass automated checks
- Audit: accessibility audit saved with no open Critical or Serious findings
