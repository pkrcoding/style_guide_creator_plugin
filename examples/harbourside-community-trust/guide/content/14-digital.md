# Digital and web

Our website, emails and videos are often the first place a family, volunteer or council officer meets us, and many read them on an older phone, with larger text turned on, or in their second language. Every digital touchpoint must feel calm and welcoming like the logo, and work for everyone first time.

## Website header and footer

- **Header:** place the full-colour primary logo top left on a white header, at least 160px wide on desktop and never below the 160px minimum on mobile. If a narrow screen cannot fit 160px alongside the menu button, switch to the symbol at 40px or more, followed by the organisation's name as live text.
- **Link:** the logo links to the home page. Its alt text is "Harbourside Community Trust home", not "logo" and not the file name.
- **Clear space:** keep the clear space from chapter 03 (the height of the sun) on every side, including from the menu.
- **Footer:** use a `surface-inverse` or Harbour Blue footer with the single-colour light logo, or a white footer with the full-colour logo. Never put the full-colour logo on `surface-subtle` or any light grey: the full-colour exception covers white only. Use the single-colour dark logo there instead.
- **Footer content:** include "[Registered charity number]", "[Registered address]", a contact link, the accessibility statement and the privacy notice. Do not leave these as images.

> **Do** show the name "Harbourside Community Trust" as live text in the page title and footer, so it is never only inside the logo image.

> **Don't** use a transparent full-colour logo in a dark-mode header; Harbour Blue disappears on dark backgrounds. Swap in the single-colour light logo.

## Buttons and links

| Element | Style | Notes |
|---|---|---|
| Primary button | `surface-brand` fill with `text-on-brand` label, `label` type token, radius `md` | One per view, for the main action ("Get help", "Volunteer", "Donate") |
| Secondary button | White fill, `border-strong` 2px outline, `text-link` label, radius `md` | For other actions next to a primary button |
| Coral button (campaign only) | `secondary-600` fill with white label | Use only for fundraising appeals, never next to error messages |
| Text link | `text-link`, always underlined | Visited links keep the underline |

- Make every button at least 44px tall with at least 16px horizontal padding, so it is easy to tap for people with less steady hands.
- Write button labels as verbs in sentence case: "Find a food hub", not "Click here" or "Submit".
- Never use exact Sunset Coral or Tide Blue for button fills with white text or for link text. They fail contrast; use the 600 steps named in the pairings table in chapter 04.

## Forms

- Every field has a visible label above it in `label` type. Placeholder text is never the only label.
- Field borders use `border-strong` (at least 3:1 against the page). Radius `sm`.
- Mark required fields with the word "(required)", not only an asterisk or colour.
- Errors: show the `error-fg` text with an error icon directly under the field, and an error summary at the top of the form that links to each field. Keep brand Sunset Coral out of error messages so people do not confuse a campaign colour with a problem.
- Ask only what you need. Explain why you ask for sensitive details such as income or housing situation, in plain English.
- Allow enough time, never expire a form without warning, and let people go back without losing what they typed.

## Interactive states

| State | Treatment |
|---|---|
| Hover | Darken the fill one step (for example `primary-700` on a `surface-brand` button) or thicken the link underline |
| Focus | The focus ring from chapter 13: `focus` colour on light backgrounds; white ring (`focus-on-brand`) inside Harbour Blue sections; `neutral-950` ring inside Sunset Coral and Tide Blue sections. Never removed |
| Active / pressed | One step darker again, with no movement for reduced-motion users |
| Disabled | Lower contrast plus a reason in text ("Choose a date first"). Avoid disabled buttons where you can: let people press and explain what is missing |
| Selected | A tick icon or bold label as well as colour |

> **Accessibility** State is never shown by colour alone. Pair every colour change with an underline, outline, icon or text.

## Favicons and app icons

The favicons use the circular sun-and-waves symbol cropped from the master logo. The 16px and 32px icons sit on a transparent background; the Apple touch icon and maskable icon sit on a Harbour Blue square so the circle keeps a clear edge when a phone crops it to a rounded shape. At 16px the waves blur into texture, which is expected: the circle and coral sun still make the icon recognisable.

{{favicons}}

- Copy the `<head>` snippet from `assets/favicons/head-snippet.html` into every page template, and publish `site.webmanifest` alongside it.
- The maskable icon keeps the symbol inside the central safe zone (the middle 80%). Do not enlarge it to fill the square; Android masks will cut the circle.
- Check the 16px favicon on both light and dark browser tabs before launch.

## Open Graph and share images

Use the 1200 × 630px share image from the social kit (chapter 15) as the default `og:image`: the single-colour light logo centred on Harbour Blue. For campaign pages, make a version with a short headline in Nunito on a solid Harbour Blue panel. Keep the headline to eight words or fewer and inside the central safe area, because platforms crop the edges. Always set `og:image:alt` to describe the image, for example "Harbourside Community Trust logo on a blue background".

## Email newsletters

| Spec | Rule |
|---|---|
| Width | 600px single column |
| Body text | `body` size (16px), never below 14px, line height 1.5, Arial or Verdana as the email-safe fallback for Atkinson Hyperlegible Next |
| Headings | Live text in Nunito with Arial fallback, never images of text |
| Buttons | Bulletproof (HTML) buttons, at least 44px tall, `surface-brand` fill |
| Logo | Full-colour PNG at 2× resolution, displayed 200px wide, on a white plate with clear space baked in |
| Images | Every image has alt text; decorative ones have empty alt. The email must make sense with images off |

- **Dark mode:** many mail apps invert backgrounds. Because Harbour Blue fails on dark backgrounds, send the logo as a PNG with its own white rounded panel (radius `lg`) rather than a transparent PNG. It then stays legible in both modes.
- Use plain-English subject lines. Put the key action in the first two sentences.
- Include a plain-text version, a "view in browser" link and a clear unsubscribe link.
- Offer translated summaries for families who read English as a second language, and say which languages are available.

## Email signatures

Use one signature for all staff and regular volunteers:

1. Name (bold), optional pronouns
2. Role, and "Volunteer" if relevant
3. Harbourside Community Trust
4. Phone number, and working days if part-time
5. Website address as live text
6. "[Registered charity number]" in 14px text

- The logo is optional. If used, it is the full-colour PNG at 2×, displayed no wider than 200px and never below the 160px minimum, with alt text "Harbourside Community Trust". A text-only signature is always acceptable.
- No image-only signatures, inspirational quotes, coloured backgrounds or extra fonts. A campaign banner is allowed only when the Communications team supplies it, with alt text, for a set period.

> **Don't** paste a screenshot of your signature. Screen readers cannot read it and it breaks in dark mode.

## Video and webinars

- **Title cards:** the single-colour light logo on Harbour Blue, or full colour on white, held for at least 2 seconds.
- **Lower thirds:** name in Nunito bold, role in Atkinson Hyperlegible Next, white text on a solid Harbour Blue panel with radius `md`. Keep them on screen for at least 4 seconds and inside the 90% title-safe area.
- **Captions:** accurate, human-checked captions on every video, burned in for social and as a `.vtt` or `.srt` file on the website. Use white text on a dark semi-opaque box, sentence case, at least 2 lines at a size readable on a phone.
- **End cards:** the logo, one call to action, and the website address as text, held for at least 5 seconds.
- **Thumbnails:** a real face or scene plus a short headline on a solid panel. No text over busy photos.
- **Webinars:** use the 16:9 slide template from chapter 17, turn on live captions, share slides beforehand and record with a transcript.

> **Do** describe key visual information out loud in videos and webinars, so people with sight loss do not miss it.

> **Don't** autoplay video with sound on our website or in emails.
