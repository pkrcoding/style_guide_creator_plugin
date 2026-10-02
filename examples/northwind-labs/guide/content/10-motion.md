# Motion

Motion helps people follow what changes on screen, such as a filter applied to a map or a panel opening. Used carelessly, it distracts, slows people down and can make some people unwell. Our motion is like our logo: precise, short and purposeful.

## Principles

- **Purposeful.** Every animation explains something: where an item came from, what changed, or what to look at next. If it explains nothing, remove it.
- **Quick and precise.** Short durations and standard easing. Nothing bounces, wobbles or overshoots.
- **Consistent direction.** New content enters from the direction the user moved towards. Rising values and progress move upwards, echoing the peak in our symbol.
- **Data first.** When data updates, animate the change (for example, bars growing to their new length) so readers can see what moved. Never animate data in a way that misrepresents it, such as overshooting a value.

## Tokens

Use the duration and easing tokens. Do not set times or curves by eye.

{{motion}}

| Use | Duration | Easing |
|---|---|---|
| Hover and press feedback, colour changes, focus rings appearing | `duration-fast` | `ease-standard` |
| Small components: dropdowns, tooltips, toggles, accordions | `duration-base` | `ease-enter` to open, `ease-exit` to close |
| Panels, dialogs, drawers, chart and map updates | `duration-slow` | `ease-enter` to open, `ease-exit` to close |
| Page transitions and large chart transitions in presentations | `duration-deliberate` | `ease-standard` |
| Focus ring and essential state changes under reduced motion | `duration-instant` | — |

- Exits are faster than entrances: people have already decided to move on.
- Never animate for longer than `duration-deliberate` in an interface. Longer animations belong only in video.
- Animate opacity and position (transform), not width, height or layout, so motion stays smooth.

## Logo animation

The logo may be animated only in video intros, end cards and presentation title slides, using a version made or approved by the Marketing team.

- The animation lasts **3 seconds at most** and always **ends on the static, approved logo**.
- Movement comes from the logo's own geometry. For example, the circle draws in and the amber peak rises into place, then the wordmark fades in.
- Never stretch, rotate, bounce, morph, recolour or distort the logo, and never move the parts out of their final relationship for longer than the animation itself.
- The clear space and background rules in chapter 3 apply to every frame.
- Supply a static logo for anyone who has turned motion off.

## Video intros and outros

- **Intro:** 3 seconds at most, or none at all on social video, where the first second must show the content.
- **Outro (end card):** the full logo on a brand-colour background, following the background table in chapter 3, held for 2 to 5 seconds, with the website address as live text.
- **Lower thirds:** Inter, on a solid Polar Night or Fjord Teal panel, entering with `ease-enter` and leaving with `ease-exit`.
- Video titles, captions and calls to action follow chapter 14.

## Motion accessibility
- **Honour reduced motion.** When a user's device is set to `prefers-reduced-motion`, follow the reduced-motion rule under the motion tokens above: replace movement with short fades and stop parallax, auto-advancing carousels and loops. Design the reduced version first, then add motion.
- **No flashing.** Nothing flashes more than three times in any one second. Avoid large areas of rapidly alternating light and dark, including in video and animated charts.
- **Pause, stop or hide.** Anything that moves, blinks or scrolls automatically for more than 5 seconds, including carousels, animated charts, background video and live data tickers, has a visible pause control that works with a keyboard.
- **No autoplaying audio.** Video with sound starts muted or only when the user presses play.
- **Avoid vestibular triggers.** Do not use parallax scrolling, large zooms, spinning or full-screen slides, which can cause dizziness and nausea.
- **Captions.** Every video has accurate captions. Videos that explain data also need an audio description or a transcript that describes what the charts show.
- **Focus stays visible.** Animations never hide or delay the focus ring.

## Motion: do and don't
> **Do** use motion to show how data changed, with the duration tokens.

> **Do** check every animation with reduced motion turned on.

> **Do** end every logo animation on the static, approved logo within 3 seconds.

> **Don't** use bounce, elastic or overshoot easing.

> **Don't** autoplay looping animation or video without a pause control.

> **Don't** spin, stretch or morph the logo.
