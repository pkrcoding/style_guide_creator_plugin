# Motion

Motion on our website, app, social posts and in-shop screens should feel like the bakery itself: unhurried, warm and purposeful. Used well, it guides attention; used carelessly, it distracts and can make some people unwell.

## Principles

- **Purposeful:** motion explains something, such as where a panel came from, that an item was added to the basket, or what changed. If it does neither, leave it out.
- **Gentle and quick:** most movement finishes within the `base` duration. Nothing bounces, spins or shakes in everyday interface.
- **Consistent direction:** things enter from where they come from and leave the way they came. Panels slide from the edge they are attached to; dialogs fade and scale slightly from the centre.
- **Soft, not mechanical:** we ease out, decelerating into place like dough settling. A small overshoot is reserved for celebrations, such as an order being confirmed.

## Durations and easing

{{motion}}

| Use | Duration | Easing |
|---|---|---|
| Hover, press, focus changes | `fast` | `standard` |
| Menus, tooltips, small panels opening | `base` | `enter` |
| Closing and dismissing | `fast` | `exit` |
| Dialogs, drawers, page transitions | `slow` | `enter` (in), `exit` (out) |
| Brand moments: logo reveal, order confirmed | `deliberate` | `enter` |

Exits are faster than entrances, so the interface never makes people wait to move on. Never exceed `deliberate` for interface motion.

## Logo animation

*Proposed — confirm with the Brand and Marketing team before production:* the emblem may animate only in video intros and outros, app launch screens and campaign openers.

- The animation lasts no more than 3 seconds and ends on the static, approved emblem.
- Suggested sequence: the outer and inner rings draw in, the tree appears, then the pip settles beside it, and finally the wordmark fades in.
- Never rotate, stretch, bounce, flip or recolour the emblem, and never separate the pip from the tree in the final frame.
- Keep the clear space throughout the animation.
- Provide a static version for reduced-motion settings and for platforms that don't play animation.

## Video intros and outros

- **Intro:** no more than 3 seconds, or skip it on short social videos and let the content start straight away.
- **Outro:** the static emblem on Flour Cream, or the white emblem on Pinecone Brown, with our web address in live text, for 2–3 seconds.
- **Captions:** every video has accurate captions, burned in for social feeds where the platform needs them, and as a caption file wherever possible. Chapter 14 sets the caption style.

## Motion accessibility

- **Reduced motion:** honour `prefers-reduced-motion`. When it is set, replace movement with simple fades of `fast` or shorter, and stop parallax, auto-advancing carousels and looping animation.
- **No flashing:** nothing flashes more than three times in any one second.
- **Pause, stop, hide:** anything that moves, scrolls or auto-updates for more than 5 seconds (carousels, animated banners, looping product videos) has a visible pause control.
- **No autoplaying sound.** Videos start muted, with captions on.
- **Avoid parallax and large zooms;** they can trigger dizziness and nausea.
- **Captions and transcripts** for every video and audio clip.

> **Do** use motion to confirm actions, such as a gentle settle when a bake is added to the basket.

> **Don't** animate text people need to read, such as prices, opening hours or allergen information.

> **Don't** loop animated GIFs or videos indefinitely without a pause control.
