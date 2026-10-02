---
name: typography
description: Choose and document brand typography that is legible and accessible — match typefaces to the logo's personality, confirm licensing and fallbacks, set the type scale, hierarchy, line length and spacing, numerals, multilingual and RTL support, and office/system font substitutes, then write chapter 05-typography. Use when selecting brand fonts, pairing typefaces, defining a type scale, or writing typography guidelines.
argument-hint: "[path/to/brand.json] [existing font names]"
---

# Typography

Load **brand-standards** first. Read `references/font-pairings.md` for vetted, freely licensed options.

## 1. Choose typefaces

Priority order:

1. **Existing brand fonts** the user names. Ask about the licence if it is unknown, and record it as an assumption.
2. **Font in the logo.** If the wordmark is set in an identifiable typeface (check SVG `fonts`, or recognise it visually), the display face can echo it. Never claim an identification you are not sure of: say "similar to".
3. **Recommend a pairing** from `references/font-pairings.md` that matches the logo's personality cues and the language coverage needed.

Legibility checks for the body face: distinct I/l/1 and O/0, open apertures, generous x-height, a regular weight that is not thin, and true italics or a clear obliques policy. Prefer variable fonts with a wide language range.

Update `brand.json → typography.families` with `name`, `fallback` (system stack, plus metric-compatible fallbacks where they exist), `source`, `license` and `url`. Keep the `mono` role for data and code.

## 2. Type scale

The default scale (`init_guide.py`) is a 1.25 ratio from 16px. Adjust only with a reason: for example, a 1.2 ratio for dense product UI, or 1.333 for editorial or marketing sites. Keep `body` at 16px or more with line height at least 1.5, `small` at 14px or more, and headings with line heights of 1.1–1.3. For responsive use, headings may scale down on mobile. Document the mobile sizes in the chapter if you add them.

## 3. Write chapter 05-typography

Keep `{{type.families}}` and `{{type.scale}}`. Cover:

1. **Our typefaces:** why they fit the brand (tie to the logo), and the weights to use and not use.
2. **Where to get them and the licence:** web (self-host or Google Fonts), desktop install, app embedding, and whether the licence covers social, video and broadcast.
3. **Fallbacks and substitutes:** the system fallback stack for web; substitutes for Office/Google Docs (e.g. Arial or Calibri for sans, Georgia for serif) when brand fonts are unavailable; email-safe stacks.
4. **Type scale and hierarchy:** how to build a page (one H1, no skipped levels, headings describe content), and the use of each token.
5. **Readable text:** line length (`typography.measure`), line height, paragraph spacing, left alignment, no justified text, no long all-caps or italic passages, minimum sizes per medium (screen 16px; print body 11–12pt; signage per chapter 18; social on-image text of at least 4% of the image height).
6. **Emphasis:** bold for emphasis. Italics for titles and terms only. Underline is reserved for links.
7. **Numbers:** tabular figures for tables, lining figures in UI, date/number formats (point to chapter 12).
8. **Languages:** script coverage, RTL rules (mirrored alignment, no letter-spacing on Arabic), CJK fallbacks, hyphenation.
9. **Accessibility:** text resizing to 200%, text spacing overrides, never using images of text, and dyslexia-friendly practices (spacing and alignment matter more than "special" fonts).
10. **Do / Don't:** e.g. don't track body text, don't use more than two families, don't fake bold or italic, don't set long text in the display face below 20px.
