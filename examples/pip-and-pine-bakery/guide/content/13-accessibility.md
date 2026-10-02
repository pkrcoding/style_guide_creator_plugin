# Accessibility

Everyone should be able to read our menu, check an allergen, find the door and enjoy what we post, whatever their eyesight, hearing, mobility or way of thinking. Accessible design is also clearer design: a price ticket that a customer with low vision can read is quicker for every customer in the queue.

## Our commitment

We design to **WCAG 2.2 level AA**. This chapter turns that standard into practical rules for everything that carries the Pip & Pine Bakery name: the website, emails, documents and PDFs, social media, printed menus and price tickets, shop signage, packaging and labels, and events.

These rules are a minimum, not a target to aim near. If a rule here seems to conflict with another chapter, the accessibility rule wins. Tell the Brand and Marketing team so that we can fix the other chapter.

*Proposed — confirm with leadership:* publish an accessibility statement on the website that names the standard we aim for, known gaps, and how to contact us. We have not published one yet, so do not refer to one until it exists.

## Colour and contrast

Contrast is the difference in brightness between text and its background. Low contrast is the most common accessibility failure, and it gets worse on a phone in sunlight or under warm shop lighting.

| What you are making | Minimum contrast | WCAG 2.2 |
|---|---|---|
| Body text, captions, prices, allergen text | 4.5:1 | 1.4.3 |
| Large text: 24px or more, or 18.66px or more in bold (about 18pt, or 14pt bold, in print) | 3:1 | 1.4.3 |
| Icons, input borders, buttons, chart lines and bars | 3:1 against what is next to them | 1.4.11 |
| Focus indicator | 3:1, at least 2px thick | 1.4.11, 2.4.7 |
| Logo | Exempt in WCAG, but we require 3:1 | 1.4.3 note |

### Use the approved pairings

The approved text and background combinations, with their measured ratios, are in the **Colour** chapter (chapter 4). Pick from that table first. The points people most often get wrong:

- **Honey Glaze is decorative on light backgrounds.** It measures 2.25:1 on white and 2.05:1 on Flour Cream, so never use it for text, icons or anything people need to read. For honey-coloured text, use Honey Glaze 600 (`accent-600`), which passes on both white and Flour Cream.
- **Flour Cream is a warm page colour, not a free pass.** Pinecone Brown, Forest Pine and Honey Glaze 600 are approved for text on it. Lighter steps of any colour are not.
- **White text on Honey Glaze fails** (2.25:1). Put dark text on Honey Glaze panels: `neutral-950` for body text, or Pinecone Brown for large text and icons.
- **Text over photographs** needs a solid panel or a dark scrim behind it. Measure the contrast over the busiest, lightest part of the photo, not the average. A loaf on a flour-dusted board is much lighter than it looks.

### Check a new combination

1. Use any WCAG contrast checker (for example, the one built into your browser's developer tools, or a free online checker) and compare the ratio with the table above.
2. The brand team can run `contrast_check.py` from the style guide toolkit, for example `contrast_check.py "#8d6300" "#fbf4e4" --use body`. It exits with an error if the pair fails.
3. If it passes and you will use it again, ask the Brand and Marketing team to add it to the approved pairings.

> **Do** use Pinecone Brown or `neutral-900` text on white or Flour Cream for menus, labels and long reading.

> **Don't** set prices, allergen information or links in Honey Glaze on a light background.

## Do not rely on colour alone

About 1 in 12 men and 1 in 200 women have a colour-vision deficiency. Colour can support meaning, but something else must carry it too: words, an icon, a pattern, or position (WCAG 1.4.1).

Our own palette has some specific risks, measured with the colour-vision simulator in our toolkit:

- **Pinecone Brown and Forest Pine** look almost the same to people with deuteranopia (red–green colour blindness). They are also very close in brightness for everyone: 1.29:1 against each other. Never use these two to tell things apart, for example two chart series, "in stock" and "sold out", or two product ranges. Add labels, or pair one of them with a much lighter tint.
- **Forest Pine and the error red** can look alike with protanopia. Never use Forest Pine in error or success messages.
- **Forest Pine is close to the success green, and Honey Glaze is close to the warning amber.** Keep brand colours out of status messages so people do not read a decorative green as "approved".
- **Success, warning and error colours** can be confused with one another (protanopia and deuteranopia), and success with info (tritanopia). Every status message needs an icon and a word such as "Sold out", "Error" or "Saved".

The full list of confusable pairs is in the colour-vision section of the **Colour** chapter.

Apply this everywhere:

- **Links:** underline links in body text. Do not rely on a brown or green link colour alone.
- **Form states:** errors are described in text next to the field, not just a red border.
- **Charts and maps:** label series directly, or add patterns or shapes. See the **Data visualisation** chapter.
- **Dietary and allergen labels:** write the word ("Vegan", "Contains nuts") or use a labelled symbol. A green sticker on its own does not mean "vegan" to everyone, and it means nothing to a screen reader.

> **Do** label a sold-out item "Sold out" with a clear symbol, as well as greying it.

> **Don't** use a green dot for vegan and a brown dot for vegetarian with no words.

## Typography

Fraunces is our display face and Source Sans 3 is our body face (see the **Typography** chapter). Both have clear letter shapes. Keep them readable with these rules.

| Medium | Body text | Smallest text allowed |
|---|---|---|
| Web and apps | 16px (`body`) | 14px (`small`, `label`), for short, non-essential text only |
| Email | 16px | 14px |
| Print (leaflets, letters, menus) | 12pt (leaflets and letters may use 11pt); menus read at arm's length 14pt | 9pt, for short legal lines only |
| Large-print versions | 16pt (never below 14pt) | 14pt |
| Social images | Large enough to read on a phone without zooming; repeat the text in the caption | |

- **Line spacing** at least 1.5 times the font size for body text, and paragraph spacing at least 1.5 times the font size. Layouts must still work if someone increases letter, word and line spacing (WCAG 1.4.12).
- **Line length** 45 to 75 characters.
- **Alignment:** left-aligned. Never justify text: uneven gaps between words make it harder to read, especially for dyslexic readers. Centre only short headings and menu item names.
- **Fraunces only at 24px and larger**, for headings. Its detail is lost at small sizes. Use Source Sans 3 for everything smaller.
- **Capitals:** the letter-spaced "BAKERY" in the logo is artwork. Do not copy that style for sentences or ingredient lists. Keep all-caps to labels of three words or fewer.
- **Weights:** do not use weights lighter than 400 for text below 24px. Use bold (600 or 700) for emphasis, not italics, for anything longer than a few words.
- **Zoom and reflow:** web pages must work at 200% zoom and at 320px wide without sideways scrolling or lost content (WCAG 1.4.4, 1.4.10).
- **No images of text.** Menus, prices, opening hours and allergen information must be real text on the website, not a photo or a PDF only (WCAG 1.4.5). The logo is the only exception.

## Focus and interaction

When someone uses a keyboard, switch or voice control, the focus indicator shows where they are on the page. It must always be visible (WCAG 2.4.7). Never remove it with `outline: none` unless you replace it with our focus style.

{{focus}}

- The focus ring is 3px, solid, with a 2px gap between it and the element. It follows the element's corner radius (`radius-md`, 8px, on buttons and cards).
- On light pages it uses Pinecone Brown 600, which measures 5.44:1 on white and 4.96:1 on Flour Cream. On Pinecone Brown or Forest Pine panels, use white. On Honey Glaze panels, use `neutral-950`.
- Sticky headers, cookie banners and chat buttons must not cover the focused item (WCAG 2.4.11).

### Keyboard and targets

- Everything that works with a mouse or a tap must work with a keyboard alone: menus, galleries, order and booking forms, and pop-ups (WCAG 2.1.1). Focus moves in a logical order and never gets stuck (WCAG 2.1.2).
- Targets such as buttons, links in lists and quantity controls are at least 24 × 24 CSS px (WCAG 2.5.8). We recommend 44 × 44 px for anything tapped on a phone, such as "Add to basket" or "+" and "−" buttons.
- Link text says where it goes: "See this week's bread menu", not "click here" or "read more".
- Buttons say what they do: "Reserve a celebration cake", not "Submit".
- **Forms** (if we add ordering, bookings or a mailing list): every field has a visible label, instructions come before the field, and errors are explained in words (WCAG 3.3.1, 3.3.2). Do not ask for the same information twice in one process (3.3.7). Do not make people solve a puzzle or remember a code to log in (3.3.8). Put the help or contact link in the same place on every page (3.2.6).

> **Do** keep the default focus ring or use our brand focus style on every link, button and form field.

> **Don't** hide the focus outline because it "looks untidy".

## Images and alt text

Alt text is the description a screen reader reads out instead of an image. Write it for the purpose of the image in that place, in about 125 characters or fewer. Do not start with "Image of" or "Picture of": screen readers already say that it is an image.

| Type | What to write | Example |
|---|---|---|
| Informative (shows something the reader needs) | What it shows that matters here | "A sourdough loaf with a deep, crackled crust, cut open to show an airy crumb." |
| Functional (a linked image or icon button) | Where it goes or what it does | Basket icon button: "View basket". Instagram icon link: "Pip & Pine Bakery on Instagram" |
| Decorative (adds mood only) | Nothing: `alt=""` in HTML; leave the alt field empty on social media | A sprig of pine used as a page border |
| Complex (charts, infographics, illustrated menus) | A short summary, plus the full information as text nearby | "Bar chart of our most popular loaves this month. The figures are in the table below." |
| Text in an image (poster, offer graphic) | All of the text that matters, in reading order | "Hot cross buns are back. Available every day from 7am until sold out." |

**Logo alt text:** "Pip & Pine Bakery logo". When the logo links to the home page, use "Pip & Pine Bakery home". Use the same alt text for the tree-and-pip symbol on its own. If the bakery name already appears as text right next to the logo, the logo can be decorative (`alt=""`) so the name is not read twice.

**Logo legibility:** do not use the full emblem below 96px on screen or 25mm in print, because the small "BAKERY" line stops being readable. Use the tree-and-pip symbol instead. The full-colour logo fails on black (2.07:1): use the white knockout version on dark backgrounds. See the **Logo** chapter.

> **Do** describe what a customer would want to know: the bake, the filling, the occasion.

> **Don't** write "IMG_2041.jpg", "photo" or a list of keywords as alt text.

## Video and audio

- **Captions on every video**, including short social clips. Check and correct automatic captions before you publish: they often get product names and ingredients wrong, which matters for allergens (WCAG 1.2.2).
- **Say what you show.** In baking and "how it's made" videos, say the steps and quantities out loud ("Fold in 200 grams of chopped walnuts") so blind and partially sighted viewers can follow. If important information is only visual, add audio description or a descriptive transcript (WCAG 1.2.5).
- **Transcripts** for audio-only content such as podcasts or radio interviews.
- **No autoplay with sound.** Video that plays automatically starts muted and has a visible pause button. Anything that moves for more than five seconds needs a pause, stop or hide control (WCAG 2.2.2).
- Keep on-screen text inside the safe zones, on a solid panel, for long enough to read twice.

## Motion

Movement can cause dizziness or nausea for people with vestibular disorders, and can distract people with attention-related conditions.

- Respect the "reduce motion" setting on phones and computers (`prefers-reduced-motion`). When it is on, replace movement with short fades and stop parallax, auto-advancing carousels and looping animation. The detailed timings are in the **Motion** chapter.
- Nothing flashes more than three times in any one second (WCAG 2.3.1). This includes "flashing" offer graphics and fast cuts in videos.
- Avoid parallax scrolling and large zoom effects.
- Carousels do not advance on their own, or they have a clearly labelled pause button.

## Documents and PDFs

Price lists, wholesale catalogues, celebration cake order forms and menus are often shared as documents. Make them accessible at the source, because fixing a finished PDF is slow and unreliable.

- **Use real styles** in Word, Google Docs, PowerPoint or InDesign: Heading 1, Heading 2, lists and table header rows. Do not make text look like a heading by making it bigger and bold.
- **Set the document title and language** (English, United Kingdom) in the file properties.
- **Reading order:** check that text boxes and columns are read in a logical order. In PowerPoint, use the Reading Order pane.
- **Alt text** on every informative image. Mark decorative images as decorative.
- **Tables** only for data, with a header row. No merged or empty cells used for layout.
- **Contrast and colour** follow the rules above.
- **PDFs** are exported as tagged PDFs, with bookmarks for documents of more than about 10 pages. Check them with an accessibility checker such as PAC (free) or Adobe Acrobat's accessibility check.
- **Always publish a web page version** of anything customers need, such as the menu, allergen information and opening hours. A PDF should be an extra, not the only way.

Run the accessibility checker built into Microsoft Office or Google Docs before you share any document. Templates are in the **Presentations and documents** chapter.

## Social media

The full rules are in the accessibility section of the **Social media** chapter (chapter 15). In short:

- Add alt text to every image using the platform's alt text field.
- Caption every video, and check the captions.
- Write hashtags in CamelCase (#FreshBread, not #freshbread) so screen readers read the words correctly. Put them at the end.
- Use emoji sparingly, at the end of a sentence, and never in place of words. Screen readers read out every emoji's name.
- Never use "fancy" Unicode letters for bold or script text. Screen readers skip them or read them as symbols.
- If an image contains text, such as an offer or opening hours, repeat that text in the caption.

## In the bakery and at events

Most of our customers meet us in person, so the shop matters as much as the screen.

### Menu boards, price tickets and labels

The sizes below are *proposed starting points — confirm by testing on site*. Stand at the farthest point where a customer would read the sign, under normal shop lighting, and check it can be read comfortably.

| Item | Proposed minimum |
|---|---|
| Counter menu board, read from 1–3 m | Item names and prices at least 25mm cap height |
| Wall or window board, read from further than 3 m | Add about 8mm of cap height for every extra metre |
| Price ticket in a display case | Price at least 24pt; product name at least 18pt |
| Shelf label or allergen card next to a product | Product name at least 14pt; allergen text at least 12pt |
| Large-print menu (on request) | Body at least 16pt, Source Sans 3, on white or Flour Cream |

- Use Source Sans 3 for prices and allergen information. Do not use decorative script or hand lettering for anything people need to read, including on chalkboards.
- Use dark text on a light background (or white on Pinecone Brown or Forest Pine), with matt finishes to reduce glare from lights and windows. Avoid putting signs behind reflective glass.
- Mount key signs at a height people can read when seated or using a wheelchair, as well as standing.

### Allergen information

UK food law sets legal requirements for allergen labelling, including a minimum text size for mandatory food information. Check the current Food Standards Agency guidance: the legal rules come first, and our brand rules add legibility on top.

- Emphasise allergens in ingredient lists in **bold**, not only in colour.
- Never put allergen information on Honey Glaze, over a photo, or in light grey.
- Keep a full, up-to-date allergen list available as text on the website and on paper in the shop, and make sure staff can read it out on request.

### Access information and signage

- Tell people about access before they visit, on the website and on the Google Business Profile: whether the entrance is step-free, whether there is a ramp or a portable ramp, seating, toilets, and whether there is space for a wheelchair or pushchair at the counter. Describe only what is true. *Proposed — confirm the facts for each shop before publishing.*
- Use the words "step-free access" with an arrow, not a symbol alone.
- Welcome assistance dogs with a clear sign at the entrance.

### Events, tastings and workshops

- Include access information on every invitation, and ask about access needs when people book.
- Offer, on request: large-print and digital copies of recipes and handouts, live captioning (CART), British Sign Language interpretation, and a quiet space or a quieter session time.
- Give a named contact for access requests and say how much notice you need. *Proposed: at least 10 working days for BSL interpreters and captioners.*

## Testing and sign-off

Automated tools find only part of the problem. Every new website page, template, campaign and shop sign is tested in both ways before it is used.

### Automated checks

- Websites and emails: an automated checker such as axe DevTools, WAVE or Lighthouse.
- Brand guide and colour changes: `validate_brand.py` and `contrast_check.py` from the style guide toolkit.
- Documents: the accessibility checker in Microsoft Office or Google Docs, and PAC or Acrobat for PDFs.

### Manual checks

- **Keyboard:** use Tab, Shift+Tab, Enter, Space and the arrow keys to reach and use everything. Check that focus is always visible and never trapped.
- **Screen readers:** test key pages and journeys with NVDA (Windows), VoiceOver (Mac and iPhone) and TalkBack (Android).
- **Zoom and reflow:** zoom to 200% and 400%, and test at 320px wide.
- **Reduced motion:** turn on "reduce motion" and check that animation stops.
- **Print and signage:** print at actual size and read it at real viewing distance. Take a photo in greyscale to check that nothing depends on colour.
- **Alt text and captions:** read them back. Are they accurate and useful?

Involve disabled people in testing, including customers and staff, and pay them for their time. They will find problems that no checklist will.

### Who signs off

*Proposed — confirm with leadership:* the Brand and Marketing team signs off accessibility for brand materials. Anything that fails a Critical or Serious check (for example, text below 4.5:1, missing captions, or colour-only status) is not published until it is fixed.

> **Do** test with a keyboard and a screen reader before any website change goes live.

> **Don't** treat a clean automated report as proof that something is accessible.

## Getting help and accessible formats

If you are not sure whether something meets these rules, ask the Brand and Marketing team before you publish.

Customers can ask for our menu, allergen information and other materials in another format, such as large print, plain text, an accessible digital document, or read aloud by a member of staff. *Proposed — confirm with leadership:* set up one accessibility contact (an email address and a phone number), publish it on the website and in the shop, and reply to requests within 5 working days.
