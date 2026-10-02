---
name: accessibility-audit
description: Write the accessibility chapter of a brand style guide and audit a guide, brand asset, post, document or page against WCAG 2.2 and the brand's own rules — colour contrast, colour-vision deficiency, typography, focus, target size, alt text, captions, motion, documents, social posts, and the rendered HTML guide itself — returning findings rated Critical/Serious/Moderate/Minor with concrete fixes. Use for chapter 13, for the pre-handover audit, or when the user asks "is this on-brand and accessible?" about any asset.
argument-hint: "[path/to/brand.json | asset path | URL] [author|audit]"
---

# Accessibility: author and audit

Load **brand-standards** first, especially `references/accessibility-baseline.md`. The detailed checklist is `references/wcag-checklist.md`.

## Author mode: chapter 13-accessibility

Keep `{{focus}}`. Write a practical chapter people can follow without being experts:

1. **Our commitment:** the conformance target (`meta.accessibilityTarget`), why it matters for the organisation's audiences, and that it applies to every channel (web, documents, social, print, events).
2. **Colour and contrast:** thresholds in plain words, where to find approved pairings (chapter 4), and how to check new combinations (any contrast checker, plus `contrast_check.py` for the brand team).
3. **Do not rely on colour alone:** links, states, charts and maps.
4. **Typography:** minimum sizes per medium, spacing, alignment and zoom.
5. **Focus and interaction:** the focus style, keyboard access, and target sizes.
6. **Images:** an alt text guide with examples (informative, functional, decorative and complex), plus logo alt text.
7. **Video and audio:** captions, transcripts, audio description, and no autoplay.
8. **Motion:** reduced motion and flashing rules.
9. **Documents and PDFs:** styles, reading order, tagged PDFs, and accessibility checkers.
10. **Social media:** summarise and link chapter 15's accessibility section.
11. **Events and physical spaces:** step-free access information, large print, captioning (CART) and sign language interpretation on request, and quiet spaces.
12. **Testing and sign-off:** automated checks plus manual keyboard, screen reader (NVDA, VoiceOver, TalkBack) and zoom tests, and involving disabled people in testing. Who signs off.
13. **Getting help:** contact and how to request accessible formats.

## Audit mode

Inputs: a workspace (`brand.json`), or a specific asset, document, post or URL.

1. **Automated:** run `validate_brand.py` for a workspace. For individual colours use `contrast_check.py`. For images, sample the text and background colours (Pillow) and check the worst case.
2. **Manual review of the rendered guide** (`style-guide.html`, read the source and screenshots if a browser is available):
   - Headings describe their sections. One h1, no skipped levels.
   - Every image's alt text is accurate and useful. Decorative images are empty.
   - Tables have captions and headers. Data is not conveyed by colour alone.
   - Keyboard: the skip link works, focus is visible on every interactive element, and there are no traps.
   - Reflow at 320px, 200% zoom, dark mode and print stylesheet.
   - Copy buttons announce the result (aria-live).
3. **Content review:** each chapter's rules are consistent with the baseline. No chapter recommends an inaccessible practice (e.g. justified text, thin light-grey type, colour-only status, image-only email, autoplay video).
4. **Asset review:** open a sample of logo variants, avatars, covers and templates. Check legibility at display size, contrast, and that the safe zones are respected.
5. **Report** using the format below. You **must** write it to `analysis/accessibility-audit.md` (the quality gate checks for it). After fixes, the lead updates each row's Fix column to start with "Fixed:" or "Resolved:". Then return a summary.

## Findings format

| ID | Severity | Where | Issue | WCAG SC | Fix |
|---|---|---|---|---|---|

Severity:

- **Critical:** blocks access for a group of users (e.g. text below 3:1, no alt text on informative images, colour-only status in a core rule, keyboard trap).
- **Serious:** major difficulty (e.g. 3–4.5:1 body text, missing captions guidance, vague link guidance, unreadable avatar).
- **Moderate:** friction or inconsistency (e.g. inconsistent terms, missing dark-mode rule).
- **Minor:** polish.

End with an overall verdict. **Pass** means no Critical or Serious findings open.

## Auditing a single asset against the brand

For "is this post or poster or slide on brand and accessible?": check logo version, size, clear space and background; approved colours and pairings; type families, sizes and hierarchy; imagery style; voice and tone; and the accessibility checklist for that medium. Return the findings table and a corrected version of the copy or spec where useful.
