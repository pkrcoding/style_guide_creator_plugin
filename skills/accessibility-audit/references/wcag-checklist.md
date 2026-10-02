# WCAG 2.2 checklist for brand guidelines and assets

Level A and AA criteria most relevant to brand systems, with how a style guide addresses each.

| SC | Name | Level | Brand guide responsibility |
|---|---|---|---|
| 1.1.1 | Non-text content | A | Alt text rules; logo alt text; decorative images; complex image alternatives |
| 1.2.2 | Captions (prerecorded) | A | Video caption requirement and style |
| 1.2.3 / 1.2.5 | Audio description | A / AA | Describe visuals that carry meaning; descriptive transcripts |
| 1.3.1 | Info and relationships | A | Real headings, lists and table headers in documents and web |
| 1.3.3 | Sensory characteristics | A | No "click the green button on the right" |
| 1.4.1 | Use of colour | A | Links underlined; states with icon and text; chart patterns and labels |
| 1.4.2 | Audio control | A | No autoplaying audio |
| 1.4.3 | Contrast (minimum) | AA | Approved pairings at 4.5:1 / 3:1 |
| 1.4.4 | Resize text | AA | Layouts survive 200% |
| 1.4.5 | Images of text | AA | Live text, not text in images (logos excepted) |
| 1.4.10 | Reflow | AA | Grids reflow at 320 CSS px |
| 1.4.11 | Non-text contrast | AA | UI borders, icons, focus and chart marks at 3:1 |
| 1.4.12 | Text spacing | AA | No fixed-height text boxes; spacing tokens tolerate overrides |
| 1.4.13 | Content on hover or focus | AA | Tooltips dismissible, hoverable and persistent |
| 2.1.1 | Keyboard | A | All interactions keyboard-operable |
| 2.2.2 | Pause, stop, hide | A | Carousels, animation and auto-advancing content |
| 2.3.1 | Three flashes | A | Motion and video rules |
| 2.4.2 | Page titled | A | Document and page titles |
| 2.4.4 | Link purpose | A | Descriptive link text |
| 2.4.6 | Headings and labels | AA | Descriptive headings |
| 2.4.7 | Focus visible | AA | Focus style token |
| 2.4.11 | Focus not obscured (minimum) | AA | Sticky headers do not hide focus |
| 2.5.3 | Label in name | A | Visible label text included in the accessible name |
| 2.5.8 | Target size (minimum) | AA | 24×24 CSS px minimum; 44 recommended |
| 3.1.1 / 3.1.2 | Language of page / parts | A / AA | Document language set; foreign phrases marked |
| 3.2.6 | Consistent help | A | Help and contact in a consistent place |
| 3.3.1 / 3.3.2 | Error identification / labels | A | Form patterns |
| 3.3.7 | Redundant entry | A | Do not ask twice |
| 3.3.8 | Accessible authentication (minimum) | AA | No cognitive tests at login |
| 4.1.2 | Name, role, value | A | Icon-only buttons named |

AAA criteria worth recommending where feasible: 1.4.6 (7:1 contrast), 2.3.3 (animation from interactions), 2.4.13 (focus appearance), 2.5.5 (44px targets), 3.1.5 (reading level).

## Manual test script (15 minutes per page or template)

1. Tab through everything. Is focus always visible and is the order logical? Can you reach and operate every control?
2. Zoom to 200% and 400% (or a 320px-wide window). Is there no loss of content and no horizontal scrolling for text?
3. Turn on a screen reader (VoiceOver: Cmd+F5; NVDA: Ctrl+Alt+N). Do the headings list, link list and image descriptions make sense?
4. Switch the OS to dark mode and reduced motion. Do logos and colours still work, and does movement stop?
5. Grayscale the screen. Is all meaning still clear?
6. Print or preview the PDF. Is the reading order right, and are the tags present?
