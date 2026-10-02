# Accessibility audit: Northwind Labs

This record has two parts:
1. **Resolution:** the status of every finding, checked against the current files in this folder.
2. **Original audit:** the accessibility-auditor agent's report, word for word. It was written during the plugin run and returned to the lead agent rather than saved, so it is preserved here.

Statuses:
- **Fixed (content):** the lead agent corrected it in the chapter text during the run.
- **Fixed (plugin):** fixed in the plugin's scripts after the run; this example was then rebuilt with the fixed plugin.
- **Open:** still needs a human decision or action.

## Resolution

| ID | Severity | Status | Notes |
|---|---|---|---|
| S1 | Serious | Fixed (content) | Chapter 09 no longer claims the series alternate in lightness, and requires labels plus line style, marker or pattern. |
| S2 | Serious | Fixed (content) | Chapter 14 email body text is at least 16px with line height of at least 1.5. |
| M1 | Moderate | Fixed (content) | Chart text minimum aligned to 14px. |
| M2 | Moderate | Fixed (content) | The '#ad' disclosure exception is documented. |
| M3 | Moderate | Fixed (content) | Logo minimum is 160px throughout; header logo rule updated. |
| M4 | Moderate | Fixed (content) | Print minimum is 8pt. |
| M5 | Moderate | Fixed (content) | Document line spacing is at least 1.5. |
| M6 | Moderate | Fixed (plugin) | Callouts render as `<div role="note">`, not unnamed `<aside>` landmarks. |
| M7 | Moderate | Fixed (plugin) | Every table has a caption (from a `Table:` line or, hidden, from the section heading). Only tables that actually scroll become focusable regions. |
| M8 | Moderate | Fixed (plugin) | Each logo variant has its own alt text, e.g. "Northwind Labs logo, single colour, white (reversed), with cut-out details". |
| M9 | Moderate | Open | Templates now place the logo bottom-left at a readable size, but chapter 15 asks for the symbol top-left. The design team should choose one placement and update either the templates or the chapter. |
| M10 | Moderate | Fixed (plugin) | Gallery and chart wrappers are no longer `<figure>` elements, so the PDF tags only real images as Figures, each with alt text. Run PAC 2024 before publishing. |
| N1 | Minor | Fixed (content) | Daybreak Amber on Fjord Teal (2.9:1) added to "never combine". |
| N2 | Minor | Fixed (content) | Logo alt text is consistent. |
| N3 | Minor | Fixed (content) | The diverging-palette midpoint is covered. |
| N4 | Minor | Fixed (content) | Email signature logo is 160–200px. |
| N5 | Minor | Fixed (plugin) | Favicons are drawn on a solid Fjord Teal tile, with the white cut-out symbol. |
| N6 | Minor | Fixed (plugin) | Covers are sized so the logo stays at or above its minimum width at phone display size (360px). |

**Verdict after fixes: Pass.** No Critical or Serious findings remain open. The automated gate (`analysis/validation-report.md`) passes. Manual testing with assistive-technology users is still recommended before publishing.

---

## Original audit report

I found no Critical issues, but 2 Serious ones. **The guide does not pass yet.** The automated quality gate passes, and it checked all 28 colour pairings. The problems are in what the chapters tell people to do, and in rules that contradict each other.

I didn't write `analysis/accessibility-audit.md`, because you told me not to edit any files. The findings are below instead.

## Serious

**S1. The chart palette doesn't do what chapter 09 says.** `content/09-data-visualisation.md` line 15 (Categorical palette); WCAG 1.4.1 and 1.4.11.
- **Problem:** the text says the order "alternates lightness" so series stay distinct in greyscale. Measured:
  - Series 2 against series 4 (`#b97500` / `#6a89ab`) is 1.03:1. In greyscale they come out almost identical (#848484 and #868686).
  - Series 1 against series 2 is 1.59:1.
  - On dark backgrounds, series 1 against 2 is 1.33:1 and series 3 against 4 is 1.14:1.

  This also breaks chapter 13 line 31: "3:1 against the background and neighbours".
- **Fix, line 15:** "Every colour reaches at least 3:1 against its background. Neighbouring series are **not** guaranteed to differ in lightness, so every series also needs a direct label and its own line style, marker shape or pattern."
- **Fix, chapter 13 line 31:** change "and neighbours" to "and a 1px background-colour gap between adjacent segments".

**S2. The email body size is below the brand minimum.** `content/14-digital.md` line 89; brand baseline (body text at least 16px).
- **Problem:** it says "Body text is at least 14px (16px recommended)".
- **Fix:** "Body text is at least 16px with a line height of at least 1.5."

## Moderate

- **M1. Chart text minimum is different in two chapters.** Chapter 09 line 92 says 12px; chapter 13 line 80 says 14px.
  - **Fix, chapter 09:** "at least 14px on screen (the `small` token)".
- **M2. The "#ad" rule contradicts the hashtag rule.** Chapter 15 line 238 puts "#ad" at the start; chapter 15 line 151 and chapter 13 line 187 say hashtags go at the end.
  - **Fix, add to both:** "The one exception is the disclosure label '#ad' or 'Ad', which goes at the start of the post."
- **M3. The logo minimum size is wrong or broken in two places.** The minimum in `brand.json` is 160px.
  - Chapter 15 line 72 says "98px minimum". **Fix:** change it to "160px minimum".
  - Chapter 14 line 12 sets the header logo at 32–40px high, or 28–32px on mobile. The logo is about 4.8 times wider than it is high, so that gives 133–191px wide, which is below the minimum. **Fix:** "Set the logo at least 34px high (160px wide). Where that does not fit, use the symbol at 32px."
- **M4. Print minimum sizes are below chapter 05's 8pt.** Chapter 16 lines 18 and 32 say 7pt; chapter 18 line 91 says 6pt.
  - **Fix:** "Minimum text size is 8pt." Keep 6pt only where the law sets that size.
- **M5. Line spacing in documents is below the baseline.** Chapter 17 line 70 says "at least 1.15"; the baseline is 1.5 (WCAG 1.4.12).
  - **Fix:** "line spacing at least 1.5".
- **M6. Callouts create 112 extra page sections.** In `style-guide.html`, every Do/Don't callout is an unnamed `<aside>`, so screen reader users get 112 unnamed sections in the landmark list (WCAG 1.3.1).
  - **Fix:** change the renderer to output `<div class="callout" role="note">`.
- **M7. 56 of the 76 tables have no caption.** Their scroll regions take their names from the first header cell, for example `aria-label="Mandatory (must follow)"` (WCAG 1.3.1 and 2.4.6).
  - **Fix:** give every table a `<caption>` named after its heading, and use that for the `aria-label`.
- **M8. The 22 logo variant images all have the same alt text, "Northwind Labs logo".** Screen readers hear the same phrase 22 times (WCAG 1.1.1). The variant names are already in the figure captions.
  - **Fix:** describe each variant, for example "Northwind Labs logo, white single-colour knockout", or use `alt=""` and let the caption name it.
- **M9. Social templates break chapter 15's own rule.** Chapter 15 line 71 puts the symbol top-left on every branded graphic. The LinkedIn post templates centre the full logo instead. On the square post, "LABS" is about 14px tall, so about 6px once the feed shrinks the image.
  - **Fix:** use the symbol at 65–86px, top-left.
- **M10. The PDF may have figures with no alt text.** `style-guide.pdf` is tagged, with language, bookmarks and table headers. But I counted 108 `/Figure` tags and only 54 alt text entries. That probably means the `<figure>` wrappers were tagged without alt text, but I haven't confirmed it.
  - **Fix:** run PAC 2024, and mark the wrappers as `Div` or give them alt text.

## Minor

- **N1. A failing pairing is missing from chapter 04.** "Never combine" (line 55) leaves out Daybreak Amber on Fjord Teal, which is 2.9:1. Chapter 15 line 87 already warns about it.
  - **Fix, add:** "Daybreak Amber text, icons or chart marks on Fjord Teal (2.9:1)."
- **N2. Logo alt text differs between chapters.** Chapter 13 says "Northwind Labs logo"; chapter 14 lines 92 and 108 say "Northwind Labs".
  - **Fix:** use "Northwind Labs" everywhere, and "Northwind Labs home" when the logo links to the home page.
- **N3. Chapter 09 line 41 needs to cover the diverging midpoint.** It says light steps need outlines but only covers sequential palettes. The diverging midpoint, `neutral-50`, is 1.07:1 on white.
  - **Fix:** extend that sentence to diverging palettes.
- **N4. The email signature logo has no room above the minimum.** Chapter 14 line 108 says "no wider than 160px", which is also the minimum.
  - **Fix:** "160–200px wide".
- **N5. The favicons are hard to read at small sizes.** At 16px and 32px the amber peak on teal (2.9:1) blurs. The teal circle against a dark browser tab is 2.71:1.
  - **Fix:** use the white peak (knockout) for the 16px and 32px files.
- **N6. The LinkedIn cover logo will drop below the minimum on phones.** It is about 600px wide in a 1512px image, so about 150px when shown on a phone.
  - **Fix:** make it at least 660px wide in the artwork.

## Checked and fine

- **Page structure:** one h1, no skipped heading levels, `lang="en-GB"`, a working skip link and a named nav.
- **Focus and controls:** the focus ring is 3px with sufficient contrast, the copy buttons announce their result, and reduced motion is respected.
- **Contrast and reflow:** dark mode and print themes pass contrast, and nothing in the CSS blocks reflow at 320px.
- **Amber rules:** chapters 04, 07, 13, 14, 17 and 18 all ban Daybreak Amber text on white.
- **Logo backgrounds:** the background tests look correct.

## Handoff
1. **Files written:** none.
2. **Proposed `brand.json` change:** `logo.altText` = `"Northwind Labs"`.
3. **Assumptions:** none new.
4. **Open issues:**
   - Fix S1 and S2 before handover.
   - M6, M7 and M10 need changes to the renderer and the asset generator.
   - M9 and N5 need the social templates and favicons regenerated.
agentId: a2fd267fb40a87fb3 (use SendMessage with to: 'a2fd267fb40a87fb3', summary: '<5-10 word recap>' to continue this agent)
