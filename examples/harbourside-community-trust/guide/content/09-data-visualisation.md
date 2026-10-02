# Data visualisation

Charts in our annual report, funding bids and reports to council partners show the difference our work makes. They must be accurate, easy to read at a glance and readable by everyone, including people who can't see colour differences and people using screen readers.

## Choosing a chart

- **Bar charts** for comparing amounts (meals served per neighbourhood). Bars run horizontally when labels are long.
- **Line charts** for change over time (families housed each month).
- **A single big number** with a short sentence when there is only one figure to show.
- **Tables** when people need exact values.
- Avoid pie and doughnut charts with more than five slices, 3D charts, and dual axes.
- Always start bar chart axes at zero. Show the source and date of the data under every chart.

## Series colours

Use colours in this order, so every chart in a report looks consistent:

| Order | On white | On dark (`neutral-950`) |
|---|---|---|
| 1 | Harbour Blue (`primary-700`) | `primary-500` |
| 2 | `secondary-500` | Sunset Coral (`secondary-400`) |
| 3 | `accent-600` | `accent-200` |
| 4 | `neutral-800` | `neutral-400` |

Every colour in this order reaches at least 3:1 against its background. We checked the set with colour-vision simulations and no pair was flagged as confusable. In greyscale, though, Harbour Blue and `neutral-800` look similar, so add patterns or labels when charts may be printed in black and white.

- **Up to four series.** If you need more, split the chart into small multiples or use a table.
- **Highlight, then mute:** to make one point, show the key series in Harbour Blue and the others in `neutral-500`.
- **Neighbouring colours don't reach 3:1 with each other**, so separate adjacent bars, stacked segments and slices with a 2px white gap (or a `neutral-950` gap in dark mode).
- Don't use exact Tide Blue or exact Sunset Coral for marks on white; they are below 3:1. They may be used for background bands or highlight areas behind data.
- Never use the success, warning or error colours as series colours, and never use red and green as the only difference.

## Labels, patterns and legends

- **Label directly:** put series names at the end of lines or next to bars instead of in a separate colour legend.
- **Patterns for print:** in printed reports, add a pattern (diagonal lines, dots) or a different marker shape (circle, square, triangle) to each series after the first.
- **Show the numbers:** label key values on bars or points so readers don't need to estimate.
- **Gridlines:** few and light, in `border-subtle`. They guide the eye but carry no meaning.

## Typography in charts

- Use Atkinson Hyperlegible Next for all chart text.
- Labels at least 14px on screen (`small`) and 10pt in print (9pt only in partner reports). Titles use `h4` on screen.
- Use tabular figures, and format numbers, dates and currency as set out in chapter 12.
- Write chart titles as the key finding: "We served 20% more meals in winter" rather than "Meals by month". (This example is illustrative, not real data.)
- Keep all text horizontal; don't rotate axis labels.

## Text alternatives

Every chart needs a text alternative, because a chart image is invisible to screen readers and hard to read for many people.

- **Alt text or caption** with three parts: the type of chart, what it shows, and the key takeaway. For example: "Bar chart of meals served in each neighbourhood in 2025. The harbour front served the most."
- **A data table** next to the chart or in an appendix, with a header row and units in the column headings.
- For council partners, provide the underlying data as a spreadsheet (CSV or XLSX) on request.
- In PDFs, tag charts as figures with alt text (chapter 17).

> **Do** label data directly, show the source, and give every chart a plain-language takeaway.

> **Don't** rely on a colour key alone, use 3D effects, or cut a bar chart's axis above zero.

> **Accessibility** Chart marks need at least 3:1 against the background, and meaning must also be shown with labels, patterns or position, never colour alone.
