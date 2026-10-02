"""Single definition of the style guide's chapters, owners, and data placeholders.

init_guide.py scaffolds these files, the section agents fill them, render_guide.py
renders them in order, and validate_brand.py checks they are complete.
"""

# (file stem, title, owning skill, data placeholders the chapter should include, what to write)
CHAPTERS = [
    ("01-introduction", "Introduction", "create-style-guide", ["{{meta.table}}"],
     "Purpose of the guide, who it is for, how to use it, what is mandatory vs flexible, where to get help, and the accessibility commitment in one paragraph."),
    ("02-brand-foundations", "Brand foundations", "voice-and-tone", [],
     "Mission, vision, values (each with a one-line behaviour), positioning statement, audiences and their needs, brand personality traits, tagline and boilerplate (25, 50 and 100 words)."),
    ("03-logo", "Logo", "logo-analysis", ["{{logo.variants}}", "{{logo.specs}}", "{{logo.backgrounds}}"],
     "Logo anatomy and meaning, logo type, variants and when to use each, clear space, minimum sizes, placement, backgrounds, logo misuse (at least 8 don'ts), file formats and naming, alt text for the logo."),
    ("04-colour", "Colour", "color-system", ["{{color.brand}}", "{{color.proportions}}", "{{color.scales}}", "{{color.semantic}}", "{{color.pairings}}", "{{color.cvd}}"],
     "Primary, secondary, accent, neutral and semantic colours with names and roles, colour proportions, accessible pairings, colour in print (CMYK/Pantone to be verified), dark mode, and the rule never to rely on colour alone."),
    ("05-typography", "Typography", "typography", ["{{type.families}}", "{{type.scale}}"],
     "Typefaces and why, licensing, fallbacks, type scale and usage, hierarchy, line length, line height, alignment, emphasis, numerals, multilingual/RTL support, and accessible typography rules."),
    ("06-layout-and-spacing", "Layout, grid and spacing", "visual-language", ["{{spacing.scale}}", "{{grid}}", "{{radius}}", "{{elevation}}"],
     "Spacing scale, grids per breakpoint, margins, corner radius, elevation, composition principles, reflow and zoom behaviour."),
    ("07-iconography", "Iconography", "visual-language", [],
     "Icon style (stroke, corners, grid, sizes), recommended icon set and licence, colour use, labels and accessible names, minimum target sizes, do and don't."),
    ("08-imagery-and-illustration", "Photography and illustration", "visual-language", [],
     "Photography style and subjects, representation and inclusion, treatment and colour grading, text over images, illustration style, image sourcing and rights, alt text rules, AI-generated imagery policy."),
    ("09-data-visualisation", "Data visualisation", "visual-language", [],
     "Chart colour order, accessible chart rules (labels, patterns, 3:1 for marks, no colour-only legends), typography in charts, tables, and text alternatives for charts."),
    ("10-motion", "Motion", "visual-language", ["{{motion}}"],
     "Motion principles, durations and easing, logo animation rules, reduced-motion behaviour, no flashing content, autoplay and pause controls."),
    ("11-voice-and-tone", "Voice and tone", "voice-and-tone", [],
     "Voice attributes (we are / we are not, with examples), tone by context (marketing, support, errors, crises, social, legal), and before/after rewrites."),
    ("12-writing-style", "Writing style", "voice-and-tone", [],
     "Spelling locale, grammar and punctuation, capitalisation, numbers, dates, times, currency, abbreviations, links, plain language and reading level, inclusive and accessible language, brand name usage, glossary."),
    ("13-accessibility", "Accessibility", "accessibility-audit", ["{{focus}}"],
     "Conformance target, colour and contrast, typography, focus indicators, target sizes, alt text, captions and transcripts, documents and PDFs, motion, social media accessibility, testing and sign-off checklist."),
    ("14-digital", "Digital and web", "brand-applications", ["{{favicons}}"],
     "Website and app basics (header, buttons, links, forms, states), favicons and app icons, email templates, email signatures, video and webinars, Open Graph images."),
    ("15-social-media", "Social media", "social-media-kit", ["{{social.specs}}", "{{social.assets}}"],
     "Channels and purpose, handles and naming, profile and cover images, post templates and layouts, safe zones, content pillars, captions, hashtags, emoji, mentions, alt text, video captions, community management and response tone, crisis protocol, employee advocacy, partners and influencers (disclosure), approvals."),
    ("16-print-and-stationery", "Print and stationery", "brand-applications", [],
     "Business cards, letterhead, envelopes, compliment slips, brochures and flyers, posters, print colour and paper, bleed and margins, accessible print (font sizes, contrast, matt stock)."),
    ("17-presentations-and-documents", "Presentations and documents", "brand-applications", [],
     "Slide templates and layouts, document templates (reports, proposals, letters), accessible Word/PowerPoint/PDF practices (styles, reading order, alt text, tagged PDFs)."),
    ("18-environment-and-merchandise", "Signage, environment and merchandise", "brand-applications", [],
     "Signage and wayfinding (sizes, contrast, mounting heights, tactile/braille where required), office and event branding, vehicles, uniforms, merchandise and promotional items, packaging if relevant."),
    ("19-co-branding-and-partnerships", "Co-branding and partnerships", "brand-applications", [],
     "Partner lock-ups, sponsorship, endorsed and sub-brands, logo ordering and spacing, approvals."),
    ("20-legal-and-governance", "Legal, governance and assets", "create-style-guide", ["{{downloads}}"],
     "Trademark use (® / ™), copyright lines, font and image licences, approvals workflow, brand owners and contacts, asset library and file naming, review cadence and version history."),
]

CHAPTER_STEMS = [c[0] for c in CHAPTERS]

PLACEHOLDERS = {
    "{{meta.table}}", "{{logo.variants}}", "{{logo.specs}}", "{{logo.backgrounds}}",
    "{{color.brand}}", "{{color.proportions}}", "{{color.scales}}", "{{color.semantic}}",
    "{{color.pairings}}", "{{color.cvd}}", "{{type.families}}", "{{type.scale}}",
    "{{spacing.scale}}", "{{grid}}", "{{radius}}", "{{elevation}}", "{{motion}}", "{{focus}}",
    "{{favicons}}", "{{social.specs}}", "{{social.assets}}", "{{downloads}}",
}

TODO_MARKER = "TODO("
