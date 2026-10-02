# Accessibility audit: Pip & Pine Bakery

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
| S1 | Serious | Fixed (content) | Text on photos sits on a Pinecone Brown or Forest Pine panel (≥ 80%) or a solid Flour Cream panel; never white on Honey Glaze. |
| S2 | Serious | Fixed (plugin) | Favicons are drawn on a solid Pinecone Brown tile with the white symbol, matching chapter 14. |
| M1–M5 | Moderate | Fixed (content) | Hashtag and emoji limits, minimum sizes, email signature sizes and caption-box styling are consistent across chapters. |
| M6 | Moderate | Fixed (plugin) | Covers are sized from the safe zone and phone display width. Where the full badge can't meet its minimum, the symbol is used. |
| M7 | Moderate | Fixed (content) | Generic "Accessibility" sub-headings renamed per chapter. |
| m1–m3, m6 | Minor | Fixed (plugin) | Header alt is empty; logo variant and avatar alt text are descriptive; every table has a caption. |
| m4, m5 | Minor | Fixed (content) | Header symbol size and chart gap rule aligned. |

**Verdict after fixes: Pass.** No Critical or Serious findings remain open. The automated gate (`analysis/validation-report.md`) passes. Manual testing with assistive-technology users is still recommended before publishing.

---

## Original audit report

# Accessibility audit: Pip & Pine Bakery style guide (WCAG 2.2 AA)

**Verdict: Fail. Two Serious findings must be fixed before handover.** I did not write `analysis/accessibility-audit.md` because you asked for a read-only audit. Contrast ratios come from `contrast_check.py`. Image colours were sampled with Pillow.

| ID | Severity | Where | Issue | WCAG SC | Fix |
|---|---|---|---|---|---|
| S1 | Serious | `content/15-social-media.md:92` | "80% opaque panel in a brand colour" allows Honey Glaze. White text on 80% Honey Glaze over a white photo is 1.89:1. | 1.4.3 | Replace with: "a Pinecone Brown or Forest Pine panel at 80% or more opacity with white text, or a solid Flour Cream panel with Pinecone Brown text. Never Honey Glaze behind white text." Both checked: brown 5.71:1, pine 4.7:1 at worst case. |
| S2 | Serious | `assets/favicons/icon-32.png`, `icon-48.png`, `icon-192.png` vs `14-digital.md:56` | The chapter says the favicon is a white symbol on Pinecone Brown, but the files are a brown symbol on a transparent background. In dark browser tabs that is 1.59:1 (#202124) and 1.19:1 (#35363a), below the brand's own 3:1 logo rule. | 1.4.11 | Regenerate the favicons as a white symbol on a #5a3a29 tile, like `apple-touch-icon.png` already is. |
| M1 | Moderate | `12-writing-style.md:114` vs `15-social-media.md:152-159` | Hashtag limits contradict: chapter 12 says no more than 3; chapter 15 allows 3 to 5 on Instagram and TikTok. | — | Pick one. Suggest changing the chapter 15 table to Instagram 3 and TikTok 3. |
| M2 | Moderate | `12:113` vs `15:174, 188, 306` | Emoji limits contradict: chapter 12 says 2 per post, chapter 15 says 3. | — | Use "no more than 3" in all three chapters (or 2 in all). |
| M3 | Moderate | `09:34`; `05:56`; `16:61`; chapter 13 typography table | Minimum sizes contradict. Chart text is 12px / 8pt in chapter 09 but 14px / 9pt in chapter 13. Menus are 14pt (05), 12pt (16) and 11pt (13). | 1.4.4 | Chart text at least 14px / 9pt. Hand-held menus at least 12pt, counter menus read at arm's length at least 14pt, stated the same way in 05, 13 and 16. |
| M4 | Moderate | `14-digital.md:104` | The email signature allows the emblem at up to 80px wide, below the 96px minimum. Its alt text "Pip & Pine Bakery" also differs from the standard in 03 and 13. | 1.1.1 | "Symbol only, 24 to 80px wide. Emblem only at 96px or wider." Use `alt=""` because the name appears as text beside it. |
| M5 | Moderate | `14-digital.md:111` vs `15:106`; `10:40` points to chapter 14 | Caption box styling differs: chapter 14 says "semi-opaque dark box", which is unmeasurable; chapter 15 says Pinecone Brown or black at 80% or more. | 1.4.3 | In chapter 14, use "Pinecone Brown or black box at 80% or more opacity", which is 5.71:1 at worst case. |
| M6 | Moderate | `assets/social/linkedin/linkedin-cover-1512x256.png` | The emblem is 220px tall with only 18px above and below it. The clear-space rule in chapter 03 needs about 55px. | Brand rule | Scale the emblem to no more than 170px tall, centred. That is still about 127px on screen, above the 96px minimum. |
| M7 | Moderate | `style-guide.html` | Six generic h3 headings called "Accessibility" (in 03, 05, 06, 07, 10 and 19). As a side effect, chapter 13's anchor became `#accessibility-5`. | 2.4.6 | Rename them, for example "Logo accessibility" and "Typography accessibility". |
| m1 | Minor | HTML header | Logo alt text repeats the h1 name next to it, against the guide's own rule (`03:123`). | 1.1.1 | Use `alt=""` on both header logo images. |
| m2 | Minor | HTML, 14 logo-variant images | All 14 share the alt text "Pip & Pine Bakery logo". The figcaptions do carry the variant names. | 1.1.1 | Use `alt=""` and let the figcaption describe the variant, or make the alt text match the caption. |
| m3 | Minor | HTML, avatar previews | Alt text says "logo on a light neutral background". The image is actually the symbol on Flour Cream (#fbf4e4). | 1.1.1 | "Pip & Pine Bakery tree-and-pip symbol on Flour Cream". |
| m4 | Minor | `03:66` vs `14:12` | The symbol's size in a header is 32px or more in one chapter and 40px or more in the other. | — | Use 40px or more in both. |
| m5 | Minor | `09` series order | Neutral-500 next to Pinecone Brown is 2.77:1, but the 2px gap rule only covers Brown next to Honey. | 1.4.11 | Apply the 2px gap to all adjacent series. |
| m6 | Minor | HTML tables | 53 of the 73 tables have no `<caption>`. Every one does have a labelled region. | 1.3.1 | Add captions when convenient. |

**Already correct:**
- White on Honey Glaze is ruled out in chapters 04, 07, 13, 14 and 17.
- Pinecone Brown next to Forest Pine (1.29:1) and the CVD warning are covered in 04, 09 and 13.
- The 96px / 25mm emblem and 24px / 8mm symbol minimums are consistent everywhere else.
- CamelCase hashtag rules agree.
- There is one h1, no skipped heading levels and no vague link text.
- The skip link and the aria-live region on the copy buttons are present.
- I found no invented facts: claims are marked "Proposed", and `02:17` says no history has been stated.

## Handoff

- **Files:** none written, at your request. Audited: `/private/tmp/claude-501/-Users-praveenrajendran-dev-claude-plugins-style-guide-creator-GitHub/368f2b3c-4834-433b-92e1-a886beba3ae5/scratchpad/build/pip-and-pine-bakery/guide/`
- **Proposed `brand.json` changes:** none required.
- **Assumptions:** dark browser-tab colours #202124 and #35363a are typical Chrome values. Panel worst case assumes a white photo area behind the panel.
- **Open issues:** S1 and S2 block handover. Regenerating the favicons and the LinkedIn cover (M6) needs `make_assets.py` or a designer.
agentId: a98a4a50d4d335d12 (use SendMessage with to: 'a98a4a50d4d335d12', summary: '<5-10 word recap>' to continue this agent)
