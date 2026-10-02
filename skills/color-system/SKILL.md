---
name: color-system
description: Build and document an accessible brand colour system from logo colours — name and assign roles, generate tonal scales, neutrals and state colours, approve WCAG 2.2 colour pairings, check colour-vision deficiencies, set proportions, dark mode, print (CMYK/Pantone) and data-visualisation colour rules, and write chapter 04-colour. Use when choosing or changing brand colours, checking colour contrast, or writing colour guidelines.
argument-hint: "[path/to/brand.json] [seed colours]"
---

# Colour system

Load **brand-standards** first.

## 1. Decide roles and names

From `analysis/logo.json → colours` (or the user's existing colours, which take priority):

- **Primary:** the most recognisable logo colour, typically the largest chromatic area. Used for key actions, highlights and brand moments.
- **Secondary:** a supporting colour, often the logo's dark colour (navy, charcoal). Used for headings, dark surfaces and footers.
- **Accent:** a small-area colour for emphasis. If it fails 3:1 on white, it is for decoration and fills only.
- If the logo is monochrome, propose one accent colour that fits the industry and personality, mark it as *proposed*, and check it the same way.

**Names:** short, evocative, brand-appropriate and unique ("Harbour Navy", "Lantern Gold"), not just "Blue". Apply them with:

```bash
python3 "${CLAUDE_PLUGIN_ROOT}/skills/brand-standards/scripts/build_palette.py" \
  --seed "#0f6e7a:primary:Northwind Teal" --seed "#1b2a3a:secondary:Harbour Navy" \
  --seed "#f2a541:accent:Lantern Gold" --brand "<abs>/brand.json"
```

## 2. Read what the palette build tells you

- `accessible.textOnLight`: the step to use whenever this colour is text or a link on white. If it differs from the exact colour, the guide must say "use {id}-{step} for text".
- `accessible.solidWithWhiteText`: the step for buttons and banners with white text.
- `accessible.textOnDark` / `uiOnDark`: dark-mode equivalents.
- `notes`: each one must become a rule in the chapter (e.g. "Lantern Gold is decorative only on white").
- `cvd`: confusable pairs, to be separated by lightness, labels or patterns wherever they appear together (charts, status, maps).

To check any extra combination: `contrast_check.py FG BG --use body`. To approve one for the guide, propose it for `color.customPairings` (`{fg, bg, use, label}`). To drop generated pairings the brand will never use, propose their labels for `color.excludedPairings`. Both survive rebuilds and are gated.

Focus rings inside brand-coloured sections use `focus.onBrand` (white or dark, chosen per brand colour). Mention it wherever the guide shows buttons or links on colour.

## 3. Proportions

Default 60 / 30 / 10 (neutrals / primary / others). Adjust to the logo's character: a bold brand can carry more primary. Edit `color.proportions` (it survives rebuilds).

## 4. Write chapter 04-colour

Keep `{{color.brand}}`, `{{color.proportions}}`, `{{color.scales}}`, `{{color.semantic}}`, `{{color.pairings}}` and `{{color.cvd}}`. Cover:

1. **Our colours:** the role and personality of each, where it comes from (the logo), and when to use it.
2. **Colour values:** the swatches placeholder covers HEX, RGB, HSL, OKLCH and CMYK. Explain that CMYK is a starting conversion and Pantone must be matched from a physical swatch and a printer's proof (coated and uncoated differ).
3. **Proportions:** with a layout example in words.
4. **Tonal scales and tokens:** what the 50–950 steps are for (tints for backgrounds, mid-tones for UI and borders, darks for text). Use token names.
5. **Accessible pairings:** the approved table. State plainly which combinations are text-safe, large-text/UI-only or decorative-only. Add a "never combine" list for failing pairs that people will be tempted to use (e.g. white on the accent).
6. **State colours:** success, warning, error and info. Always with icon and text. Note any clash with brand colours from `notes`.
7. **Colour-vision deficiency:** explain the simulation table and the rules for confusable pairs.
8. **Dark mode:** which steps replace which (`textOnDark`), and avoiding pure black (#000) large surfaces in favour of the dark neutral.
9. **Colour in data visualisation:** the order of series colours (brand first, then distinct-lightness steps), at least 3:1 for marks against the background, direct labels, and patterns for print. Cross-reference chapter 09.
10. **Print and other media:** CMYK, Pantone, embroidery (thread matching), signage paint (e.g. RAL or NCS to be matched), screen calibration caveat.
11. **Do / Don't:** at least three of each.

## Rules

- Never recommend a pairing that fails its use. The gate recomputes all ratios.
- Never alter the exact logo colour to make it pass. Use a scale step for text and UI, and keep the exact colour for the logo and large fills.
- Gradients: allowed only if every point under text passes. Otherwise, text goes on a solid panel.
