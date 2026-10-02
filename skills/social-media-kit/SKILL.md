---
name: social-media-kit
description: Create the brand's social media guidelines and asset kit — per-platform profile images, covers, banners and post templates with safe zones (Instagram, Facebook, LinkedIn, X, YouTube, TikTok, Threads, Pinterest, Bluesky, Mastodon, WhatsApp Business, Google Business Profile, Open Graph), handles and naming, content pillars, captions, hashtags, emoji, alt text, video captions, community management, crisis protocol, employee advocacy, influencer disclosure and approvals. Use when writing chapter 15-social-media or creating social assets or social media brand rules.
argument-hint: "[path/to/brand.json] [platforms]"
---

# Social media kit

Load **brand-standards** first. Platform sizes, safe zones and accessibility features are in `references/social-platforms.json`; editorial guidance is in `references/social-guidelines.md`.

## 1. Platforms and assets

- Set the platforms in your handoff (`social.platforms`, using ids from the JSON). Default: Instagram, Facebook, LinkedIn, X, YouTube, TikTok, plus `web` for Open Graph images.
- Platform specs change. If WebSearch or WebFetch is available, spot-check the sizes of the chosen platforms against official help pages. If a value has changed, update `social-platforms.json` (sizes and `lastReviewed`) and mention it in your handoff.
- Assets come from `make_assets.py`. Inspect at least one avatar and one cover per platform. Avatars must stay legible inside the circular crop. If not, the lead needs a symbol (`logo.symbol`).
- Each format has a PNG preview, an editable SVG template (a `guides` layer to hide before export) and a `-guides.svg` safe-zone overlay.

## 2. Write chapter 15-social-media

Keep `{{social.specs}}` and `{{social.assets}}`. Cover, adapting to the organisation:

1. **Channels and purpose:** what each platform is for, its audience and posting frequency (as guidance, not a promise).
2. **Handles and naming:** consistent handle pattern, display name, bio template per platform (character limits), link-in-bio policy, verification, and sub-accounts (regions or departments) with naming rules.
3. **Profile and cover images:** which asset to use, the logo version on the avatar, update rules for campaigns (never alter the avatar logo for campaigns beyond approved variants).
4. **Post design:** templates, safe zones, the logo's position and size on posts (small, consistent corner, inside safe zone), text on images (at most about 20 words, at least 4% of image height, contrast checked), brand colours and type on posts, carousels (consistent cover, numbered slides, final slide with a call to action), video (intro or outro length, lower thirds, burned-in captions style).
5. **Content pillars:** three to five themes with the purpose and approximate share of each.
6. **Writing for social:** voice per platform (link to chapter 11), caption length, hooks, calls to action, links, mentions and tagging policy.
7. **Hashtags:** brand and campaign hashtags (CamelCase), how many per platform, and placement at the end.
8. **Emoji:** an approved set and usage rules (see the accessibility section).
9. **Accessibility on social (mandatory section):** alt text on every image (how, per platform, from the JSON), captions and transcripts, CamelCase hashtags, emoji limits, no fancy Unicode text, text in images repeated in captions, contrast on graphics, no flashing content, sound-off design, plain language, descriptive links, and the "accessibility features by platform" table.
10. **Community management:** response times, tone for replies, escalation path, handling complaints and trolls, moderation rules, and when to take conversations private.
11. **Crisis and sensitive moments:** pause scheduled posts, an approval chain, holding statements, and when to stay silent.
12. **Employee advocacy:** what staff may share, disclosure, personal vs corporate accounts, and using the personal LinkedIn banner.
13. **Partners, influencers and user-generated content:** disclosure (#ad or paid-partnership labels per local advertising rules), co-branded posts (link to chapter 19), and permission and credit for reposting UGC.
14. **Governance:** who can post, approvals, account security (2FA, shared password managers, offboarding), record-keeping, legal and privacy (no personal data, consent for photos of people, especially children).
15. **Do / Don't**, plus a pre-publish checklist (brand, accessibility, legal, proof-read).

Propose `social.hashtags`, `social.contentPillars` and `social.handles` (only handles the user gave) in your handoff.
