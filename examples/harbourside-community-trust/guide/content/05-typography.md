# Typography

Many of the people we write for are older, have low vision, or read English as a second language. Our type is chosen to be friendly like our logo and, above all, easy to read: clear letter shapes, generous sizes and plain layouts.

## Our typefaces

{{type.families}}

### Nunito: display

Nunito is a rounded sans-serif. Its soft, rounded stroke ends echo the heavy, rounded letters of "Harbourside" in our logo, so headlines feel part of the same family. (We have not identified the typeface used in the logo itself; Nunito is chosen because it is similar in feel, not because it is the same font.)

- Use **ExtraBold (800)** or **Bold (700)** for the `display`, `h1` and `h2` styles, and **SemiBold (600)** for `h3`.
- Use **Regular (400)** only for large pull quotes.
- Don't use the Light and ExtraLight weights: thin strokes are hard to read for people with low vision.

### Atkinson Hyperlegible Next: body

Atkinson Hyperlegible Next was designed with the Braille Institute for readers with low vision. Letters that are often confused, such as capital I, lower-case l and the number 1, or capital O and zero, are drawn to look clearly different. That makes it a strong fit for older residents and anyone reading in a second language.

- Use **Regular (400)** for body text, **SemiBold (600)** for labels and `h4`, and **Bold (700)** for emphasis.
- Use its true italic for titles and terms only.

### JetBrains Mono: code and reference numbers

Use JetBrains Mono, with the `code` style, only for reference numbers, case IDs, code and data tables on our website. Don't use it for headings or body text.

## Getting the fonts and licences

All three typefaces are free under the **SIL Open Font License 1.1**. You may use them in print, on the web, in apps, on social media, in video and in broadcast, and embed them in PDFs. You must not sell the font files themselves.

- **Website:** self-host the font files (download from Google Fonts) rather than linking to Google's servers, which avoids sending visitor data to a third party. Load only the weights listed above.
- **Desktop (design and office):** download from the Google Fonts specimen pages linked in the table and install them. Staff laptops need IT to install fonts; ask the Communications team.
- **Canva and Google Docs:** Nunito is available in both. Search for Atkinson Hyperlegible in the font menu; if only the original Atkinson Hyperlegible is offered, you may use it.
- **Video and social graphics:** fonts are covered; embed or outline them in exported files.

## Fallbacks and substitutes

When our fonts are not available, use these substitutes so documents still look tidy and stay readable.

| Where | Headings | Body text |
|---|---|---|
| Websites (automatic fallback) | The fallback stack in the table above | The fallback stack in the table above |
| Word, PowerPoint, Outlook (fonts not installed) | Arial, Bold | Verdana, Regular |
| Google Docs and Slides | Nunito, Bold | Atkinson Hyperlegible, or Verdana |
| Email newsletters and signatures | Arial, Bold | Verdana, Arial, sans-serif |

We choose Verdana for body text because, like Atkinson Hyperlegible Next, it is wide and open, with letters that are easy to tell apart at small sizes. Verdana runs wider than our body font, so expect longer documents; reduce the size by no more than one point (and never below the minimums in "Readable text").

> **Don't** send Word or PowerPoint files that rely on our fonts to partners who may not have them. Export a PDF with fonts embedded, or use the substitute fonts.

## Type scale and hierarchy

{{type.scale}}

The scale goes up in steps of about 1.25, from 16px body text. Each style has one job:

- **`display`:** one campaign headline or hero banner per page.
- **`h1`:** the page or document title. Exactly one per page.
- **`h2`, `h3`, `h4`:** sections, sub-sections and card titles. Don't skip levels: an `h3` always sits inside an `h2`.
- **`body-lg`:** the first paragraph of an article, or short introductions.
- **`body`:** all running text.
- **`small`:** captions, dates and legal notes. Never for whole paragraphs.
- **`label`:** buttons, form labels and tags.

Choose heading levels for structure, not for size. Headings should describe what follows ("How to apply for a food parcel", not "Next steps"), because many people jump between headings with a screen reader or by scanning.

On screens narrower than 768px, *proposed:* reduce `display` to 40px, `h1` to 36px, `h2` to 28px and `h3` to 24px, keeping weights and line heights. Body sizes stay the same.

## Readable text

- **Line length:** keep lines to the measure in the type settings, 45–75 characters (about 66 is ideal). On wide screens, limit the text column, not the font size.
- **Line height:** at least 1.5 for body text; 1.1–1.3 for headings, as set in the scale.
- **Paragraph spacing:** leave at least one line of space between paragraphs (`space-4` or more on screen).
- **Alignment:** left-aligned, with a ragged right edge. Never justify text: it creates uneven gaps that make reading harder, especially for people with dyslexia.
- **Capitals:** use sentence case for headings and buttons. Avoid all caps except for a short label of no more than three words.
- **Italics:** no more than one sentence at a time.

### Minimum sizes

| Medium | Body text | Smallest text |
|---|---|---|
| Websites and email | 16px (`body`) | 14px (`small`) |
| Printed letters, leaflets and posters for families and residents | 14pt | 10pt for footnotes and legal lines |
| Reports for partners and internal documents | 12pt | 9pt for footnotes |
| Large-print versions (on request) | 16pt or larger | 14pt |
| Posters and signs | See chapter 18 | — |
| Text on social images | At least 4% of the image height | — |
| Slides | 24pt | 18pt |

Because many readers are older, never set public materials below 14pt body text, and never use 11pt for body text anywhere.

## Emphasis

- Use **bold** for emphasis, sparingly.
- Use *italics* only for titles of publications and to introduce a term.
- Underline is reserved for links. Never underline text for emphasis.
- Don't use colour alone for emphasis: a word in Harbour Blue is not emphasised for someone who can't see the difference.

## Numbers

- In tables, financial summaries and charts, use tabular (equal-width) figures so columns line up. Check that the font supports them in your software (in CSS, `font-variant-numeric: tabular-nums`); if not, right-align the numbers.
- Use lining figures (the default) in interface text.
- Follow the date, time, money and phone number formats in chapter 12.

## Languages

We work with families who speak many languages. Before publishing in any language other than English, check that every character displays correctly.

- **Latin-script languages** such as Polish, Romanian, Lithuanian, Portuguese, Turkish and Vietnamese: both Nunito and Atkinson Hyperlegible Next are published with extended Latin character sets, but check the specific letters before you print, for example Polish ą ę ł ś ź ż, Romanian ș ț (with a comma below, not a cedilla) and Turkish ğ ı ş. Look at the "Glyphs" or "Language support" section on the Google Fonts specimen page.
- **Cyrillic** (for example Ukrainian or Russian): check coverage for each font on its specimen page. If a font lacks Cyrillic, use Noto Sans for that language.
- **Scripts our fonts don't cover**, such as Arabic, Urdu, Persian, Kurdish (Sorani), Bengali, Punjabi (Gurmukhi), Tamil, Amharic or Tigrinya, and Chinese: use the matching **Noto Sans** family (for example Noto Sans Arabic, Noto Sans Bengali, Noto Sans SC), which is also free under the SIL Open Font License. Keep our English headings in Nunito if the page is bilingual.
- **Right-to-left languages** (Arabic, Urdu, Persian): align text to the right, mirror the layout (navigation, icons that point forwards), never add letter-spacing (it breaks joined letters), and don't use italics. Ask a native speaker to check the layout before printing.
- **Translations are often longer than English** (often 20–30% longer). Leave room in layouts rather than shrinking the text.
- **Hyphenation:** turn automatic hyphenation off in English. For other languages, ask the translator.

## Typography accessibility
- Text must stay readable when zoomed to 200%, and websites must allow people to change line, letter and word spacing without content being cut off.
- Never use images of text. Posters and graphics shared online must repeat their words in the post text or alt text.
- For readers with dyslexia, spacing, left alignment, short lines and plain words matter more than any "special" font. Our body font and these rules already serve them well.
- Keep contrast to the approved pairings in chapter 04.

## Typography: do and don't
> **Do** use Nunito for headlines and Atkinson Hyperlegible Next for everything people need to read.

> **Do** set body text at 16px on screen, 14pt in print for families and residents, and 12pt for partner reports.

> **Don't** use more than two typefaces in one design (JetBrains Mono for reference numbers is the only exception).

> **Don't** set long passages in Nunito below 20px, track out (letter-space) body text, or squash text to fit.

> **Don't** use your software's fake bold or fake italic buttons with a font that lacks those styles; install the real weights.
