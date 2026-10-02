# Presentations and documents

Tender responses, council reports and investor decks are where we win or lose work. Public-sector buyers must publish accessible documents themselves, and they may score suppliers on whether ours are accessible too. A well-built template makes every document on-brand and accessible by default, so you can focus on the content.

All templates are owned by the Marketing team. Request them from hello@northwindlabs.example; do not build your own from an old file.

## Fonts in Office and Google tools

Manrope, Inter and JetBrains Mono are free under the SIL Open Font License, so anyone can install them. However, documents we send outside are opened on computers that do not have them, and Word and PowerPoint then substitute fonts unpredictably.

| Use | Brand font (installed) | Office substitute for shared files |
|---|---|---|
| Headings | Manrope | Arial bold |
| Body | Inter | Arial |
| Data, code, IDs | JetBrains Mono | Consolas |

- **Templates for external editing** (tender forms, Word documents clients will edit, procurement portal uploads): use the substitutes. Arial is installed on every Windows and Mac computer and in Microsoft 365 on the web.
- **Internal or PDF-only documents:** use the brand fonts. When exporting to PDF, the fonts are embedded, so recipients see them correctly.
- **PowerPoint on Windows:** you may embed the brand fonts (File > Options > Save > Embed fonts in the file). Check the file on a Mac before sending, because embedding support differs.
- **Google Docs and Slides:** Manrope, Inter and JetBrains Mono are available under "More fonts".

*Proposed — confirm with leadership:* Arial and Consolas are the official substitutes. Aptos (the Microsoft 365 default) is a reasonable alternative inside Microsoft 365, but it is not available in older Office versions or Google tools.

## Slide templates

**Format:** 16:9 (1920 × 1080 px, or 13.33 × 7.5 in in PowerPoint). Keep all text and logos inside a safe area of 64px from every edge so nothing is cropped on projectors.

| Layout | Use | Brand treatment |
|---|---|---|
| Title | Opening slide | Polar Night background, single-colour light logo top left, title in Manrope |
| Section | Divider between parts | Fjord Teal background, white title, symbol bottom right |
| Content | Heading and up to 6 bullet points | White background, small full-colour logo bottom left |
| Two-column | Comparison, text and image | White, 2 equal columns |
| Image | One full-bleed photo with a caption | Caption on a solid panel, never directly on the photo |
| Quote | Client or partner quote | Neutral-50 background, quote in Manrope, attribution in Inter |
| Data | One chart with a takeaway headline | White, chart colours from chapter 9 |
| End | Contact and call to action | Polar Night, single-colour light logo, hello@northwindlabs.example |

- Slide text is at least 24pt; titles 36–44pt. If text will not fit at 24pt, split the slide.
- One idea per slide. Write the takeaway as the slide title (an illustrative example: "Street-level heat data shows where tree planting cools most"), not a topic label ("Results").
- Daybreak Amber is for small highlights: a rule under a title, a key data point marker. Never for text on white; on dark slides, Daybreak Amber text on Polar Night is approved.
- The logo appears once per slide at most, in the same place, and is never animated by slide transitions.

## Accessible slides

1. Build every slide from a layout in the master. Never add free text boxes for content; they fall outside the reading order.
2. Give every slide a unique title, even if you hide it visually. Screen-reader users navigate by titles.
3. Check and fix the reading order (PowerPoint: Home > Arrange > Selection Pane, or the Reading Order pane).
4. Add alt text to every meaningful image and chart. Mark decorative images as decorative.
5. Never put text inside images. Charts must have a text summary in the notes or on the slide.
6. Use real lists and table header rows.
7. Run the built-in checker (PowerPoint: Review > Check Accessibility; Keynote and Google Slides: review manually against this list) and fix every error before sending.
8. Avoid auto-advancing slides and flashing transitions. Use fade or no transition.

## Document templates

We maintain Word templates (`.dotx`) and Google Docs equivalents for:

| Template | Typical use |
|---|---|
| Report | Council and utility reports, research summaries |
| Proposal / tender response | Procurement responses, statements of work |
| Letter | Formal correspondence on the digital letterhead (chapter 16) |
| Policy | Internal and published policies, accessibility statements |

### Rules for every document

- Use the built-in styles: Title, Heading 1, Heading 2, Heading 3, Normal, List Bullet, List Number, Caption. Never fake a heading by making text bold and bigger.
- One Heading 1 per document (usually the title), and never skip levels.
- Body text at least 11pt (12pt recommended), line spacing at least 1.5, left-aligned, never justified.
- Tables: simple grids with a header row marked as "Repeat as header row", no merged or empty cells used for layout. Add a caption above each table.
- Links have descriptive text ("Download the 2026 heat-risk methodology"), never a bare URL or "click here".
- Use colour from the approved text pairings in chapter 4 only. Headings in Polar Night or Fjord Teal; never Daybreak Amber text on white.
- Cover pages: logo top left, title in Heading style, then date, version and document owner.
- Run Review > Check Accessibility in Word and fix every error.

## Tagged PDFs

Most tender and council documents end up as PDF. Export them as **tagged PDF** so screen readers can follow the structure.

- In Word: File > Save As > PDF > Options, and tick "Document structure tags for accessibility" and "Create bookmarks using headings".
- Set the document title (File > Info > Properties > Title) and language (English UK) before exporting. Set the PDF to display the document title, not the file name.
- Check the PDF with an accessibility checker such as the Adobe Acrobat Accessibility Checker or the free PAC tool, and fix reading order, alt text and table headers.
- Never scan a document to PDF as an image. If you must share a signed form, also provide the accessible version.

> **Accessibility** A public-sector client may need to publish our report on their website. If it is not accessible, they cannot publish it, and that reflects on us.

> **Do** start every document from the current template and its styles.

> **Don't** paste slides or pages as images into another document; the text becomes unreadable to assistive technology and search.

## File naming and version control

- Name files `northwind-labs-[client or project]-[document type]-[yyyy-mm-dd]-v[n].[ext]`, for example `northwind-labs-cityname-tender-response-2026-10-02-v3.docx`. Use lowercase and hyphens, no spaces.
- Mark drafts with "DRAFT" in the header, and remove it before issue.
- Keep one source file in the shared drive. Do not email edited copies back and forth.
- Record the version, date and owner in the document properties and on the cover of reports and proposals.
