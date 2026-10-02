# Writing style

Consistent spelling, numbers and units make our work look precise and make it easier to trust. This matters more for Northwind Labs than for most organisations: a misplaced unit or an ambiguous date in a report can change an engineering decision or a council budget. These rules apply to everything we publish, from product labels to investor updates. Our house language is British English (en-GB).

When this chapter does not cover something, follow the GOV.UK style guide, which many of our public-sector readers already know. For scientific notation and units, follow the International System of Units (SI).

## Our name

- Write **Northwind Labs** in full, with capital N and L, the first time it appears. After that, "Northwind Labs" or "we" are both fine.
- Never write "NWL", "Northwind" alone in formal text, "NorthWind", "northwind labs" or "NORTHWIND LABS". The logo sets "LABS" in capitals as a design detail. Do not copy that in text.
- The possessive is **Northwind Labs'** ("Northwind Labs' methodology"). Where that reads awkwardly, rephrase: "the Northwind Labs methodology" or "our methodology".
- Treat the name as singular in British English when it means the company: "Northwind Labs is", not "Northwind Labs are". Use "we" for the people.
- *Proposed — confirm with leadership:* Product and feature names follow the same rules. Capitalise them only once they are formally named and approved.

## Spelling

Use British spelling with -ise endings.

| Use | Not |
|---|---|
| organisation, prioritise, analyse, optimise | organization, prioritize, analyze, optimize |
| colour, behaviour, modelling, labelled | color, behavior, modeling, labeled |
| centre, metre (unit), litre | center, meter (unit), liter |
| programme (a plan of work), program (software) | program (for a plan of work) |
| licence (noun), license (verb) | license (noun) |
| decarbonisation | decarbonization |

"Data" is singular in our general content ("the data shows"). In academic papers, follow the journal's style.

When you write for a US partner or audience, keep British spelling unless the partner's own guidelines require otherwise for co-branded material.

## Grammar and punctuation

- **Active voice.** "We updated the model", not "The model was updated". Passive voice that hides who did something is never acceptable in a correction or apology.
- **Serial comma.** We do not use the serial (Oxford) comma by default ("energy, water and transport"). Add one when a list would otherwise be ambiguous.
- **Quotation marks.** Use single quotation marks, with double marks for a quote inside a quote: 'The officer said, "The map was clear," and approved the plan.' Put full stops outside the quotation marks unless the quote is a full sentence.
- **Dashes.** Use a spaced en dash ( – ) for an aside, sparingly. Use an unspaced en dash for ranges in tables (2025–2030). Use a hyphen for compound adjectives (a net-zero target, a long-term plan). The em dash in this guide's "Proposed — confirm with leadership" label is an editorial marker, not a style to copy.
- **Ampersands.** Write "and". Use "&" only in official names that include it.
- **Exclamation marks.** Avoid them. Never use more than one.
- **Contractions.** Use common contractions (we're, you'll, don't) in marketing, social and product copy. Avoid them in reports, legal text and investor material.

## Capitalisation

- Use **sentence case** for headings, titles, buttons, menu items, labels, table headers, chart titles and email subject lines: "Download the summer demand report", not "Download The Summer Demand Report".
- Capitalise proper nouns, product names, programmes with official names and job titles only when they come before a name: "Head of Data Priya Shah" (illustrative name), but "our head of data".
- Write "net zero", "climate change", "the grid" and "the council" in lower case unless part of an official name.
- Never use ALL CAPS for emphasis in text. Some screen readers spell capitals letter by letter, and capitals are harder to read. Where a design calls for small capital labels, use CSS `text-transform` so the underlying text stays in sentence case.

## Numbers

- Write one to nine in words and 10 and above as numerals: "three sites", "12 substations".
- Always use numerals for data, measurements, units, percentages, money, dates and times, even below 10: "4 MW", "3%", "£5".
- Use a comma for thousands: 1,000 and 24,500. Use a full stop for decimals: 2.5.
- Write "million" and "billion" in prose (£2.5 million, 1.2 million tonnes). In tables and charts you may use "m", "bn" and unit prefixes, with a key.
- Use the true minus sign (−) for negative numbers in typeset documents and charts. A hyphen is acceptable in CSV and code.
- Say **percentage points** when comparing two percentages: "Renewable share rose from 30% to 35%, an increase of 5 percentage points", not "5%".
- Start a sentence with a word, not a numeral: "Twelve sites" or rephrase.
- Ranges: "from 10 to 20" or "10 to 20" in prose; "10–20" in tables. Repeat the unit if it could be misread: "5 MW to 10 MW".

### Uncertainty and precision

- Round to the precision the data supports, and say when figures are rounded. Do not write 12,437.6 tCO₂e if the uncertainty is about 10%; write "about 12,400 tCO₂e".
- Show ranges as "1,800 to 2,300 tCO₂e (central estimate 2,050 tCO₂e)". In technical documents you may add the interval type: "(90% confidence interval)".
- *Proposed — confirm with leadership:* Use these likelihood terms consistently, and define them in methodology notes.

| Term | Use when the probability is about |
|---|---|
| virtually certain | over 99% |
| very likely | over 90% |
| likely | over 66% |
| about as likely as not | 33% to 66% |
| unlikely | under 33% |
| very unlikely | under 10% |

These bands follow the calibrated language used in climate science assessment reports, which many of our readers recognise.

## Units and scientific notation

Our engineers need exact units. Our policy and investor readers need to know what those units mean. Do both.

- Use **metric (SI) units first**. *Proposed — confirm with leadership:* add imperial equivalents in brackets only for audiences that need them.
- Put a space between the number and the unit: 5 MW, 120 kWh, 20 °C. Use a non-breaking space so the number and unit stay on the same line. The exception is the per cent sign: 45%.
- Unit symbols are case-sensitive and never take an "s" for plurals: kW (not KW or kw), MWh (not Mwh), GWh, kV, tCO₂e (not tons CO2).
- Do not confuse power and energy. **kW, MW and GW measure power** (a rate, such as a substation's capacity). **kWh, MWh and GWh measure energy** (an amount over time, such as a household's annual use).
- Write **tonnes**, not "tons". Use Mt for million tonnes (MtCO₂e) and kt for thousand tonnes.
- **CO₂ and tCO₂e** take a subscript 2. Use true subscript formatting in HTML, Word and slides. Where formatting is unavailable and the font supports it, use the subscript character (₂). On social platforms and in plain-text fields, write "CO2" and "tCO2e": platform fonts and screen readers handle subscript characters inconsistently.
- Write intensities with a solidus: gCO₂e/kWh, kWh/m².
- Explain each unit in plain words on first use in non-technical content: "tonnes of carbon dioxide equivalent (tCO₂e), a single measure that combines the warming effect of different greenhouse gases".
- Name the emissions scope when it matters: "Scope 2 (purchased electricity) emissions", using the Greenhouse Gas Protocol's definitions.

> **Accessibility** Screen readers may read "MW" as a word and "tCO2e" as letters. In audio, video and alt text, write units out in full ("megawatts", "tonnes of CO2 equivalent").

## Dates and times

- Write dates as **day month year**: 2 October 2026. Use "Friday 2 October 2026" when the day matters. Do not use ordinals (2nd) or numeric dates (02/10/26) in prose, because they are read differently in different countries.
- Date ranges: "2 to 6 October 2026" in prose, "2–6 Oct 2026" in tables.
- Financial and reporting years: "the 2026 to 2027 financial year" in prose, "2026/27" in tables. Always say which year type you mean (calendar, financial or a customer's reporting year).
- Times: use the 12-hour clock in general content (9am, 2:30pm, midday, midnight). Use the 24-hour clock with a time zone for operational schedules and incidents: 14:30 BST.
- In data files, APIs and logs, use ISO 8601 with a time zone: 2026-10-02T14:30:00Z. Say "UTC" or "local time" in every interface that shows timestamps.

## Currency, phone numbers and addresses

- Use the symbol before the number with no space: £10, £10.50, €5. Do not add ".00" to whole amounts.
- When a document mixes currencies, use ISO codes in tables (GBP, EUR, USD) and say which exchange rate and date you used.
- Phone numbers use the international format with spaces: +44 20 7946 0000 (fictional example). Make phone numbers selectable links on mobile.
- Write addresses on separate lines with no commas at line ends, in the order the country's postal service uses. Do not abbreviate street names in body text.

## Abbreviations and acronyms

- Spell out an acronym the first time you use it on a page, followed by the acronym in brackets: "greenhouse gas (GHG)". Then use the acronym.
- Do not define acronyms people already know better in short form, such as UK, PDF or CSV.
- Do not use full stops in acronyms or abbreviations: BST, UK, CSV.
- Write "for example", "that is" and "and so on" instead of "eg", "ie" and "etc" in prose, because some screen readers misread them.
- Limit each page or screen to a few acronyms. If you need more, add a glossary.

## Links and calls to action

- Link text must make sense on its own and say where it goes: "Read the methodology note", not "click here" or "learn more".
- Start buttons with a verb and keep them short: "Export as CSV", "Book a demo", "Download the report".
- Say when a link opens a file, with its format and size: "Annual impact summary (PDF, 2 MB)".
- Do not open links in new tabs unless the user would lose work. If you must, say so in the link text.

## Lists

- Introduce a list with a lead-in line that ends in a colon.
- Start each item with a capital letter only if it is a full sentence. Otherwise use lower case.
- Do not put semicolons or "and" at the end of items. Use a full stop only after full sentences.
- Use numbered lists for steps in order and bullets for everything else. Keep lists to about seven items.

## Plain language

Plain language is how we make precise content usable by everyone, including people reading in a second language, people with cognitive or learning disabilities, and busy experts.

- **Reading age:** aim for a reading age of 9 to 11 for public-facing content such as the website, social posts and summaries written for residents. Technical documents may use technical terms, but still use plain sentence structure.
- **Sentence length:** average 15 to 20 words, and no sentence over 30 words. One idea per sentence.
- **Put the point first.** Every report, email and page opens with the finding or the action, then the detail.
- **Layer technical content.** Give a plain-language summary at the top, the detail below it, and the full method in a linked note.
- **Use common words.** "Use", not "utilise"; "help", not "facilitate"; "about", not "approximately"; "start", not "commence".

## Inclusive language

- **Disability:** we follow the UK social model and say "disabled people", unless an individual or community tells us they prefer another term. Never use "suffers from", "wheelchair-bound", "the disabled" or "normal" as the opposite of disabled.
- **Ableist metaphors:** avoid "blind spot" (say "gap"), "falling on deaf ears" (say "being ignored"), "crippling costs" (say "severe costs"), "sanity check" (say "quick check") and "lame" or "crazy".
- **Gender:** use gender-neutral terms: "they", "everyone", "chair", "staff", "person-hours", "engineers" (not "linesmen" or "manpower").
- **Age:** do not describe people by age unless it is relevant to the data, such as "people over 75 are more vulnerable to heat".
- **Race, culture and place:** use the names communities use for themselves. Say "lower-income countries", not "third world". Avoid idioms, sports and military metaphors ("war on carbon", "moonshot", "hit it out of the park"), which exclude many readers and translate badly.
- **Climate impacts on people:** describe exposure, not weakness. Say "people most exposed to flooding", not "vulnerable populations", and "people displaced by climate-related disasters", not "climate refugees", which has a specific legal meaning. Do not imply that communities are to blame for the risks they face.
- **Technical terms:** use "primary and replica" and "allowlist and blocklist".

## Accessible content

- Use meaningful headings in order (heading 1, then 2, then 3), so people can navigate with assistive technology.
- Never give instructions that depend on sight, colour or position alone. Write "Select Export", not "click the green button on the right".
- Describe charts in text: state the main finding in the title or caption, and offer the data as a table or CSV.
- Every meaningful image needs alt text that explains its purpose. Every video needs accurate captions, and audio needs a transcript.
- **Hashtags:** use CamelCase so screen readers read them as words (#ClimateData, not #climatedata). Use no more than three per post, at the end.
- **Emoji:** use sparingly, never more than one or two per post, never in place of words, and only at the end of a sentence. Screen readers announce each emoji by name.
- Never use "fancy" Unicode letters (bold or script characters from symbol blocks) on social. Screen readers cannot read them.

> **Do** write "Peak demand rose by an estimated 8% (range 6% to 10%) between 2023 and 2025."

> **Don't** write "Peak demand rose 8.137%!!" with no baseline, period or uncertainty.

## Glossary of preferred spellings

| Term | Notes |
|---|---|
| Northwind Labs | Never abbreviated |
| climate data analytics | Lower case |
| net zero, net-zero target | Two words as a noun, hyphenated as an adjective |
| decarbonisation | British spelling |
| tCO₂e | Tonnes of carbon dioxide equivalent. Explain on first use |
| kW, MW, GW | Power (rate) |
| kWh, MWh, GWh | Energy (amount) |
| Scope 1, Scope 2, Scope 3 | Capital S, numerals. Greenhouse Gas Protocol definitions |
| dataset | One word |
| real time, real-time data | Two words as a noun, hyphenated as an adjective |
| email, online, website | No hyphens |
| heatwave | One word |
| grid carbon intensity | Lower case. Give the unit (gCO₂e/kWh) |
