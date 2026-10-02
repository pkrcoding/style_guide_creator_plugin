# Accessibility

Many of the people we serve are older residents. Many others speak English as a second language, have a disability, or rarely go online. If they cannot read, hear or use something we make, we have not helped them. Accessibility is part of being kind, fair and local first, so this chapter applies to everyone who makes anything for Harbourside Community Trust.

## Our commitment

Everything we publish meets **WCAG 2.2 level AA**. That includes our website, Facebook, Instagram, LinkedIn and WhatsApp posts, documents and PDFs, letters, posters, signs, videos and events. Where this chapter sets a higher bar than AA, such as larger touch targets or larger print, we follow the higher bar because of who our audiences are.

We always offer a way to get help that does not need the internet. Every leaflet, post, page and letter that asks people to do something also gives a phone number or an in-person option.

### The law in the UK

- **Equality Act 2010:** as a service provider, we must make reasonable adjustments for disabled people. We should plan for them in advance, not only when someone asks. This applies to us now.
- **Public Sector Bodies (Websites and Mobile Applications) (No. 2) Accessibility Regulations 2018:** these apply to our council partners. Charities are usually exempt. They can apply to a charity that is mostly publicly funded, or that provides services which are essential to the public or aimed mainly at disabled people. *Proposed — confirm with the trustees whether they apply to us.* Either way, council contracts may require us to meet WCAG 2.2 AA and publish an accessibility statement, and we do both.

> **Note** We publish an accessibility statement on our website. It says how well the site meets WCAG 2.2 AA, lists known problems, and explains how to report a problem or ask for another format. The Communications team reviews it every 12 months.

## Colour and contrast

Contrast is the difference in brightness between text and its background. Many older readers find low contrast hard to read, especially in daylight or on a cracked phone screen.

| What | Minimum contrast | WCAG 2.2 |
|---|---|---|
| Text under 24px (or under 18.66px bold) | 4.5:1 | 1.4.3 |
| Large text, 24px or more (or 18.66px bold or more) | 3:1 | 1.4.3 |
| Buttons, form borders, icons that carry meaning, chart lines and bars | 3:1 against what is next to them | 1.4.11 |
| Focus indicators | 3:1, at least 2px thick | 1.4.11, 2.4.7 |

The approved colour pairings are listed in the Colour chapter (chapter 4). Use those first. Our brand colours behave differently:

- **Harbour Blue** passes for text of any size on white.
- **Sunset Coral** is 2.95:1 on white. Use it only for decoration and large shapes. For coral text, links or icons on white, use `secondary-600`.
- **Tide Blue** is 1.77:1 on white. Use it only for decoration and backgrounds behind dark text. For text, use `accent-600`.

The full-colour logo on white is an approved exception, because logos are exempt from the contrast rule. "Community Trust" in Sunset Coral is hard for some people to read, so the logo must never be the only place our name appears. Always write "Harbourside Community Trust" in real text nearby, for example in the page title, the first line of a post or the letter heading.

### Checking a new combination

1. Look for the pairing in chapter 4.
2. If it is not there, check it with any WCAG contrast checker, such as the WebAIM Contrast Checker.
3. The brand team can also run `contrast_check.py FG BG --use body` (or `--use large`, or `--use ui`). The script fails any pairing below the threshold.
4. Ask the Communications team to add new approved pairings to the brand data. Do not use an unapproved pairing in the meantime.

For text over photos, put the text on a solid panel or a dark scrim. Measure the contrast against the busiest, lightest part of the photo, not the average.

> **Do** use `secondary-600` for coral text and Harbour Blue for links on white backgrounds.

> **Don't** set text in Sunset Coral or Tide Blue on white, even in headlines.

## Do not rely on colour alone

About 1 in 12 men and 1 in 200 women see colour differently. Others print in black and white or use high-contrast settings. Colour must never be the only way to show something (WCAG 1.4.1).

- **Links in body text** are always underlined.
- **Errors, warnings and success messages** have an icon and a text label, such as "Error: enter your postcode". Keep Sunset Coral out of error messages: it looks like the error colour. Keep Harbour Blue and Tide Blue out of information messages for the same reason.
- **States** such as selected, required or unavailable are shown in words or with an icon as well as with colour.
- **Charts and maps** label each series or area directly, or use patterns and different line styles. Success, warning and error colours look alike to many people with colour-vision deficiency, and so do Sunset Coral and the success green. Never let a reader tell these apart by colour alone. See Data visualisation (chapter 9).

> **Don't** write "the items in red are full". Write "Full" next to each item.

## Typography

Our body typeface, Atkinson Hyperlegible Next, was designed for people with low vision. Its letters, such as I, l and 1, are easy to tell apart. Set it well, or the benefit is lost.

| Medium | Body text | Notes |
|---|---|---|
| Web and apps | `body` (16px) minimum. Use `body-lg` (20px) for pages aimed at older residents | Nothing below 14px (`small`), and only for captions and legal lines |
| Social images | Text at least 4% of the image height (54px on a 1080 × 1350 post) | Repeat the words in the caption |
| Letters and leaflets for the public | 14pt minimum | 12pt only for partner and internal reports |
| Large print | 16pt minimum | Supply on request, and offer it by default at events for older people |
| Posters and signs | Readable from the expected viewing distance | See Environment and merchandise (chapter 18) |

- Line height at least 1.5 for body text, with paragraph spacing at least 1.5 times the text size.
- Lines of 45–75 characters.
- Text is left-aligned and **never justified**. Justified text creates uneven gaps that make reading harder for people with dyslexia.
- Write headings in sentence case. Do not set more than a few words in capitals, and do not put whole paragraphs in italics or light weights.
- Pages must work when people zoom to 200% and when the screen is 320px wide, with nothing cut off and no sideways scrolling (WCAG 1.4.4, 1.4.10). Layouts must cope when people increase letter, word and line spacing (1.4.12).
- Do not use pictures of text, except the logo (1.4.5).

### Plain English, Easy Read and translations

Write for a reading age of 9 to 11. Use short sentences, common words and the active voice. Avoid idioms such as "touch base" or "in the same boat", which do not translate and confuse readers new to English. Explain any acronym the first time you use it.

- Produce **Easy Read** versions of important information, such as how to get help with housing, food or work. Easy Read uses short sentences, each paired with a supporting picture.
- Offer **translations** of key information. *Proposed — confirm the community languages with frontline staff.* Use professional or community-checked translations, not unchecked machine translation. On the web, mark the language of a translated page or passage in the code (WCAG 3.1.1, 3.1.2).
- Always put a text label with an icon. An icon alone can mean different things to different people.

## Focus and interaction

The focus indicator shows keyboard users where they are on a page. Never remove it. Our focus style, including the colours to use on brand-colour backgrounds and in dark mode:

{{focus}}

- Everything that works with a mouse must also work with a keyboard alone. Keyboard focus must never get stuck (2.1.1, 2.1.2).
- Focus moves in a logical order and is never hidden behind sticky headers or cookie banners (2.4.3, 2.4.11).
- **Targets:** WCAG requires at least 24 by 24px (2.5.8). Because many of our users have tremor or limited dexterity, **we make every button and standalone control at least 44 by 44px**, with space between them. Inline text links cannot be that size, so give them generous line spacing (at least 1.5) and keep them apart from other links.
- Do not make people drag, swipe or use two fingers. Offer a simple tap or click instead (2.5.1, 2.5.7).
- **No time limits** on forms or content. If a time limit is unavoidable, warn people and let them extend it (2.2.1).
- Forms have visible labels, give instructions before the field, explain errors in words, and do not ask for the same information twice (3.3.1, 3.3.2, 3.3.7). Do not make people solve puzzles or remember passwords to sign in (3.3.8).
- Put help in the same place on every page: our phone number and email address, as well as any online option (3.2.6).
- Link text says where the link goes, for example "Find a warm meal near you". Never use "click here" or "read more".

## Images

Every meaningful image needs alt text: a short description that screen readers read aloud (WCAG 1.1.1). Describe what matters for the purpose of the image, in about 125 characters or fewer. Do not start with "Image of" or "Photo of".

| Type | What to write | Example |
|---|---|---|
| Informative | What the image shows that matters | "Volunteers serve hot soup to families at the Harbourside community kitchen." |
| Functional (a link or button) | Where it goes or what it does | A phone icon linking to our helpline: "Call our helpline" |
| Decorative | Nothing. Use `alt=""` on the web and leave the alt field empty on social media | A wave pattern behind a heading |
| Complex (charts, maps, infographics) | A short summary, plus the full information in text or a table nearby | "Bar chart: meals served rose each month from January to June. Full figures in the table below." |
| Text in an image | The same words as the image | A poster that says "Free lunch, Saturday 12 till 2": write exactly that |

**Logo alt text:** "Harbourside Community Trust logo". When the logo links to the home page, use "Harbourside Community Trust home".

> **Do** describe people by what they are doing, not what they look like, unless their appearance is the point of the image.

> **Don't** put important information only in an image. Repeat it in the text or caption.

## Video and audio

- **Captions** on every video, checked by a person for accuracy and speaker names (1.2.2). Automatic captions are a starting point, not a finished job. For social media, burn captions into the video as well, because many people watch with the sound off.
- **Transcripts** for every audio clip, podcast and WhatsApp voice note we send to groups.
- **Audio description**, or a described transcript, when important information is shown but not said (1.2.5). The easiest fix is to say it out loud: "You'll see our address on screen: …".
- **No autoplay with sound.** Videos on our website do not play until someone presses play.
- Speak clearly, with background music kept low, so people with hearing loss can follow.

## Motion

- Respect the device's "reduce motion" setting. When it is on, replace movement with fades of 120ms or less, and stop parallax, auto-advancing carousels and looping animation. See Motion (chapter 10).
- Nothing flashes more than three times a second (2.3.1). This includes GIFs on social media.
- Anything that moves, scrolls or updates by itself for more than five seconds has a pause or stop control (2.2.2).

## Documents, PDFs and letters

Most of our documents are read by people using screen readers, magnifiers or printouts. Build accessibility in from the start, using the templates in Presentations and documents (chapter 17).

- Use the built-in **heading styles** (Heading 1, Heading 2) in order, real bulleted and numbered lists, and tables with a header row. Do not use empty lines or spaces to create layout.
- Set the document **title and language** (English (United Kingdom)) in the file properties.
- Add alt text to images and mark decorative images as decorative.
- Make the **reading order** logical: check it in the Word or PowerPoint selection pane.
- Run the **Accessibility Checker** in Microsoft Word or PowerPoint and fix every error before you share or export.
- Export **tagged PDFs** (in Word, "Save as PDF" with document structure tags turned on). Add bookmarks to anything over 10 pages. Check the PDF with PAC (PDF Accessibility Checker) or Adobe Acrobat's accessibility check.
- For information on the website, publish a web page rather than a PDF. If you must use a PDF, also offer the content in Word or as a web page.
- **Letters** use the body font at 14pt minimum, left-aligned, on white or cream paper, not glossy. Put the most important information, and our phone number, at the top. Offer large print, Easy Read, audio and other languages, and record people's format preferences so we use them every time.

> **Don't** scan a printed page and share it as a PDF. A scanned page is a picture, so screen readers cannot read the text.

## Social media and WhatsApp

The Social media chapter (chapter 15) has the full rules and its own accessibility section. The essentials:

- Add alt text to every image in the platform's alt text field on Facebook, Instagram and LinkedIn.
- WhatsApp has no alt text field, so describe important images in the message text.
- Caption every video and burn the captions in.
- Write hashtags in CamelCase, for example #HarboursideTrust, and put no more than three at the end.
- Use emoji sparingly, at the end of a sentence, and never in place of words. Screen readers read out every emoji name.
- Never use "fancy" Unicode letters for bold or italic effects. Screen readers cannot read them.
- Put any words that appear in an image in the post text as well.

## Events and physical spaces

Our events must welcome older residents, disabled people and families with young children.

- **Before booking a venue**, check for step-free access to the entrance, main room and an accessible toilet. Check for a hearing loop, good lighting, seating with backs and arms, and accessible parking or a nearby bus stop.
- **In every invitation**, describe the access (for example, "Step-free entrance from the main car park. Hearing loop in the main hall"). Give a phone number and email address for asking for adjustments, and a date to ask by. Do not invite people by social media or online forms alone.
- **On request**, provide **British Sign Language (BSL)** interpreters and live captioning by a speech-to-text reporter (CART). Book them at least four weeks ahead, as they are in short supply.
- Have **large print** copies of anything handed out, and a printed agenda.
- Offer a **quiet space** away from the main room, and a clear way to leave.
- Speakers use a microphone every time, including for questions from the floor, so the hearing loop works.
- Signs use the brand's high-contrast pairings, large text and simple words, with symbols plus words.

## Testing and sign-off

Automated tools find only some problems. Test every new web page, template, campaign and important document in these ways.

1. **Automated:** run axe DevTools, WAVE or Lighthouse on web pages, and the Microsoft or PAC checker on documents.
2. **Keyboard:** use Tab, Shift+Tab, Enter and Space to reach and use everything. Focus must always be visible.
3. **Screen reader:** NVDA on Windows, VoiceOver on iPhone or Mac, and TalkBack on Android. Check headings, links, alt text, form labels and reading order.
4. **Zoom and reflow:** zoom to 200% and 400%, or use a 320px-wide screen. Nothing should be cut off or overlap.
5. **Colour:** check contrast for any new pairing, and view the design in greyscale to confirm nothing depends on colour.
6. **Plain English:** read the copy aloud, or run it through a readability checker, and aim for a reading age of 9 to 11.
7. **Real people:** test important services and campaigns with the people who will use them. Include older residents, disabled people and people who speak English as a second language. Pay them or offer vouchers for their time, and test both online and offline routes.

**Sign-off:** the person who made the work completes the checks. The Communications team gives final approval before anything is published. Anything that fails a contrast, alt text, caption or keyboard check is not published until it is fixed. *Proposed — confirm a named accessibility lead within the Communications team.*

> **Accessibility** If you are not sure whether something is accessible, ask before you publish, not after.

## Getting help and accessible formats

Anyone can ask for our information in another format, such as large print, Easy Read, audio, Braille, another language, or a phone call. They can also report something that is hard to use.

- Email [comms@harbourside.example](mailto:comms@harbourside.example)
- Phone: *Proposed — add the main phone number*
- Or speak to any member of staff or volunteer, who will pass the request on.

We aim to reply within five working days. *Proposed — confirm this response time.* Put this route, including a phone option, on our website footer, the accessibility statement and printed materials.
