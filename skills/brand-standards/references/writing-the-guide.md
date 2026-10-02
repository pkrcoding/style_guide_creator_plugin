# Writing the guide

The audience is the people who apply the brand: marketers, designers, developers, agencies, printers, social media managers, and staff writing their first LinkedIn post. They skim, then come back for a specific rule. Write for that.

## Chapter structure

Each `content/NN-*.md` file:

1. Starts with exactly one `# Chapter title`. Keep the title from the skeleton.
2. Opens with one or two sentences on **why this matters** for the brand and its audience.
3. Uses `##` for sections and `###` for sub-sections. Never skip a level. The renderer shifts levels down one. Make headings specific: write "Logo accessibility", not a bare "Accessibility" repeated in every chapter, so the heading list makes sense out of context (WCAG 2.4.6).
4. Keeps every data placeholder from the skeleton (e.g. `{{color.pairings}}`) on its own line, near the prose that explains it.
5. Ends sections with practical rules. Use Do/Don't callouts:

   ```markdown
   > **Do** place the logo on white, light neutral or Northwind Teal backgrounds.

   > **Don't** place the full-colour logo on Lantern Gold; use the dark single-colour logo.
   ```
   Callouts can also start with `**Note**`, `**Accessibility**` or `**Warning**`. The label is text, so the meaning does not depend on the callout colour.
6. Removes the `TODO(...)` line and the brief comment once the brief is covered. The gate fails while any `TODO(` remains.

## Style

- Use the locale's spelling (`meta.locale`). Write plainly, in the active voice, with short sentences. Address readers as "you", and speak as "we" for the organisation.
- Be specific and measurable: "at least 24px", "no more than 3 hashtags", "4.5:1". Avoid "where possible" unless you say what to do otherwise.
- Use names from `brand.json`: colour names, token names (`primary-600`) and type tokens (`h2`, `body`). Never retype a hex value or size that a placeholder already shows. If you must mention one, copy it exactly from `brand.json`.
- Use tables for comparisons and specs, lists for rules, and prose for rationale. Give every table a caption by putting a line `Table: What this table shows` directly above it. Without one, the renderer falls back to a caption read only by screen readers, built from the section heading.
- Describe images in links and alt text. Never write "click here".

## Never invent

- Facts about the organisation: history, awards, customer numbers, certifications, legal entity names, registered trademarks.
- Exact Pantone matches. Write "to be matched from a physical Pantone swatch". Name a candidate only if marked "suggested, verify".
- Font licence terms beyond what the source states. SIL OFL fonts are free for commercial use. For commercial foundries, say "confirm licence covers web, apps, print, social and broadcast".

Where something is needed but unknown, write a clearly marked proposal: `*Proposed — confirm with leadership:* …`, and list it in your handoff as an assumption.

## Images in chapters

- Prefer data placeholders: they embed generated assets with alt text automatically.
- If you add `![alt](assets/...)`, the alt text must describe the image's purpose. The path is relative to the workspace root and the file must exist.

## Depth benchmark

A professional chapter is usually 300–900 words plus its data. It covers every item in its brief, gives the reason behind each non-obvious rule, includes at least one Do and one Don't, and calls out the accessibility consideration specific to that topic.
