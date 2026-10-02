# Social media

Social media is often the first place a family looks for a warm meal tonight, and the first place a donor checks whether we are trustworthy. Every post should be easy to read, easy to act on and safe for the people in it. That includes people using a screen reader, reading in their second language or looking at an old phone with the sound off.

This chapter is for anyone who posts, replies or designs for Harbourside Community Trust. The Communications team owns it. Send questions to [comms@harbourside.example](mailto:comms@harbourside.example).

## Channels and purpose

We use four social channels and one website-sharing format. Each one has a clear job. Posting frequencies are guidance for planning. They are not promises to our audience.

| Channel | What it is for | Main audiences | Suggested rhythm |
|---|---|---|---|
| Facebook (Page, Events and community groups) | Service updates, opening times, events, community stories | Local families, older residents, volunteers | 3–5 posts a week, plus events |
| Instagram | Stories of people and places (shared with consent), volunteer life, appeals | Younger families, volunteers, local supporters | 2–4 feed posts a week, Stories as needed |
| WhatsApp Business (Channel and broadcast lists) | Short, practical updates: closures, food club times, volunteer rotas | Families and volunteers who have opted in | Only when there is something useful, at most 3 messages a week per list |
| LinkedIn (Company Page) | Impact, partnerships, corporate volunteering, jobs | Donors, council partners, local businesses | 1–2 posts a week |
| Website sharing (Open Graph) | The preview image and text shown when someone shares a link to our website | Everyone | Set on every web page |

Facebook matters most for older residents, so post every service change there first. WhatsApp reaches people who do not use other platforms, so keep every WhatsApp message useful.

> **Note** Platform sizes and features change often. The table below was checked against official help pages on the review date shown in the specs. Check it again before a major campaign.

{{social.specs}}

## Handles and naming

No official handles have been confirmed yet. Until they are, use **[@handle — to be confirmed]** in drafts and templates.

*Proposed — confirm with leadership:* use one pattern everywhere, **HarboursideTrust**, so people can find us by guessing. Write it in CamelCase in print and captions (`@HarboursideTrust`). This helps screen readers and people reading in a second language. Before deciding, check that the name is free on every platform. If it is taken on one, add the same suffix everywhere (for example `HarboursideTrustUK`). Do not use a different name for each platform.

| Item | Rule |
|---|---|
| Display name | "Harbourside Community Trust" in full, on every platform. No emoji or campaign words |
| Short bio (LinkedIn tagline limit is 120 characters) | "We help Harbourside families find safe homes, warm meals and good work. A local charity." |
| Long bio | The short bio, then opening hours or how to get help, then the website link |
| Charity details | *Proposed:* add "Registered charity no. [number — to be confirmed]" wherever the bio or page details allow |
| Link in bio | One link only, to a page on our own website that lists current help and appeals. Never use a third-party link page that tracks visitors |
| Verification | Apply for verification or a business badge where it is free and the platform offers it to charities. Never pay a third party for it |

**Sub-accounts.** We do not open separate accounts for projects, places or teams. Post through the main accounts so families see one trusted source. A Facebook group (for example a volunteer group) must be named "Harbourside Community Trust – [Purpose]", link back to our Page and have at least two staff admins. A new account needs agreement from the Communications team.

> **Do** use the same name, avatar and bio pattern on every platform so people can tell the real account from a fake.

> **Don't** let a project, volunteer or partner open an account using our name or logo.

## Profile and cover images

Our logo is wide, so it becomes unreadable in a small circle. Avatars use the **circular symbol only** (the sun over the waves) on a white background, which keeps the circle's edge visible. Covers use the full logo in white (knockout) on Harbour Blue.

{{social.assets}}

- **Avatar:** use the avatar PNG for each platform exactly as supplied. It is already sized to fit inside the circular crop. Do not add a frame, ribbon or campaign badge.
- **Covers:** use the cover template. Keep text and the logo inside the dashed safe zone (the `guides` layer, which you hide before export). On Facebook, phones crop about a sixth from each side of the cover. Keep words and the logo in the middle two-thirds.
- **LinkedIn cover:** keep it simple, using the logo plus at most one short line. The cover displays at about 191 pixels high, so a second line becomes too small to read.
- **Campaigns:** you may change the cover for a campaign for up to eight weeks, then change it back. The avatar never changes.
- **Open Graph image:** every web page needs a share image (1200 × 630) with `og:image:alt` set. Keep text inside the 8% safe margin.

> **Warning** The symbol was cropped from the master PNG. A designer must confirm it, or supply vector artwork, before the avatars are used on live accounts.

## Post design

Templates for every format are in `assets/social/<platform>/`. Each format has an editable SVG with a `guides` layer, which you must hide before export, and a safe-zone overlay. Start from a template every time.

> **Warning** In this first version of the kit, the generated templates need three fixes before use. The supporting line on post templates is too small: set it to at least 4% of the image height (54px on a 1080 × 1350 post) in Atkinson Hyperlegible Next, and keep the headline short enough to stay inside the safe zone. On the Facebook cover, keep text at least 17% in from each side, because phones crop the edges. On the LinkedIn cover, remove the supporting line. Also note that the PNG previews centre the logo, but the SVG templates place it bottom-left. Follow the SVG templates.

### Layout and the logo

- Place the full-colour or white logo in the **bottom-left corner, inside the safe zone**. It should be about a quarter of the image width and never less than 160px wide. On Stories, Reels and WhatsApp Status, keep it above the bottom safe zone, because the reply bar covers the bottom edge.
- On Reels, the bottom 35% is covered by captions and buttons. Keep all text and the logo above it.
- Use one logo per post. On a photo, use the white logo on a Harbour Blue band rather than straight on a busy image.

### Text on images

- At most **20 words** on an image. If you need more, put it in the caption.
- Make text **at least 4% of the image height** (54px on a 1080 × 1350 post). Headlines use Nunito Bold or ExtraBold. Supporting text uses Atkinson Hyperlegible Next.
- Left-align text. Use sentence case, not capitals.
- Repeat every word from the image in the caption or alt text.

### Colour on posts

The colour pairings below have been checked against our contrast rules.

| Use | Pairing | Contrast |
|---|---|---|
| Default post | White text on Harbour Blue (`primary`) | 8.4:1 |
| Light post | Harbour Blue text on white or `primary-100` | 8.4:1 / 7.1:1 |
| Warm highlight panel | White text on `secondary-600` | 5.8:1 |
| Sunset Coral panel | Near-black (`neutral-950`) text on Sunset Coral | 6.5:1 |

Sunset Coral and Tide Blue are for shapes, waves and decoration. Never use Sunset Coral text on Harbour Blue or on white, because both fail (2.84:1 and 2.95:1).

### Carousels

Use the same cover design on every carousel. Number the slides ("2 of 5") in the bottom-right corner. End with one clear call to action, such as "Find your nearest food club: link in bio." Use no more than 10 slides.

### Video

- Use a brand intro of no more than 2 seconds, or none at all, because people scroll past slow starts. Keep the outro end card to 5 seconds or less, with one call to action.
- **Lower thirds:** a Harbour Blue bar with the person's first name and role in white Atkinson Hyperlegible Next. Use a first name only, and only with consent.
- **Burned-in captions:** white Atkinson Hyperlegible Next on a near-black box (`neutral-950` at 80% or more opacity). Use at most 2 lines of about 40 characters, placed above the platform's bottom safe zone.

> **Do** start from the template, check the safe zone, then hide the `guides` layer before export.

> **Don't** stretch, recolour or add effects to the logo, or put text on a photo without a solid panel behind it.

## Content pillars

Most of what we post should help someone do something today.

| Pillar | Purpose | Share |
|---|---|---|
| Help near you | Opening times, services, how to get help, changes to services | 30% |
| Local stories | Stories of families, volunteers and neighbours, shared with written consent | 25% |
| Get involved | Volunteering, events and rotas | 20% |
| Fund our work | Appeals, donor thanks and what donations pay for | 15% |
| Working together | Partners, council work, impact figures and jobs (mainly on LinkedIn) | 10% |

## Writing for social

Follow chapter 11, Voice and tone: kind, plain and local. Social posts are casual. Replies to complaints are serious and kind.

- **Plain English for everyone.** Many readers speak English as a second language, and many are older. Use short sentences, common words and no idioms or slang. Write numbers as digits and dates in full ("Tuesday 4 November").
- **Structure:** start with a hook in the first 125 characters, because most platforms cut the post off there. Then make the point. End with one call to action, then any hashtags.
- **Length:** Facebook and LinkedIn posts are under 100 words. Instagram captions are under 150 words. WhatsApp messages are under 60 words, with the most important fact first.
- **Links:** say where a link goes ("Book a place on our website: [link]"). Never write "click here". Avoid unexplained short links.
- **Mentions and tagging:** tag partners only when they took part and have agreed. Never tag or name a person who receives our help.
- **Translated posts:** for safety-critical updates (closures, flooding, food club changes), publish translations as separate posts or messages. Start each one with the language name written in that language. Use a professional translator or a trained community volunteer to check every translation. Do not rely only on machine translation. Never put translated text only inside an image. *Proposed — confirm with frontline teams:* the main community languages to translate into.

## Hashtags

- Write every hashtag in **CamelCase** (`#HarboursideTrust`, not `#harboursidetrust`) so screen readers say the words correctly.
- Put hashtags **at the end** of the post, never in the middle of a sentence.
- Use **no more than 3 hashtags** per post on any platform. On Facebook use 0–1, on Instagram and LinkedIn 2–3, and on WhatsApp none.
- *Proposed brand hashtags:* `#HereForHarbourside` (our proposed tagline) and `#HarboursideTrust`. Check that nobody else is using them before launch.
- Before using a campaign or awareness-day hashtag, check what else it is being used for.

## Emoji

Use emoji to add warmth, not meaning. Our approved set is red heart (thanks), waving hand (welcome), house (homes), steaming bowl (meals), handshake (partners), calendar (dates) and sun (good news). Screen readers read each one aloud by name.

- Use **at most 2 emoji** per post, at the end of a sentence, never in place of a word.
- Never repeat an emoji in a row, and never put emoji in display names or handles.
- **No emoji** in crisis posts, safety updates, complaint replies or anything about hardship.

## Accessibility on social

This section is mandatory. A post that fails it is not ready to publish.

- **Alt text on every image.** Describe what the image shows and why it matters, in about 125 characters. For an infographic, use longer alt text and link to a text version. Never start with "Image of".
- **WhatsApp has no alt text.** Put all the essential information in the message text, never only in the image.
- **Captions on every video.** Check and correct auto-captions before publishing. Add a transcript for videos longer than 1 minute. Make sure videos make sense with the sound off.
- **Hashtags in CamelCase**, with emoji limited as above.
- **No Unicode "fonts".** Never use fake bold or italic letters from text-generator websites. Screen readers read them as symbols or skip them.
- **Text in images is repeated** in the caption or alt text.
- **Contrast:** at least 4.5:1 for text on graphics, or 3:1 for very large headlines. Use the pairings in the post design section.
- **No flashing** of more than 3 flashes a second. Avoid fast cuts and strobe effects.
- **Plain language:** spell out acronyms and make links descriptive.

### Accessibility features by platform

| Platform | Alt text | Video captions |
|---|---|---|
| Facebook | Edit photo, then Alternative text (replaces the automatic alt text) | Upload an .srt file, or use auto-captions and then correct them |
| Instagram | Advanced settings, then Accessibility, then Write alt text (feed posts) | Auto-captions on Reels, which you must correct, or burned-in captions |
| LinkedIn | Use the Alt text option when adding an image | Upload an .srt file with native video |
| WhatsApp Business | Not available, so put the information in the message text | Burn in captions you have checked |
| Website sharing (Open Graph) | Set the `og:image:alt` and `twitter:image:alt` tags | Not applicable |

> **Accessibility** Our audience includes many older residents and people reading in their second language. Large, high-contrast text, plain words and full information in the caption help everyone.

## Safeguarding, consent and privacy

The people we help can be vulnerable. Protecting them matters more than any post.

- **Written consent is required** before posting any photo, video or story of a person. Use the Trust's photo consent form, and keep it linked to the image. For children under 18, a parent or guardian must sign. Consent can be withdrawn at any time. Remove the content within 2 working days if it is.
- **Never identify a person receiving help** without their written consent, by name, face, voice, home, school or anything else that could identify them. If you are unsure, use photos of hands, places or volunteers instead.
- **Never share the location of vulnerable people**, such as a home, a temporary housing address or a refuge. Turn off geotagging. Post event photos after people have left.
- **Never ask for personal details in public.** Move the conversation to a private message.

## WhatsApp: consent and privacy

- Use the **WhatsApp Channel** or **broadcast lists** for families. Use them instead of groups, because groups show every member's phone number to the others.
- Add people only after they **opt in**, and record when they did and how. Every broadcast message ends with: "Reply STOP to stop these messages." Remove anyone who replies STOP the same working day.
- Volunteer groups are allowed only with each member's agreement. Set them so that only admins can post, and include at least two staff admins.
- Never share personal details, case information or photos of service users on WhatsApp.

## Community management

We reply as a person from the Trust: kind, clear and brief. Sign replies with a first name if the team agrees to that.

| Situation | Response time (working hours, guidance) | What to do |
|---|---|---|
| Someone asks for help in a comment or message | Within 1 working day | Reply kindly, move to a private message, and signpost to the right service. Never assess need on social media |
| Someone may be in immediate danger | As soon as seen | Tell them to call 999. Alert the duty manager and follow the safeguarding policy |
| General question | Within 1 working day | Answer, or link to the right web page |
| Complaint | Acknowledge within 4 working hours | Say sorry where we got it wrong, take it to a private message, and follow up publicly once it is resolved |
| Wrong information about us | Same working day | Correct it calmly, with a source |
| Abuse, hate, harassment, scams | As soon as seen | Hide or remove, report to the platform and log a screenshot. Do not reply |

- **Out of hours:** set an automatic reply on Facebook, Instagram and WhatsApp. It should give our opening hours and say: "If you or someone else is in danger, call 999."
- **Escalation:** the team member handles it first. If unsure, go to the Communications lead, then the chief executive. Safeguarding concerns go straight to the safeguarding lead.
- **Moderation rules:** pin the house rules in Facebook groups. We remove abuse, discrimination, personal information, spam and scams. We do not remove criticism that is polite.

## Crisis and sensitive moments

Storms, flooding, service closures, a data breach or negative press all need a fast, calm and accurate response.

1. **Pause** all scheduled posts on every channel straight away. Anyone on the team can do this.
2. **Confirm the facts** with the duty manager. Do not guess about causes or blame.
3. **Post a holding statement** within 1 hour if families are affected, after the Communications lead approves it. For example: "Our [service] at [place] is closed today because of [flooding]. Your nearest open point is [place, time]. We will update you here by [time]."
4. **Get approval:** the Communications lead approves service updates. The chief executive approves anything about safety, reputation or the media. For a data breach, the data protection lead decides whether to report it to the ICO, which must happen within 72 hours for breaches that have to be reported. Post nothing about a breach until the data protection lead and the chief executive approve it.
5. **Update** at the times you promised, on Facebook and WhatsApp first, in plain English and the agreed translations.
6. **Stay silent** about tragedies that have nothing to do with us. Do not post promotional or upbeat content during a local emergency.

## Staff and volunteer advocacy

We welcome staff and volunteers sharing our work.

- Share official posts, and add your own words in your own voice.
- Say you work or volunteer for us when you post about us. On LinkedIn, the personal banner template (in `assets/social/linkedin/`) is available for staff.
- Your personal account is yours. Do not speak for the Trust, reply to complaints or make promises about services.
- Never post photos, names or stories of people we help from a personal account. Never give advice about someone's case. Signpost them to our official channels.

## Fundraising appeals

Our appeals follow the Fundraising Regulator's Code of Fundraising Practice. Fundraising must be legal, open, honest and respectful.

- Say clearly what the money is for, and use only real, checked figures. When a figure shows only an example ("£10 could pay for…"), say so.
- Do not pressure people, use guilt, or target people who may be in vulnerable circumstances.
- Use real stories only with written consent. Never exaggerate need.
- The Communications lead must check every fundraising post.

## Partners, influencers and user-generated content

- **Disclosure:** if a business pays, gifts or rewards someone to post about us, the post must say so clearly at the start. Use `#Ad` or the platform's paid-partnership label, following the UK ASA/CAP advertising rules. Ask for a legal check if you are unsure.
- **Co-branded posts:** follow chapter 19, Co-branding and partnerships. Our logo and the partner's logo should be the same visual size, inside the safe zone.
- **Reposting user content:** ask the owner for permission in writing (a message is fine) and credit them by handle. Never repost an image showing a child or a person we help, even with the owner's permission, unless we also hold our own written consent.

## Governance and account security

| Item | Rule |
|---|---|
| Owner | Communications team |
| Who can post | Communications team (admins). Named, trained staff (editors) can schedule posts. Volunteers never hold admin access |
| Approvals | Routine posts need one person. A second person must check posts that show people, ask for money or name a partner. Crisis posts follow the crisis steps |
| Security | Two-factor authentication on every account. Store logins in the Trust's password manager, never in personal accounts. At least two admins on every account |
| Offboarding | Remove access on the day someone leaves. Review the admin list every 3 months |
| Records | Keep a register of all official accounts, owners and recovery details. Keep consent forms with their images. Log every crisis post and every comment removed |
| Privacy | No personal data in posts or public replies. Follow the Trust's data protection and safeguarding policies |

## Social media: do and don't
> **Do** write alt text, captions and plain-English copy for every post, every time.

> **Do** move every request for help into a private message and signpost it within 1 working day.

> **Don't** post a person's photo or story without signed consent, or reveal where a vulnerable person lives.

> **Don't** use fake Unicode bold, more than 3 hashtags, or more than 2 emoji.

## Pre-publish checklist

- [ ] **Brand:** made from a template, logo bottom-left inside the safe zone, approved colour pairing, brand fonts
- [ ] **Accessibility:** alt text added (or all information in the text on WhatsApp), captions checked, CamelCase hashtags at the end, no more than 2 emoji, no Unicode fonts, text in images repeated
- [ ] **Safeguarding and legal:** written consent on file, no one we help identified without it, no locations of vulnerable people, `#Ad` where needed, fundraising claims checked
- [ ] **Proof-read:** names, dates, times, place names and links tested. Read it aloud once
