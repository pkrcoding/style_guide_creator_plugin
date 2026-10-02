# Digital and web

Most people meet Northwind Labs on a screen first: our website, a dashboard, a webinar or an email from a sales lead. Our public-sector clients must meet the UK Public Sector Bodies Accessibility Regulations 2018, so everything we put on a screen has to be as precise and accessible as the data we sell.

This chapter applies the logo (chapter 3), colour (chapter 4), typography (chapter 5), layout (chapter 6) and accessibility (chapter 13) rules to websites, product interfaces, email and video. Use token names from `tokens/tokens.css`, never typed colour values.

## Website header and footer

### Header

- Place the primary full-colour logo top left, on a white (`surface-default`) header. Align it to the first grid column and centre it vertically in the header bar.
- Set the logo at least 34px high (about 160px wide, the primary logo's minimum digital size in chapter 3) on desktop and mobile. If the space is narrower than that, use the symbol instead.
- On a Polar Night or Fjord Teal header, use the single-colour light (knockout) logo. Never place the full-colour logo on either: its teal circle disappears into the background.
- Link the logo to the home page. Give the image the alt text "Northwind Labs home", not "logo" and not the file name.
- Keep the logo's clear space (chapter 3) free of navigation items, search boxes and banners.

### Footer

- Use a Polar Night (`surface-inverse`) footer with the single-colour light logo or the symbol, and `text-inverse` for links.
- Include: contact (hello@northwindlabs.example), an accessibility statement link, privacy and cookie notices, and the copyright line from chapter 20. Our public-sector clients will look for the accessibility statement first.

> **Do** link the header logo home with the alt text "Northwind Labs home".

> **Don't** use the full-colour logo on the Polar Night footer; use the single-colour light version.

## Buttons and links

| Element | Surface | Text | Notes |
|---|---|---|---|
| Primary button | `surface-brand` (Fjord Teal) | `text-on-brand` (white) | One per view: the main action |
| Secondary button | `surface-default` with a `border-strong` outline | `text-link` | For the alternative action |
| Tertiary / text button | None | `text-link`, underlined | Low-emphasis actions such as "Cancel" |
| Text link | Inherits | `text-link`, underlined | Underline always visible in body text |

- Use the `md` radius (`--radius-md`) for buttons and inputs. Our corners stay tight to echo the sharp peak in the symbol.
- Buttons are at least 44px tall on touch screens and never smaller than 24 × 24px anywhere.
- Write button labels as verbs that describe the result: "Download the report", "Book a demo".
- Daybreak Amber is never a button colour with white text. If you need an amber highlight, use `accent-600` with white text, or Polar Night text on exact Daybreak Amber.

## Forms

- Every field has a visible label above it. Placeholder text is never the label.
- Field borders use `border-strong` so they reach 3:1 against the page.
- Mark required fields with the word "required", not only an asterisk.
- Show errors with an icon, a text message under the field (using the error `fg` token) and a summary at the top of the form that links to each field. Never rely on a red border alone.
- Keep the field's width related to the expected answer (a postcode field is short).

## States

| State | Treatment |
|---|---|
| Hover | Darken the surface one step (for example `primary-700` for a primary button) and keep the underline on links |
| Focus | The brand focus ring defined in chapter 13: the `focus` token on light surfaces and `focus-on-brand` on brand-coloured ones, always outside the element |
| Active / pressed | Darken one further step |
| Disabled | Reduced-emphasis colours **plus** the `disabled` attribute, a "not-allowed" cursor and, where useful, a text hint explaining why |
| Selected | A check icon or bold weight in addition to colour |

> **Accessibility** Never remove the focus ring, and never make colour the only signal of a state. Disabled controls do not need to meet contrast, but they must still be readable and explained.

## Dashboards and data products

Our product UI is where precision matters most.

- Use Inter for interface text and JetBrains Mono for values that people compare, copy or cross-check, such as meter IDs, coordinates and timestamps.
- Use tabular figures in tables and KPI tiles so digits line up.
- Follow chapter 9 for chart colours. Never encode status by colour alone: pair the success, warning and error colours with icons and labels. Daybreak Amber is a brand highlight, not a warning colour.
- Every chart has a text summary or a data table alternative.
- Content reflows at 320px wide, and tables scroll inside their own container, not the page.

## Favicons and app icons

The favicon and app icons use the symbol only: the Fjord Teal circle with the Daybreak Amber peak. The wordmark is unreadable at these sizes. The maskable icon places the knockout symbol on a full Fjord Teal square, with the circle well inside the central safe zone, so Android can crop it to any shape without clipping the peak.

{{favicons}}

Copy every file from `assets/favicons/` to your web root and paste `assets/favicons/head-snippet.html` into the `<head>` of every page. It links `favicon.ico`, `icon-192.png`, `apple-touch-icon.png` and `site.webmanifest`, and sets the browser theme colour to Fjord Teal. The manifest also lists `icon-512.png` and `icon-maskable-512.png`.

> **Don't** make a favicon from the full horizontal logo, or add a border or drop shadow to the icon.

## Open Graph and link previews

- Use `assets/social/web/web-og-image-1200x630.png` as the default share image. It shows the single-colour light logo, centred on Polar Night.
- For individual pages, build a share image from the SVG template in the same folder: a short headline in Manrope, the logo bottom left, and all text inside the safe zone shown in the `-guides.svg` file.
- Always set `og:title`, `og:description` and `og:image:alt`. The alt text describes the image's message, not "share image".

## Email templates

- Width: 600px, single column, so it reads well on phones.
- Use live HTML text, not images of text. Body text is at least 16px with a line height of at least 1.5.
- Use Inter with the system fallback stack in chapter 5. Many email clients ignore web fonts, so the layout must still work in Arial.
- Buttons are bulletproof HTML buttons (not images), at least 44px tall, on `surface-brand` with `text-on-brand`.
- Logo: a transparent PNG at twice its displayed size, with at least 8px of padding around it and the alt text "Northwind Labs". In dark-mode email clients, a transparent full-colour logo can land on a dark background, so place it on a white header cell or use a version on a solid Polar Night panel with the single-colour light logo.
- Every image has alt text. The email must still make sense with images turned off.
- Include a plain-text version and a visible unsubscribe link for marketing emails.

## Email signatures

Keep signatures short, consistent and useful.

```text
[First name] [Last name] ([pronouns, optional])
[Job title], Northwind Labs
[Phone number]
hello@northwindlabs.example | [Website]
```

- Text is live, in the default sans of the email client (Arial or the system font), at 14px or larger. Name in bold, title in `text-muted` colour.
- An optional small logo sits below the text: the full-colour primary logo, 160–200px wide when displayed, saved as a PNG at twice that size, with the alt text "Northwind Labs". A text-only signature is always acceptable.
- Never use an image-only signature: screen readers, plain-text clients and image blocking all lose it.
- No quotes, personal slogans, animated GIFs or banners. Campaign or event banners need approval from the Marketing team and must have alt text.

## Video and webinars

| Element | Rule |
|---|---|
| Title card | Polar Night background, single-colour light logo, title in Manrope, at least 2 seconds on screen |
| Lower thirds | Name in Manrope bold and role in Inter on a solid Polar Night bar, bottom left inside the title-safe area, on screen for at least 4 seconds |
| Captions | Accurate, human-checked captions (.srt or .vtt) on every video; burned-in captions on social cuts, in Inter on a semi-opaque dark box |
| End card | Logo, one call to action and the web address as text, at least 5 seconds |
| Thumbnails | Use `assets/social/youtube/youtube-thumbnail-1280x720.svg`; a short headline of 5 words or fewer, a real image, the symbol in a corner; no clickbait |
| Webinar slides | Use the presentation template (chapter 17) and share slides in advance on request |

- Logo animation, if used, lasts no more than 3 seconds and ends on the static logo. Follow chapter 10 for motion and reduced-motion rules.
- Provide a transcript for webinars and recorded talks. Public-sector clients often need one for their own records.

> **Do** caption every video, including internal recordings shared with clients.

> **Don't** put important information only in the audio or only on screen: say it and show it.
