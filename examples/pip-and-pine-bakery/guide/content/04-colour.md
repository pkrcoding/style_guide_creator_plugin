# Colour

Colour is the fastest way customers recognise us across the street or a feed. Our palette starts from the logo's warm brown on cream and adds two supporting colours from the pine forest and the bakery counter, and every combination we approve is readable for people with low vision or colour-vision deficiency.

## Our colours

| Colour | Role | Where it comes from | Use it for |
|---|---|---|---|
| Pinecone Brown | Primary | The logo | The logo, primary buttons, headings, footers, dark panels |
| Forest Pine | Secondary (*proposed*) | Echoes the tree in the logo | Secondary buttons, section bands, seasonal and outdoor moments |
| Honey Glaze | Accent (*proposed*) | The colour of a glazed crust | Small highlights: stickers, offer flashes, illustration details, dividers |
| Flour Cream | Warm surface | The logo's own background | Page and packaging backgrounds that feel like paper bags and flour |

Pinecone Brown is the only colour in the logo. Forest Pine and Honey Glaze are proposals that give the palette range; the Brand and Marketing team must confirm them before large print runs.

{{color.brand}}

The swatches show HEX, RGB, HSL, OKLCH and CMYK. CMYK values are a mathematical starting point, not a print specification. Pantone references are still to be matched from a physical Pantone swatch book and confirmed on a printer's proof; coated and uncoated papers give different results, so match each stock separately.

## Proportions

{{color.proportions}}

Neutrals (Flour Cream, white and the warm greys) cover about 55% of any layout, Pinecone Brown 30%, Forest Pine 10% and Honey Glaze 5%.

A menu board, for example, has a Flour Cream background, Pinecone Brown headings, prices and logo, one Forest Pine band for "This week's bakes", and a single Honey Glaze sticker shape behind "New". If Honey Glaze starts covering whole panels, the layout stops feeling like us and starts feeling like a warning sign.

## Tonal scales and tokens

{{color.scales}}

Each colour has steps from 50 (palest) to 950 (darkest). Use them by token name, never by eye.

| Steps | Use |
|---|---|
| 50–200 | Tinted backgrounds, cards, selected rows, hover fills |
| 300–500 | Borders, dividers, illustration, chart marks (500 meets 3:1 on white) |
| 600 | Text, links and buttons with white text on light backgrounds |
| 700–950 | Headings, dark panels, hover states for buttons |

Exact Pinecone Brown is step `primary-800`; exact Forest Pine is `secondary-700`; exact Honey Glaze is `accent-400`. Keep exact values for the logo and large brand fills, and use the steps the pairing table names for text and interface.

## Accessible pairings

{{color.pairings}}

| Type | Approved combinations |
|---|---|
| **Text-safe (4.5:1 or more)** | `neutral-900` on white or Flour Cream; exact Pinecone Brown or Forest Pine on white or Flour Cream; `primary-600`, `secondary-600` and `accent-600` text and links on white; `accent-600` on Flour Cream; white on exact Pinecone Brown, exact Forest Pine, `primary-600`, `secondary-600` or `accent-600`; `neutral-950` on Honey Glaze |
| **Large text and icons only (3:1)** | Pinecone Brown on Honey Glaze panels |
| **Decorative only** | Honey Glaze on white or Flour Cream: shapes, rules, illustration fills. Never text, icons or chart marks |

Never combine:

- White text on Honey Glaze. It fails badly; use `neutral-950` or Pinecone Brown on Honey Glaze, or switch the panel to `accent-600`.
- Honey Glaze text or icons on white or Flour Cream. Use `accent-600`.
- Pinecone Brown on Forest Pine, or Forest Pine on Pinecone Brown. Both are dark and fail.
- `neutral-400` or lighter grey text on any light background.

Inside a Pinecone Brown or Forest Pine section, focus rings are white; on Honey Glaze they are `neutral-950`. The `focus.onBrand` tokens already set this.

> **Do** use Pinecone Brown for primary buttons with white text, and `primary-600` for links on white.

> **Don't** set any text in exact Honey Glaze on a light background, however large.

## State colours

{{color.semantic}}

Success, warning, error and info have their own scales. Use the `-600` step for text, the `-50` step for the message background and the `-500` step for borders. Every message always has an icon and a written label ("Error:", "Saved") as well as colour.

Two brand colours sit close to state colours:

- **Forest Pine is close to success green.** Keep Forest Pine out of success messages and use the success tokens. Don't use Forest Pine buttons or bands right next to a success message.
- **Honey Glaze is close to warning amber.** Never use Honey Glaze for warnings, and never use warning colours for offers. A Honey Glaze "New" sticker must not look like an alert.

## Colour-vision deficiency

{{color.cvd}}

The table shows how our colours appear to people with protanopia, deuteranopia and tritanopia, and flags pairs that become hard to tell apart:

- **Pinecone Brown and Forest Pine** look alike with deuteranopia. Wherever both carry meaning, such as two product ranges or two chart series, add text labels or a clear difference in lightness.
- **Forest Pine and Error** look alike with protanopia. Error messages always carry an icon and the word "Error"; never place a Forest Pine element where it could be read as an error, or the reverse.
- **Success, warning, error and info** can be confused with each other. Always pair them with an icon and text.

Bakery-specific rule: allergen and dietary information (vegan, contains nuts, gluten) must be written out in words. Never code it by colour alone, for example a green dot for vegan.

## Dark mode

On dark backgrounds use the dark neutral (`neutral-950`), not pure black, for large surfaces; it is warmer and less harsh. Body text is `neutral-50`. For brand text and links, swap to the `textOnDark` steps: `primary-500`, `secondary-500` and `accent-500`. Exact Honey Glaze also reads well on the dark neutral for highlights. The logo switches to white.

## Colour in charts

Series follow a fixed order with alternating lightness, every mark keeps at least 3:1 against the background, and series are labelled directly. Chapter 09 gives the order and rules.

## Print and other media

- **CMYK:** start from the values in the swatches and approve a hard-copy proof before any run.
- **Pantone:** to be matched from a physical swatch book, coated and uncoated separately. Record the agreed references with the Brand and Marketing team so every printer uses the same ones.
- **Embroidery:** match thread to a printed Pantone chip of Pinecone Brown under daylight, not to a screen.
- **Signage paint and vinyl:** match to a RAL or NCS reference from a physical fan deck, approved by the Brand and Marketing team.
- **Screens:** colours vary between devices. Judge colour on a calibrated monitor, and judge print only from a proof.

## Colour: do and don't
> **Do** let Flour Cream and white do most of the work, with Pinecone Brown as the confident main colour.

> **Do** use the step named in the pairing table whenever a colour carries text or meaning.

> **Do** write every allergen, status and error in words, with an icon where it helps.

> **Don't** adjust the exact Pinecone Brown to make something pass. Use a scale step instead.

> **Don't** place text over a gradient unless every point behind the text passes; otherwise use a solid panel.

> **Don't** use Forest Pine for success or Honey Glaze for warnings.
