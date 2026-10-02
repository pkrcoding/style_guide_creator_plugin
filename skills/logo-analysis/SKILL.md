---
name: logo-analysis
description: Analyse an organisation's logo and write the logo chapter of a brand style guide — classify the mark, extract colours and proportions, judge legibility, choose single-colour treatment (solid or knockout), define clear space, minimum sizes, approved backgrounds, placement, file formats and naming, alt text, and at least eight misuse rules. Use when analysing a logo, defining logo usage rules, generating logo variants, or writing chapter 03-logo.
argument-hint: "<path/to/logo> [path/to/brand.json]"
---

# Logo analysis and usage

Load **brand-standards** first.

## 1. Measure

Run `analyze_logo.py <logo>` (or read `analysis/logo.json`). Note:

- `colours`: hex values, share of area, and contrast on white and black. Anything below 3:1 on white cannot carry the logo on light backgrounds in full colour.
- `background`: `transparent`, `solid` or `complex`. Complex means the artwork is unusable as supplied: ask for a transparent or vector master.
- `orientation` and `contentAspectRatio`: wide logos (≥ 2.5:1) need a symbol or stacked lock-up for square spaces.
- `resolutionWarning`: raster below 1000px. Ask for a vector master and record the assumption.
- SVG `fonts` and `hasText`: live text in an SVG logo renders inconsistently. Recommend outlining text in the master.
- `recommendations.suggestedMinSize`: a starting point only.

## 2. Look

Read the image. Decide and record in `brand.json → logo`:

| Field | How to decide |
|---|---|
| `type` | Wordmark (name only), lettermark (initials), pictorial (recognisable icon), abstract mark, mascot, emblem (text inside a badge), combination (symbol + wordmark) |
| `description` | Factual: "A teal circle containing a gold upward triangle, to the left of the name set in a heavy geometric sans." |
| personality cues | Geometric/organic, rounded/sharp, heavy/light, formal/playful, static/dynamic. Pass these to type, radius, icon and illustration decisions |
| `clearSpace.rule` | Tie it to a visible element ("the height of the circle's triangle", "the cap height of the N") and set `fraction` to that element's height divided by the logo height (default 0.25) |
| `minSize` | Check the logo at `digitalPx` width: the smallest counter, stroke or letter must stay distinct. Raise the size if not. Print ≈ digital px × 0.35 mm, rounded up |

## 3. Variants and backgrounds

After `make_assets.py`, open `assets/logo/*` and `assets/logo/backgrounds/*`:

- **Single-colour treatment:** compare `primary-mono-dark.png` with `primary-mono-dark-knockout.png`. Choose the one that keeps internal detail and set `logo.monoStyle`. If neither works, say so: the organisation needs designer-drawn single-colour artwork.
- **Backgrounds:** `assets/manifest.json → backgroundTests` gives the variant and contrast for each brand background. Only logo colours that touch the background count (`touchesBackground` in the analysis); a light shape enclosed inside a dark disc never meets the background.
- **Near misses:** if full colour falls just short of 3:1 on a key background (e.g. 2.9:1), do not quietly allow it. Propose an exception in your handoff. The lead decides whether to add the background to `logo.fullColourExceptions` (WCAG exempts logotypes) and records it in `meta.assumptions`. The guide then states the exception. Turn it into rules, e.g. "Full colour on white is not allowed because Lantern Gold is 2.05:1; use the dark single-colour logo."
- **Photography:** the logo goes only on calm, even areas, or on a solid panel, and must keep 3:1 against the area directly behind it.

## 4. Write chapter 03-logo

Cover, in this order, keeping `{{logo.variants}}`, `{{logo.specs}}` and `{{logo.backgrounds}}`:

1. **Our logo:** what it is and what it represents. Describe meaning only if the user gave it; otherwise describe form.
2. **Anatomy:** name the parts (symbol, wordmark, tagline lock-up if any).
3. **Versions and when to use each:** primary, symbol only, single-colour dark, single-colour light (reversed), and any lock-ups. Prefer full colour wherever it passes.
4. **Clear space:** the rule, with the reason (impact and legibility).
5. **Minimum size:** screen and print, and when to switch to the symbol.
6. **Placement:** preferred corners or centring per format, alignment to the grid, and consistent placement across a campaign.
7. **Backgrounds:** an approved table from the background tests, plus photos and patterns.
8. **Misuse:** at least eight don'ts, also proposed for `logo.misuse`: stretch or squash; rotate; recolour outside the palette; add effects (shadows, glows, bevels, outlines); rearrange or resize elements; place on busy or low-contrast backgrounds; place inside other shapes not in the guide; use old versions; type the name in another font next to the symbol; crop.
9. **Files and naming:** SVG for digital, PDF/EPS for print, PNG for office tools. Use naming like `{org}-logo-{version}-{colour}.{ext}`. Point to `{{downloads}}` in chapter 20.
10. **Accessibility:** alt text (`logo.altText`), "home" wording when linked, contrast of at least 3:1, never use an image of the logo in place of the organisation's name in running text, and the logo is never the only means of identifying the organisation in alt text or a page title.

## Edge cases

- **Gradient logos** (`possibleGradient: true`, or gradients in the SVG): define a flat-colour version for small sizes, single-colour use and embroidery. Check contrast at the gradient's lightest point.
- **Photographic or highly detailed logos:** require a simplified mark for sizes under 64px.
- **Multiple wordmark languages:** specify each lock-up and which market uses it. For RTL, check that the lock-up mirrors correctly, or state that it must not.
- **Logo has a tagline:** define a version without the tagline for small sizes, and the minimum size at which the tagline remains legible (tagline cap height at least 6px on screen).
