# Iconography

Icons help customers scan quickly: opening hours, delivery, allergens, a basket. Ours should feel like they were drawn by the same hand as the tree in our logo: simple, friendly shapes with softened ends.

## Style

| Property | Rule |
|---|---|
| Style | Outline for interface icons; solid fill only for selected states and small decorative spots |
| Stroke | 2px at 24px size, scaled with the icon |
| Caps and joins | Round, to match the emblem's rings and the pip |
| Grid | 24×24px with 2px padding on every side (20×20px live area) |
| Detail | As few strokes as possible. If an icon needs more than about six strokes to read, it is too detailed |
| Perspective | Flat, front-on. No 3D, shadows or gradients |

The logo's tree is a solid, filled shape. Don't use it, or a copy of it, as a general icon; it belongs to the logo. A generic tree icon from the icon set is fine for unrelated meanings, such as "outdoor seating".

## Recommended icon set

Use **Lucide** (lucide.dev). Its default style (2px stroke, round caps and joins, 24px grid) matches our rules, and it has the food, shop and delivery icons a bakery needs. Lucide is released under the ISC licence, which allows commercial use; keep its licence notice with the files in our codebase.

If Lucide has no suitable icon, ask the Brand and Marketing team before drawing a new one. Custom icons follow the same grid, stroke and caps.

Don't mix icon sets on one screen or document. Their stroke weights and corners will clash.

## Sizes

| Size | Use |
|---|---|
| 16px | Inline with `small` text only |
| 20px | Inline with `body` text, inside buttons |
| 24px | Default for navigation and interface |
| 32px | Feature lists, menu category headers, print at A4 |

Keep the stroke at 2px at 24px. At 16px the stroke scales down; check that the icon still reads.

## Colour

- Default: `neutral-900` on light backgrounds, `neutral-50` on dark.
- Brand: `primary-600`, `secondary-600` or exact Pinecone Brown or Forest Pine on white or Flour Cream; all meet 3:1.
- Never use exact Honey Glaze for icons on white or Flour Cream; it fails 3:1. Use `accent-600`.
- On Pinecone Brown or Forest Pine panels, icons are white. On Honey Glaze panels, icons are `neutral-950` or Pinecone Brown.
- State icons use their state colour's `-600` step and always sit with a written label.

## Meaning and consistency

Use one icon per meaning across every channel. For example, the same bag icon always means "basket", and the same wheat icon always means "contains gluten". Keep a shared list of icon meanings in the design library so the website, menus and social posts never disagree.

## Icon accessibility

- **Accessible names:** icon-only buttons need a name read by assistive technology, such as `aria-label="Open basket"`. Write the action, not the picture.
- **Decorative icons:** hide them from assistive technology (`aria-hidden="true"`) when a text label next to them says the same thing.
- **Never icon alone for critical meaning.** Allergen, dietary and error information always includes words, for example a wheat icon with "Contains gluten".
- **Target size:** the clickable area is at least 24×24px, and 44×44px on touch screens, even when the icon drawn inside is smaller.
- **Contrast:** icons that carry meaning keep at least 3:1 against their background.

> **Do** pair icons with short text labels in navigation and on menus.

> **Don't** use colour as the only difference between two icons, such as a green leaf for vegan and a brown leaf for vegetarian.

> **Don't** stretch, outline-and-fill or add drop shadows to icons.
