# Social media

Social media is where most city sustainability officers, utility engineers, investors and partners first meet Northwind Labs, often in a feed, on a phone and with the sound off. Every post should look like us, be accurate enough to cite in a council report, and work for everyone, including people who use screen readers, captions or magnification.

This chapter covers our channels, profiles, post design, writing, accessibility, community management, crisis handling and governance. The Marketing team owns it. Send questions to hello@northwindlabs.example.

## Channels and purpose

Each channel has one job. If a post does not fit the channel's job, do not post it there. Frequencies are guidance for planning, not a promise to followers.

| Channel | Main job | Primary audience | Guide frequency |
|---|---|---|---|
| LinkedIn (primary) | Insight, case studies, webinars, hiring and partnerships | Sustainability officers, utility engineers, investors, partners | 3–5 posts a week |
| X | Fast commentary on climate data, policy news and events; live updates at conferences | Journalists, policy specialists, the climate-tech community | 3–7 posts a week, when there is something to add |
| YouTube | Webinars, product explainers, method walk-throughs, Shorts that point to them | Technical evaluators and procurement teams researching us | 2–4 videos a month |
| Instagram | People, places and the visual side of climate data; behind the scenes | Future hires, partners, the wider public | 1–3 posts a week plus Stories |
| Web (Open Graph) | Share image for every page and report link | Anyone sharing our links | Every published page |

> **Note** LinkedIn is our primary business-to-government and business-to-business channel. When time is short, publish on LinkedIn first and adapt for other channels afterwards.

## Handles and naming

Use one handle pattern everywhere so people can find us and spot impostors.

- **Handle:** `@northwindlabs` on every platform. *Proposed — confirm with leadership:* this handle is an illustrative placeholder. Confirm that it is available and registered on each platform before you print it anywhere.
- **Display name:** "Northwind Labs" on every platform. Never add slogans, campaign names or emoji to the display name.
- **Sub-accounts:** do not open regional, product or team accounts without approval from the Marketing team. If one is approved, use `@northwindlabs` + a short suffix with no separator where the platform allows it (for example `@northwindlabsuk`), and the display name "Northwind Labs + space + name" (for example "Northwind Labs UK"). Each sub-account needs a named owner and an entry in the account register.
- **Verification:** apply for platform verification on every official account where it is available, so that partners and city officials can tell us apart from copycats.

### Bio templates

Write bios in plain language. Spell out acronyms. Put the most important words first, because bios are cut off in search results.

| Platform | Field and limit | Template |
|---|---|---|
| LinkedIn | Tagline, 120 characters | "Climate data analytics for city governments and utilities." Then add the full company description in the About section. |
| X | Bio, 160 characters | "Climate data analytics for city governments and utilities. News, research and events from the Northwind Labs team." |
| Instagram | Bio, 150 characters | "Climate data analytics for cities and utilities. The people and places behind the numbers." |
| YouTube | Channel description, 1,000 characters | Two sentences on what we do, what the channel publishes and how often, then a link to the website and contact address. |

> **Do** link the bio to a page on our own website, such as a social landing page. You control it, it can be updated in minutes, and it is accessible.

> **Don't** use third-party link-in-bio services. They add tracking, often fail accessibility checks, and break when someone leaves.

## Profile and cover images

{{social.assets}}

- **Avatar:** use the generated avatar for each platform. It shows the Northwind Labs symbol (the circle and peak) knocked out in white on Fjord Teal. We use the symbol rather than the full logo because the wide combination mark is too small to read inside a circular crop.
- **Covers and banners:** use the generated covers. They show the full logo in white on Polar Night, placed inside each platform's safe zone so profile photos and buttons do not cover it.
- **YouTube watermark:** use the 150 × 150 symbol file.
- **Open Graph:** every web page needs a share image (`og:image`) and matching alt text (`og:image:alt`).

Campaigns may change the cover image for up to eight weeks, using an approved template. Covers must still keep the logo or campaign text inside the safe zone and meet the contrast rules below.

> **Don't** change the avatar for a campaign, cause or awareness day: no frames, overlays, colour changes or added text. People recognise us by the avatar, and changing it makes impostor accounts harder to spot.

## Post design

Every format has an editable SVG template with a `guides` layer and a separate `-guides.svg` safe-zone overlay. Hide or delete the `guides` layer before you export.

{{social.specs}}

### Safe zones

Keep all text, logos and key data inside the dashed safe zone. Platform interfaces cover the edges: Story and Reel captions and buttons at the top and bottom, the duration badge in the lower-right of YouTube thumbnails, and profile photos in the lower-left of LinkedIn and X headers.

### Logo on posts

- Put the white symbol in the **top-left corner**, inside the safe zone, on every branded graphic. A single corner means it never clashes with the YouTube duration badge or Story controls.
- Size the symbol at 6–8% of the shorter side of the image (65–86px on a 1,080px canvas), and never below 48px on the canvas.
- Use the full logo only on cover or title slides, at least 240px wide on a 1,080px canvas. Feeds shrink images to about 40%, so anything smaller drops below the logo's 160px minimum and "LABS" becomes unreadable.

### Text on images

- Use no more than about 20 words on an image. Repeat every word of it in the caption or alt text.
- Make text at least 4% of the image height (at least 43px on a 1,080px canvas). Use Manrope for headlines and Inter for supporting text.
- Use only these pairings for text on graphics:

| Text | Background | Contrast | Use |
|---|---|---|---|
| White | Polar Night | 14.59:1 | Any text |
| White | Fjord Teal | 5.95:1 | Any text |
| Daybreak Amber | Polar Night | 7.11:1 | Highlighted numbers and short headlines |
| Polar Night | Daybreak Amber | 7.11:1 | Short labels and tags |

> **Warning** Never use Fjord Teal text on Polar Night (2.45:1), Daybreak Amber on Fjord Teal (2.9:1) or Daybreak Amber text on white (2.05:1). All three fail.

### Data and charts on social

Charts are our most-shared content and the easiest to misread. Follow the data visualisation chapter, and on social also:

- Show one point per graphic. Put the takeaway in the headline ("Heat-related call-outs rose in July"), not just the topic.
- Label lines and bars directly instead of using a colour-only legend, and give chart marks at least 3:1 contrast against the background.
- State the source, the date range and whether figures are measured, modelled or forecast, in the graphic or the first line of the caption.
- Never crop axes to exaggerate a change, and never present a forecast as a fact.

### Carousels

- **Slide 1:** a consistent cover using the template, with the takeaway in the headline.
- **Slides 2 onwards:** number every slide in the top-right ("2/7"). Use a maximum of 10 slides.
- **Final slide:** one call to action, such as "Read the full report: northwindlabs.example/…" or "Register for the webinar".
- Add alt text to each image. LinkedIn document (PDF) carousels cannot take alt text per page, so put a text summary of every slide in the post or link to an accessible version.

### Video

- **Intro:** 2 seconds or less, or none at all. Put the point in the first 3 seconds.
- **Outro:** no more than 5 seconds, showing the full logo and one call to action.
- **Lower thirds:** name and role in white Inter on a Polar Night box, left-aligned inside the safe zone, on screen for at least 4 seconds.
- **Burned-in captions:** white Inter on a Polar Night box at least 80% opaque, no more than two lines, placed above the platform's bottom interface.

## Content pillars

Plan around five themes, and review the mix every quarter. The shares are approximate.

| Pillar | Purpose | Share |
|---|---|---|
| Climate data insight | Explain what the data shows about heat, flooding, energy and emissions in cities, with sources | 35% |
| Customer and partner stories | Show real outcomes, only with written permission and approved figures | 20% |
| How it works | Open up our methods, data sources, models and their limits, to build trust with technical buyers | 20% |
| Events and learning | Webinars, conferences and guides for sustainability officers and utility engineers | 15% |
| People and culture | The team, hiring and how we work | 10% |

> **Accessibility** Every pillar includes data and visuals. Write the alt text when you design the graphic, not at the moment of posting.

## Writing for social

Our voice on social is the same as everywhere else: confident, precise and optimistic (see chapter 11, Voice and tone). On social, be a little shorter and a little warmer.

- **LinkedIn:** expert and practical. Write up to 1,300 characters, with short paragraphs and a hook in the first 2 lines.
- **X:** direct, with one point per post. Use threads for explainers, and number them ("1/5").
- **YouTube:** say in the title what the viewer will learn. In the description, put a summary first, then chapters, links and the transcript.
- **Instagram:** human and visual. Lead with people and places, and keep captions under 150 words.

Structure each caption as: a **hook** (the first ~125 characters), the **value** in plain language, **one call to action**, then mentions and hashtags.

- **Links:** say where a link goes ("Read the full methodology: [link]"). Use our own domain for short links.
- **Mentions:** tag partners, cities and people only when they appear in the post and have agreed to it. Never tag public officials to push a sale.
- **Claims:** be optimistic, never overclaiming. Substantiate every environmental claim with evidence we can show, in line with the CMA Green Claims Code and section 11 (environmental claims) of the CAP Code. Avoid vague terms such as "green", "eco-friendly" or "carbon neutral" unless the claim is specific, measured and approved.

> **Do** write (illustrative figures): "Our model estimates a 12% drop in peak demand for the pilot district (modelled, 2025 data). Method in the comments." This uses an approved figure with its basis.

> **Don't** write: "We're saving the planet one city at a time." It is vague, unprovable and reads as greenwashing.

## Hashtags

- **Brand hashtag:** #NorthwindLabs.
- **Topic hashtags (approved starting set):** #ClimateData, #ClimateAdaptation, #UrbanResilience, #EnergyTransition, #SmartCities.
- **Campaign hashtags:** CamelCase, short and unique. Check that a campaign tag is not already in use before launch, and retire it when the campaign ends.
- Always write hashtags in CamelCase (#ClimateData, not #climatedata) so screen readers read the separate words.
- Place hashtags at the end of the post, never mid-sentence. The one exception is the disclosure label '#ad' or 'Ad', which goes at the start of the post.

| Platform | Hashtags per post |
|---|---|
| LinkedIn | 3–5 |
| X | 1–2 |
| Instagram | 3–5 |
| YouTube | 2–3, in the description |

## Emoji

Emoji are optional. Our voice is precise, so we use them as signposts, not decoration.

- **Approved set:** chart increasing, globe showing Europe-Africa, high voltage, droplet, sun, calendar, pushpin, right arrow, and the national flag for a named event location.
- Use no more than 3 per post, and never more than one in a row.
- Put them at the end of a sentence or as a list marker. Never use them in place of a word: screen readers read out the emoji's full name.
- Never put emoji in display names, alt text or hashtags.

## Accessibility on social

This section is mandatory for every post, on every account, including employees posting on our behalf.

- **Alt text on every image.** Describe the purpose, not just the picture. For charts, give the chart type, what it measures, the trend, the key numbers and the source. For example (illustrative figures): "Line chart of daily peak electricity demand in the pilot district, June to August 2025. Demand peaks at 410 megawatts on 18 July, the hottest day. Source: utility meter data." For complex graphics, add a link to a full text or data version.
- **Captions on every video.** Review and correct auto-captions before publishing. Upload a caption file (.srt) where the platform supports it, and burn in reviewed captions for Reels and Shorts. Link webinar transcripts from the description.
- **Design for sound off.** Do not rely on audio alone to carry meaning. Describe key visuals out loud when they carry information.
- **Repeat text from images** in the caption or alt text.
- **Use CamelCase hashtags** and no more than 3 emoji.
- **Never use Unicode "fonts"** (mathematical bold or italic letters). Screen readers skip them or read them letter by letter, and search cannot find them.
- **Check contrast on graphics:** 4.5:1 for text (3:1 for display text of 24px or more), and 3:1 for chart marks. Never use colour alone to carry meaning.
- **No flashing:** nothing that flashes more than three times a second. Add a warning before any unavoidable strobe.
- **Use plain language:** spell out acronyms the first time (for example "megawatts (MW)"), and keep to one idea per sentence.
- **Describe links:** never write "link in bio" or "click here" without saying what the link is.

### Accessibility features by platform

| Platform | Image alt text | Video captions |
|---|---|---|
| LinkedIn | Use the alt text option when you add an image | Upload a .srt caption file with native video |
| X | Add a description when you attach an image (up to 1,000 characters) | Upload a .srt file through Media Studio, or burn in reviewed captions |
| YouTube | No image alt text: describe visuals in the video, title and description | Upload reviewed caption files. Never rely on unedited auto-captions |
| Instagram | Advanced settings > Accessibility > Write alt text (feed posts) | Review auto-captions on Reels, or burn in reviewed captions |
| Web | Set the `og:image:alt` and `twitter:image:alt` meta tags | Not applicable |

## Community management

Reply as Northwind Labs: knowledgeable, calm and helpful. Never sarcastic, and never defensive. Thank people for corrections. The Marketing team monitors official accounts from 09:00 to 17:30 UK time, Monday to Friday.

| Situation | Response time (business hours) | What to do |
|---|---|---|
| Question about our work or data | Same business day | Answer, or link to the method or help page. Bring in a specialist for technical questions |
| Sales or procurement enquiry | Same business day | Thank them and move to email or a direct message. Pass to the sales lead |
| Complaint | Within 4 business hours | Acknowledge, apologise where appropriate, take it private, then follow up publicly once it is resolved |
| Error in our data or post | Within 2 business hours | Confirm with the data owner, then correct it publicly (see below) |
| Misinformation about us | Same day | Correct once, calmly, with a source. Do not argue |
| Abuse, hate or harassment | Immediately | Hide or remove, report to the platform, and keep a screenshot. Never engage |

- **Take it private** whenever a conversation involves personal data, account details, contract terms or an individual customer's situation.
- **Moderation:** remove spam, abuse, personal data, threats and illegal content. Do not remove criticism just because it is critical. Our house rules should be published on the website.
- **Escalation:** social lead, then Head of Marketing, then the relevant executive. Bring in Legal for any legal threat, regulator or press enquiry.
- **Corrections:** never silently delete a post with a wrong figure that has been shared. Edit it or post a correction that says what changed, and pin the correction for 7 days.

## Crisis and sensitive moments

A crisis could be a data error that affects a client's decision, a security incident, an extreme weather event in a city we serve, or a story about the company in the news.

1. **Pause** all scheduled posts on every channel within 30 minutes of the crisis being declared.
2. **Alert** the social lead, Head of Marketing, the executive on call and Legal.
3. **Hold:** publish only an approved holding statement, if one is needed. For example: "We're aware of [issue] and are looking into it now. We'll share an update by [time]. Questions: hello@northwindlabs.example."
4. **Approve:** every crisis post needs sign-off from the executive on call and Legal. Nobody else posts or replies on the subject, including employees on personal accounts.
5. **Update** at the times you promised, even if there is no news.
6. **Resume** scheduled content only when the Head of Marketing agrees, and review it for tone first.

**Stay silent** on events where we have no expertise or role. During disasters and extreme weather, do not post promotional content, and never use a disaster to sell. Before local elections, respect the pre-election period rules that apply to our council clients: do not publish content featuring their officers or initiatives without their communications team's approval.

## Employee advocacy

We welcome staff sharing our work. Personal accounts are personal, so these rules protect you and us.

- **Share freely:** published posts, reports, job adverts, webinars and event news.
- **Never share:** client names or data not yet announced, internal figures, unreleased products, security details, or anything under a non-disclosure agreement.
- **Disclose:** say that you work at Northwind Labs when you post about our products or our market. A line in your profile and "(I work here)" on promotional posts is enough.
- **Personal views:** your profile can say that views are your own, but this does not cover confidential information.
- **LinkedIn banner:** staff may use the personal banner (1,584 × 396) from the asset kit. Do not edit it apart from the approved variants.
- **Crisis:** do not comment on a crisis. Share only the official statement.

## Partners, influencers and user-generated content

- **Disclosure:** any post we pay for, give something of value for, or control is an advert under the UK ASA/CAP rules. Label it "#ad" or "Ad" at the start of the post, and also use the platform's paid-partnership label. A label at the end of the post or hidden among hashtags is not enough. Legal reviews every paid partnership before it goes live.
- **Co-branded posts:** follow chapter 19, Co-branding and partnerships, for logo lock-ups and approvals. Both parties approve the final post.
- **User-generated content:** ask the creator for permission in writing (a reply or direct message is enough) before reposting, credit them by handle, and do not edit their content beyond cropping to fit. Never repost content that shows identifiable members of the public without consent.

## Governance

- **Who can post:** only trained members of the Marketing team, and named delegates they approve, can post on official accounts.
- **Approvals:** routine posts need one reviewer. Posts with data claims need sign-off from the data owner. Client stories need written approval from the client. Paid, partner and crisis posts need Legal.
- **Account security:** use two-factor authentication on every account and store logins in the business password manager. Never use shared personal logins. Remove access on the day someone leaves, and review admins every quarter.
- **Account register:** the Marketing team keeps a register of every official account, its owner, its admins and its recovery details.
- **Records:** *Proposed — confirm with leadership:* keep approvals, published posts and crisis logs for 24 months, in line with chapter 20.
- **Privacy:** never post personal data. Get written consent for photos of identifiable people, and parental consent for anyone under 18. Avoid showing children at all unless it is essential.
- **Spec review:** platform specifications were last reviewed on 2 October 2026. Review them again by 2 April 2027, or sooner if a platform changes its layout.

## Social media: do and don't
> **Do** use the generated templates, keep the logo and text inside the safe zone, and put the symbol in the top-left corner.

> **Do** add alt text and reviewed captions to every post, and give the source and basis for every number.

> **Don't** alter the avatar, use Unicode "fonts", stack emoji, or put hashtags in lowercase.

> **Don't** publish an environmental claim, a client figure or a paid partnership without the approvals listed above.

## Pre-publish checklist

- [ ] **Brand:** the correct template, logo top-left inside the safe zone, and approved colour pairings only.
- [ ] **Accuracy:** each number has a source and a date range, and is labelled as measured, modelled or forecast. The data owner has approved it.
- [ ] **Accessibility:** alt text, reviewed captions, text from the image repeated, CamelCase hashtags, 3 emoji or fewer, no Unicode "fonts", no flashing, and descriptive links.
- [ ] **Legal:** permissions and consent are in place, #ad is at the start where needed, and environmental claims are substantiated.
- [ ] **Proofread:** UK English spelling, names and handles are correct, and links work.
