# Data visualisation

Charts appear in our reports, supplier updates, social posts and slide decks: sales by bake, footfall by day, waste reduced over a season. A chart is only useful if everyone can read it, including people with colour-vision deficiency and people using screen readers.

## Series colour order

Use the colours in this order. They alternate between dark and mid tones, so neighbouring series differ in lightness, not only in hue.

| Order | Colour | Token | Against white |
|---|---|---|---|
| 1 | Pinecone Brown | `primary-800` | Passes 3:1 comfortably |
| 2 | Honey Glaze (mid) | `accent-500` | Passes 3:1 |
| 3 | Forest Pine (deep) | `secondary-900` | Passes 3:1 comfortably |
| 4 | Warm grey | `neutral-500` | Passes 3:1 |

- Use no more than four series in one chart. For more, split into small multiples or highlight the one that matters in Pinecone Brown and show the rest in `neutral-500`.
- Never use exact Honey Glaze (`accent-400`) or any step lighter than 500 for marks on white or Flour Cream. They fall below 3:1.
- Pinecone Brown and deep Forest Pine look similar to people with protanopia or deuteranopia. They are never neighbours in the order, and every series must be labelled directly.
- Several neighbouring series (for example Pinecone Brown and Honey Glaze, or Pinecone Brown and `neutral-500`) have less than 3:1 between them, so always separate every pair of adjacent bars, segments and areas with a 2px gap in the background colour.
- **On dark backgrounds** (`neutral-950`), use exact Honey Glaze, `primary-400` and `secondary-400`, all above 3:1. These three are close in lightness to each other, so direct labels and gaps are required, and patterns are recommended.

## Accessible chart rules

- **Contrast:** every mark (bar, line, point, segment) has at least 3:1 against the background. Lines are at least 2px thick.
- **Direct labels:** label series at the end of a line or on the bar, rather than in a colour-only legend. If a legend is unavoidable, put it next to the chart in the same order as the data.
- **Never colour alone:** combine colour with labels, position, line style (solid, dashed, dotted) or marker shape (circle, square, triangle).
- **Patterns for print:** in one-colour or black-and-white print, use hatching, dots and solid fills to distinguish series.
- **State colours:** don't use red and green to mean bad and good. If a chart needs to show gains and losses, use arrows, signs (+/−) and words.

## Typography in charts

- Chart text uses Source Sans 3, at least 14px on screen (the `small` token) and 9pt in print.
- Numbers use tabular figures so they line up.
- Titles state the finding, not just the topic: for example "Saturday is our busiest day", not "Sales by day". Only state findings the data actually shows.
- Axis labels include units ("Loaves sold", "£ thousands").

## Gridlines and axes

- Gridlines are subtle, in `neutral-200`, and horizontal only for bar and column charts.
- Bar and column axes always start at zero. Line charts may start elsewhere, but label the axis clearly.
- No 3D, shadows, gradients or decorative backgrounds behind data.
- Avoid pie and donut charts with more than five slices. Use a bar chart instead.

## Tables

Tables are often the clearest way to show exact figures, and they are the accessible alternative to a chart.

- Use real table markup (or table styles in Word and PowerPoint) with a header row.
- Right-align numbers and use tabular figures. Left-align text.
- Use a `neutral-50` tint for alternate rows or a `neutral-200` divider; never colour alone to mark a total or a highlight. Add bold or a label.

## Text alternatives

Every chart needs:

1. **Alt text** naming the chart type, what it shows and the key takeaway, for example: "Bar chart of weekly loaves sold, January to March. Sales rose steadily, peaking in the last week of March."
2. **The data** in an accessible table, a linked spreadsheet or a written summary next to the chart.

> **Do** label every series directly and give each chart a title that states its point.

> **Don't** rely on a colour legend, red and green, or 3D effects to tell the story.
