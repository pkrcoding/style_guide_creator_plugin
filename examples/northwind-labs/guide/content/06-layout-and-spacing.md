# Layout, grid and spacing

Our logo is built from exact geometry: a perfect circle and sharp, symmetrical angles. Our layouts follow the same idea. A strict grid, consistent spacing and generous white space make dense climate data feel calm, ordered and trustworthy.

## Spacing

All spacing is a multiple of our 4px base unit. Use the `space-` tokens for padding, margins and gaps. Never use values in between.

{{spacing.scale}}

How to choose a step:

| Relationship | Tokens |
|---|---|
| Inside a component (icon to label, label to input) | `space-1` to `space-3` |
| Between related items (list items, form fields, card content) | `space-4` to `space-5` |
| Between groups (cards in a row, paragraphs to a chart) | `space-6` to `space-8` |
| Between page sections | `space-9` to `space-12` |

The rule is simple: things that belong together sit closer together than things that do not. If two groups look equally spaced, readers cannot tell where one ends.

## Grid

We use a column grid that changes with the screen width. Content never grows wider than the maximum content width, so lines of text and charts stay comfortable on large monitors.

{{grid}}

- **Text containers:** keep paragraphs to 45–75 characters per line. On desktop this is usually 6 to 8 of the 12 columns, never the full width.
- **Charts and maps:** may span the full content width, with their title and caption aligned to the same left edge as the text.
- **Dashboards:** use the 12-column grid with cards that span 3, 4, 6 or 12 columns. Keep the gutter between all cards the same.
- **Margins:** the outer margins in the table are minimums. Content, including the logo, never sits inside them.

## Composition

- **Align to a strong left edge.** Headings, text, charts and the logo share one left edge. This echoes the clean geometry of the mark.
- **One focal point per view.** Each page, slide or post has one main message: a headline, a key number or a chart. Use Daybreak Amber for that one point at most.
- **Use white space as a material.** Leave space rather than adding boxes and dividers. A page that is about 40% empty usually reads better than a full one.
- **Hierarchy through size and weight,** not through extra colours.
- **Keep the logo and data separate.** Never place the logo inside a chart or map area.

## Common formats

| Format | Margins | Grid | Notes |
|---|---|---|---|
| Web page | Per the grid table | 4, 8 or 12 columns | Logo top left in the header, aligned to the first column |
| A4 report (portrait) | 20mm on all sides, 25mm at the binding edge | 12 columns, 5mm gutter | Body text spans 8 columns; side notes and small charts use the other 4 |
| US Letter | 0.75in on all sides | 12 columns | Same structure as A4 |
| Slide (16:9) | At least 5% of the width on each side | 12 columns | One idea per slide; see chapter 17 |
| Social square (1:1) | At least 8% of the width on each side | 4 columns | Keep text and the logo inside the platform safe zones in chapter 15 |

## Corner radius

Our logo combines sharp apexes with a soft circle. We echo that with **small, crisp corners**: enough to feel considered, never bubbly.

{{radius}}

- Use `radius-none` for tables, charts, maps and full-bleed images, so data edges stay exact.
- Use `radius-sm` for inputs and tags, and `radius-md` for buttons and cards.
- Use `radius-lg` for panels and dialogs, and `radius-xl` only for large feature cards and media.
- Use `radius-pill` only for avatars, toggles and status pills. The circle is our symbol, so we use full circles deliberately and sparingly.
- Nested shapes use a smaller radius than their container.

## Elevation

We prefer flat surfaces separated by space and subtle borders. Shadows show that something is above the page, such as a menu or dialog, not decoration.

{{elevation}}

- On dark surfaces, shadows are hard to see. Use a lighter surface step, such as Polar Night on the dark neutral, to show elevation.
- Never rely on a shadow alone to mark an interactive element. Interactive cards also need a `border-strong` outline or a clear label.

## Layout accessibility
- **Reflow:** every page works at a width of 320 CSS px without horizontal scrolling, except for content that needs two dimensions, such as large data tables and maps. Give those their own scroll area with a visible label.
- **Zoom:** text can be zoomed to 400% without horizontal scrolling and without loss of content.
- **Reading and focus order:** the order in the code matches the visual order. Do not use the grid to move content visually so that it reads in a different order.
- **Spacing overrides:** layouts must not break when users increase line height, letter spacing or word spacing.
- **Targets:** keep at least 24 × 24px for every interactive target, and 44 × 44px on touch screens, with at least `space-2` between neighbouring targets.

## Layout: do and don't
> **Do** use the `space-` tokens for every gap, and the grid for every layout.

> **Do** keep text columns narrow, even on wide screens.

> **Don't** round the corners of charts, maps or data tables.

> **Don't** fill white space with decorative shapes or extra logos.

> **Don't** use large radii or pill shapes for buttons and cards. They do not match our sharp, precise mark.
