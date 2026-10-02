# Motion

Movement should feel like our logo: a calm tide and a slowly rising sun, never a jolt. We use motion only to help people understand what is happening, and we always respect people who need less of it.

## Principles

- **Purposeful:** motion explains a change, such as a menu opening, a message appearing or a step completing. Never animate just to decorate.
- **Gentle and quick:** short movements with a soft ease-out, so things settle into place like water coming to rest. No bouncing, except a single small overshoot for a celebration (for example, "Thank you for your donation").
- **Consistent direction:** things enter from where they will be and leave the way they came. Panels slide from the side they are attached to; messages rise up gently from the bottom.
- **Small distances:** move items by no more than `space-5` to `space-6`. Large sweeps across the screen are tiring and can cause motion sickness.

## Durations and easing

{{motion}}

| Interaction | Duration | Easing |
|---|---|---|
| Hover, focus and pressed states | `duration-fast` | `ease-standard` |
| Toggles, tabs, small menus | `duration-base` | `ease-standard` |
| Items appearing (messages, dropdowns, cards) | `duration-base` to `duration-slow` | `ease-enter` |
| Items leaving | `duration-fast` to `duration-base` | `ease-exit` |
| Dialogs and side panels | `duration-slow` | `ease-enter` in, `ease-exit` out |
| Page transitions and large panels | `duration-deliberate` at most | `ease-standard` |

Exits are faster than entrances: people have already decided to move on.

## Logo animation

*Proposed — confirm with the Communications team:* a short logo sting for video, in which the sun rises gently from behind the waves, then the wordmark fades in.

- Lasts no more than 3 seconds and ends on the static, approved logo, held for at least 1 second.
- Never stretches, spins, bounces or distorts the logo, or changes its colours.
- Uses vector artwork prepared by a designer, not the PNG.
- Plays once. Never loops.

## Video intros and outros

- **Intro:** no more than 3 seconds of branding before the content starts. On social media, start with the story, not the logo.
- **Outro (end card):** the logo on white (full colour) or on Harbour Blue (reversed), with our website address and a call to action in text, held for 3 to 5 seconds.
- **Captions** on every video, with our type styles from chapter 05, and lower thirds kept inside the platform's safe zone (chapter 15).

## Motion accessibility
- **Reduced motion:** honour the `prefers-reduced-motion` setting. Replace movement with short fades, as set out in the reduced-motion rule above, and stop parallax, looping animation and auto-advancing carousels.
- **No flashing:** nothing may flash more than three times in any one second.
- **Pause, stop, hide:** anything that moves, scrolls or updates automatically for more than 5 seconds needs a visible pause or stop button.
- **No autoplaying sound.** Videos start muted, with captions on.
- **Avoid parallax, large zooms and full-screen sweeps**, which can trigger dizziness and nausea.
- **Captions and transcripts** for all video and audio content.

> **Do** use short, soft ease-out movements that explain a change on screen.

> **Don't** autoplay video with sound, loop animations endlessly, or animate the logo in ways that distort it.
