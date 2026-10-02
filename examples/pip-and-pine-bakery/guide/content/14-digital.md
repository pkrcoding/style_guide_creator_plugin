# Digital and web

For many customers, our website, emails and order confirmations are the first and most frequent contact with Pip & Pine Bakery. They should feel as warm and unhurried as the shop counter, and work for everyone: on a small phone, with a screen reader, with a keyboard or at 200% zoom.

Every rule here uses the tokens in `tokens/` (CSS, SCSS, Tailwind and DTCG JSON). Developers should take values from those files, never from screenshots or this page.

## Website and app basics

### Header and footer

- **Logo:** use the full emblem in the top-left of the header, linked to the home page. Display it at least 96px tall on desktop and tablet, the emblem's minimum digital size (chapter 3). Leave the clear space defined in chapter 3 between the outer ring and any navigation item.
- **Small screens:** if the header cannot hold the emblem at 96px, use the tree-and-pip symbol at 40px or larger, still linked home. Do not set "Pip & Pine Bakery" in a font next to the symbol to imitate a horizontal logo; that is a misuse (chapter 3). *Proposed — confirm with leadership:* commission a designer-drawn horizontal lock-up (symbol beside the wordmark) for narrow headers and email.
- **Linked logo alt text:** "Pip & Pine Bakery home". The page `<title>` and the visible footer must also contain the name in text, so the logo is never the only place the name appears.
- **Header background:** white (`surface-default`) or Flour Cream with the full-colour emblem; Pinecone Brown or Forest Pine with the light single-colour (white) emblem. Never use the full-colour emblem on a dark footer.
- **Footer:** a Pinecone Brown or `surface-inverse` band is a good close to the page. Put the light emblem or symbol, contact details, opening hours (once confirmed), social links with text labels, and the accessibility statement link here.

> **Do** use the PNG logo files at 2× resolution until a vector (SVG) master exists, and set width and height attributes so the page does not jump while loading.

> **Don't** use `assets/logo/primary-original.jpg` on the web. It carries a cream box that shows as a rectangle on any other background.

### Buttons and links

| Element | Style | Tokens |
|---|---|---|
| Primary button | Solid fill, white label in `label` type, `radius-md` corners, at least 44px tall | `surface-brand` + `text-on-brand` |
| Secondary button | Transparent fill, 2px outline, brand-coloured label | border and label `text-link` |
| Tertiary / text link | Underlined text in running copy | `text-link` |
| Destructive action | Error colour with an icon and a clear verb ("Cancel order") | semantic `error` tokens |

- Keep one primary button per view, labelled with a verb: "Order a cake", "Book a table".
- Links in running text are always underlined. Colour alone does not mark a link.
- Honey Glaze is not a button colour on white. If a button sits on a Honey Glaze panel, use the dark text pairing from chapter 4.

### Forms

- Every field has a visible label above it in `label` type. Placeholder text is a hint only and never replaces the label.
- Field borders use `border-strong`, which reaches 3:1 on white and on Flour Cream.
- Errors appear below the field as text plus an error icon, and are summarised at the top of the form on submit, with links to each field. Never mark an error by a red border alone.
- Mark required fields with the word "required", not only an asterisk.
- Collection and delivery forms (if offered) ask for allergies or dietary needs in a free-text field, not a tick-list alone.

### Interactive states

| State | Treatment |
|---|---|
| Hover | Darken the fill one scale step (for example `primary-700`); links lose or thicken the underline |
| Focus | The `focus` ring from chapter 13, never removed; on brand-coloured surfaces use `focus-on-brand` |
| Active / pressed | One further step darker, no movement larger than 1px |
| Disabled | Reduced-contrast fill **plus** a reason in text ("Choose a collection date first"); prefer keeping the button active and explaining what is missing |
| Selected | A tick icon and text label as well as colour |

> **Accessibility** Disabled styling is exempt from contrast rules, so never rely on it alone. Tell people why an action is unavailable.

## Favicons and app icons

The favicon set uses the tree-and-pip symbol in white on a Pinecone Brown tile, so it stays visible in both light and dark browser tabs, and because the full emblem's lettering cannot survive at 16–48px. All files and the `<head>` snippet are in `assets/favicons/`.

{{favicons}}

- Copy every file to the site root and paste `assets/favicons/head-snippet.html` into the `<head>` of every page. The snippet already sets the browser theme colour to Pinecone Brown.
- The maskable icon keeps the symbol inside the central safe zone (the inner 80% circle), so Android can crop it to a circle, squircle or square without clipping the pip.
- At 16px and 32px the pip becomes a few pixels. Check the favicon in a real browser tab on light and dark browser themes before launch. If it reads as a speck, ask the designer for a favicon-only version with a slightly larger pip.

> **Don't** use the full emblem as a favicon or app icon, or place the symbol on Honey Glaze or Forest Pine for these files. One icon colourway everywhere builds recognition.

## Open Graph and link previews

- Size: 1200 × 630px, PNG or JPG under 1MB. A template is in `assets/social/web/`.
- Layout: a Flour Cream or Pinecone Brown background, the emblem (correct variant for the background) left of centre, and a short headline in `h2` Fraunces. Keep text and logo inside the central 1080 × 560px, because platforms crop the edges.
- Product photography can fill the image if the emblem sits on a solid panel, never directly on the photo.
- Always set `og:image:alt` describing the image, for example "A loaf of seeded rye on a wooden board, with the Pip & Pine Bakery logo".

## Email templates

| Spec | Rule |
|---|---|
| Width | 600px single column, fluid down to 320px |
| Text | Live HTML text, at least 14px (16px recommended), line height at least 1.5 |
| Fonts | Fraunces and Source Sans 3 as web fonts where supported, with Georgia (headings) and Arial (body) fallbacks |
| Buttons | Bulletproof HTML buttons (not images), at least 44px tall, `surface-brand` + `text-on-brand` |
| Images | Every image has alt text; decorative images have empty alt; key messages never live only in an image |
| Logo | Transparent PNG of the emblem, 120px wide displayed (240px file), on a Flour Cream or white header band with at least 16px padding |
| Footer | Bakery name and postal address in text, unsubscribe link, plain-language reason for receiving the email |

**Dark mode:** some email apps invert backgrounds. Because the full-colour emblem is a single dark brown, it can disappear on an inverted dark background. Place it inside a solid Flour Cream or white table cell with padding, so the cell protects it, or supply the light single-colour version via a dark-mode media query where the email platform supports it. Test in Apple Mail, Gmail and Outlook (light and dark) before every new template goes live.

> **Do** write a real subject line and preview text; they are the first brand impression in the inbox.

> **Don't** send an email that is one large image. It fails screen readers, blocks in many inboxes, and cannot be read on small screens.

## Email signatures

Keep signatures short, friendly and text-first:

```text
Name Surname (she/her)
Role, Pip & Pine Bakery
Phone number
Website address
```

- Pronouns are optional and the individual's choice.
- Type: the email app's default sans-serif (Arial or Calibri) at 10–11pt or 14px; name in bold. Do not install brand fonts into signatures, because recipients will not have them.
- Optional logo: the tree-and-pip symbol as a PNG at 2×, displayed 24–80px wide, with empty alt text (`alt=""`) because the name appears as text beside it. Use the full emblem only at 96px or wider. Every word of the signature must also exist as text, so it works with images blocked.
- No quotes, animated GIFs, seasonal banners or social icons without text labels, unless the brand team approves a campaign banner for a set period.

## Video and webinars

- **Title cards:** Flour Cream or Pinecone Brown background, emblem (correct variant) centred, title in Fraunces. Hold for at least 3 seconds; follow chapter 10 for any logo animation.
- **Lower thirds:** name in `label` weight Source Sans 3, role below, on a solid Pinecone Brown or Flour Cream bar with radius `radius-md`. Keep them inside the title-safe area (the inner 90% of the frame).
- **Captions:** accurate, human-checked captions on every video, as a burned-in option for social and as `.srt`/`.vtt` files for web players. Source Sans 3 or the player default, white or Flour Cream text on a Pinecone Brown or black box at 80% or more opacity, no more than two lines of about 32–42 characters.
- **End cards:** emblem plus one call to action in text (for example the website address), for 3–5 seconds.
- **Thumbnails:** a clear photo of the bake or person, a headline of no more than five words in Fraunces on a solid panel, and the symbol in a corner; never text set directly over a busy photo.
- **Webinars and online events:** use a branded background or slide (chapter 17) rather than a virtual background that crops the presenter's hands, and offer live captions.

> **Accessibility** Provide a transcript for recorded videos and audio-describe anything shown but not said (for example, a step in a recipe demonstration).
