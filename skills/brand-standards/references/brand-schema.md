# brand.json schema (`style-guide-creator/brand@1`)

`init_guide.py` writes every field below with defaults. Fields marked *generated* are produced by scripts and must not be hand-edited.

## meta

| Field | Type | Notes |
|---|---|---|
| `name` | string | Organisation name exactly as it should be written |
| `slug` | string | Lowercase, hyphenated |
| `version` | semver | Bump on every published change |
| `lastUpdated` | ISO date | |
| `owner` | string | Team accountable for the brand |
| `contact` | string | Email or channel for brand questions. Required by the gate |
| `accessibilityTarget` | string | `WCAG 2.2 AA` (default) or `WCAG 2.2 AAA` |
| `locale` / `languages` | BCP 47 | Spelling and formatting locale, e.g. `en-GB`, `en-US`, `ar` |
| `reviewCadence` | string | |
| `assumptions` | string[] | Everything not confirmed by the organisation |

## foundations

`mission`, `vision`, `positioning`, `tagline` (strings); `values` (`[{name, description, behaviour}]`); `personality` (string[]: 3–5 traits); `audiences` (`[{name, needs, channels}]`); `boilerplate` (`{short ≈25 words, medium ≈50, long ≈100}`); `industry`.

## logo

| Field | Notes |
|---|---|
| `master` | Path relative to `brand.json` (copied into `assets/source/`) |
| `symbol` | Optional symbol/monogram path, used for avatars and favicons |
| `type` | wordmark, lettermark, pictorial, abstract, mascot, emblem, combination |
| `description` | Factual description of shapes and letterforms |
| `altText` | e.g. "Northwind Labs logo". Must name the organisation |
| `orientation`, `aspectRatio` | *generated* from analysis |
| `clearSpace` | `{fraction, rule}`: `fraction` × logo height is padded in clear-space assets; `rule` is the human wording, ideally tied to a logo element ("the height of the N") |
| `minSize` | `{digitalPx, printMm, symbolDigitalPx, symbolPrintMm}` |
| `monoStyle` | `auto`, `knockout` or `solid`: how single-colour versions treat lighter internal shapes |
| `fullColourExceptions` | Backgrounds (colour id, `white` or hex) where a person approved the full-colour logo below 3:1. WCAG exempts logotypes; record who approved it and why in chapter 03 |
| `misuse` | string[]: the logo don'ts, also written up in chapter 03 |

## color (*generated* by build_palette.py, except names, `pantone`, `usage` and `proportions`)

- `brand[]`: `{id, name, role, hex, rgb, hsl, oklch, cmyk, pinnedStep, scale{50..950}, steps{step: {hex, contrastWithWhite, ...}}, accessible{textOnLight, uiOnLight, textOnDark, uiOnDark, solidWithWhiteText}, original{...}, pantone?, usage?}`
- `neutral`: `{scale, steps, accessible{body, secondaryText, border, decorativeBorder}}`
- `semantic[]`: `{id: success|warning|error|info, scale, tokens{fg, bg, border, solid, fgOnDark}}`
- `surfaces`: `{light, dark}`
- `proportions`: `{neutral: 60, primary: 30, ...}`, editable
- `pairings[]`: `{fg, bg, fgToken, bgToken, use: body|large|ui|decorative, label, ratio, required, pass, custom?}`
- `customPairings[]`: human-approved extra pairings `{fg, bg, use, label, fgToken?, bgToken?}`. Kept on rebuild, recomputed, and gated like the rest
- `excludedPairings[]`: labels of generated pairings to leave out (e.g. combinations the brand never uses)
- `cvd[]`: `{pair, vision, deltaE}`
- `notes[]`: issues the colour chapter must address

## typography

- `families[]`: `{role: display|body|mono, name, fallback, source, license, url, weights[]}`
- `baseSizePx` (16), `scaleRatio`, `measure`
- `scale[]`: `{token, sizePx, lineHeight, weight, letterSpacing, family (role), usage}`. Tokens `body`, `small` and `label` are required by the gate.

## spacing, grid, radius, elevation, motion, focus

- `spacing`: `{basePx, scale{"0": 0, "1": 4, ...}}`
- `grid`: `{maxContentWidthPx, breakpoints[{id, minPx, columns, gutterPx, marginPx}]}`
- `radius`: `{none, sm, md, lg, xl, pill}` in px
- `elevation`: `{"0".."3": CSS box-shadow}`
- `motion`: `{durations{}, easing{}, reducedMotion}`
- `focus`: `{colorOnLight, colorOnDark, widthPx (≥2), offsetPx, style, onBrand{colourId: {surfaces[], focus, ratio}}}`. `onBrand` is *generated*: the ring colour to use inside sections filled with each brand colour

## social

`handles` (`{platform: "@handle"}`), `platforms` (ids from `skills/social-media-kit/references/social-platforms.json`), `avatarBackground` / `coverBackground` (colour id, `white`, `dark`, `light` or a hex), `hashtags{brand[], campaign[]}`, `contentPillars[{name, purpose, share}]`.

## content

`{dir: "content"}`: the chapter folder.
