# Typography

Our readers are often reading numbers that matter: emissions totals, heat-risk scores, grid loads. Our typography has to make those numbers clear first and express the brand second. It should feel as confident and precise as the logo's heavy, geometric wordmark.

## Our typefaces

We use three free, open-licence families. Each has one job.

| Role | Typeface | Weights we use | Why it fits |
|---|---|---|---|
| Display | Manrope | 600, 700, 800 | A geometric sans with a sturdy build, like the heavy lowercase of our wordmark. Its open shapes keep large headlines friendly, not cold |
| Body | Inter | 400, 600, 700 | Designed for screens, with a large x-height, open shapes and clear figures. It stays readable in dense dashboards and long reports |
| Data and code | JetBrains Mono | 400, 600 | Monospaced, with a clearly different 0 and O, and 1, l and I. Use it for identifiers, station codes, API examples and aligned data |

Manrope and Inter are similar in spirit but not identical. This is deliberate: the display face gives character, and the body face gives comfort over long reading. We are not claiming that the wordmark is set in Manrope. The wordmark is artwork and must never be retyped.

**Weights not to use:** do not use Manrope below 600, or light and thin weights of any family. Thin strokes break up on low-quality projectors and in print. Use Inter 700 sparingly, for emphasis inside text and for table headers.

{{type.families}}

## Where to get them and the licence

All three families are on Google Fonts under the **SIL Open Font License 1.1**. You may use them free of charge for commercial work, including websites, apps, print, social media, video and broadcast. You may embed them in apps and PDFs. You may not sell the font files on their own.

- **Websites:** self-host the WOFF2 files with our site assets rather than loading them from a third-party server. This is faster and avoids sending visitor data to another company. Load only the weights listed above, and use `font-display: swap`.
- **Desktop:** download the families from Google Fonts and install them. Ask IT if you cannot install fonts yourself.
- **Agencies:** may download the fonts directly. There is no licence to transfer.

## Fallbacks and substitutes

Fallback stacks are in the table above. They use each operating system's own sans-serif so text stays readable while the brand fonts load.

When the brand fonts are not available:

| Where | Use |
|---|---|
| Microsoft Office, if fonts cannot be installed | Arial for headings and body |
| Google Docs and Slides | Manrope and Inter are available in the font menu. Use them |
| Email (HTML templates and signatures) | `Arial, Helvetica, sans-serif` |
| Code in documents | Consolas or Menlo |

Never mix a substitute with a brand font in the same document. Use one or the other.

## Type scale and hierarchy

The scale steps up by a ratio of 1.25 from the `body` size. Use the tokens; do not set sizes by eye.

{{type.scale}}

How to build a page:

- Use **one `h1`** per page or document. It names the page.
- Never skip a level. An `h3` sits under an `h2`.
- Headings describe what follows ("Heat risk by ward, summer 2026"), not labels ("Results").
- Use `display` only for campaign headlines and hero banners, once per page.
- Use `body-lg` for the introduction under a page title.
- Use `small` for captions, sources and footnotes, never for paragraphs.
- Use `label` for buttons, form labels and tags.
- Use `code` (JetBrains Mono) for identifiers, units in tables when aligned, and code.

On screens narrower than 768px, `display`, `h1` and `h2` may step down one level in size (for example, `h1` set at the `h2` size), keeping their weight and order.

## Readable text

- **Line length:** keep text between 45 and 75 characters per line, aiming for 66.
- **Line height:** at least 1.5 for body text, as set in the scale.
- **Paragraph spacing:** at least `space-4` between paragraphs. Do not indent first lines.
- **Alignment:** left-aligned, with a ragged right edge. Never justify text; it creates uneven gaps that slow down readers with dyslexia.
- **Capitals:** use sentence case for headings and buttons. Use all capitals only for short labels of three words or fewer, with added letter spacing.
- **Italics:** never set whole paragraphs in italics.

**Minimum sizes**

| Medium | Minimum |
|---|---|
| Screen body text | The `body` token |
| Screen captions and metadata | The `small` token |
| Print body text | 11pt (12pt for public-facing reports) |
| Print footnotes | 8pt |
| Slides | 24pt |
| Social images | Text at least 4% of the image height |
| Signage | See chapter 18 |

## Emphasis

- Use **bold** (Inter 600 or 700) for emphasis.
- Use *italics* only for titles of publications and for introducing a technical term. Manrope has no italic, so never italicise headings.
- Underline only links.
- Never fake bold or italic with software effects or outlines.

## Numbers

Numbers are our product, so set them carefully.

- Use **tabular figures** (`font-variant-numeric: tabular-nums`) in tables, dashboards and any column of numbers, so digits line up.
- Use lining figures everywhere else (Inter's default).
- Right-align numbers in tables and keep the same number of decimal places in a column.
- Put a non-breaking space between a number and its unit (12 °C, 450 MWh, 3.2 tCO₂e).
- Use true subscripts for chemical formulae such as CO₂, not a lowered "2".
- For date, time and number formats, follow chapter 12.

## Languages

Our locale is British English. Manrope, Inter and JetBrains Mono all cover Latin-script European languages. Coverage of other scripts, such as Cyrillic, Greek and Vietnamese, differs between the three families, so check each family's language list on Google Fonts before setting any language other than English.

- **Right-to-left scripts** (for example Arabic or Hebrew): use a typeface designed for that script, chosen with a native-speaking designer. Mirror the alignment to the right. Never add letter spacing to Arabic.
- **Chinese, Japanese and Korean:** fall back to a matching system face (for example Noto Sans CJK) and increase line height.
- **Hyphenation:** turn automatic hyphenation off for headings. In body text, allow it only in narrow columns.

## Typography accessibility
- Text must still work when it is resized to 200%, with nothing cut off or overlapping.
- Layouts must allow users to increase letter, word and line spacing without breaking.
- Never use images of text, except for the logo. Charts must have their labels in real text where possible.
- For readers with dyslexia, spacing, left alignment and short lines help more than any "special" font. Our rules above cover this.

## Typography: do and don't
> **Do** use tabular figures in every table and dashboard.

> **Do** keep to two families on a page, plus JetBrains Mono only where data or code needs it.

> **Don't** add letter spacing to body text.

> **Don't** set long text in Manrope below 20px. Switch to Inter.

> **Don't** retype the "Northwind Labs" wordmark in Manrope or any other font. Use the logo file.

> **Don't** justify text or set paragraphs in all capitals.
