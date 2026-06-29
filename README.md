# weakspot

A small, data-driven pipeline that turns the topics you *actually keep missing* into a structured Anki deck — and lets you rebuild that deck from source without ever losing your review history.

Built on [`genanki`](https://github.com/kerrickstaley/genanki). Shipped with a worked example: an OB/GYN shelf-exam deck (159 cards) generated from a real question-log.

> **This repo is a live record, not a frozen demo.** I'm a med student actively using `weakspot` for shelf prep — the example deck *is* my real weak set, and it grows as I keep logging question blocks. Card counts move, clusters get added, and the repeat-miss badges tick up. See [A live record](#a-live-record) below.

## Why this exists

Hand-making Anki cards has two problems once a deck gets serious:

1. **Cards drift from your weak spots.** You make cards for whatever you happened to think of, not for what you measurably keep getting wrong.
2. **You can't safely regenerate a deck.** Reword 50 cards or fix a template and re-import, and Anki either creates duplicates or resets your scheduling — so people stop editing in bulk and the deck rots.

`weakspot` fixes both: cards are generated from a structured log of your weak areas, and the build is **idempotent** — rebuild as often as you like and Anki updates cards *in place*, preserving every card's scheduling.

## The key idea: stable, identity-keyed GUIDs

Each card's GUID is derived from its **cluster identity** (`genanki.guid_for("cluster::<name>")`), **not** its text.

- Reword a card, change its tags, swap its diagram → on re-import Anki recognizes it by GUID and **updates it in place. Your due dates and intervals survive.**
- The build **fails loudly** if two cards share a cluster key, so you can never silently collide two cards' scheduling.

This is the difference between a one-off export script and a deck you can maintain as code for years.

## What a card looks like

Two tiers, same front/back template:

- **Text cards** (the bulk) — a tight clinical vignette + lead-in question on the front; **Answer → Tell** (the one-line discriminator) **→ Beats** (the trap it beats) **→ 💡 Mnemonic** (optional) on the back.
- **Image cards** — same, with a hand-built SVG diagram on the back. An image card only earns its place when there's a *visual* discriminator you keep missing.
- **Diagram-back cards** — the back is a generated arrow-chart (cue chips → *the tell* → boxed answer → a "ruled out" column with each distractor's one-line reason). Authored as data, laid out by `diagram.py` — no hand-placed coordinates, auto-sized, so the elimination logic reads as a chart instead of a paragraph.

## Three-axis tagging — study any slice

Every card is tagged on three independent hierarchical axes (plus its cluster identity), so the same deck slices any way you study:

- `rotation::OBGYN` · `rotation::Medicine` · `rotation::Surgery` …
- `system::Reproductive` · `system::Renal_Urinary` · `system::Nervous` …
- `discipline::Pathology` · `discipline::Pharmacology` · `discipline::Microbiology::Bacteria` …

Example queries in the Anki browser: `tag:discipline::Microbiology::Bacteria` (every bug, every rotation) · `tag:system::Renal_Urinary tag:weak`.

A cluster with no taxonomy entry falls back to a default **and prints a build warning** — so a new card can't go silently untagged.

## Repeat-miss badges

When the *same* concept burns you across multiple logged sessions, the card carries a scaled badge baked from that miss history — **amber at 2×, orange at 3–4×, red "leech" at 5+** — plus a `repeat::N` tag so you can drill your most persistent holes as their own slice. The emphasis grows with the count, so the stuff you keep flipping *looks* louder than a one-off instead of blending in.

```python
C(front, answer, discrim, trap, cluster, misses="s4 s5 s6 s9")  # 4 misses → orange badge + repeat::4
```

## How it's wired

```
build_deck.py     model/template + image cards; renders SVG→PNG at build time; packages the .apkg
text_cards.py     the text-only cards (TEXT_CARDS) + mnemonics (MNEM), keyed by cluster
taxonomy.py       cluster → (system, discipline) map + the tag vocabulary
*.svg             source for each image card (plain-text, editable, version-controlled)
diagram.py        generates discriminator arrow-chart SVGs (the "diagram-back" cards) from a spec
diagram_cards.py  the diagram-back cards (DIAGRAM_CARDS), keyed by cluster
examples/         a built sample deck (OB/GYN shelf, 159 cards)
```

The pipeline is one-directional: **weak-area log → SVG → (temp) PNG → `.apkg` → import.** Rendered PNGs are written to a temp dir, bundled into the deck, and deleted — only the editable SVG sources live in the repo.

## Usage

```bash
pip install genanki
python3 build_deck.py      # writes the .apkg; double-click to import into Anki
```

Add a card:
- **text** → add a `C(front, answer, discrim, trap, cluster)` to `TEXT_CARDS` in `text_cards.py`
- **image (schematic)** → write an SVG, add a card dict (with `svg="..."`) to `cards` in `build_deck.py`
- **image (ready-made raster)** → set `img="..."` on a card dict — a real photo/scan committed to the repo, or a personal/bring-your-own file in the gitignored `local_media/`. If a `local_media/` file is absent (e.g. on a fresh clone) the card builds text-only instead of failing.
- classify any new cluster in `taxonomy.py` (the build warns you if you forget)

> **SVG→PNG rendering** uses macOS `qlmanage` (Quick Look). On Linux, swap that one `subprocess` call in `build_deck.py` for `rsvg-convert` or `inkscape`.

## A live record

heads up — this isnt a polished one-and-done demo, its the actual tool im studying off of. im a med student grinding through clerkship shelves, and the OB/GYN example deck is my real weak set: the cards come straight from a question-log of stuff i actually kept missing, badges and all. so it moves. i log a qbank block, the genuine content holes get folded in as cards, the `missed:` ledgers tick up, the deck rebuilds. clone this a month from now and the counts wont match whats written above — thats the point. the deck tracks what im currently bad at, it doesnt sit frozen.

the medicine in the cards is my own terse summaries from my qbank review — standard med-ed content, no patient data, nothing identifiable. the pipeline is the part im actually showing off; the OB content is just the worked example it happens to be carrying.

## License

MIT — see [LICENSE](LICENSE).
