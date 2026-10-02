# Iconography

Icons help people find what they need quickly, including people who read English as a second language or find long text tiring. They only help if they are simple, consistent and always paired with words.

## Our icon style

Our icons match the rounded, friendly character of the logo:

- **Outline style** with a **2px stroke** at 24px.
- **Rounded line ends and rounded corners**, like the wave lines in our symbol.
- Drawn on a **24px grid with 2px padding**, so the artwork sits inside a 20px live area.
- **Filled** versions only for a selected state (for example, the active tab in a menu).
- **Simple and literal:** one idea per icon, no tiny details, no text inside the icon.

## Recommended icon set

Use **[Lucide icons](https://lucide.dev)**. Its rounded line ends, rounded joins and 2px stroke on a 24px grid match our style without changes. Lucide is free and open source under the ISC licence, which allows commercial use; keep the licence notice with any code that includes it.

If an icon is missing from Lucide, draw a new one in the same style (24px grid, 2px stroke, rounded ends and joins) and add it to the asset library. Don't mix icons from different sets in one design.

## One icon per meaning

Use the same icon for the same idea everywhere, so people learn it once.

| Meaning | Lucide icon |
|---|---|
| Housing and homes | `house` |
| Food and meals | `utensils` |
| Work and training | `briefcase` |
| Phone us | `phone` |
| Email us | `mail` |
| Find us / location | `map-pin` |
| Opening times | `clock` |
| Volunteering | `hand-heart` |
| Donate | `heart` |
| Information | `info` |
| Warning | `triangle-alert` |
| Error | `circle-x` |
| Success | `circle-check` |

Avoid hand gestures (thumbs up, OK sign) and culturally specific symbols: their meaning varies across the communities we serve.

## Sizes

| Size | Use |
|---|---|
| 16px | Inline with `small` text only, always next to a word |
| 20px | Inline with `body` text, buttons and form fields |
| 24px | Default: navigation, cards, lists |
| 32px | Service tiles and feature lists |
| 48px and up | Posters, leaflets and signage pictograms |

Scale icons as whole units; don't change the stroke width. At 32px and above, the stroke scales with the icon. In print, keep icons at least 6mm high.

## Colour

- Use `text-default` (`neutral-900`) or Harbour Blue on white and light backgrounds.
- Use white on Harbour Blue and on `neutral-950` backgrounds.
- Sunset Coral icons on white must use `secondary-500` or darker. Exact Sunset Coral and exact Tide Blue are below 3:1 on white, so use them only for decorative icons that add no information.
- Status icons use their state colour from chapter 04, always with a text label.
- Meaningful icons need at least 3:1 against their background.

## Icon accessibility
- **Labels:** show a visible text label with every icon wherever there is room. Many of our readers will understand "Food" faster than a fork and knife.
- **Icon-only buttons** (for example, close or search) need an accessible name, such as `aria-label="Close"`, and a tooltip on hover and focus.
- **Decorative icons** next to a text label are hidden from screen readers (`aria-hidden="true"`), so the label isn't read twice.
- **Never use an icon alone for critical meaning**, such as an error, a deadline or a cost.
- **Target size:** the clickable area is at least 44 by 44px on all screens, even if the icon itself is smaller. This is stricter than the WCAG minimum of 24 by 24px because many of our users are older.

> **Do** pair every icon with a short, plain word: "Call us", "Food", "Opening times".

> **Do** use the same icon for the same meaning on the website, leaflets and social media.

> **Don't** mix outline and filled icons, or icons from different sets, in one design.

> **Don't** use exact Sunset Coral or Tide Blue for icons that carry meaning on white.
