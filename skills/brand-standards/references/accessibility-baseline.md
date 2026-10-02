# Accessibility baseline (WCAG 2.2 AA)

Everything the style guide recommends must meet this baseline. The success criteria (SC) numbers refer to WCAG 2.2.

## Colour and contrast

| Requirement | Threshold | SC |
|---|---|---|
| Normal text (< 24px, or < 18.66px bold) | 4.5:1 | 1.4.3 |
| Large text (≥ 24px, or ≥ 18.66px bold) | 3:1 | 1.4.3 |
| UI components (input borders, toggles, icon buttons) and states | 3:1 against adjacent colours | 1.4.11 |
| Meaningful graphics (icons, chart lines and bars, infographic parts) | 3:1 | 1.4.11 |
| Focus indicator | 3:1 against adjacent colours, at least 2px thick | 1.4.11, 2.4.7, 2.4.13 (AAA guidance) |
| Logos and logotypes | Exempt from 1.4.3, but this plugin requires 3:1 as best practice | 1.4.3 note |
| AAA (if chosen) | 7:1 normal, 4.5:1 large | 1.4.6 |

- **Use of colour (1.4.1):** never use colour as the only way to show information, state, links or chart series. Underline links in body text. Pair state colours with an icon and text. Label chart series directly or use patterns.
- **Colour-vision deficiency:** about 1 in 12 men and 1 in 200 women have a colour-vision deficiency. Check key colours with `contrast_check.py --cvd`, and separate confusable pairs by lightness, labels or patterns.
- **Text over images:** use a solid or scrim overlay that guarantees the ratio over the busiest part of the image. Measure the worst case, not the average.

## Typography

- Body text at least 16px on screen. Nothing below 12px; 12–13px only for non-essential text. In print, body text 11–12pt minimum, and 14pt for large-print versions.
- Line height at least 1.5 for body text. Paragraph spacing at least 1.5× the font size. Layouts must survive the user overriding text spacing (1.4.12).
- Line length 45–75 characters. Left-aligned (right-aligned for RTL). Never justified.
- Avoid long passages in all caps, italics or light weights (≤ 300) at small sizes.
- Choose typefaces with distinguishable characters: I, l and 1; O and 0; rn and m.
- Text must reflow at 320 CSS px width and zoom to 200% without loss of content (1.4.4, 1.4.10).
- Never use images of text, except logos (1.4.5).

## Interaction (for digital chapters)

- Keyboard access to everything, with a visible focus that is never obscured by sticky headers (2.1.1, 2.4.7, 2.4.11).
- Target size at least 24×24 CSS px (2.5.8). 44×44 recommended for touch.
- Link text makes sense out of context. Buttons say what they do.
- Forms: visible labels, instructions before inputs, errors described in text (3.3.1, 3.3.2). Do not ask for the same information twice (3.3.7). Accessible authentication (3.3.8).
- Consistent help location across pages (3.2.6).

## Motion and media

- Respect `prefers-reduced-motion`. Avoid parallax and large zooms.
- Nothing flashes more than 3 times per second (2.3.1).
- Anything that moves, blinks or scrolls automatically for more than 5 seconds needs pause, stop or hide controls (2.2.2).
- Video: accurate captions (1.2.2), audio description or a descriptive transcript where visuals carry meaning (1.2.5), and no autoplaying audio.
- Audio and podcasts: transcripts.

## Images and alt text

- Informative images: describe the content and purpose in about 125 characters or fewer. Do not start with "Image of".
- Logos: "[Organisation] logo", or "[Organisation] home" when the logo links home.
- Decorative images: empty alt in HTML (`alt=""`); omit the description on social media.
- Complex images (charts, infographics): short alt text plus a full text alternative nearby, such as a data table or summary.

## Documents

- Use real heading styles, lists and table headers. Set the document language and title. Make the reading order logical.
- Add alt text to images. Do not use colour alone. Use contrast as above.
- PDFs are tagged, with bookmarks for documents over about 10 pages, and checked with an accessibility checker (e.g. PAC or Acrobat).

## Social media

- Alt text on every image (use the platform field), and video captions burned in or uploaded and reviewed.
- Hashtags in CamelCase (#BrandValues). Put them at the end, three to five maximum.
- Emoji: sparing, never in place of words, never repeated in strings, and at the end of sentences. Screen readers read every emoji name aloud.
- No "fancy" Unicode letters (𝗯𝗼𝗹𝗱, 𝓈𝒸𝓇𝒾𝓅𝓉). Screen readers read them as symbols or skip them.
- Put text in images in the caption as well. Keep on-image text short and high-contrast, inside safe zones.
- Plain language. Spell out acronyms. Links described in words.

## Cognitive accessibility and plain language

- Aim for a reading age of about 9–11 years (UK) or US grade 6–8 for public content. Use short sentences and active voice.
- Use consistent terms. One idea per paragraph. Front-load key information.
