# Accessibility audit: Harbourside Community Trust

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
| S1 | Serious | Fixed (content + plugin) | Chapter 14 names the right ring per surface. Tokens now include `focus-on-<colour>` for every brand colour, plus `[data-surface]` CSS rules. |
| S2 | Serious | Fixed (content) | Social image text is at least 4% of image height (54px on 1080×1350). |
| S3 | Serious | Fixed (content) | Nothing below 14px on screen. |
| S4 | Serious | Fixed (plugin) | Template text scales with the canvas (supporting line ≥ 54px on 1080px) and uses the body typeface. |
| M1–M3 | Moderate | Fixed (content) | Print minimums aligned (10pt public print; 9pt contact details; legal text 8pt or larger). |
| M4 | Moderate | Fixed (content) | Buttons and standalone controls are 44×44px on all screens; inline-link spacing rule added. |
| M5, M6 | Moderate | Fixed (plugin) | Descriptive per-variant alt text; avatars say "symbol" when the symbol is shown. |
| M7 | Moderate | Fixed (plugin) | Captions on every table; tab stops only on tables that scroll. |
| M8 | Moderate | Fixed (plugin) | Facebook cover safe zone widened to 18% each side for mobile cropping. |
| M9 | Moderate | Fixed (plugin) | Template text sizes scale with the canvas. |
| m1 | Minor | Fixed (plugin) | Header logo has `alt=""` because the h1 beside it names the organisation. |
| m2 | Minor | Fixed (content) | Example hashtag uses a brand hashtag. |
| m3 | Minor | Fixed (plugin) | PNG previews and SVG templates share one layout. |
| Exception | — | Open | The full-colour logo on white (coral line at 2.95:1) is approved as a logotype exception in `logo.fullColourExceptions`. The Communications team must sign it off. |

**Verdict after fixes: Pass.** No Critical or Serious findings remain open. The automated gate (`analysis/validation-report.md`) passes. Manual testing with assistive-technology users is still recommended before publishing.

---

## Original audit report

**Verdict: Fail.** I found 4 Serious, 8 Moderate and 3 Minor issues, and no Critical ones. I did not write `analysis/accessibility-audit.md` because you said not to edit any files. Every contrast ratio quoted in the prose matches `contrast_check.py` (2.84, 2.95, 8.4, 7.1, 5.8 and 6.5 to 1), and the 27 pairings in `brand.json` pass.

| ID | Sev | Where | Issue | WCAG / rule | Fix |
|---|---|---|---|---|---|
| S1 | Serious | `content/14-digital.md:44` (states table, Focus row); `tokens/tokens.css:188,218,246` | The chapter says to use `focus-on-brand` "inside Harbour Blue or Sunset Coral sections". That token is white, and white on Sunset Coral (#f36c5c) is 2.95:1. `brand.json` `focus.onBrand.secondary` and chapter 04 both say `#0c1015`. | 1.4.11, 2.4.7 | Replace the cell with: "`focus` colour on light backgrounds; white ring (`focus-on-brand`) inside Harbour Blue sections; `neutral-950` ring inside Sunset Coral and Tide Blue sections. Never removed". Ask the lead to add a token such as `--focus-on-light-brand: #0c1015`, because the generator only emits the white one. |
| S2 | Serious | `content/13-accessibility.md:68` (Typography table) | "Text at least 24px on a 1080px-wide image" disagrees with chapter 15 line 73 and chapter 05 line 88 (4% of image height, 54px). On a phone, 24px shows at about 9px. | 1.4.3 context; brand body minimum | "Text at least 4% of the image height (54px on a 1080 × 1350 post)" |
| S3 | Serious | `content/13-accessibility.md:67` | "Nothing below 12px. 12–13px only for text people do not need" goes against chapter 05 (14px is the smallest) and chapter 14 email ("never below 14px"). This audience is mostly older readers. | Brand baseline | "Nothing below 14px (`small`), and only for captions and legal lines" |
| S4 | Serious (generator) | `assets/social/*/…-1080x1350.svg` supporting line | The supporting line is 36px (2.7% of height), below the 54px rule. It is also set in Nunito, while chapter 15 says supporting text uses Atkinson Hyperlegible Next. The 65px headline placeholder (29 characters) probably runs past the 907px safe zone. | Brand rule, ch15:73 | Set the supporting line to 54px or more in Atkinson Hyperlegible Next, and shorten the placeholder headline. This needs a plugin fix. |
| M1 | Moderate | `content/16-print-and-stationery.md:39` | Footer "in 9pt" contradicts line 11 and chapter 05 line 84 (10pt minimum). | Brand rule | "…website in 10pt `text-muted`." |
| M2 | Moderate | `content/09-data-visualisation.md:43` | Print chart labels are "9pt", below the 10pt public print minimum. | Brand rule | "…and 10pt in print (9pt only in partner reports)." |
| M3 | Moderate | `content/16-print-and-stationery.md:32` | Contact details at 8pt and legal text at 7pt are too small, and the phone number is the key offline route. | Brand audience rule | "Name 11pt bold, role and contact details at least 9pt; legal text never below 8pt" |
| M4 | Moderate | Target sizes: ch13:96 vs ch07:69 and ch06:73 | Chapter 13 says every link and control is at least 44×44px. Chapters 07 and 06 say 24px, or 44px only on touch screens. The guide's own table-of-contents links are 24px (`style-guide.html:313`). Inline text links cannot meet 44×44. | 2.5.8 | Chapter 13: "…every button and standalone control at least 44 by 44px; inline text links have generous line spacing." Align chapters 06 and 07 to "44 by 44px on all screens". |
| M5 | Moderate | `style-guide.html` logo gallery | All 23 logo variants have the same alt text, "Harbourside Community Trust logo", so screen reader users cannot tell them apart. The symbol is called "logo". | 1.1.1 | Use `alt=""` and let the `figcaption` carry the meaning, or describe each one, for example "Symbol, single-colour dark knockout". This needs a renderer fix. |
| M6 | Moderate | `style-guide.html` social avatars | The alt text "Logo on a white background" is wrong: the image is the symbol only, with no wordmark. | 1.1.1 | "Harbourside Community Trust symbol: coral sun over waves in a blue circle" |
| M7 | Moderate | `style-guide.html`, 77 tables | 57 tables have no `<caption>`. Each `role="region"` is named only by its first column header (for example "Part" or "Version") and has `tabindex="0"`, which adds 77 tab stops. | 1.3.1, 2.4.3, 4.1.2 | Add captions, use `aria-labelledby` pointing to the caption, and add `tabindex` only when the table overflows. |
| M8 | Moderate (generator) | Facebook cover template | The side safe zone is too narrow. | Brand safe zone | Fix in the plugin. |
| M9 | Moderate (generator) | LinkedIn cover SVG | The supporting line is too small. | Brand rule | Fix in the plugin. |
| m1 | Minor | `style-guide.html` header | The logo alt text repeats the h1 text next to it. Chapter 03 line 141 says to use `alt=""` when the name is already there as text. | 1.1.1 good practice | Set `alt=""`. |
| m2 | Minor | `content/13-accessibility.md:157` | The example hashtag #LocalFirst is not a brand hashtag. The counts agree across chapters 11, 13 and 15 (no more than 3). | Consistency | "…for example #HarboursideTrust…" |
| m3 | Minor (generator) | Social PNG previews vs SVG templates | The PNG previews centre the logo, but the SVG templates and chapter 15 line 66 put it bottom-left. The SVG `guides` layer is visible, while chapter 15 line 62 calls it "hidden". | Consistency | Fix in the plugin, or change line 62 to "a `guides` layer you must hide before export". |

I checked and found no problem with these:
- The logo background tests: knockout versions on light neutral, coral and primary are legible.
- The 32px favicon.
- The avatar: the symbol fills its circle.
- Rendered page basics: one h1, no skipped heading levels, a skip link, copy buttons that announce through `aria-live`, reduced-motion, print and dark-mode styles.
- The rule on Sunset Coral and Tide Blue as text, which is consistent across chapters 04, 07, 09, 13, 14, 15 and 16.

**Handoff**
- **Files written:** none (report only).
- **Proposed changes:**
  - Make the S2 and S3 edits and the M1 to M4 edits in the chapter prose.
  - Add a dark focus token for light brand surfaces (S1). It needs a token or generator change, not a `brand.json` edit, because `focus.onBrand` is already correct.
  - Plugin fixes needed: renderer (M5, M6, M7, m1) and generator (S4, M8, M9, m3).
- **Open issues:** sign-off on the coral logotype exception (2.95:1) and on the cropped symbol are still pending.
agentId: a60ec32d9602d70fa (use SendMessage with to: 'a60ec32d9602d70fa', summary: '<5-10 word recap>' to continue this agent)
