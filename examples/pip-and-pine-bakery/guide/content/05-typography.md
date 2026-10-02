# Typography

Type carries most of what we say: menus, prices, ingredients, allergen notes and posts. Our typefaces echo the classic serif in the logo while staying easy to read on a chalkboard-style menu, a phone screen or a printed label.

## Our typefaces

{{type.families}}

| Role | Typeface | Why it fits | Weights |
|---|---|---|---|
| Display | Fraunces | A warm, old-style serif with soft, slightly bulbous details. It shares the traditional, handmade feel of the PIP & PINE wordmark without copying it | Regular 400, SemiBold 600, Bold 700 |
| Body | Source Sans 3 | A clear, friendly sans-serif with open shapes, a generous x-height and distinct I, l and 1. It keeps long text and small labels readable | Regular 400, SemiBold 600, Bold 700 |
| Mono | JetBrains Mono | Fixed-width figures for order numbers, codes and data tables | Regular 400, SemiBold 600 |

Fraunces is used for headings and short display lines; Source Sans 3 for everything else. Avoid thin and light weights (below 400): they break up on screens, menus and receipts.

Fraunces is a variable font with extra design axes. Leave optical sizing on (`font-optical-sizing: auto`), and if your tool shows the "Wonky" (WONK) or "Soft" (SOFT) axes, keep them at their defaults so headings look the same everywhere.

> **Note** The PIP & PINE wordmark is drawn artwork. Fraunces is a companion, not the logo's font. Never retype the name in Fraunces to imitate the logo.

## Where to get them and the licence

All three families are free from Google Fonts under the SIL Open Font License 1.1. The licence allows commercial use in print, websites, apps, social media, video and broadcast, and embedding in documents and apps. You may not sell the fonts on their own.

- **Websites:** self-host the WOFF2 files (download from Google Fonts or the projects' official repositories) for speed and privacy, or link Google Fonts. Load only the weights listed above.
- **Desktop:** install from the Google Fonts specimen pages for design tools, Word and PowerPoint.
- **Apps:** bundle the font files with the app and include the licence text.

## Fallbacks and substitutes

| Situation | Display substitute | Body substitute |
|---|---|---|
| Web (while fonts load, or if they fail) | The fallback stack in the table above | The fallback stack in the table above |
| Word, PowerPoint, Google Docs without brand fonts | Georgia | Arial or Calibri |
| Email | Georgia, serif | Arial, Helvetica, sans-serif |

Shared documents should use the substitutes unless every recipient has the brand fonts; otherwise their software swaps the font unpredictably.

## Type scale and hierarchy

{{type.scale}}

- Use one `h1` per page or document, matching its title.
- Don't skip levels: `h2` follows `h1`, `h3` follows `h2`. Choose a heading level for structure, then style it with the matching token.
- Headings describe the content below them: "Opening hours", not "Info".
- `display` is for one campaign headline per page or poster. `body-lg` introduces a page. `small` is for captions and legal lines, never full paragraphs. `label` is for buttons, form labels and tags.
- `h1` to `h3` use Fraunces; `h4` and below use Source Sans 3 so small headings stay crisp.

## Readable text

- **Line length:** keep text containers to 45–75 characters per line, aiming for 66.
- **Line height:** at least 1.5 for body text; headings use the line heights in the scale.
- **Paragraph spacing:** leave at least 1em between paragraphs, using spacing token `4`.
- **Alignment:** left-aligned. Never justify body text; the uneven gaps make reading harder, especially for people with dyslexia. Centre only short lines, such as a two-line poster headline or an emblem sign-off.
- **Capitals:** keep all-caps to labels of three words or fewer. The spaced capitals in BAKERY belong to the logo, not to our text style.
- **Minimum sizes:** screen body 16px; print body 11–12pt; menus held in the hand 12pt or more; menus read at arm's length 14pt or more; social on-image text at least 4% of the image height. Signs follow chapter 18.

## Emphasis

- Use **SemiBold or Bold** for emphasis.
- Use *italics* only for titles of works and terms being defined, never for whole paragraphs.
- Underline is reserved for links.
- Don't use colour alone for emphasis; it is lost for some readers and in black-and-white print.

## Numbers

- Use tabular figures (`font-variant-numeric: tabular-nums`) in price lists, tables and order summaries, so columns line up.
- Use lining figures in interface text and headings.
- Write prices, dates and times as set out in chapter 12, for example "£3.50" and "Saturday 4 October".

## Languages

Our locale is English (UK). Fraunces and Source Sans 3 cover Latin-based European languages; Source Sans 3 also covers Greek, Cyrillic and Vietnamese. Check the Google Fonts specimen page before setting another language. If we add a right-to-left language, mirror the layout and alignment and never add letter-spacing to Arabic. For Chinese, Japanese or Korean, pair Source Sans 3 with Noto Sans in the relevant script. Turn on automatic hyphenation for narrow columns only, and never hyphenate headings.

## Typography accessibility

- Text must resize to 200% without loss of content, and layouts must survive user overrides of line height (1.5), paragraph spacing (2×), letter spacing (0.12em) and word spacing (0.16em).
- Never use images of text for menus, prices, opening hours or allergen information. Live text can be enlarged, translated and read aloud.
- For readers with dyslexia, spacing, left alignment and short lines matter more than special fonts. Our scale already builds them in.
- Keep text colours to the approved pairings in chapter 04.

## Typography: do and don't
> **Do** pair a Fraunces heading with Source Sans 3 body text, and stop there: two families plus the mono for data.

> **Do** use the type tokens (`h2`, `body`, `label`) rather than picking sizes by eye.

> **Don't** set long text in Fraunces below 20px; switch to Source Sans 3.

> **Don't** letter-space body text, or fake bold and italic by slanting or outlining letters. Use the real weights.

> **Don't** set menus or price lists in all capitals or italics.
