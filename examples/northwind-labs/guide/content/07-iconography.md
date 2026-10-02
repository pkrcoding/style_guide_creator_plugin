# Iconography

Icons help busy city and utility teams find their way through our products and reports quickly. They work only if they are consistent, clear and backed by text, so one icon always means one thing.

## Our icon style

Our icons are drawn the way our logo is drawn: simple geometry, straight lines and sharp, clean corners.

| Property | Rule |
|---|---|
| Style | Outline (unfilled). A filled version is used only to show a selected or active state |
| Grid | 24 × 24px, with 2px of padding on every side (a 20 × 20px live area) |
| Stroke | 2px at 24px, scaled in proportion at other sizes |
| Corners and caps | Sharp corners and square or butt line ends, to match the logo's apexes |
| Detail | The fewest strokes that still read clearly. No perspective, no 3D, no gradients |
| Direction | Arrows and trend icons point up and to the right for growth or improvement, echoing the peak in our symbol |

## Recommended icon set

Use **Material Symbols, Sharp style**, set to outlined (fill 0), weight 400 and grade 0. It is published by Google under the **Apache License 2.0**, which allows commercial use and changes. Keep the licence notice with any icon files you ship in code.

We recommend it because:

- the Sharp style has square corners that match our logo;
- it includes many climate and energy icons, such as thermostat, water drop, bolt, solar power, wind power and CO₂;
- it is a variable font as well as SVG files, so weight and size stay consistent.

If you need an icon that is not in the set, a designer draws it on the same grid with the same stroke and corners, and the Marketing team approves it. Never mix icon sets on the same screen or page.

> **Note** If your product already uses another open-licence set such as Lucide (ISC licence) or Tabler (MIT licence), you may keep it in that product only, provided you use it consistently and keep the 24px grid and 2px stroke. Their rounded line ends are a little softer than our ideal.

## Sizes

| Size | Use |
|---|---|
| 16px | Inline with `small` text, table cells. Decorative or paired with a text label only |
| 20px | Inline with `body` text, inside buttons and form fields |
| 24px | Default: navigation, toolbars, standalone actions |
| 32px | Feature lists, empty states, section markers in reports |
| 48px and above | Illustrative use only, such as infographics and slides |

Align icons to the text they sit next to: centre them on the line height, with `space-2` between icon and label.

## Colour

- By default, icons use the same colour as the text next to them (`text-default` or `text-muted`).
- For brand emphasis, use Fjord Teal (`primary-600`) on light backgrounds and `primary-500` on dark backgrounds.
- Every meaningful icon must reach at least 3:1 against its background.
- Never draw icons in exact Daybreak Amber on white or light neutral; it is below 3:1. Use `accent-600` if an amber icon is needed.
- State icons use their state token (`success-fg`, `warning-fg`, `error-fg`, `info-fg`) and always sit next to a text label.
- Never use one icon in several colours to mean different things. Change the icon and the label, not just the colour.

## Labels and accessible names

- **Visible labels first.** Pair icons with a short text label wherever there is room, especially in navigation and on actions with consequences, such as "Delete" or "Publish".
- **Icon-only buttons** need an accessible name that describes the action ("Download data as CSV", not "Download icon"). Show a tooltip with the same text on hover and focus.
- **Decorative icons**, such as an icon next to a heading that already says the same thing, are hidden from assistive technology (`aria-hidden="true"`).
- **Never use an icon alone for critical meaning**, such as an alert, a data-quality warning or a status. Always add text.
- **One meaning, one icon.** Keep a shared list of icon meanings in the design library. For example, the warning triangle is used only for warnings.

## Target size

- Every interactive icon has a target of at least 24 × 24px, and 44 × 44px on touch screens, even if the drawn icon is smaller.
- Leave at least `space-2` between neighbouring icon buttons.
- Show focus with our standard focus ring (chapter 13) around the whole target, not just the icon.

## Icons: do and don't
> **Do** use outline icons from one set, on a 24px grid with a 2px stroke.

> **Do** give every icon-only button an accessible name that describes the action.

> **Do** use the same icon for the same meaning everywhere.

> **Don't** use the logo's peak or circle as an icon, bullet or arrow.

> **Don't** use an icon alone to show status, risk or a warning.

> **Don't** mix filled and outline icons, or icons from different sets, on one screen.

> **Don't** use emoji in place of icons in products, reports or slides.
