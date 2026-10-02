# Layout, grid and spacing

Consistent spacing and a shared grid make everything we produce feel calm and orderly, like a well-kept counter. Our layouts borrow the logo's balance: simple shapes, soft round edges and plenty of breathing room around each item.

## Spacing

{{spacing.scale}}

Every gap, margin and padding is a multiple of our 4px base unit. Use the spacing tokens, not arbitrary values.

| Token | Typical use |
|---|---|
| `1`–`2` | Between an icon and its label; inside tags |
| `3`–`4` | Inside buttons and form fields; between paragraphs |
| `5`–`6` | Inside cards; between related groups |
| `8`–`9` | Between page sections |
| `10`–`12` | Around hero areas and campaign headlines |

Related things sit closer together than unrelated things. A product name, price and allergen note belong in one tight group; the next product starts after a clearly larger gap.

## Grid

{{grid}}

- Content never runs wider than the maximum content width; centre it on wider screens.
- Text containers stay at 45–75 characters per line even when the grid column is wider. Let images and product cards use the extra width, not paragraphs.
- Align every element to a column edge. Images, cards and buttons sharing a row share top edges.

## Composition

- **One focal point per layout.** Usually a product photo or a Fraunces headline, never both competing at the same size.
- **Generous space.** Neutrals cover about 55% of a layout (see chapter 04). Empty Flour Cream space is part of the look, not wasted room.
- **Clear hierarchy.** Headline, then image, then supporting text, then action, in that reading order.
- **Circles as an echo.** The emblem is round, so circular crops suit staff portraits, ingredient close-ups and stickers. Use at most one circular element per layout so it stays special.

## Common formats

| Format | Margins and grid | Logo |
|---|---|---|
| Web page | Grid per breakpoint above | Top left of header, 96px or more |
| A4 portrait (menus, flyers, letters) | 15mm margins, 6 columns with 5mm gutters, 3mm bleed for professional print | Top left or centred top, 25mm or more |
| Slide 16:9 (1920×1080) | 80px margins, 12 columns | Bottom right on content slides, centred on title slides |
| Social square (1080×1080) | 64px safe margin on every side | One corner, consistent across a campaign |

## Corner radius

{{radius}}

Rounded corners echo the emblem's rings and the pip's soft oval, and keep the brand friendly rather than corporate.

| Token | Use |
|---|---|
| `sm` | Form fields, checkboxes, small tags |
| `md` | Buttons, alerts, menus and dropdowns |
| `lg` | Cards, product tiles, image containers |
| `xl` | Hero images, large promotional panels |
| `pill` | Filter chips, status badges, the "New" sticker shape |

Use one radius per component type throughout a product. Nested shapes take a smaller radius than their container.

## Elevation

{{elevation}}

We prefer flat, paper-like surfaces. On Flour Cream and white, separate cards with a 1px `neutral-200` border before reaching for a shadow.

- Level `1`: cards that can be selected or opened.
- Level `2`: dropdown menus and sticky headers.
- Level `3`: dialogs only.

Shadows never carry meaning on their own; a selected card also gets a visible border or tick.

## Layout accessibility

- **Reflow:** every page works at 320px wide with no horizontal scrolling for text. Columns stack on the mobile grid.
- **Zoom:** text zooms to 400% without horizontal scrolling or overlapping. Don't fix heights on text containers.
- **Order:** reading order and keyboard focus order follow the visual order: left to right, top to bottom. Don't rearrange content visually with CSS in a way that changes its meaning.
- **Targets:** buttons and links are at least 24×24px, and 44×44px for touch.

> **Do** build every layout from the spacing tokens and align to the grid.

> **Don't** fill empty space with extra logos, patterns or stickers. Let the layout breathe.
