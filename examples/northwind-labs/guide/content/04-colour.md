# Colour

Colour is the first thing people notice about Northwind Labs, and in our charts and maps it carries data. Our palette has to look like us and stay readable for everyone, including people with colour-vision deficiencies who read our reports.

## Our colours

All three brand colours come straight from the logo.

- **Fjord Teal (primary)** is the circle of our symbol and the "LABS" descriptor. It is cool, steady and technical. Use it for key actions, links, highlights and brand moments. Exact Fjord Teal passes 4.5:1 on white, so it works for text and buttons.
- **Polar Night (secondary)** is the colour of our wordmark. It is deep, serious and confident. Use it for headlines, dark sections, footers, covers and data-heavy dashboards.
- **Daybreak Amber (accent)** is the open peak in our symbol. It is the warm, optimistic spark in a cool palette. Use it in small amounts, such as a highlight bar, a key number, an illustration detail or one series in a chart.
- **Neutrals** are cool greys tinted towards Fjord Teal. They carry most text, backgrounds and borders.

{{color.brand}}

The swatches give HEX, RGB, HSL and OKLCH for screens and a CMYK starting point for print. CMYK values are mathematical conversions, not printer-tested values. Pantone references must be matched from a physical Pantone swatch book and confirmed on a printer's proof. Coated and uncoated stocks need separate matches.

## Proportions

Most of what we make is calm and light, with colour used on purpose.

{{color.proportions}}

A typical report page is mostly white and light neutral with neutral body text. Fjord Teal appears in links, the section marker and the main chart series. Polar Night is used for headings and perhaps one dark data panel. Daybreak Amber appears once, for example as the bar that highlights the key finding. If amber is everywhere, it stops meaning "look here".

## Tonal scales and tokens

Each colour has a scale from 50 (lightest) to 950 (darkest). Use the tokens, not eyedropped values.

- **50–200:** tinted backgrounds, table stripes, selected rows, map fills for low values.
- **300–500:** borders, icons, chart marks and UI on dark backgrounds.
- **600–950:** text, buttons and dark surfaces.

The exact logo colours are pinned into the scales: Fjord Teal is `primary-600`, Polar Night is `secondary-900` and Daybreak Amber is `accent-300`.

{{color.scales}}

## Accessible pairings

These are the only approved text and background combinations. Each one shows its contrast ratio and what it is approved for.

{{color.pairings}}

How to read it:

- **Text-safe (4.5:1 or more):** any size of text.
- **Large text and UI (3:1 or more):** text of 24px and above, or 18.66px bold, plus icons, borders and chart marks.
- **Decorative only:** shapes, fills and illustration with no meaning. Never use these for text, icons or data.

### Daybreak Amber needs care

Exact Daybreak Amber is 2.05:1 on white. On light backgrounds it is **decorative or large-area only**: a background panel, an illustration fill, a highlight bar. For amber text or links on light backgrounds, use `accent-600`. For amber buttons with white text, also use `accent-600`. Text on an exact Daybreak Amber panel must be dark (`neutral-950`).

### Never combine

- White text on exact Daybreak Amber.
- Exact Daybreak Amber text, icons or chart lines on white or light neutral.
- Fjord Teal text on Polar Night (2.45:1).
- Daybreak Amber text, icons or chart marks on Fjord Teal (2.9:1).
- Polar Night text on the dark neutral background.
- Mid-scale steps (300–500) of any colour as text on white.

## State colours

Success, warning, error and info have their own scales, kept apart from the brand colours.

{{color.semantic}}

Every state message has **an icon, a text label and a colour**. For example, write "Error: enter a postcode" with an error icon, not just a red border.

> **Warning** Daybreak Amber is close in hue to our warning colour. Never signal a warning by colour alone, and keep brand Daybreak Amber out of warning messages. Use the `warning-` tokens for warnings, and Daybreak Amber only for brand highlights.

Fjord Teal also sits close to the success and info colours for some readers. Do not use Fjord Teal styling on status messages.

## Colour-vision deficiency

Colour-vision deficiency is common, especially among men, so some of our readers in every audience will see our colours differently. The table simulates our colours for the main types and lists pairs that some people may confuse.

{{color.cvd}}

Pairs to watch, and the rule for each:

| Pair | Who may confuse them | Rule |
|---|---|---|
| Fjord Teal and success | Tritanopia | Never use teal next to success states without a label |
| Fjord Teal and info | Tritanopia | Info messages always carry the info icon and the word "Info" or "Note" |
| Success and warning | Protanopia, deuteranopia | Different icons (tick vs triangle) and text labels |
| Success and error | Deuteranopia | Different icons (tick vs cross), text labels, and never green/red alone |
| Success and info | Tritanopia | Icons and labels |
| Warning and error | Protanopia, deuteranopia | Different icons and labels; in charts, use different lightness and patterns |

In short: **never use colour alone to carry meaning.** Add a label, an icon, a pattern, a position or a clear difference in lightness.

## Dark mode

Dark interfaces use the dark neutral (`neutral-950`) as the main surface, never pure black, because pure black makes bright text halo and tires the eyes. Polar Night (`secondary-900`) works as a raised panel or a branded dark section.

| On light | On dark |
|---|---|
| Body text `neutral-900` | `neutral-50` |
| Fjord Teal text and links `primary-600` | `primary-500` |
| Polar Night text `secondary-600` | `secondary-500` |
| Daybreak Amber text `accent-600` | `accent-500`, or exact Daybreak Amber, which passes on dark |
| State text `{state}-600` | `{state}-500` |

Inside brand-coloured sections, use the focus ring colour set for that section (chapter 13): white on Fjord Teal and Polar Night, dark on Daybreak Amber.

## Colour in data visualisation

Charts follow a fixed series order: Fjord Teal first, then distinct lightness steps of Daybreak Amber and Polar Night. Every mark must reach at least 3:1 against its background. Label series directly and add patterns for print. Chapter 9 has the full palettes for categories, sequences, temperature anomalies and maps.

## Print and other media

- **Print:** start from the CMYK values above, then approve a printed proof. Ask the printer to match Pantone references from a physical swatch book. Specify coated and uncoated separately.
- **Embroidery:** match thread colours to a physical swatch, and use the single-colour logo for small stitching.
- **Signage and paint:** match RAL or NCS references from physical samples under the light where the sign will hang.
- **Screens:** colours differ between uncalibrated screens. Judge colour on a calibrated display or a printed proof, never on a laptop alone.

## Colour: do and don't
> **Do** use `primary-600` (exact Fjord Teal) for links and primary buttons with white text.

> **Do** keep Daybreak Amber to small, deliberate highlights, about one per page or slide.

> **Do** pair every state colour with an icon and a text label.

> **Don't** set text in exact Daybreak Amber on white. Use `accent-600`.

> **Don't** use brand Daybreak Amber to signal a warning.

> **Don't** use pure black for large dark backgrounds. Use `neutral-950` or Polar Night.

> **Don't** make your own tints with opacity. Use the scale steps so contrast stays predictable.
