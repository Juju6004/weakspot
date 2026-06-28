#!/usr/bin/env python3
"""
Build the OBGYN weak-cluster pilot Anki deck (.apkg) from QLog clusters.

Each card: Front = tight vignette + lead-in question + the mnemonic image.
           Back  = answer  ·  one-line discriminator  ·  the trap it beats.

Run:  python3 build_deck.py
Out:  OBGYN_weak_pilot.apkg   (double-click to import into Anki)
"""

import os
import genanki

HERE = os.path.dirname(os.path.abspath(__file__))

# ---- stable IDs (do NOT change once shared / cards will duplicate) ----
# MODEL_ID bumped when the note schema changed (added Mnemonic field, stable guids).
MODEL_ID = 1607392320
DECK_ID  = 2059400110

model = genanki.Model(
    MODEL_ID,
    "OBGYN Vignette (image)",
    fields=[
        {"name": "Front"},
        {"name": "Image"},
        {"name": "Answer"},
        {"name": "Discriminator"},
        {"name": "Trap"},
        {"name": "Mnemonic"},
    ],
    templates=[
        {
            "name": "Vignette",
            "qfmt": """
<div class="vignette">{{Front}}</div>
<div class="flip">— recall, then flip —</div>
""",
            "afmt": """
<div class="vignette">{{Front}}</div>
<hr id="answer">
<div class="answer">{{Answer}}</div>
{{#Image}}<div class="img">{{Image}}</div>{{/Image}}
<div class="discrim"><b>Tell:</b> {{Discriminator}}</div>
<div class="trap"><b>Beats:</b> {{Trap}}</div>
{{#Mnemonic}}<div class="mnem">💡 {{Mnemonic}}</div>{{/Mnemonic}}
""",
        }
    ],
    css="""
.card { font-family: -apple-system, Helvetica, Arial, sans-serif;
        font-size: 19px; text-align: left; max-width: 720px;
        margin: 0 auto; padding: 14px; }
.vignette { font-size: 18px; line-height: 1.45; }
.flip { margin-top: 18px; font-size: 13px; color: #999; font-style: italic; }
.img { text-align: center; }
.img img { max-width: 100%; height: auto; margin: 12px 0; border-radius: 8px;
           background: #fff; }
hr#answer { border: none; border-top: 2px solid #ccc; margin: 14px 0; }
.answer { font-size: 21px; font-weight: 700; margin-bottom: 8px; }
.discrim { font-size: 17px; margin-bottom: 6px; }
.trap { font-size: 16px; }
.mnem { margin-top: 10px; padding: 8px 10px; font-size: 15px; line-height: 1.4;
        border-radius: 7px; background: #fff8e1; border-left: 3px solid #f2c200; color: #5b4a00; }

/* repeat-miss badge — emphasis scales with the QLog miss count */
.miss-badge { display: block; margin: 0 0 12px 0; padding: 6px 11px; border-radius: 6px;
              font-size: 13px; font-weight: 700; letter-spacing: .02em; }
.miss-badge .miss-ledger { display: block; font-weight: 400; font-size: 11px;
                           opacity: .8; margin-top: 2px; letter-spacing: 0; }
.tier-amber  { background: #fff4d6; color: #8a6d00; border-left: 4px solid #e8b500; }
.tier-orange { background: #ffe3cc; color: #9c4a00; border-left: 4px solid #ff7a18; }
.tier-red    { background: #ffd9d6; color: #a01b10; border-left: 4px solid #e23b2e; }
.nightMode .tier-amber  { background: #2a2410; color: #f0d98a; border-left-color: #e8b500; }
.nightMode .tier-orange { background: #2e1d10; color: #ffb27a; border-left-color: #ff7a18; }
.nightMode .tier-red    { background: #2e1413; color: #ff9b91; border-left-color: #e23b2e; }

/* light mode */
.answer { color: #1b5e20; }
.trap   { color: #a93226; }

/* night mode — brighten so it reads on dark */
.nightMode .answer { color: #6ed98f; }
.nightMode .discrim { color: #e6e6e6; }
.nightMode .trap   { color: #f0998c; }
.nightMode .flip   { color: #888; }
.nightMode .mnem { background: #2a2613; border-left-color: #f2c200; color: #f0e2a8; }
""",
)

deck = genanki.Deck(DECK_ID, "OBGYN Shelf::Weak clusters")


def miss_badge(misses):
    """Repeat-miss badge driven off QLog history.

    misses = space-separated QLog session codes where this concept was missed
    (e.g. "b4 b5 b6 b15"). Returns (badge_html, repeat_tags). The badge is
    prepended to the Front field (renders on both sides — the "slow down" cue
    is wanted on the answer side too). Emphasis scales with the count so a 5x
    miss looks scarier than a one-off. Nothing renders below 2 misses.
    """
    codes = misses.split()
    n = len(codes)
    if n < 2:
        return "", []
    if n >= 5:
        tier, icon, label = "tier-red", "🔥", f"leech &times;{n} &mdash; slow down"
    elif n >= 3:
        tier, icon, label = "tier-orange", "&#9888;", f"keeps catching you &times;{n}"
    else:
        tier, icon, label = "tier-amber", "&#9888;", f"repeat miss &times;{n}"
    ledger = " &middot; ".join(codes)
    badge = (f'<div class="miss-badge {tier}">{icon} {label}'
             f'<span class="miss-ledger">missed: {ledger}</span></div>')
    tags = [f"repeat::{n if n < 5 else '5plus'}"]
    if n >= 5:
        tags.append("leech")
    return badge, tags

# ----------------------------------------------------------------------
# CARDS  — front, image filename, answer, discriminator, trap, tags
# ----------------------------------------------------------------------
cards = [
    dict(
        front=(
            "G3P2 at 34 wk, chronic HTN, sudden severe constant abdominal pain "
            "and dark vaginal bleeding. Uterus is firm and exquisitely tender, "
            "contracting every 1–2 min. FHT category II.<br><br>"
            "<b>Abruption or uterine rupture — and what's the single tell?</b>"
        ),
        svg="demo_abruption-vs-rupture.svg",
        answer="Placental ABRUPTION.",
        discrim=(
            "Firm + tender uterus with the fetus <b>holding station</b> = abruption. "
            "Rupture goes <b>soft</b>, the presenting part <b>loses station</b> / retracts, "
            "pain breaks through an epidural, and you may feel <b>palpable fetal parts "
            "(irregular protuberance)</b> with maternal shock."
        ),
        trap=(
            "Don't default to rupture just because pain is sudden — rupture needs a "
            "prior scar and shows LOST station; abruption's clot is retroplacental "
            "(concealed bleed can exceed what you see)."
        ),
        cluster="abruptio_placentae",
        extra=["discriminator"],
    ),
    dict(
        front=(
            "Postpartum woman with a new seizure (or focal deficit). You reflexively "
            "reach for MgSO4.<br><br>"
            "<b>Before you commit to eclampsia — what one question gates the whole call, "
            "and what are the mimics if it fails?</b>"
        ),
        svg="eclampsia-mimics.svg",
        answer="Ask: are HTN AND proteinuria BOTH present? If either is missing → it is NOT eclampsia.",
        discrim=(
            "Focal weakness + severe HTN → <b>stroke</b> (CT head). "
            "Dilated pupils + ↓Na, no proteinuria → <b>amphetamine</b> (tox). "
            "Papilledema + thrombophilia, no proteinuria → <b>CVST</b> (MR venography)."
        ),
        trap=(
            "Pregnancy + seizure ≠ automatic eclampsia. The stem strips out HTN or "
            "proteinuria on purpose and drops one extra clue pointing at the mimic."
        ),
        mnem="No HTN <i>and</i> no protein, no eclampsia. Both boxes ticked before you reach for the Mg.",
        cluster="eclampsia_mimics",
        extra=["discriminator"],
    ),
    dict(
        front=(
            "Woman 3 months postpartum: palpitations, heat intolerance, weight loss. "
            "TSH low, free T4 high, gland painless.<br><br>"
            "<b>What test splits this from Graves, and how does it change treatment?</b>"
        ),
        svg="postpartum-thyroiditis-uptake.svg",
        answer="Radioactive iodine UPTAKE. LOW uptake = postpartum (destructive) thyroiditis.",
        discrim=(
            "LOW uptake = gland is <b>leaking preformed hormone</b> (destruction): "
            "TRAb neg, TPO pos, painless. HIGH uptake = Graves: TRAb pos, bruit/orbitopathy."
        ),
        trap=(
            "Do NOT give a thionamide for low-uptake thyroiditis — there's no overproduction "
            "to block. β-blocker only; it's self-limited (often → transient hypothyroid phase)."
        ),
        cluster="postpartum_thyroiditis",
        extra=["discriminator"],
    ),
    dict(
        front=(
            "Three women with urine leakage. (A) constant wetness day and night after "
            "an obstructed labor. (B) post-void dribbling + a tender anterior vaginal-wall "
            "mass, recurrent 'UTIs' with negative cultures. (C) leaks exactly when she "
            "coughs, no urgency, normal post-void residual.<br><br>"
            "<b>Name each — and which one do you keep over-picking?</b>"
        ),
        svg="urinary-leakage-matcher.svg",
        answer="A = vesicovaginal fistula · B = urethral diverticulum · C = stress incontinence.",
        discrim=(
            "<b>Continuous</b> day+night = VVF (only). <b>Intermittent</b> + tender anterior "
            "mass that expresses discharge = diverticulum. <b>Positional / with Valsalva</b> = SUI."
        ),
        trap=(
            "You over-pick VVF. It must be CONSTANT — if the leak is intermittent or "
            "positional, it's not a fistula. Confirm VVF with a methylene-blue dye test."
        ),
        mnem="Constant = Conduit (fistula). If the leak has a trigger or a schedule, it's NOT VVF.",
        cluster="urinary_leakage",
        extra=["discriminator"],
    ),
    dict(
        front=(
            "A red, painful breast in a postpartum woman. The options on the shelf: "
            "engorgement, mastitis, abscess, inflammatory breast cancer, Paget.<br><br>"
            "<b>Which four findings split them — and what's the cancer tell?</b>"
        ),
        svg="breast-complaint-differential.svg",
        answer="Split on laterality · fever · antibiotic response · the NIPPLE.",
        discrim=(
            "<b>Bilateral + afebrile</b> day 3–5 = engorgement. <b>Unilateral wedge + fissure</b> "
            "= mastitis. <b>Fluctuant focal</b> = abscess → I&D. <b>Fails abx + normal nipple</b> "
            "= inflammatory cancer → punch biopsy. <b>Eczematous nipple</b> = Paget."
        ),
        trap=(
            "Don't keep treating a red breast that FAILS antibiotics — normal nipple + no "
            "discrete mass = inflammatory cancer, not 'more abx.' Eczematous nipple = Paget, not mastitis."
        ),
        mnem="Antibiotics fail + nipple looks NORMAL → stop refilling abx, think cancer (IBC). Nipple looks WRONG (eczema) → Paget.",
        cluster="breast_differential",
        extra=["discriminator"],
    ),
    dict(
        front=(
            "Third-trimester woman with deranged LFTs. She's itchy. You want to call it "
            "intrahepatic cholestasis and move on.<br><br>"
            "<b>Which two labs must you check first — and how do they split ICP, HELLP, and AFLP?</b>"
        ),
        svg="third-tri-liver.svg",
        answer="GLUCOSE and FIBRINOGEN. Both low = AFLP.",
        discrim=(
            "<b>Hypoglycemia + low fibrinogen</b> (DIC) = AFLP → deliver now. "
            "<b>Low platelets but glucose/fibrinogen normal</b> = HELLP. "
            "<b>Everything normal + ↑bile acids, itch, no rash</b> = ICP → ursodiol."
        ),
        trap=(
            "Don't pattern-match the pruritus to ICP and stop. AFLP can itch too — the "
            "hypoglycemia + low fibrinogen is what unmasks the hepatic synthetic failure."
        ),
        mnem="<b>A</b>FLP = <b>A</b>ll the synthesis is dead → sugar LOW + fibrinogen LOW. Itch alone doesn't equal ICP; check the two labs first.",
        cluster="third_tri_liver",
        extra=["discriminator"],
    ),
    dict(
        front=(
            "Intra-amniotic infection: maternal fever + uterine tenderness / fetal tachycardia "
            "at 31 weeks. FHR is reassuring.<br><br>"
            "<b>You deliver — but by what route, and what's the reflex error?</b>"
        ),
        svg="chorioamnionitis-route.svg",
        answer="Deliver + IV antibiotics regardless of GA — by VAGINAL induction/augmentation.",
        discrim=(
            "Reassuring FHR → augment with oxytocin and deliver vaginally. Cesarean is "
            "ONLY for standard OB indications (non-reassuring tracing, arrest) — never for the infection itself."
        ),
        trap=(
            "You reflex to cesarean here. Cutting into an infected field ↑ maternal morbidity — "
            "the infection is a reason to deliver, not a reason to operate."
        ),
        cluster="chorioamnionitis",
        extra=["discriminator"],
    ),
    dict(
        front=(
            "Forceps delivery. The RIGHT side of the face: smooth forehead, can't close the eye, "
            "and the mouth pulls toward the LEFT when crying.<br><br>"
            "<b>Injury — and how do you tell it from Erb-Duchenne?</b>"
        ),
        svg="facial-nerve-vs-erb.svg",
        answer="Right facial nerve (CN VII) palsy.",
        discrim=(
            "Forehead involvement + can't close the eye = a WHOLE half-face (CN VII) lesion; "
            "the mouth is pulled toward the healthy (left) side. Erb-Duchenne is the ARM "
            "('waiter's tip'), not the face."
        ),
        trap=(
            "Don't pick Erb-Duchenne — that's C5–C6 brachial plexus (adducted, internally "
            "rotated, pronated arm). Forehead + eye = facial nerve."
        ),
        mnem="Forehead's out → it's the FACE nerve (VII), not the arm (Erb). Mouth runs AWAY from the bad side.",
        cluster="birth_injury_facial_palsy",
        extra=["discriminator"],
    ),
    dict(
        front=(
            "Counseling on the 9-valent HPV vaccine: it covers the non-oncogenic types (6/11) "
            "behind a benign genital dermatosis.<br><br>"
            "<b>What does that lesion look like — and what's it NOT?</b>"
        ),
        svg="condyloma-vs-molluscum.svg",
        answer="Soft, cauliflower-like papules — condyloma acuminata (HPV 6/11).",
        discrim=(
            "HPV 6/11 → ~90% of anogenital warts = soft, fleshy, cauliflower clusters. The "
            "9-valent vaccine covers these plus oncogenic 16/18."
        ),
        trap=(
            "Not umbilicated pearly nodules — those are molluscum contagiosum (a poxvirus), "
            "which the HPV vaccine doesn't cover."
        ),
        mnem="Cauliflower = condyloma (HPV). Pearly with a belly-button dimple = molluscum (pox). Vaccine hits the cauliflower, not the pearls.",
        cluster="condyloma_hpv",
        extra=["discriminator"],
    ),
]

# Text-only vignette cards (one per weak QLog cluster) — same template, no image.
from text_cards import TEXT_CARDS
cards += TEXT_CARDS

# Multi-axis tags (rotation / system / discipline) assembled from the taxonomy.
from taxonomy import tags_for

ROTATION = "OBGYN"  # this deck's rotation; new rotations build their own batch

# Render each SVG -> PNG in a throwaway temp dir (PNGs never touch the vault).
import subprocess, tempfile, shutil

build_dir = tempfile.mkdtemp(prefix="anki_png_")
media = []
seen_keys = set()
try:
    for c in cards:
        # Stable identity keyed to the cluster name. The guid seed string is
        # "cluster::<name>" (unchanged from before), so editing a card's wording
        # OR its tags keeps the guid -> Anki updates in place, scheduling preserved.
        cluster = c["cluster"]
        key = f"cluster::{cluster}"
        if key in seen_keys:
            raise SystemExit(f"Duplicate cluster (would collide scheduling): {key}")
        seen_keys.add(key)
        guid = genanki.guid_for(key)
        tags = tags_for(cluster, rotation=ROTATION, extra=c.get("extra"))

        # repeat-miss badge (from the QLog miss history) → prepend to Front + tag
        badge, repeat_tags = miss_badge(c.get("misses", "") or "")
        tags = list(tags) + repeat_tags
        front_field = badge + c["front"]

        svg = c.get("svg")
        if svg:
            svg_path = os.path.join(HERE, svg)
            if not os.path.exists(svg_path):
                raise SystemExit(f"Missing source SVG: {svg_path}")
            png_name = os.path.splitext(svg)[0] + ".png"
            png_path = os.path.join(build_dir, png_name)
            # qlmanage (macOS Quick Look) renders SVG -> <name>.svg.png in -o dir
            subprocess.run(
                ["qlmanage", "-t", "-s", "1360", "-o", build_dir, svg_path],
                check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
            )
            os.replace(os.path.join(build_dir, svg + ".png"), png_path)
            media.append(png_path)
            img_field = f'<img src="{png_name}">'
        else:
            img_field = ""  # text-only card
        note = genanki.Note(
            model=model,
            fields=[
                front_field,
                img_field,
                c["answer"],
                c["discrim"],
                c["trap"],
                c.get("mnem", ""),
            ],
            tags=tags,
            guid=guid,
        )
        deck.add_note(note)

    pkg = genanki.Package(deck)
    pkg.media_files = media
    out = os.path.join(HERE, "OBGYN_weak_pilot.apkg")
    pkg.write_to_file(out)
    print(f"Wrote {out} with {len(cards)} cards + {len(media)} images.")
finally:
    shutil.rmtree(build_dir, ignore_errors=True)
