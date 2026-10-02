# Colour

Our colours come straight from the logo: the deep blue of the harbour, the warm coral of a rising sun and the soft blue of the tide. Used consistently, they make us recognisable at a glance. Used carefully, they keep every word readable for older residents, people with low vision and people with colour-vision deficiencies.

## Our colours

{{color.brand}}

| Colour | Role | Personality | Use it for |
|---|---|---|---|
| **Harbour Blue** | Primary | Calm, dependable, local | Headlines, the website header and footer, primary buttons, large brand panels, the reversed logo background |
| **Sunset Coral** | Secondary | Warm, hopeful, kind | Highlights, illustrations, shapes and large panels that carry dark text; calls to action using its darker step |
| **Tide Blue** | Accent | Gentle, fresh, coastal | Backgrounds of cards and quote panels, wave dividers, illustration fills |
| **Neutrals** | Text and surfaces | Quiet, clear | Body text, backgrounds, borders, dividers |

Harbour Blue is dark enough to use for text at its exact value. Sunset Coral and Tide Blue are not: on white they are for shapes and large areas only. When you need either as text, use its 600 step (`secondary-600`, `accent-600`). Never lighten or darken the exact logo colours to make them pass; use a scale step instead and keep the exact colour for the logo and large fills.

## Colour values

The swatches above give HEX and RGB for screens, HSL and OKLCH for developers, and CMYK for print.

- **CMYK** values are a mathematical starting point, not a print specification. Ask your printer for a proof and compare it with a screen calibrated by the Communications team or a previous printed sample.
- **Pantone** spot colours have not been chosen. They must be matched from a physical Pantone swatch book under daylight-balanced light, separately for coated (C) and uncoated (U) paper, because the same ink looks different on each. Until then, print in CMYK.

## Proportions

{{color.proportions}}

Most of what we make should feel light, open and calm, with colour used to guide the eye. For example, on an A5 flyer:

- **Neutral (60%):** a white or light neutral page with near-black body text.
- **Harbour Blue (25%):** the headline and a footer band carrying the reversed logo and contact details.
- **Sunset Coral (10%):** one highlight, such as a rounded shape behind the key date, set with dark text.
- **Tide Blue (5%):** a wave divider or a light panel behind a quote.

One warm Sunset Coral moment per page is enough. More than that, and nothing stands out.

## Tonal scales and tokens

{{color.scales}}

Each colour has a scale from 50 (lightest) to 950 (darkest). Refer to colours by token name, such as `primary-600`, so designers and developers use the same values.

| Steps | Use for |
|---|---|
| 50–100 | Page and card backgrounds, highlighted table rows |
| 200–300 | Decorative borders, dividers, illustration fills |
| 400–500 | Icons, chart marks, form borders and other UI (check 3:1) |
| 600 | Text and links on white; buttons with white text |
| 700–950 | Headings, dark panels, text on light tints |

Key tokens: `text-default` is `neutral-900`, `text-muted` is `neutral-600`, `text-link` is `primary-600`, `border-strong` is `neutral-500`, `border-subtle` is `neutral-200` (decorative only), and `surface-brand` is `primary-600`.

## Accessible pairings

{{color.pairings}}

Every pairing in the table has been checked against WCAG 2.2 AA:

- **Any text (4.5:1):** safe for body text, links, buttons and captions.
- **Large text and UI only (3:1):** text 24px and above (or 18.66px bold), icons, borders and chart marks.
- **Decorative only:** shapes and fills that carry no information. Never use these for text, icons or chart marks.

Buttons: use `surface-brand` with `text-on-brand` (white text on Harbour Blue) as the primary button. For a warm call to action such as "Donate", use `secondary-600` with white text. Exact Sunset Coral with `neutral-950` text works for large panels and stickers, but don't use it for buttons on white, because its edge is less than 3:1 against the page.

Focus rings: inside Harbour Blue sections, use the white focus ring; inside Sunset Coral and Tide Blue sections, use the `neutral-950` ring. These are the `focus.onBrand` colours, listed in chapter 13.

### Never combine

These combinations fail contrast, but people will be tempted to use them:

- White text on exact Sunset Coral or exact Tide Blue.
- Exact Sunset Coral or exact Tide Blue text, icons or thin lines on white or light neutral.
- Sunset Coral text on Harbour Blue (it is below 3:1, although the sun in the logo is fine because it is artwork).
- Harbour Blue text on the dark neutral background in dark mode.
- Mid-grey `neutral-400` or lighter for any text on white.

> **Note** Harbour Blue text on Tide Blue panels, Tide Blue text on Harbour Blue and Harbour Blue on light tints all pass 4.5:1. We have proposed adding them to the approved table so they can be used for quote panels and highlights.

## State colours

{{color.semantic}}

Success, warning, error and information messages use their own colours, never brand colours.

- **Always use an icon and words**, not colour alone: "Error: enter your postcode" with an error icon, not just a red border.
- **Sunset Coral is close to the error colour.** Keep Sunset Coral out of forms and error messages, and keep the error colour out of marketing. Sunset Coral tints (`secondary-50`, `secondary-100`) look almost the same as the error background, so don't use them as panel backgrounds on forms or account pages.
- **Harbour Blue and Tide Blue are close to the information colour.** Information messages must use the `info` tokens with an information icon and a heading such as "Good to know", never a plain blue box.

## Colour-vision deficiency

{{color.cvd}}

About 1 in 12 men and 1 in 200 women have some form of colour-vision deficiency. The table simulates how our colours appear to them. The pairs listed may look the same, so wherever they appear together:

- **Success, warning and error** can be confused with each other. Always add a distinct icon (tick, triangle, cross) and a text label.
- **Success and information** can be confused (tritanopia). Use different icons and headings.
- **Sunset Coral and the success colour** can be confused (protanopia). Never use Sunset Coral to mean "bad" or "done".
- In charts, maps and timetables, separate these colours with labels, patterns or a clear difference in lightness (chapter 09).

## Dark mode

Dark mode swaps surfaces and text, and uses lighter steps of each brand colour:

| Purpose | Light mode | Dark mode |
|---|---|---|
| Page background | white | `neutral-950` |
| Body text | `neutral-900` | `neutral-50` |
| Links and Harbour Blue text | `primary-600` | `primary-500` |
| Sunset Coral text | `secondary-600` | `secondary-500` |
| Tide Blue text | `accent-600` | `accent-500` |
| Logo | Full colour | Single colour, light (reversed) knockout |

Use the dark neutral (`neutral-950`) rather than pure black for large surfaces: it is softer on the eyes and keeps the blue character of the brand.

## Colour in data visualisation

Charts use brand colours first, in a fixed order, with every mark at least 3:1 against its background and a white gap between neighbouring bars or segments. Label data directly and add patterns for print. Chapter 09 sets out the series order and rules.

## Print and other media

- **Litho and digital print:** use CMYK until Pantone references are matched (see "Colour values"). Always ask for a hard-copy proof for anything printed in quantity.
- **Uncoated paper** makes colours look duller and darker. Check proofs on the actual stock.
- **Embroidery:** match thread colours to a physical sample of the printed logo, not to a screen. Use the single-colour symbol for small embroidery.
- **Signage paint and vinyl:** match to a RAL, NCS or vinyl manufacturer's swatch, chosen against a printed proof. Record the references in the asset library once agreed.
- **Screens** vary. Judge colour on a calibrated monitor, and never approve print colour from a phone screen.

## Colour: do and don't
> **Do** use Harbour Blue for headlines and large brand areas, with plenty of white space around them.

> **Do** use `secondary-600` or `accent-600` whenever Sunset Coral or Tide Blue needs to be text or a link.

> **Do** pair every status colour with an icon and words.

> **Don't** put white text on exact Sunset Coral or exact Tide Blue.

> **Don't** use Sunset Coral in error messages, or the error colour in marketing.

> **Don't** invent new colours, tints with transparency over photos, or gradients behind text.

> **Accessibility** Never rely on colour alone to carry meaning. Pair it with text, icons, patterns or position.
