# Sada-e-Rehmat — website

Static site for GitHub Pages. No build step is needed to host it: every `.html` file in the root is ready to serve.

## Editing

The pages are generated from `_src/` so the header, footer and package data stay consistent:

- `_src/data.py` — the Hajj 2027 packages (collections, hotels, itineraries, PKR and USD prices, add-ons, terms).
- `_src/build.py` — page copy and layout for every page.
- `_src/content/` — the guide and policy article text.

After editing, regenerate the pages and commit the result:

```bash
python3 _src/build.py
```

GitHub Pages ignores folders that start with `_`, so `_src/` is never published.

## Hajj 2027 collections

The twelve Category A packages from the 2027 rate sheet are grouped into four collections:

| Collection | Meaning | Rate-sheet tier | Rate-sheet packages |
|---|---|---|---|
| Sakinah | Tranquillity | Silver | 01, 03, 04 |
| Noor | Light | Gold | 02, 09, 10, 11 |
| Rahmah | Mercy | Platinum | 05, 06, 12 |
| Firdaus | The highest garden | Diamond | 07, 08 |

Each journey keeps its rate-sheet number in `data.py` (`sheet=`) for reference.

## Assets

Optimised photographs live in `assets/img/` as WebP at 1000px and 2000px wide. The original full-size JPEGs in `assets/` are kept as source files but are no longer loaded by the site.

## Motion

`script.js` drives the scroll-linked effects (hero that shrinks into a card, words that light up as you read, stacking collection cards, the pinned horizontal Hajj timeline, full-screen site chapters, parallax and count-ups). All motion is switched off for visitors who set "reduce motion" in their operating system.
