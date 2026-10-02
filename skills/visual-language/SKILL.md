---
name: visual-language
description: Define the brand's wider visual language so it feels like the logo everywhere — layout grids and spacing, corner radius and elevation, iconography, photography, illustration, AI imagery policy, data visualisation and motion — with accessibility built in (reflow, target sizes, alt text, chart contrast and patterns, reduced motion). Use when writing chapters 06–10 or advising on layout, icons, imagery, charts or animation for a brand.
argument-hint: "[path/to/brand.json] [chapter]"
---

# Visual language

Load **brand-standards** first. Derive every choice from the logo's personality cues (`logo.description`, personality notes in the brief): the guide should feel like one system.

| Logo cue | Layout | Radius | Icons | Imagery | Motion |
|---|---|---|---|---|---|
| Geometric, sharp | Strict grid, generous white space | 0–4px | Outline, 2px stroke, square caps | Architectural, clean light | Precise, short, standard easing |
| Rounded, friendly | Softer, card-based | 8–16px | Rounded caps and joins | Warm, candid people | Gentle ease-out, slight overshoot only for celebrations |
| Heavy, bold | High-contrast blocks of colour | 4–8px | Filled or duotone | High-energy, saturated | Snappy, quick |
| Light, elegant | Editorial, asymmetric | 0–2px | Thin (1.5px), minimal | Calm, natural light, muted | Slow fades |
| Playful | Loose, layered | 12–24px | Hand-drawn feel | Illustration-led | Bouncy, but within reduced-motion rules |

Update `radius`, `spacing`, `elevation` and `motion` in your handoff if the defaults do not fit.

## 06 Layout, grid and spacing

Keep `{{spacing.scale}}`, `{{grid}}`, `{{radius}}` and `{{elevation}}`. Cover the spacing principle (multiples of the base unit), the grids per breakpoint, margins, a maximum line length for text containers, composition principles (alignment, hierarchy, white space), layouts for common formats (web page, A4/Letter, slide, social square), corner radius and elevation use, and **accessibility**: content reflows at 320px, zoom to 400% without horizontal scroll for text, and logical reading and focus order that matches the visual order.

## 07 Iconography

Cover: the style (stroke width, corner treatment, grid such as 24px with 2px padding, filled vs outline), a recommended open-licence set that matches (e.g. Lucide, Phosphor, Tabler or Material Symbols; check the licence), sizes (16/20/24/32), colour (`text-default` or brand step with at least 3:1), and **accessibility**: icon-only buttons need an accessible name; decorative icons are hidden from assistive technology; never use an icon alone for critical meaning; target size at least 24px (44px touch); keep metaphors consistent (one icon per meaning).

## 08 Photography and illustration

Cover: photography style (subjects, composition, light, colour grading toward brand hues without distorting skin tones), people and **representation** (age, ethnicity, disability, body type, gender; authentic, not tokenistic; disabled people shown as active participants), what to avoid (staged clichés, heavy filters, text baked into photos), text over images (use a scrim or panel and check the worst-case contrast), illustration style (line weight, palette from brand scales, level of detail), image sourcing and rights (licences, model releases, credits), **alt text rules** (purpose over appearance, ~125 characters, decorative = empty alt), and an **AI-generated imagery policy** (disclosure, no realistic depictions of real people without consent, review for bias and artefacts, follow platform labelling rules).

## 09 Data visualisation

Cover: series colour order from the palette (alternate lightness so neighbours differ under CVD), at least 3:1 for marks against the background and between adjacent segments, direct labels instead of colour-only legends, patterns or shapes for print and monochrome, typography in charts (at least 12px, tabular figures), gridlines subtle (decorative border step), always starting bar axes at zero, tables as an accessible alternative, chart alt text (type, what it shows, key takeaway) plus a data table or summary, and avoiding 3D, pie charts with more than five slices, and red/green-only encodings.

## 10 Motion

Keep `{{motion}}`. Cover: principles (purposeful, quick, consistent direction), durations and easing tokens per use (hover, enter, exit, page transitions), logo animation rules (if any, at most 3 seconds, ending on the static logo, never distorting it), video intros and outros, **accessibility**: honour `prefers-reduced-motion`, no flashing above 3 per second, pause/stop/hide for anything over 5 seconds, no autoplaying audio, avoid parallax and large zoom, and captions for all video.
