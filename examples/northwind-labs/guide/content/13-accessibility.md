# Accessibility

Our dashboards, reports and campaigns help city sustainability officers, utility engineers, investors and partners make decisions about climate risk. If someone cannot see a chart, use a keyboard, follow a video or read a PDF, they cannot act on our data, so accessibility is part of being precise, not an extra.

## Our commitment

We design and build everything to **WCAG 2.2 Level AA**. This applies to every channel: websites, dashboards and apps, documents and PDFs, presentations, email, social media, video, print and events. Agencies, freelancers and partners working on Northwind Labs material must meet the same standard.

### Working with public sector clients

Many of our clients are UK and European public bodies. Websites, apps and documents they publish are often covered by the [Public Sector Bodies (Websites and Mobile Applications) Accessibility Regulations 2018 on legislation.gov.uk](https://www.legislation.gov.uk/uksi/2018/952/contents/made), explained in the [GOV.UK guidance on accessibility requirements for public sector websites and apps](https://www.gov.uk/guidance/accessibility-requirements-for-public-sector-websites-and-apps). Across the EU, procurement usually refers to the harmonised standard EN 301 549, which includes WCAG.

This guide is not legal advice. For each contract:

- Check the accessibility clauses in the tender or contract before design starts.
- Ask the client which standard and version they report against, and who maintains their accessibility statement.
- Give the client the information they need for that statement: what we tested, how, and any known issues with dates for fixing them.
- Refer legal questions to the client's accessibility lead or to legal advisers.

> **Accessibility** If a client asks for a higher standard than this guide, the client's requirement wins. Never deliver to a lower one.

## Colour and contrast

Contrast keeps text and data readable for people with low vision, on projectors and on phones in daylight.

| What | Minimum contrast | WCAG 2.2 |
|---|---|---|
| Body text, labels, table text (below 24px, or below 18.66px bold) | 4.5:1 | 1.4.3 |
| Large text (24px and above, or 18.66px bold and above) | 3:1 | 1.4.3 |
| Input borders, toggles, icons and other controls | 3:1 against what is next to them | 1.4.11 |
| Chart lines, bars, map areas and other meaningful graphics | 3:1 against the background, with a 1px background-colour gap between adjacent segments | 1.4.11 |
| Focus indicator | 3:1 against adjacent colours | 1.4.11, 2.4.7 |

Use the approved pairings in Chapter 4, Colour. They have already been checked. Key rules:

- Use Fjord Teal (`primary-600`) and Polar Night freely for text on white and light neutrals.
- Never use Daybreak Amber for text, icons or thin lines on white or light backgrounds. It fails contrast there. Use it for large decorative areas, or put Polar Night text on it. When you need amber text on a light background, use `accent-600`.
- Daybreak Amber is close in hue to our warning colour. Keep brand amber out of warning messages, and never use it alone to signal a problem.
- For text over photography or maps, use a solid panel or scrim and check the busiest part of the image, not the average.

### Checking a new combination

1. Check the pairing in Chapter 4 first.
2. If it is not there, test it in any WCAG contrast checker, such as the WebAIM contrast checker or the Colour Contrast Analyser.
3. Brand team members can run `contrast_check.py` with `--use body`, `--use large` or `--use ui`, and `--cvd` to check colour-vision deficiency.
4. Ask the brand team to add any new approved pairing to the guide so others can reuse it.

> **Do** check text contrast against the actual background it sits on, including tinted cards and image scrims.

> **Don't** set captions, labels or links in Daybreak Amber on white, even at large sizes.

## Never use colour alone

About 1 in 12 men and 1 in 200 women have a colour-vision deficiency. In our palette, these pairs can look alike (WCAG 2.2 SC 1.4.1):

- Fjord Teal with Success or Info (tritanopia).
- Success with Warning or Error, and Warning with Error (protanopia and deuteranopia).

So every meaning carried by colour also needs text, an icon, a pattern or a position.

- **Links:** underline links in body text. Colour alone does not count.
- **States:** pair success, warning, error and info colours with an icon and a word, for example "Error: enter a postcode".
- **Charts:** label series directly at the end of lines or on bars. Where series overlap, add line styles (solid, dashed, dotted) or fill patterns, and different marker shapes.
- **Maps:** label key areas, use patterns or hatching as well as fills, and show values in tooltips and a linked table.
- **RAG ratings:** write the status ("On track", "At risk", "Off track") next to every red, amber or green indicator.

> **Don't** show a "good versus bad" comparison using only teal and green, or only green and red.

## Accessible charts, dashboards and maps

Data products are our core work, so they must work for screen reader users, keyboard users and people with low vision or cognitive disabilities. Chapter 9, Data visualisation, sets the visual style. These rules make it accessible.

### Every chart

- **Title that states the finding:** "Peak demand fell 12% after the retrofit" is better than "Peak demand 2020–2025". (Example only.)
- **Short alt text** naming the chart type and the key message, plus **a text summary** of two or three sentences next to the chart.
- **A data table** with the same numbers, either visible below the chart or one keyboard step away ("Show data table"). Tables need a caption and header cells (SC 1.3.1).
- **Contrast** of at least 3:1 for every line, bar, point and segment against the background, and gaps or borders between adjacent segments.
- **Direct labels** instead of, or as well as, a legend.
- Axis labels and tick text at least 14px (`small`), set in Inter or JetBrains Mono with tabular figures.
- Start bar charts at zero, and state units and the data source in text.

### Interactive dashboards

- Every filter, tab, chart point and tooltip can be reached and used with a keyboard, in a logical order (SC 2.1.1, 2.4.3).
- Tooltips open on focus as well as hover, stay visible while the pointer is over them, and close with Esc (SC 1.4.13).
- Anything that needs dragging, such as range sliders or brushing, also has a single-pointer alternative, such as buttons or number inputs (SC 2.5.7).
- Targets are at least 24×24px, and 44×44px for touch (SC 2.5.8).
- Announce updates, such as "Showing 14 results", with a polite live region (SC 4.1.3).
- Live or auto-refreshing data has a pause control if it moves or updates automatically for more than 5 seconds (SC 2.2.2).
- Layouts reflow at 320px wide and at 400% zoom without losing content. Where a chart cannot reflow, the data table must (SC 1.4.10).
- Login screens do not depend on memorising or transcribing codes without an alternative, such as password managers and copy-paste (SC 3.3.8).

### Maps

- Provide the same information outside the map: a sortable table or list by area, and a written summary of the main pattern.
- Zoom and pan with visible buttons and the keyboard, not only by dragging or scrolling.
- Do not trap keyboard focus inside the map. Give a "Skip map" link.
- Use sequential colour scales that change clearly in lightness, so they still work in greyscale.

> **Do** ship every chart with a text summary and a data table.

> **Don't** publish a chart or map as a flat image with no text alternative, in a dashboard, report or social post.

## Typography

| Medium | Minimum size | Notes |
|---|---|---|
| Web and apps: body | `body` (16px) | Never smaller for paragraphs |
| Web and apps: captions, metadata | `small` (14px) | Short, non-essential text only. Nothing below 12px |
| Print: body | 11pt | 12pt for reports to public bodies |
| Large-print versions | 16pt | 14pt is the absolute floor |
| Slides | 24pt | 18pt for footnotes and sources |
| Social images | Large enough to read on a phone without zooming | Repeat the text in the post |

- Line height at least 1.5 for body text, with clear space between paragraphs.
- Lines of 45 to 75 characters.
- Left-align text. Never justify it, because uneven gaps slow down readers, including many dyslexic readers.
- Avoid long passages in capitals or italics. The spaced capitals in our logo are a logo feature, not a text style.
- Do not use Manrope or Inter below weight 400 for text.
- Text must resize to 200% and reflow at 320px without being cut off or overlapping (SC 1.4.4, 1.4.10), and survive users increasing letter, word and line spacing (SC 1.4.12).
- Use real text, not images of text, except for the logo (SC 1.4.5).

## Focus and interaction

Keyboard users, switch users and many screen reader users rely on the focus indicator to know where they are. Our focus style is a solid Fjord Teal outline, offset from the element, with a lighter teal on dark surfaces and a contrasting colour inside brand-coloured sections:

{{focus}}

- Never remove the focus outline (`outline: none`) without replacing it with this style.
- Sticky headers, cookie banners and chat widgets must not cover the focused element (SC 2.4.11).
- Everything that works with a mouse works with a keyboard, with no keyboard traps (SC 2.1.1, 2.1.2).
- Buttons say what they do ("Download the report"). Links make sense out of context. Avoid "click here".
- Forms have visible labels, instructions before the field and errors described in text (SC 3.3.1, 3.3.2). Do not ask for the same information twice in one process (SC 3.3.7).
- Keep the help and contact link in the same place on every page (SC 3.2.6).

> **Do** test every new component by tabbing through it before review.

## Images and alt text

Alt text tells people who cannot see an image what it shows and why it is there (SC 1.1.1). Keep it to about 125 characters, and do not start with "Image of".

| Type | What to write | Example |
|---|---|---|
| Informative | The content and why it matters | "Engineer checking a substation sensor on a frosty morning" |
| Functional (a link or button) | Where it goes or what it does | Logo linking home: "Northwind Labs home" |
| Decorative | Nothing: `alt=""` in HTML, and leave the platform field empty | Background texture, divider graphic |
| Complex (chart, map, infographic) | Short alt text plus a full text alternative nearby | "Line chart of city heat-risk days, 2015–2025. Full data in the table below." |
| Logo | The organisation's name | "Northwind Labs" ("Northwind Labs home" when it links to the home page) |

> **Don't** write keyword-stuffed alt text or repeat the caption word for word.

## Video and audio

- **Captions** on every video, checked by a person for accuracy, names and technical terms. Edit automatic YouTube captions before publishing (SC 1.2.2).
- **Audio description** or a described transcript when visuals carry information that the narration does not, such as a chart appearing on screen (SC 1.2.5). Narrating the key numbers in the script avoids the need for a separate description track.
- **Transcripts** for podcasts, webinars and audio clips.
- **No autoplay with sound.** Autoplaying silent loops must have pause controls.
- For live webinars, provide live captions and share slides in an accessible format beforehand.

## Motion and flashing

- Follow the reduced-motion rule in Chapter 10, Motion. When the user has turned on reduced motion, replace movement with short fades and stop parallax, carousels and looping animation.
- Nothing flashes more than three times per second (SC 2.3.1).
- Anything that moves, scrolls or auto-updates for more than 5 seconds has pause, stop or hide controls (SC 2.2.2). This includes animated chart transitions on loop and data tickers.

## Documents and PDFs

Reports for public bodies are often republished on their websites, so they must be accessible from the start. Chapter 17, Presentations and documents, has the templates.

- Use the template's built-in heading, list and caption styles. Never fake headings with bold text.
- Set the document title and language (English, United Kingdom) in file properties.
- Give images and charts alt text, and add a data table or summary for every chart.
- Tables have a header row that repeats across pages. Avoid merged and empty cells.
- Check the reading order, especially for text boxes, sidebars and footnotes.
- Export **tagged PDFs** with bookmarks for documents over 10 pages, and check them with the Word or PowerPoint Accessibility Checker and then a PDF checker such as PAC or Adobe Acrobat's accessibility check.
- Where the client publishes online, offer an HTML version. Public bodies in the UK are encouraged to publish in HTML rather than PDF.

> **Do** build the accessibility into the Word file. Fixing tags in a finished PDF takes much longer.

## Social media

Chapter 15, Social media, has the full accessibility rules for each platform. In short:

- Write alt text in the platform's alt text field for every image, and repeat any on-image text in the post.
- Caption every video, and burn captions in for short clips that autoplay without sound.
- Write hashtags in CamelCase, such as #ClimateData, and put them at the end. The one exception is the disclosure label '#ad' or 'Ad', which goes at the start of the post.
- Use emoji sparingly, at the end of sentences, never in place of words.
- Never use "fancy" Unicode letters for bold or italics. Screen readers cannot read them.

## Events and physical spaces

For workshops, conferences and stands, we:

- Publish step-free access, accessible toilets, parking and the nearest transport in the invitation.
- Ask every attendee about access needs when they register, and act on the answers.
- Offer, on request, large-print and digital copies of materials, live captioning (CART), sign language interpretation (BSL in the UK, or the national sign language elsewhere) and a hearing loop.
- Provide a quiet space and step-free routes to the stage and stands.
- Use signage that follows the contrast and size rules in Chapter 18.

## Testing and sign-off

Automated tools find only part of the issues, so every release combines automated and manual checks.

1. **Automated:** run axe, WAVE or Lighthouse on every page or dashboard view, and the document checkers above.
2. **Keyboard:** complete every task with the keyboard only. Focus must stay visible and follow a logical order.
3. **Screen readers:** test with NVDA on Windows, VoiceOver on macOS and iOS, and TalkBack on Android.
4. **Zoom and reflow:** 200% and 400% zoom, a 320px-wide window, and increased text spacing.
5. **Colour:** greyscale and colour-vision simulations of charts and maps, plus Windows contrast themes.
6. **Content:** alt text, captions, headings, link text and plain language.
7. **People:** for products and major releases, include disabled people in user research and testing, and pay them for their time.

*Proposed — confirm with leadership:* the Marketing team signs off brand and communications material, and the product owner for each dashboard or app signs off digital products. Nothing is published or handed to a client with an open Critical or Serious accessibility issue.

## Getting help and accessible formats

For accessibility questions, or to ask for any Northwind Labs material in another format (large print, accessible Word, plain text, Easy Read or audio), email [hello@northwindlabs.example](mailto:hello@northwindlabs.example).

*Proposed — confirm with leadership:* we reply within 2 working days and agree a delivery date with the person who asked.
