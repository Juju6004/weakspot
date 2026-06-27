# weakspot

A small, data-driven pipeline that turns the topics you *actually keep missing* into a structured Anki deck — and lets you rebuild that deck from source without ever losing your review history.

Built on [`genanki`](https://github.com/kerrickstaley/genanki). Shipped with a worked example: an OB/GYN shelf-exam deck (84 cards) generated from a real question-log.

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

## Three-axis tagging — study any slice

Every card is tagged on three independent hierarchical axes (plus its cluster identity), so the same deck slices any way you study:

- `rotation::OBGYN` · `rotation::Medicine` · `rotation::Surgery` …
- `system::Reproductive` · `system::Renal_Urinary` · `system::Nervous` …
- `discipline::Pathology` · `discipline::Pharmacology` · `discipline::Microbiology::Bacteria` …

Example queries in the Anki browser: `tag:discipline::Microbiology::Bacteria` (every bug, every rotation) · `tag:system::Renal_Urinary tag:weak`.

A cluster with no taxonomy entry falls back to a default **and prints a build warning** — so a new card can't go silently untagged.

## How it's wired

```
build_deck.py     model/template + image cards; renders SVG→PNG at build time; packages the .apkg
text_cards.py     the text-only cards (TEXT_CARDS) + mnemonics (MNEM), keyed by cluster
taxonomy.py       cluster → (system, discipline) map + the tag vocabulary
*.svg             source for each image card (plain-text, editable, version-controlled)
examples/         a built sample deck (OB/GYN shelf, 84 cards)
```

The pipeline is one-directional: **weak-area log → SVG → (temp) PNG → `.apkg` → import.** Rendered PNGs are written to a temp dir, bundled into the deck, and deleted — only the editable SVG sources live in the repo.

## Usage

```bash
pip install genanki
python3 build_deck.py      # writes the .apkg; double-click to import into Anki
```

Add a card:
- **text** → add a `C(front, answer, discrim, trap, cluster)` to `TEXT_CARDS` in `text_cards.py`
- **image** → write an SVG, add a card dict (with `svg="..."`) to `cards` in `build_deck.py`
- classify any new cluster in `taxonomy.py` (the build warns you if you forget)

> **SVG→PNG rendering** uses macOS `qlmanage` (Quick Look). On Linux, swap that one `subprocess` call in `build_deck.py` for `rsvg-convert` or `inkscape`.

## A note on content

The example deck is OB/GYN shelf material curated from a personal question-log — standard medical-education content, no patient data. The medicine in the cards is the author's own; the pipeline is the point.

## License

MIT — see [LICENSE](LICENSE).
