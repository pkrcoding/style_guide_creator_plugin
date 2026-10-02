# Data visualisation

Charts and maps are our product. City officers and utility engineers make public decisions from them, and investors judge our rigour by them. Every chart we publish must be accurate, honest about uncertainty and readable by everyone, including people with colour-vision deficiencies, people using screen readers and people printing in black and white.

## Principles

1. **Lead with the finding.** The chart title states what the reader should take away ("Night-time heat risk is highest in the eastern wards"). The subtitle says what is measured, where and when.
2. **Show the data honestly.** Bar axes start at zero, scales are labelled, and ranges and gaps are visible, never smoothed away.
3. **Never use colour alone.** Every colour has a direct label, a pattern, a shape or a position to back it up.
4. **Show uncertainty.** Estimates, models and projections always show their range.
5. **Give an alternative.** Every chart has alt text and a data table or downloadable data.

## Categorical palette

Use these in order for series that are different categories, such as sectors, scenarios or districts. Every colour reaches at least 3:1 against its background. Neighbouring series are **not** guaranteed to differ in lightness, and some pairs look almost identical in greyscale, so every series also needs a direct label and its own line style, marker shape or pattern.

| Order | On light backgrounds | On dark backgrounds |
|---|---|---|
| 1 | Fjord Teal `primary-600` | `primary-500` |
| 2 | `accent-500` (dark amber) | `accent-400` |
| 3 | Polar Night `secondary-900` | `secondary-300` |
| 4 | `secondary-500` (slate) | Exact Daybreak Amber, `accent-300` |
| Context, "other" or benchmark | `neutral-500`, dashed or hatched | `neutral-400`, dashed or hatched |

- Use **four categories at most** in one chart. For more, group the smallest into "Other", or use small multiples (a grid of small charts with one series each).
- The context series is grey **and** dashed or hatched, because grey can be confused with series 4 (light) or series 1 (dark) by some readers.
- Exact Daybreak Amber is below 3:1 on white, so it is never a series colour on light backgrounds.
- Do not use the state colours (success, warning, error, info) as series colours. They mean status, not category.
- In stacked bars, pies and area charts, separate adjacent segments with a 1px line in the background colour. This keeps segments distinct even when two colours have similar lightness.

## Sequential palettes

Use a sequential palette for a single quantity that goes from low to high, such as tree canopy cover, rainfall or energy demand. Use five steps (classes) by default and seven at most.

| Palette | Steps, low to high | Use for |
|---|---|---|
| Fjord Teal | `primary-100`, `primary-300`, `primary-500`, `primary-700`, `primary-900` | Neutral or positive quantities: coverage, capacity, rainfall, population |
| Daybreak | `accent-100`, `accent-300`, `accent-500`, `accent-700`, `accent-900` | Quantities of pressure or heat: emissions, heat exposure, peak load |

- Darker always means more. Do not reverse a palette.
- The lightest steps of the sequential palettes, and the light midpoint of the diverging palettes, are below 3:1 against white. Use them only as **area fills** in maps and heatmaps, where each area has an outline and the legend shows the number range for each step. Never use them for lines, points or bars.

## Diverging palette and temperature

Use a diverging palette when values sit above and below a **meaningful midpoint**, such as a temperature anomaly against a baseline, change from last year, or performance against a target.

| Far below | | | Near below | Midpoint | Near above | | | Far above |
|---|---|---|---|---|---|---|---|---|
| `primary-800` | `primary-600` | `primary-400` | `primary-300` | `neutral-50` | `accent-200` | `accent-400` | `accent-600` | `accent-800` |

We checked this palette under protanopia, deuteranopia and tritanopia and found no confusable steps. Teal-to-amber is a cool-to-warm scale that reads naturally for temperature.

Rules for temperature, emissions and other climate scales:

- **Never use a rainbow (spectral or "jet") scale.** Its bright bands create false boundaries, it has no natural order, and it fails for colour-vision deficiencies.
- **Never use red and green as the two ends.**
- **Name the midpoint.** State it in the legend: for example, "0 °C = average for [baseline period]". Always name the baseline period.
- **Keep it symmetrical.** Use the same number of steps and the same range on each side of the midpoint, unless the data is truly one-sided. If so, use a sequential palette instead.
- **Show absolute temperatures sequentially** (Daybreak palette). Use the diverging palette only for anomalies and changes.
- **Keep scales fixed** across a series of maps or charts that readers will compare, such as each month of a year.
- **Daybreak Amber is not a warning colour.** Warm steps mean "above the midpoint", not "danger". If a threshold matters, such as a heat-health alert level, mark it with a labelled line or outline, not a colour change alone.

## Maps

- **Choropleths (shaded areas) show rates, not totals.** Normalise by population, area or households (for example, "tCO₂e per resident"). For totals, use proportional symbols (sized circles) on a muted base map.
- **Classes:** use 5 to 7 classes with round-number breaks, and state the classification method (equal interval, quantile or natural breaks) in the caption.
- **Boundaries:** outline every area in a 0.5–1px line in the background colour, or `neutral-500` where areas need to stand out from the background.
- **Base maps:** muted neutrals only (`neutral-50` to `neutral-200` for land, `primary-50` for water), so the data layer leads. Roads and labels in `neutral-600`.
- **No data:** show missing areas in `neutral-200` with a diagonal hatch and a "No data" entry in the legend. Never let missing data look like zero.
- **Labels:** name key areas directly on the map. Include a scale bar on any map used for distances, and use an equal-area projection when comparing regions by size.
- **Interactive maps:** every value must also be reachable without a mouse, for example through a sortable table of areas below the map.

## Uncertainty

Our users plan for ranges, not single numbers. Show them.

- **Confidence or prediction bands:** draw the central estimate as a solid 2px line, and the range as a fill in a light step of the same hue (`primary-200` for a Fjord Teal series). Label the band directly, for example "90% interval".
- **Projections:** draw observed data as a solid line and projected data as a dashed line, with a labelled vertical marker at the point where projection begins.
- **Scenarios:** name each scenario on the line, not only in a legend.
- **Estimates in bars:** use error bars, and hatch the bars for modelled or estimated values. Explain the hatching in a note.
- **Never** show a projection as a single line with no range, or crop a range so a trend looks more certain than it is.

## Units, sources and numbers

- Put units in every axis title or label: °C, mm, MWh, tCO₂e. Use SI units and the formats in chapter 12.
- Say whether values are totals, per person, per area or percentages.
- Every chart has a source line in `small` text: data source, period and date of last update.
- Round to a sensible precision and keep the same number of decimal places across a chart.

## Typography and structure in charts

- Use Inter for all chart text, at least 14px on screen (the `small` token), with tabular figures.
- Chart titles use `h4`. Axis titles and labels use `small` in `neutral-600` or darker.
- Gridlines are 1px in `neutral-200` (`border-subtle`): visible, but quieter than the data. Axis lines use `neutral-500`.
- Avoid 3D effects, dual axes, pie charts with more than five slices, and decorative backgrounds.
- Use `radius-none` on chart areas. A small radius on bar ends is not allowed, because it hides the exact value.

## Accessible charts

- **Contrast:** lines, bars, points and outlines reach at least 3:1 against the background.
- **Direct labels:** label series at the end of lines or on bars, instead of relying on a colour legend. If a legend is unavoidable, put it above the chart in the same order as the data.
- **Patterns and shapes:** add hatching to bars and areas, and different marker shapes (circle, triangle, square) to lines, so charts work in greyscale print and for people with colour-vision deficiencies.
- **Alt text:** state the chart type, what it shows and the key takeaway. An illustrative pattern, not real data: "Line chart of average summer night temperature by district, [start year]–[end year]. All districts rise; the steepest rise is in [district]." Do not list every value.
- **Data table:** provide the data as an accessible table below the chart or as a CSV download. In reports, put it in an appendix and link to it.
- **Interactive charts:** tooltips open on keyboard focus as well as hover, and nothing is shown only on hover.

## Charts: do and don't
> **Do** use the categorical, sequential and diverging palettes in this chapter, by token name.

> **Do** state the midpoint and baseline period on every anomaly map or chart.

> **Do** show the uncertainty range for every estimate and projection.

> **Don't** use rainbow or red–green scales.

> **Don't** show raw totals on a choropleth map.

> **Don't** use exact Daybreak Amber for lines, points or text on light backgrounds.
