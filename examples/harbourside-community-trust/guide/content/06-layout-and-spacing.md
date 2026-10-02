# Layout, grid and spacing

Good layout makes our information easy to find and calm to read, which matters when someone is looking for help with housing, food or work. Our layouts are open and card-based, with rounded corners that echo the circle and waves of our logo.

## Spacing

{{spacing.scale}}

All spacing is a multiple of our 4px base unit. Use the `space-*` tokens rather than typing your own values, so every page shares the same rhythm.

| Use | Token |
|---|---|
| Between an icon and its label; inside tags | `space-2` |
| Inside buttons and form fields; between a label and its field | `space-3` to `space-4` |
| Between paragraphs; inside small cards | `space-4` to `space-5` |
| Inside large cards and panels; between form groups | `space-6` |
| Between sections | `space-9` to `space-10` |
| Above and below page-level bands (hero, footer) | `space-11` to `space-12` |

Related items sit closer together than unrelated ones. If two things look equally spaced, people assume they are equally related.

## Grid

{{grid}}

- Text columns never span the full grid. Keep paragraphs to the line length in chapter 05; on desktop, that is roughly 6 to 8 of the 12 columns.
- On mobile, stack cards in a single column, in the same order as the desktop reading order.
- Align the logo, headings and body text to the same left margin.

### Common formats

| Format | Margins | Grid | Notes |
|---|---|---|---|
| Web page | As the grid table | 4, 8 or 12 columns | Content no wider than the maximum content width |
| A4 and A5 print | 15mm (A5) to 20mm (A4), plus 3mm bleed | 12 columns (A4) or 6 columns (A5), 5mm gutters | Logo top left inside the margin |
| Slides (16:9) | At least 80px at 1920×1080 | 12 columns | One idea per slide; see chapter 17 |
| Social square and portrait | At least 80px at 1080px wide | 4 columns | Keep text inside the platform safe zone (chapter 15) |

## Composition

- **One focal point per layout:** a headline, a photo or a key number, not all three competing.
- **White space is part of the design:** it gives the page the calm, uncluttered feel of our brand. Don't fill every gap.
- **Clear hierarchy:** headline, then supporting text, then the action. Put the most important information, such as a phone number or opening times, where people look first.
- **Consistent alignment:** left-align text blocks to the grid. Centre only short headlines on posters, social cards and end slides.

## Corner radius

{{radius}}

Our corners are noticeably rounded, to match the circular symbol and the rounded letters of the wordmark.

- Use `radius-md` for buttons and cards, `radius-sm` for inputs and tags, `radius-lg` for panels and dialogs, and `radius-xl` for feature cards and photos in marketing layouts.
- Use `radius-pill` for avatars, status pills and toggles.
- Use one radius per component type throughout a design; don't mix rounded and square cards.
- Keep tables, full-bleed photos and page edges square (`radius-none`).
- When a rounded item sits inside another, the inner radius is smaller than the outer one, so the gap between them looks even.

## Elevation

{{elevation}}

We are a flat, friendly brand: most surfaces use `shadow-0` and are separated by colour, space or a `border-subtle` line. Use `shadow-1` for cards that can be clicked, `shadow-2` for menus and pop-ups, and `shadow-3` only for dialogs. Shadows are decorative; a card's edge must still be clear without them (use a border or a background tint).

## Supporting graphic: the wave line

*Proposed — confirm with the Communications team:* the three wave lines from the symbol may be used on their own as a section divider or the edge of a panel, in Tide Blue, Harbour Blue or white. A designer should draw this from vector artwork. Never use the sun on its own as a graphic, or the wave line where it could be mistaken for the logo; and never place text on top of it.

## Layout accessibility
- **Reflow:** web pages must work at 320px wide without horizontal scrolling, except for data tables, maps and diagrams.
- **Zoom:** text must remain readable when zoomed to 400%, with no horizontal scrolling for text blocks.
- **Order:** the reading order and keyboard focus order follow the visual order. Don't use layout tricks that place content visually in a different order from the code or the document structure.
- **Targets:** keep at least `space-2` between tappable items, and make buttons and controls at least 44 by 44px on all screens.
- **Print:** keep text out of the bleed and fold areas.

> **Do** use generous white space and the `space-*` tokens to group related content.

> **Don't** squeeze extra content in by shrinking margins, line spacing or text size.
