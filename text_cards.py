# -*- coding: utf-8 -*-
"""
Text-only vignette cards (no image) — one per weak QLog cluster.
Same front/back format as the image cards: vignette -> Answer / Tell / Beats.
Sourced from your own question-log (QLog) weak-cluster summaries — curated, not model-generated.
Each dict has no "svg" key, so build_deck.py leaves the Image field empty.
"""

def C(front, answer, discrim, trap, cluster, mnem="", misses="", extra=None):
    # tags are assembled at build time from the taxonomy (rotation/system/discipline);
    # here we just carry the stable cluster identity.
    # misses = space-separated QLog session codes where this concept was missed
    # (e.g. "b4 b5 b6 b15"); build_deck renders a scaled repeat-miss badge from it.
    # extra = additional flat tags (e.g. ["source::NBME", "nbme-only"]).
    return dict(front=front, answer=answer, discrim=discrim, trap=trap, mnem=mnem,
                cluster=cluster, misses=misses, extra=extra)

# Mnemonics keyed by cluster — kept separate so they're easy to edit/prune.
# Keep them standard, or add your own personal hooks — prune whatever doesn't land.
MNEM = {
    "pregnancy_first": "Before any fancy test, <b>P</b>ee in the cup — β-hCG is always move #1.",
    "galactorrhea_hyperprolactinemia": "High TSH driving high prolactin: fix the thyroid, the milk dries up. Treat the ROOT (thyroid), not the leaf (prolactin).",
    "POI_POF": "Ovary quits early → pituitary SCREAMS (↑FSH/LH) but the room goes DARK (↓estradiol). Loud gonadotropins, low estrogen.",
    "atrophic_vaginitis_GSM": "'Recurrent UTI' but cultures keep coming back NEGATIVE = it's not bugs, it's atrophy. Estrogen, not antibiotics.",
    "aromatase_deficiency": "Aromatase turns Androgens → Estrogen. Lose it → androgens pile up (virilized XX) but 17-OHP stays NORMAL — that normal 17-OHP is your 'not CAH' stamp.",
    "postmenopausal_bleeding": "Postmenopausal bleed = biopsy. Tissue before treatment — no exceptions.",
    "GTD_surveillance": "A new pregnancy's hCG looks exactly like cancer coming back — so no pregnancy until the number hits zero and stays.",
    "PCOS_pathophys": "<b>T</b>heca makes <b>T</b>estosterone; <b>G</b>ranulosa does the <b>G</b>irly conversion (aromatase → estrogen).",
    "leiomyoma_iud": "Submucosal fibroid = a speed-bump in the cavity → the IUD gets bounced OUT (expulsion). Fibroids basically never turn cancerous.",
    "HSIL_colposcopy": "HIGH-grade = look NOW (colposcopy). Save the wait-and-retest moves for LOW-grade.",
    "androgen_insensitivity": "No receptor for androgen → no hair, no uterus, but 46,<b>XY</b>. Scant hair = the body literally can't hear testosterone.",
    "Rh_kleihauer": "<b>K</b>leihauer-<b>B</b>etke = <b>K</b>ount the <b>B</b>abies' cells (fetal RBC volume). Titer (Coombs) is a different test.",
    "magnesium_kidney": "Mg leaves through the kidneys only — bad kidneys = Mg builds up. Reflexes fade → breathing fades → arrest; rescue with Calcium.",
    "ICP": "Itch on palms & soles with NO rash + high bile acids = ursodiol. A rash means it's NOT ICP (think PUPPP).",
    "uterine_inversion": "Can't find the fundus up top because it flipped down to the door. Push it back BEFORE the cervix slams shut.",
    "amniotic_fluid_embolism": "Sudden Hypoxia + Hypotension + Hemorrhage(DIC) with a FIRM uterus = AFE. PE is slower and pleuritic — don't grab the flashy one.",
    "wernicke": "Thiamine before the sugar — dextrose burns the last thiamine and you torch the brain.",
    "well_patient_observe": "When the stem screams DO SOMETHING and the finding is normal — sit on your hands. Like waiting out a trade that hasn't triggered: no setup, no action.",
    "ovarian_torsion_vs_corpus_luteum": "Torsion twists, it doesn't bleed you out. Big hemoperitoneum + shock = ruptured corpus luteum, not torsion.",
    "syphilis_chancre": "PainLESS, clean, solitary, hard rim = syphilis. If it HURTS, it's herpes or chancroid.",
    "pregnancy_dating": "First-tri ultrasound is the boss — when LMP argues with the early scan, the scan wins and you throw the LMP out.",
    "labor_arrest_oxytocin": "Weak contractions (MVU <200) = turn up the Pitocin before you call the OR. Power problem → more power.",
    "vasa_previa": "Membranes rupture → blood + fetal brady = FETAL vessels tore. Baby's bleeding, not mom — cut now.",
    "twin_chorionicity": "<b>λ</b>ambda has more lines (4 layers) = <b>Di</b>-Di. <b>T</b>-sign is <b>T</b>hin (2 layers) = Mo-Di.",
    "GBS_prophylaxis": "Bacteriuria, prior baby, or unknown+risk = just give the penicillin. Don't stop to culture what history already answered.",
    "chorioamnionitis": "Don't take a knife into a dirty field — deliver from BELOW. Cesarean only for the usual reasons.",
    "ectopic_overcall": "A NEGATIVE pregnancy test deletes ectopic from the list → pivot to torsion.",
    "sheehan": "Can't make milk after a big postpartum bleed = the pituitary infarcted. Trace the dry breast back to the hemorrhage.",
    "luteal_placental_shift": "Before ~10 weeks the corpus luteum pays the rent (progesterone); lose it early → you cover the rent.",
    "postpartum_mood": "Horrified by the thought (ego-DYStonic) + reality intact = depression, treatable. Believes it / hallucinating = psychosis, emergency.",
    "cervical_screening_ages": "Pap starts at 21, HPV co-test at 30 — the calendar decides, not her history.",
    # ---- b13 (2026-06-22) new clusters ----
    "prenatal_syphilis_screen": "Cast the cheap wide net first: RPR/VDRL (nontreponemal) screens, the treponemal test confirms the catch.",
    "oligohydramnios_term": "At term, low fluid + no meds taken = the bag is leaking (ROM).",
    "contraception_vte": "Clot in the history = no estrogen, ever. Wants no periods on top → the levonorgestrel coil.",
    "postpartum_endometritis": "Post-section fever + tender boggy uterus = the lining's infected. Clean incision → it's inside, not the skin.",
    "femoral_nerve_lithotomy": "Femoral = knee Extension + patellar reflex + Front of thigh. Too much hip flexion in stirrups crushes it under the ligament.",
    "parvovirus_hydrops": "Parvo eats the marrow → anemic baby → heart pumps double → it floods (hydrops). MCA PSV high = baby's anemic.",
    # ---- b14 (2026-06-24, UWorld) new clusters ----
    "rectovaginal_fistula": "Gas & stool out the wrong door = a tunnel rectum→vagina. (Urine → urinary fistula.)",
    "ohss": "Over-stimulated ovaries swell and weep fluid into the belly; vessels left dry → hemoconcentration.",
    "pemphigoid_gestationis": "Blisters that START at the belly button = pemphigoi<b>D</b> (deep tense bullae). PUPPP avoids the umbilicus and doesn't blister.",
    "functional_hypothalamic_amenorrhea": "Body senses a famine → shuts the reproductive lights off. Find the famine (eating disorder), not a tumor.",
    "ecc_conization": "Disease up the canal the colposcope can't fully see → cut it out (cone) for a specimen, don't burn it (ablate).",
    "influenza_vaccine_pregnancy": "Dead virus = safe anytime in pregnancy. Live nasal spray = never (like MMR/varicella).",
    "ca125_adnexal_mass": "Postmenopausal mass → CA-125 means more (no endometriosis/fibroids/PID to muddy it).",
    "abo_incompatibility": "Anti-A/B are already there from birth → first baby can be hit, but gently. Rh must be taught first, then hits hard.",
    "leiomyoma_submucosal_rpl": "Submucosal = IN the cavity → reach it from inside (hysteroscope). Cavity problem, cavity fix.",
    "cervical_stenosis_post_cone": "Cone scars the os two opposite ways: stenosis (too TIGHT, obstructed/painful) vs insufficiency (too LOOSE, painless dilation).",
    "cervical_screening_hiv": "Weak immune system can't clear HPV → screen more often. The standard calendar is for the immunocompetent.",
    "aub_under45_biopsy": "Failed the pills → sample the lining. Don't ablate or image what you haven't biopsied.",
}

TEXT_CARDS = [

    # ===================== GYN: repro endocrine / amenorrhea =====================
    C("Reproductive-age woman, amenorrhea. The stem dangles a fancier test — hypothyroid "
      "symptoms, athlete-triad picture, a prolactinoma headache.<br><br><b>First move?</b>",
      "Urine β-hCG. Always — before TSH, prolactin, FSH, DEXA, or any imaging.",
      "Pregnancy itself causes amenorrhea (± galactorrhea) and makes every downstream test uninterpretable.",
      "Don't be lured to the dressed-up test. hCG first is the single most repeated GYN rule — free points.",
      "pregnancy_first", extra=["source::NBME"]),

    C("Amenorrhea + bilateral milky discharge. Pregnancy excluded. Prolactin 45, TSH 15.<br><br>"
      "<b>Treatment?</b>",
      "Levothyroxine — treat the hypothyroidism; the prolactin normalizes on its own.",
      "Primary hypothyroidism → ↑TRH, which also stimulates lactotrophs → hyperprolactinemia.",
      "Don't reflex to MRI or a dopamine agonist (cabergoline/bromocriptine). Only chase a prolactinoma if prolactin stays up after TSH is fixed.",
      "galactorrhea_hyperprolactinemia", misses="b9 b11 b16"),

    C("Woman &lt;40 with amenorrhea + hot flashes + vaginal atrophy. Hormone panel shows high "
      "FSH and high LH.<br><br><b>What is the estradiol doing, and what's the diagnosis?</b>",
      "Estradiol is LOW. Diagnosis = primary ovarian insufficiency (hypergonadotropic hypogonadism).",
      "Ovary quits → no follicles → no negative feedback → pituitary screams (↑FSH/LH) while estrogen falls. Vaginal atrophy = it's ovarian-level.",
      "The part you keep flipping: estradiol is LOW, not high. And don't fall for Sheehan — POI's FSH is HIGH (hypergonadotropic) with NORMAL prolactin; Sheehan (post-PPH pituitary infarct) has LOW FSH + can't lactate (low prolactin). Causes of POI: chemo/alkylators, radiation, Turner.",
      "POI_POF", misses="b4 b5 b6 b15 n5", extra=["source::NBME"]),

    C("Primary infertility ~12 mo. REGULAR ovulatory menses with molimina, normal semen analysis, "
      "and an adolescent hospitalization for PID (fever, dyspareunia, discharge).<br><br><b>Next test?</b>",
      "Hysterosalpingogram — first-line for suspected tubal-factor infertility (prior PID → tubal scarring). No intraperitoneal contrast spill = obstruction.",
      "Regular ovulatory menses + molimina point AWAY from an endocrine/ovulatory cause toward an anatomic (tubal) one — and the PID history is the setup.",
      "Don't order the endocrine panel (FSH/TSH/testosterone) — that's the workup for IRREGULAR menses (POI/thyroid/PCOS), which bring oligomenorrhea + hot flashes/hirsutism. Laparoscopy needs prior surgery/dyspareunia; mid-cycle LH + progesterone challenge are for ovulatory dysfunction she doesn't have.",
      "infertility_tubal_hsg", extra=["source::NBME"]),

    # ===================== b15 (2026-06-28, UWorld) — new content gaps =====================
    C("Exclusively breastfeeding, ~8 wk postpartum: amenorrhea + nighttime hot flushes. "
      "Normal BP, lactating fine.<br><br><b>Mechanism — and why not Sheehan or PCOS?</b>",
      "Breastfeeding → ↑prolactin → inhibits GnRH → ↓LH/FSH → anovulation + lactational amenorrhea; low estrogen → vasomotor flushes.",
      "Intact lactation + normal BP rule OUT Sheehan (post-PPH panhypopituitarism → CAN'T lactate, everything low). Vasomotor sx need LOW estrogen.",
      "Don't pick PCOS — it has NORMAL estrogen, so no vasomotor symptoms. And Sheehan can't be lactating. This is physiologic prolactin-driven GnRH suppression.",
      "lactational_amenorrhea"),

    C("49-yo, perimenopausal, 3×4 cm INTRAMURAL fibroid, mild symptoms, thin endometrium. "
      "Asks what'll happen to it over time.<br><br><b>Natural history?</b>",
      "Spontaneous regression — fibroids are estrogen-responsive; estrogen falls near menopause → the fibroid shrinks and symptoms improve.",
      "Intramural (not pedunculated) → no torsion risk; abundant myometrial blood supply → no spontaneous necrosis. Perimenopausal → regression expected.",
      "Don't reflex to rapid growth / sarcoma — that concern is a POSTmenopausal fibroid that's ENLARGING (sarcoma arises de novo). A perimenopausal fibroid should regress.",
      "leiomyoma_menopause_regression"),

    C("Days after a labor epidural: fever 38.2 + progressive focal back pain → quadriceps "
      "weakness, ↓knee reflex, sensory loss.<br><br><b>Dx and next step?</b>",
      "Spinal epidural abscess → URGENT MRI of the spine (then surgical decompression + antibiotics).",
      "FEVER + a PROGRESSIVE neuro deficit after neuraxial anesthesia = abscess (direct inoculation). Benign labor-related nerve injury has NO fever and doesn't progress.",
      "Don't write it off as labor-associated peripheral nerve injury (no fever) or radiculopathy, and don't reassure — progression goes to paralysis. Image now.",
      "spinal_epidural_abscess"),

    C("On tamoxifen ≥5 yr for ER+ breast cancer.<br><br><b>Most common adverse effect — and "
      "the SERM organ effects you can't miss?</b>",
      "Hot flashes = most common. Tamoxifen is an estrogen AGONIST in the uterus → ↑endometrial cancer, uterine sarcoma, and VTE.",
      "Mixed agonist/antagonist: antagonist in BREAST (the therapeutic point), agonist in UTERUS + bone. So uterine/VTE risks go UP.",
      "Not ovarian cancer (may be DECREASED). Not endometrial atrophy — it's the opposite (proliferation). Doesn't drive CAD (lowers lipids).",
      "tamoxifen_adverse_effects"),

    C("Postpartum fecal/flatal incontinence after a THIRD-degree perineal laceration. "
      "Exam: weak, asymmetric anal sphincter tone.<br><br><b>Next test?</b>",
      "Endoanal ultrasonography — locates and sizes the external anal sphincter (EAS) defect to guide repair.",
      "Weak/asymmetric sphincter tone (or a palpable defect) = STRUCTURAL EAS injury → image it. A normal exam would just get reassurance (resolves).",
      "Don't reach for fiber/stool softeners — that's incontinence from constipation/impaction (she has 1–2 BMs/day; softeners would worsen it). CT/barium are inferior to endoanal US for the sphincter.",
      "obstetric_anal_sphincter_injury"),

    C("Trouble conceiving, now convinced she's pregnant: amenorrhea, morning sickness, "
      "abdominal distension. TWO negative urine hCG; US shows an empty uterus / thin stripe. "
      "The belief is fixed but NOT delusional.<br><br><b>Dx?</b>",
      "Pseudocyesis — a persistent, nondelusional belief of pregnancy in a non-pregnant patient. Needs psychiatric evaluation.",
      "Pregnancy SYMPTOMS but objective tests EXCLUDE pregnancy (neg hCG ×2 + empty uterus). Nondelusional = she can accept the evidence (vs a true delusion of pregnancy).",
      "Not missed abortion — that has a POSITIVE test + a nonviable intrauterine gestation, and symptoms usually stop. Ectopic/mole both have positive hCG.",
      "pseudocyesis"),

    C("Shoulder dystocia is an emergency that's mostly UNPREDICTABLE (&gt;50% of cases have no "
      "risk factors).<br><br><b>What best reduces neonatal complications (eg brachial plexus injury)?</b>",
      "Scheduled, recurring simulation-based team training (whole clinical team) — sharpens team performance + the technical maneuvers.",
      "Because it can't be predicted, you can't screen it away — you prepare by DRILLING the response with the team.",
      "Not risk-factor checklists (most cases have none), not retrospective root-cause analysis (it's not a preventable error), not debriefings alone (they help communication, not the maneuvers).",
      "shoulder_dystocia_simulation"),

    C("Incapacitated patient, NO advance directive. Husband is the default surrogate; her parents "
      "are involved.<br><br><b>What standard governs the decision, and what matters most?</b>",
      "Substituted judgment — base the decision on what the PATIENT would have chosen, not the surrogate's own preference.",
      "No advance directive → substituted judgment (reconstruct HER wishes). The surrogate's job is to estimate her choice, not impose his own.",
      "Don't default to the husband's preference or the parents' values. Clinical findings/prognosis inform the choice, but the governing question is what SHE would have wanted.",
      "substituted_judgment"),

    # ===================== b16 (2026-06-29, Ora) — new content gaps =====================
    C("9-wk dates but the fundus is at the UMBILICUS: hyperemesis, thyrotoxicosis, HTN, "
      "bilateral adnexal (theca lutein) cysts, very high hCG.<br><br><b>Dx + the US finding?</b>",
      "Complete hydatidiform mole — US shows a 'snowstorm' / cystic intrauterine mass with no fetus.",
      "Uterus >> dates + thyrotoxicosis (hCG cross-reacts at the TSH receptor) + theca lutein cysts + sky-high hCG = molar. The mass is cystic tissue, not a fetus.",
      "Not ectopic (that's pain + bleeding + HYPOtension + empty uterus, not HTN/thyrotoxicosis with a bulky uterus). Not a missed AB (hCG falling, symptoms regress) or twins (wouldn't give frank thyrotoxicosis / large theca lutein cysts).",
      "complete_mole"),

    C("Na 115 with a SEIZURE (eg paraneoplastic SIADH from ovarian cancer), urine osm 600."
      "<br><br><b>Immediate treatment?</b>",
      "3% hypertonic saline — reverse the cerebral edema now.",
      "Symptomatic (seizure/coma) hyponatremia is a neuro emergency → osmotic correction with 3% saline, regardless of the cause.",
      "Not conivaptan (aquaresis, onset too slow for an acute seizure). Not fluid restriction (days — fine only for mild/asymptomatic SIADH). Not 0.9% saline (in SIADH urine osm > NS osm → worsens the Na). Antiepileptics won't fix a metabolic seizure.",
      "symptomatic_hyponatremia_3pct"),

    C("Primary amenorrhea, Tanner 5, 46,XX, NORMAL ovaries, normal pubic/axillary hair, "
      "female-range testosterone — but uterus/cervix not visualized.<br><br><b>Dx?</b>",
      "Müllerian agenesis (MRKH) — absent uterus + upper vagina, with normal ovaries and normal secondary sex characteristics.",
      "46,XX + normal ovaries → normal estrogen (breasts) and normal hair; the müllerian structures just didn't form. Ovaries are spared because they aren't müllerian-derived.",
      "Not AIS (46,XY, male-range testosterone, SCANT sexual hair). Not hypothalamic amenorrhea or POI (uterus is PRESENT in both). Not Swyer (46,XY streak gonads → uterus present, no puberty).",
      "mullerian_agenesis_mrkh"),

    C("AROM → immediate blood-tinged fluid; mother stable + pain-free. FHR: smooth undulating "
      "sine wave, 3–5 cycles/min, absent variability.<br><br><b>What does that tracing mean?</b>",
      "Sinusoidal pattern = severe FETAL ANEMIA (here ruptured vasa previa → fetal blood loss). Category III → deliver now.",
      "A true sinusoidal tracing (smooth regular sine wave, absent variability) is highly specific for severe fetal anemia. Painless blood-tinged fluid at ROM = torn fetal vessels (vasa previa).",
      "Not cord compression — that's VARIABLE decels (abrupt drop &lt;30s, abrupt return), not a smooth undulation. Not fetal sleep (flat baseline, not sine waves) or head compression (early decels).",
      "sinusoidal_fhr_anemia", extra=["source::NBME"]),

    C("Pregnant, pyelonephritis, still febrile at 96h despite a culture-sensitive cephalosporin."
      "<br><br><b>Next step?</b>",
      "Renal ultrasound — image for a complication (abscess, stone, obstruction). US is the preferred first imaging in pregnancy.",
      "Persistent fever &gt;48–72h on appropriate antibiotics means look for a structural complication; in pregnancy you start with US to avoid fetal radiation.",
      "Not CT (ionizing radiation — only if US nondiagnostic). Not switching/adding antibiotics (culture is sensitive → the problem is structural, not the drug). Not inducing labor (treat the infection; delivery at 24wk = high neonatal morbidity).",
      "pyelonephritis_persistent_imaging"),

    C("37wk, HTN 174/112, platelets 48k, AST 210, LDH 1200, RUQ pain, schistocytes on smear."
      "<br><br><b>Mechanism of the hemolysis?</b>",
      "Microangiopathic hemolytic anemia (MAHA) — RBCs mechanically fragmented (schistocytes) crossing fibrin-rich, vasospastic microvasculature. Coombs-NEGATIVE.",
      "HELLP hemolysis is mechanical/shear, not immune — Coombs-negative, schistocytes, ↑LDH. The HTN + thrombocytopenia + liver injury cluster rides along.",
      "Not antibody-mediated (AIHA is Coombs-POSITIVE, no HTN/liver injury). Not G6PD oxidative (Heinz bodies), not splenic sequestration, not marrow suppression (that's ↓production with low retic — HELLP is ↑destruction).",
      "hellp_hemolysis_maha"),

    C("SLE mother. Fetus: atrial rate 140, ventricular rate 55 (AV dissociation), no structural "
      "defect.<br><br><b>Mechanism?</b>",
      "Maternal anti-Ro/SSA + anti-La/SSB IgG cross the placenta → irreversible fibrosis of the fetal AV node → congenital complete heart block.",
      "Atrial rate normal (140) but ventricular slow (55) = block AT the AV node, SA intact. It's direct antibody binding to the fetal conduction system.",
      "Not immune-complex vasculitis (Type III — that's maternal organ damage like lupus nephritis). Not coronary thrombosis (APS). Not SA-node suppression (that would give a matched 1:1 sinus brady).",
      "neonatal_lupus_heart_block"),

    C("Chronic urinary frequency + SUPRApubic pain that worsens as the bladder fills and is "
      "RELIEVED by voiding. Cultures repeatedly negative, normal pelvic exam.<br><br><b>Dx?</b>",
      "Interstitial cystitis (bladder pain syndrome) — pain with filling, relief with voiding, negative infection workup.",
      "Pain is suprapubic, fill-worsened / void-relieved, with a NORMAL exam and negative cultures — that pattern is IC.",
      "Not urethral diverticulum (tender ANTERIOR vaginal-wall mass that expresses discharge — her exam is normal). Not recurrent cystitis (needs positive cultures). Not OAB (urgency without pain) or prolapse (bulge worse with standing).",
      "interstitial_cystitis"),

    C("Complex MULTILOCULATED thick-walled adnexal mass + fever 38.4, WBC 16,500, ESR 85, and a "
      "prior PID hospitalization.<br><br><b>Dx?</b>",
      "Tubo-ovarian abscess (TOA) — a complex inflammatory adnexal mass, classically after PID.",
      "A complex multiloculated mass PLUS a systemic inflammatory profile (fever, leukocytosis, ↑ESR) + prior PID = TOA. The infection signature is the tell.",
      "Not a pedunculated leiomyoma (solid, shadowing, no fever unless acute degeneration). Not endometrioma (homogeneous ground-glass, no fever) or ovarian carcinoma (mass + weight loss, not high fever/leukocytosis). A sigmoid diverticular abscess sits by bowel, not discrete adnexa.",
      "tubo_ovarian_abscess"),

    C("Neonate: macrocephaly/hydrocephalus, chorioretinitis (yellow-white retinal scars), "
      "hepatosplenomegaly.<br><br><b>Head-CT calcification pattern + Dx?</b>",
      "Congenital toxoplasmosis — DIFFUSE parenchymal (cortical/basal ganglia) intracranial calcifications.",
      "Toxo triad = chorioretinitis + hydrocephalus/macrocephaly + DIFFUSE parenchymal calcifications.",
      "Not CMV (PERIVENTRICULAR calcifications + MICROcephaly + hearing loss). Not Dandy-Walker (vermis hypoplasia, no chorioretinitis/HSM), not neonatal HSV (temporal necrosis), not tuberous sclerosis (subependymal nodules).",
      "congenital_toxoplasmosis"),

    C("Non-immune hydrops fetalis. BOTH parents microcytic (MCV 70–72) with NORMAL ferritin; "
      "maternal antibody screen negative.<br><br><b>Dx + why?</b>",
      "Alpha-thalassemia major (4-gene deletion) → Hb Barts (γ4) → extreme O2 affinity → fetal hypoxia → hydrops.",
      "Microcytosis with NORMAL iron in both parents = a hemoglobinopathy-carrier couple. Fetal Hb (α2γ2) needs alpha chains — absent → Hb Barts → in-utero hydrops.",
      "Not beta-thal major (beta defects are SILENT in utero — fetal Hb uses gamma, not beta — so no hydrops). Not Rh (antibody screen negative). Not spherocytosis (↑MCHC, not micro) or syphilis (no serology/risk factors).",
      "alpha_thalassemia_hydrops", extra=["source::NBME"]),

    C("Postmenopausal bleeding + enlarging uterus, prior pelvic radiation 20 yr ago. Biopsy: "
      "BOTH malignant glandular AND malignant spindle cells.<br><br><b>Dx?</b>",
      "Uterine carcinosarcoma (MMMT) — a biphasic malignant tumor (epithelial + mesenchymal), strongly linked to prior pelvic radiation.",
      "The biphasic histology (malignant glandular AND spindle) is the tell — that combination defines carcinosarcoma. Prior radiation is the classic risk.",
      "Not leiomyosarcoma (PURE malignant spindle, no glandular). Not adenocarcinoma (pure epithelial). Not leiomyoma (benign, regresses postmenopause — a growing postmeno mass with high-grade cells rules it out).",
      "uterine_carcinosarcoma"),

    # ===================== n1 (2026-06-29, NBME) — card every concept, source::NBME =====================
    C("Pregnant, fever 38.9, flank pain, pyuria (100 WBC/hpf) with only occasional RBC."
      "<br><br><b>Most appropriate next step in DIAGNOSIS?</b>",
      "Urine culture — pyuria with few RBCs points to infection (pyelonephritis); confirm the organism, don't image.",
      "Pyuria (&gt;10 WBC/hpf) + LOW RBC = infection, not a stone. Culture confirms + guides antibiotics.",
      "Not CT/IVP (image only if dx uncertain — avoid fetal radiation when pyuria already says infection). Not barium enema (lower GI) or laparoscopy (surgical abdomen).",
      "pyelo_pregnancy_urine_culture", extra=["source::NBME"]),

    C("On cyclophosphamide: urgency, frequency, GROSS hematuria, STERILE urine, no discharge."
      "<br><br><b>Dx?</b>",
      "Hemorrhagic cystitis — a noninfectious cystitis from cyclophosphamide (the acrolein metabolite injures the bladder).",
      "Cyclophosphamide + gross hematuria + STERILE urine = hemorrhagic cystitis (prevent with mesna + hydration).",
      "Not infection (urine is sterile). Not bladder calculi (cyclophosphamide isn't a stone risk — it's a hemorrhagic-cystitis risk). Not lithium tox (GI/neuro, not bladder bleeding) or DI (dilute polyuria, no blood).",
      "cyclophosphamide_hemorrhagic_cystitis", extra=["source::NBME", "nbme-only"]),

    C("Progressive urine loss with a SUDDEN urge she can't suppress, variable volume, no "
      "cough/Valsalva trigger.<br><br><b>Mechanism?</b>",
      "Detrusor overactivity — urge incontinence (overactive bladder).",
      "A SUDDEN urge with no exertional trigger = an involuntary detrusor contraction.",
      "Not urethral hypermobility or intrinsic sphincter deficiency (those are STRESS incontinence — leak with ↑intra-abdominal pressure / cough). A diuretic raises volume but doesn't cause the detrusor spasm.",
      "urge_incontinence_detrusor", extra=["source::NBME", "nbme-only"]),

    C("4 days post-TAH/BSO for extensive endometriosis (dense adhesions): severe flank pain, "
      "fever, CVA tenderness, US shows hydronephrosis + hydroureter.<br><br><b>Most likely cause?</b>",
      "Iatrogenic ureteral injury (ligation/kinking) — obstruction in a scarred surgical field.",
      "Postop TIMING + obstructive imaging (hydronephrosis/hydroureter) after adhesion-heavy pelvic surgery = ureteral injury. The fever/pyuria is downstream of the obstruction, not primary pyelo.",
      "Don't stop at pyelonephritis (it fits the fever/CVA, but the NEW obstruction right after surgery is the underlying cause). Not a stone (no colic/gross hematuria), not endometriosis obstruction (indolent, preop), not ureterovaginal fistula (delayed watery vaginal discharge).",
      "ureteral_injury_hysterectomy", extra=["source::NBME", "nbme-only"]),

    C("Long-standing PREgestational (type 1) DM with retinopathy + poor control, first trimester."
      "<br><br><b>Fetus is at greatest risk for what?</b>",
      "Congenital CARDIAC malformations (eg TGA, VSD) — the classic teratogenic outcome of pregestational hyperglycemia.",
      "PREgestational DM = high glucose during ORGANOGENESIS → structural anomalies, cardiac most characteristic (also caudal regression, NTDs).",
      "Not cystic hygroma (Turner/Noonan), diaphragmatic hernia, Potter (ACE-I/ARB/oligo), or trisomy 18 (maternal age) — none are driven by maternal DM. Contrast GESTATIONAL DM → macrosomia/neonatal hypoglycemia, not organogenesis defects.",
      "pregestational_dm_cardiac", extra=["source::NBME"]),

    C("Prior child has CF, so the mother is an OBLIGATE carrier. She wants this pregnancy's risk."
      "<br><br><b>Most appropriate screening test?</b>",
      "Test the PARTNER's CF carrier status (paternal DNA / molecular testing).",
      "Autosomal recessive: the child needs 2 mutant alleles. The mother's carrier status is already known → the unknown that sets the risk is the FATHER.",
      "Not maternal DNA (she's already a known carrier — adds nothing). Not karyotype (CF isn't chromosomal). Not serum screen (aneuploidy/NTD). Amnio/CVS are later/invasive — carrier testing comes first.",
      "cf_carrier_screen_partner", extra=["source::NBME", "nbme-only"]),

    C("Rh-NEGATIVE pregnancy.<br><br><b>(a) what prevents alloimmunization, and WHEN? "
      "(b) what screen is due at 28 weeks?</b>",
      "(a) Anti-D (RhoGAM) at the FIRST sensitizing pregnancy — and at 28wk + postpartum if the baby is Rh+. (b) A repeat antibody screen at 28 weeks.",
      "Prevention is about TIMING: the sensitizing event was the prior pregnancy, so RhoGAM had to be given THEN. At 28wk an Rh-neg patient gets a repeat antibody screen (then RhoGAM if still negative).",
      "RhoGAM in the CURRENT pregnancy can't undo sensitization that already happened; plasmapheresis treats established disease, doesn't prevent it. At 28wk it's not NST/quad/GBS (wrong indications/timing).",
      "rh_prevention_screening", extra=["source::NBME"]),

    C("Healthy preconception patient, very athletic (runs 60 mi/wk), normal BMI and exam."
      "<br><br><b>Her pregnancy is at increased risk for…?</b>",
      "Nothing — moderate exercise confers NO increased risk in a healthy singleton pregnancy (the no-increased-risk option is the answer).",
      "The NBME trap is EXPECTING a complication. Moderate activity is safe/encouraged; the only caution is fall/high-impact/contact sports.",
      "Not chorioamnionitis, oligohydramnios, previa, or postdates — none are caused by exercise (it actually lowers obesity-related risk). This is a 'reassurance' stem — same instinct as the over-intervention reflex.",
      "exercise_pregnancy_no_risk", extra=["source::NBME"]),

    C("Postmenopausal woman: recurrent 'UTIs' with NEGATIVE cultures, dyspareunia, postcoital "
      "spotting. Exam: pale thin walls, lost rugae. Thin endometrial stripe.<br><br><b>Treatment?</b>",
      "Topical vaginal estrogen (genitourinary syndrome of menopause).",
      "Low estrogen → thin friable epithelium → phantom 'UTIs' (neg cultures) + atrophy. Thin stripe reassures it's not cancer.",
      "Don't treat the phantom UTI with antibiotics or urgency with oxybutynin. But in postmenopausal BLEEDING, rule out cancer (biopsy) before calling it atrophy.",
      "atrophic_vaginitis_GSM", extra=["source::NBME"]),

    C("46,XX infant with ambiguous (virilized) genitalia + maternal virilization during the "
      "pregnancy. 17-OHP is NORMAL, electrolytes normal.<br><br><b>Enzyme defect?</b>",
      "Aromatase (placental CYP19) deficiency.",
      "Normal 17-OHP + normal lytes rules out 21-hydroxylase CAH (which has high 17-OHP ± salt-wasting). Later: tall stature + low bone density (no estrogen).",
      "You reflex to CAH 3×. The NORMAL 17-OHP is the discriminator — aromatase, not 21-OH.",
      "aromatase_deficiency"),

    C("Any vaginal bleeding &gt;12 months after the LMP. She's on HRT, stripe looks thickened.<br><br>"
      "<b>Next step?</b>",
      "Endometrial biopsy — tissue first.",
      "Postmenopausal bleeding = endometrial cancer until excluded. On HRT the TVUS stripe is unreliable, so don't lean on it.",
      "Don't 'treat presumed atrophy' with estrogen before sampling. Sample first, treat second.",
      "postmenopausal_bleeding"),

    C("Complete mole, suction-evacuated. She wants to conceive again.<br><br>"
      "<b>Why contraception during β-hCG surveillance?</b>",
      "A new pregnancy's hCG is indistinguishable from recurrent GTN — it would mask disease.",
      "Trend hCG to zero; contraception is TEMPORARY (conceive after remission), not permanent.",
      "Don't jump to choriocarcinoma on a plain complete-mole stem, and don't call the contraception permanent. (3rd time missing the why.)",
      "GTD_surveillance"),

    C("Lean teen, anovulation, hirsutism/acne. PCOS.<br><br>"
      "<b>Which ovarian cell makes the excess androgen, and which one aromatizes?</b>",
      "Theca interna MAKES androgens; granulosa AROMATIZES them to estrogen.",
      "Rapid GnRH pulses → LH&gt;FSH → theca androgens; relative FSH deficiency → granulosa can't aromatize → follicular arrest.",
      "Don't swap them — theca = androgen factory, granulosa = aromatase.",
      "PCOS_pathophys"),

    C("Amenorrhea workup (pregnancy excluded). Progestin challenge → NO withdrawal bleed.<br><br>"
      "<b>Next test, and how do you read it?</b>",
      "Sequential estrogen-progestin challenge. Bleed = patent outflow → it was hypoestrogenism; no bleed = outflow obstruction (Asherman).",
      "No bleed on progestin alone = either no estrogen priming OR an outflow problem; the E+P challenge separates them.",
      "Don't stop at the negative progestin challenge — it doesn't distinguish the two causes.",
      "progestin_challenge", extra=["source::NBME"]),

    C("Heavy menstrual bleeding, wants children in a few years (planned oocyte cryo).<br><br>"
      "<b>What's contraindicated, and what do you offer?</b>",
      "Endometrial ablation is contraindicated — offer the LNG-IUD instead.",
      "Ablation destroys the endometrium → any future pregnancy is high-risk (accreta, ectopic, IUGR, loss).",
      "The fertility wish is the tell. LNG-IUD also dodges estrogen contraindications (vWD, migraine w/ aura).",
      "endometrial_ablation"),

    C("Dysmenorrhea + dyspareunia + chronic pelvic pain, fixed retroverted uterus. Empiric "
      "NSAIDs and OCPs failed.<br><br><b>Definitive diagnostic step?</b>",
      "Diagnostic laparoscopy (with biopsy) — the gold standard.",
      "US/MRI MISS superficial peritoneal implants, so imaging only rules in, never out.",
      "Even a 'ground-glass' endometrioma on imaging still gets laparoscopy to confirm.",
      "endometriosis"),

    C("Heavy menses + an enlarged, irregular uterus. A submucosal fibroid distorts the cavity; "
      "she wants an IUD.<br><br><b>What's the relevant risk?</b>",
      "High IUD EXPULSION rate (cavity distortion) — a relative contraindication.",
      "Fibroids are estrogen-driven smooth-muscle tumors; the lumpy/irregular contour is the tell vs adenomyosis (smooth/boggy).",
      "Fibroids essentially NEVER malignantly transform — 'leiomyosarcoma' is a false-premise trap. (Missed the expulsion angle 3×.)",
      "leiomyoma_iud"),

    C("Sexually active 19-year-old, monogamous, uses condoms, declines a pelvic exam.<br><br>"
      "<b>What screening does she still need?</b>",
      "Annual gonorrhea/chlamydia NAAT — urine/self-swab (no speculum needed).",
      "GC/CT screening is AGE-based (all sexually active women ≤24, USPSTF grade B), not risk-based.",
      "'Monogamous + condoms' does NOT exempt her. Don't default to RPR/HIV or HPV co-test (HPV co-test starts at 30; Pap at 21).",
      "age_sti_screening"),

    C("HSIL on cervical cytology — patient is 23 (or pregnant).<br><br><b>Next step?</b>",
      "Colposcopy — at any age, including 21–24 and in pregnancy (no LEEP/ECC if pregnant).",
      "Reflex HPV testing and repeat cytology are for LOW-grade results (ASC-US/LSIL), not HSIL.",
      "Don't downgrade the workup. HSIL needs direct visualization now. (Missed 2×.)",
      "HSIL_colposcopy", extra=["source::NBME"]),

    C("7-year-old: breast/areolar development + vaginal estrogen signs + a UNILATERAL adnexal mass. "
      "Advanced bone age.<br><br><b>Tumor?</b>",
      "Granulosa cell tumor (estrogen-secreting) → peripheral (GnRH-independent) precocious puberty.",
      "Unilateral mass driving estrogen = granulosa. Central (GnRH-dependent) PP gives symmetric/bilateral ovarian enlargement.",
      "Don't anchor on 'foreign body' for the bleeding, and don't pick dysgerminoma (hormonally silent). Sertoli-Leydig = virilization, the opposite.",
      "granulosa_cell_tumor"),

    C("Phenotypic female, Tanner-5 breasts, SCANT pubic/axillary hair, blind vaginal pouch, NO uterus. "
      "Sometimes inguinal gonads.<br><br><b>Karyotype?</b>",
      "46,XY — complete androgen insensitivity (broken androgen receptor).",
      "Testes make testosterone + AMH → Müllerian regression (no uterus) but female externals; can't respond to androgen → scant hair.",
      "Hair amount is the discriminator: scant + no uterus = CAIS (46,XY); normal hair + ovaries = MRKH (46,XX). Don't slip to Klinefelter 47,XXY.",
      "androgen_insensitivity", misses="n5", extra=["source::NBME"]),

    C("Prepubertal girl: persistent foul, sometimes bloody vaginal discharge, no response to antifungals. "
      "Friable material seen.<br><br><b>Management?</b>",
      "Retained foreign body (toilet paper #1) → remove with warm saline irrigation.",
      "Friable/soft material = irrigate; forceps are for solid objects.",
      "Don't chase candida — no estrogen, no yeast risk in a prepubertal child.",
      "vaginal_foreign_body"),

    C("Woman with bone metastases that are MIXED lytic + blastic ('mottled').<br><br>"
      "<b>Most likely primary?</b>",
      "Breast (mammary ductal).",
      "Mixed lytic+blastic = breast; purely lytic = lung/renal/thyroid/myeloma; purely blastic = prostate.",
      "Don't pick follicular thyroid — that would be purely lytic.",
      "mixed_mets"),

    # ===================== OB: bleeding / peripartum =====================
    C("Painless bright-red 3rd-trimester bleeding. Prior cesarean.<br><br>"
      "<b>The cardinal rule, and the strongest specific risk factor?</b>",
      "NO digital cervical exam until ultrasound rules out previa. Strongest RF = prior cesarean.",
      "Placenta over the internal os → painless bleed (vs abruption = painful + tender). A digital exam can trigger catastrophic hemorrhage.",
      "Contrast vasa previa: bleeding WITH membrane rupture + fetal bradycardia.",
      "placenta_previa"),

    C("PPROM confirmed (nitrazine+, pooling, ferning, low AFI). What's the big modifiable risk factor "
      "the shelf wants?<br><br><b>And name two complications.</b>",
      "Untreated genitourinary infection (asymptomatic bacteriuria, BV). Complications: abruption, cord prolapse, chorioamnionitis, oligo → cord compression/pulmonary hypoplasia.",
      "Ascending infection → membranes give way. That's why asymptomatic bacteriuria is screened and treated in pregnancy.",
      "Don't treat ASB as harmless — it's the link to PPROM and abruption.",
      "PPROM"),

    C("Rh-negative mom with an antepartum bleed. Rosette screen is positive.<br><br>"
      "<b>What does the Kleihauer-Betke test measure, and what does it NOT?</b>",
      "KB quantifies fetal RBC volume in maternal blood (to calculate RhoGAM vials). It does NOT measure the maternal antibody titer.",
      "Any bleed in an Rh-neg mom → RhoGAM within 72h. Rosette screens qualitatively; KB quantifies.",
      "The antibody titer is the indirect Coombs — don't confuse it with KB. (KB ÷30 mL + 1 safety = vials.)",
      "Rh_kleihauer"),

    C("Woman on MgSO4 for preeclampsia, now with renal insufficiency. Areflexia, RR 9.<br><br>"
      "<b>What's happening, the antidote, and why is she the setup?</b>",
      "Magnesium toxicity → IV calcium gluconate.",
      "Mg is cleared entirely by the kidney → renal insufficiency is THE risk. Toxicity marches: lose DTRs → respiratory depression → cardiac arrest.",
      "Persistent high Mg after delivery = kidneys aren't clearing it (ATN), not ongoing dosing.",
      "magnesium_kidney"),

    C("Tocolysis &lt;32 weeks; maternal hypotension/tachycardia rules out nifedipine/terbutaline/Mg. "
      "Indomethacin is chosen.<br><br><b>Fetal effect, and mechanism?</b>",
      "Oligohydramnios — via ↓fetal urine production.",
      "COX inhibitor → ↓fetal prostaglandins → fetal renal vasoconstriction → ↓urine. Capped at &lt;32 wks (also constricts the ductus near term).",
      "Mechanism is ↓fetal urine, NOT ↑swallowing.",
      "indomethacin_tocolysis"),

    C("3rd-trimester pruritus of palms and soles, NO primary rash (only excoriations), ↑bile acids, "
      "normal glucose and coags.<br><br><b>Diagnosis, treatment, and the main mimic to exclude?</b>",
      "Intrahepatic cholestasis of pregnancy → ursodeoxycholic acid. Exclude viral hepatitis.",
      "Dx of exclusion: normal glucose/coags separates it from AFLP. Danger = stillbirth, so it drives delivery timing.",
      "Don't pattern-match the itch and stop. If there's an actual rash within striae (sparing umbilicus) = PUPPP → topical steroids, not ursodiol.",
      "ICP"),

    C("Pregnant woman with GBS bacteriuria this pregnancy (or a prior infant with invasive GBS).<br><br>"
      "<b>What do you do at delivery — and do you culture first?</b>",
      "Give intrapartum penicillin automatically — no culture needed.",
      "Three automatic triggers: GBS bacteriuria this pregnancy, prior infant w/ invasive GBS, or unknown status + a risk factor (preterm, ROM ≥18h, fever).",
      "The trap is ordering a culture when the history already mandates antibiotics. Pen-allergic: low-risk → cefazolin; high-risk → vancomycin.",
      "GBS_prophylaxis"),

    C("After delivery: smooth mass at the introitus, brisk hemorrhage, vagal bradycardia. You CANNOT "
      "palpate the fundus abdominally.<br><br><b>Diagnosis and immediate management?</b>",
      "Uterine inversion → immediate manual replacement before the cervix clamps down.",
      "Non-palpable fundus is the discriminator (vs a prolapsed fibroid where the fundus IS palpable).",
      "Do NOT remove the placenta or give uterotonics first, and don't jump to hysterectomy.",
      "uterine_inversion"),

    C("Sudden hypoxia + hypotension + coagulopathy (DIC) just after ROM/delivery. Uterus is FIRM.<br><br>"
      "<b>Diagnosis, and how to separate it from PE?</b>",
      "Amniotic fluid embolism (anaphylactoid) — supportive care, dx of exclusion.",
      "Firm uterus rules out atony as the bleeding source. AFE = sudden collapse + early DIC.",
      "Don't over-call AFE on the flashier stem — PE is more gradual, pleuritic, no early DIC. (You flip PE↔AFE.)",
      "amniotic_fluid_embolism"),

    C("Post-IVF, empty uterine cavity, an eccentric sac with a thin (&lt;5 mm) myometrial mantle, "
      "+ free fluid, unstable.<br><br><b>Diagnosis and management?</b>",
      "Cornual (interstitial) ectopic → surgical removal (cornual resection / laparotomy).",
      "Sits in myometrium → ruptures LATE and bleeds catastrophically. 'Looks almost intrauterine.'",
      "Methotrexate is contraindicated with size + cardiac activity + free fluid + instability. Not a C-section.",
      "cornual_ectopic"),

    C("Pregnant woman: fever, CVA tenderness, N/V, no rebound. She's warm, flushed, hypotensive "
      "despite fluids.<br><br><b>Diagnosis, type of shock, and worst complication?</b>",
      "Pyelonephritis → septic (distributive) shock. Worst complication = ARDS.",
      "Dilated, stasis-prone collecting system (esp right) makes pyelo common; warm/flushed/hypotensive-despite-fluids = distributive (vs cold/clamped hypovolemic).",
      "ARDS = bilateral infiltrates with a NORMAL EF (noncardiogenic). Persistent fever despite 48–72h abx → renal US for stone/abscess, don't reflex to delivery.",
      "pyelonephritis_pregnancy"),

    C("Nullipara, second stage &gt;3h, ADEQUATE contractions, head at +2, OA, fully dilated, membranes "
      "ruptured.<br><br><b>Best next step?</b>",
      "Operative vaginal delivery (vacuum or forceps).",
      "Prerequisites met + adequate contractions (not an oxytocin problem) → OVD beats cesarean (lower morbidity); favored to spare maternal pushing/cardiac strain.",
      "Don't augment (contractions already adequate) and don't reflex to C-section.",
      "second_stage_arrest_OVD"),

    C("Hyperemesis gravidarum (or bariatric history) + confusion, ophthalmoplegia, ataxia.<br><br>"
      "<b>The do-or-die rule?</b>",
      "Give IV THIAMINE before (or with) glucose.",
      "Thiamine depletion → Wernicke. Dextrose first burns the last thiamine and precipitates/worsens it → irreversible Korsakoff.",
      "Any vomiting-pregnant-patient + neuro signs = thiamine first. Never load glucose alone.",
      "wernicke"),

    C("Post-dates pregnancy in a woman with BMI 39.<br><br>"
      "<b>What's driving the postterm course?</b>",
      "Maternal adiposity → impaired cervical ripening + myometrial contractility → failure to initiate labor.",
      "Obesity INCREASES postterm and indicated preterm, but DECREASES spontaneous preterm birth.",
      "Don't pick precipitous or spontaneous-preterm — high BMI on a postdates stem points to adiposity.",
      "obesity_postterm"),

    C("PAINLESS 2nd-trimester cervical dilation with bulging membranes, no contractions, prior LEEP. "
      "Two prior 2nd-trimester losses.<br><br><b>Diagnosis and management?</b>",
      "Cervical insufficiency → history-indicated cerclage at 12–14 weeks.",
      "'Silent/painless dilation' separates it from preterm labor (painful contractions). Classic after cervical trauma (LEEP, cone, D&E).",
      "Cerclage needs ≥2 prior losses; with fewer (e.g., one prior conization), do 2nd-tri TVUS cervical-length surveillance first.",
      "cervical_insufficiency", extra=["source::NBME"]),

    C("Postpartum day 1: firm uterus at/below the umbilicus, lochia rubra, a postural gush of pooled "
      "blood, vitals stable.<br><br><b>Management?</b>",
      "Reassurance — this is normal involution.",
      "Firm + at/below umbilicus + stable = normal. Atony is the contrast: BOGGY uterus, often above the umbilicus, ongoing bleeding.",
      "The test is trusting 'firm + stable = normal' under a stem built to make you act.",
      "normal_involution_vs_atony"),

    C("Migraine prophylaxis in a woman who is pregnant or trying to conceive (bonus: she also has HTN).<br><br>"
      "<b>Drug of choice?</b>",
      "A beta-blocker (propranolol/metoprolol) — covers HTN too.",
      "Topiramate and valproate are teratogenic and out.",
      "Don't ignore the pregnancy/TTC qualifier and pick topiramate. And migraine WITH AURA = estrogen contraindicated → progestin-only contraception.",
      "migraine_repro"),

    C("Blood pressure 150/95 documented at 14 weeks.<br><br>"
      "<b>Gestational or chronic hypertension — and why?</b>",
      "Chronic hypertension (pre-existing).",
      "BP normally DROPS in early pregnancy (nadir 2nd tri); HTN before 20 weeks = chronic, not gestational/preeclampsia (those are &gt;20 wks).",
      "Don't call an early high BP 'physiologic.' Chronic HTN raises superimposed preeclampsia risk and often drives indicated preterm delivery.",
      "chronic_htn_pregnancy"),

    C("Reproductive-age woman, pelvic pain + an adnexal mass, β-hCG NEGATIVE.<br><br>"
      "<b>What does the negative test do to your differential?</b>",
      "A negative pregnancy test EXCLUDES ectopic → think ovarian torsion.",
      "Check β-hCG first, but account for the data it gives you. Passed tissue + relief + closed os + simple cyst = completed abortion (ectopic = a COMPLEX mass).",
      "Don't over-call ectopic. The stem usually hands you the rule-out point — use it before reflexing.",
      "ectopic_overcall"),

    C("Diet-controlled GDM: fasting 110–130 and 2-hr postprandials &gt;140 despite adherence.<br><br>"
      "<b>Next step — and what's the trap answer?</b>",
      "Start insulin (first-line; gold standard).",
      "Postprandials over target despite diet → pharmacotherapy. Insulin doesn't cross the placenta.",
      "Don't order an HbA1c to 'titrate' — A1c isn't used for GDM management; that's choosing a test over the treatment. (Screen at 24–28 wks = 50g 1-hr; postpartum = 75g 2-hr GTT at 6–12 wks.)",
      "GDM"),

    C("Intrauterine fetal demise at 26 weeks.<br><br>"
      "<b>Delivery route, the coagulation risk if retained, and how to monitor it?</b>",
      "≥24 weeks → vaginal INDUCTION. Retained &gt;3–4 weeks → consumptive DIC; monitor with serial fibrinogen.",
      "Route is GA-driven: D&E if &lt;24 wks, induction if ≥24 wks (not cesarean). Retained tissue releases thromboplastin → DIC.",
      "Serial fibrinogen detects subclinical DIC — NOT prophylactic FFP (that's only for active bleeding). When asked the cause: 'we may never know,' don't invent one.",
      "IUFD"),

    C("You need to deliver devastating news (e.g., a fetal demise).<br><br>"
      "<b>What's the shelf-preferred opening move?</b>",
      "ASK the patient's permission before delivering bad news, then be honest, empathetic, non-blaming.",
      "When a patient-centered communication option exists, it's usually the answer over a premature test or treatment.",
      "Don't assign a false specific cause to soften it; respect autonomy but keep the dialogue open (don't coerce, don't shut the conversation down).",
      "communication_bad_news"),

    C("An ASYMPTOMATIC finding engineered to make you act: Actinomyces on Pap with an IUD in place; "
      "or prior gestational HTN now normotensive.<br><br><b>What's the move?</b>",
      "Observe / reassure — no treatment, no workup.",
      "Asymptomatic Actinomyces = colonization → keep the IUD, no antibiotics. Now-normotensive prior gestational HTN → routine screening, not a 24-hr urine.",
      "This is your #1 cross-bank error: trusting 'normal' under distraction. The stem buries 'observe' under pressure to do something.",
      "well_patient_observe", misses="b14 b15 n4"),

    C("Twin ultrasound: the dividing membrane shows a lambda (twin-peak) sign.<br><br>"
      "<b>Chorionicity, timing of the split, and membrane layer count?</b>",
      "Dichorionic-diamniotic; split days 0–3; 4 layers (amnion-chorion-chorion-amnion).",
      "T-sign = monochorionic-diamniotic (split 4–8 d) = 2 layers (amnion-amnion). Later splits → mono-mono/conjoined.",
      "Don't swap lambda↔T. Lambda = Di-Di (4 layers); T = Mo-Di (2 layers).",
      "twin_chorionicity"),

    C("Postpartum hemorrhage. The exam findings, not the story, should pick the cause.<br><br>"
      "<b>Walk the four 'T's by finding: boggy vs firm-with-laceration vs enlarged-with-clots vs normal-coags-but-bleeding.</b>",
      "Boggy = atony (Tone). Firm + sidewall laceration = Trauma. Enlarged + large clots, afebrile = retained products (Tissue). Normal exam + prolonged bleeding time = von Willebrand (Thrombin).",
      "A FIRM uterus that's still bleeding points away from atony — look for trauma or coagulopathy.",
      "Both your misses came from anchoring on a story (infection, atony) and ignoring the discriminator handed to you (the afebrile clue, the coag panel).",
      "pph_puerperium"),

    C("Young woman, STI risk, pelvic pain + cervical motion tenderness, now vomiting, T 39.4, can't "
      "tolerate orals. IUD in place.<br><br><b>Disposition, regimen, and what about the IUD?</b>",
      "Admit for IV antibiotics (cefoxitin/cefotetan + doxycycline). Leave the IUD.",
      "CMT is the defining sign of PID. Admission criteria: severe illness, high fever, can't tolerate orals, pregnancy, or tubo-ovarian abscess.",
      "Treat empirically — never await NAAT. Don't pull the IUD unless no improvement at 48–72h. (RUQ pain worse with inspiration = Fitz-Hugh-Curtis.)",
      "pid_fitzhugh"),

    C("Sudden severe unilateral pelvic pain. Which way the two discriminators point: a NEGATIVE "
      "pregnancy test vs massive hemoperitoneum + anemia.<br><br><b>Torsion or ruptured corpus luteum?</b>",
      "Negative hCG → favors torsion (excludes ectopic). Massive hemoperitoneum/anemia → favors ruptured corpus luteum (torsion doesn't exsanguinate).",
      "Torsion: enlarged ovary twists → diagnostic laparoscopy + DETORSION, never observe (Doppler flow can persist, so normal flow doesn't exclude it).",
      "You OVER-call torsion. Big bleed + shock + anticoagulation/luteal phase = ruptured corpus luteum, not torsion.",
      "ovarian_torsion_vs_corpus_luteum"),

    C("Preterm labor likely within 7 days at 30 weeks. The mother is diabetic and hyperglycemic.<br><br>"
      "<b>Single biggest mover of neonatal outcomes?</b>",
      "Antenatal corticosteroids (betamethasone/dexamethasone) — give even with diabetic hyperglycemia.",
      "↓RDS, IVH, NEC, mortality — more than any tocolytic (tocolytics just buy time for the steroids).",
      "The transient glucose bump is far outweighed by the lung benefit. 'Best intervention for neonatal mortality' = steroids, not the tocolytic.",
      "antenatal_corticosteroids"),

    C("After ROM (risk: unstable lie, polyhydramnios, high station): fetal bradycardia with a "
      "pulsating cord at the introitus.<br><br><b>Acute threat and management?</b>",
      "Cord prolapse → fetal ASPHYXIA. Elevate the presenting part, knee-chest, emergent cesarean.",
      "Cord compressed → gas exchange stops → bradycardia. Prolonged compression = MIXED acidosis (respiratory CO₂ + metabolic lactate).",
      "Name the acute event (asphyxia/demise), not downstream RDS. Management is immediate, not observation.",
      "cord_prolapse"),

    C("New mother with intrusive thoughts of harming the baby. She is HORRIFIED by them, reality "
      "testing intact, no hallucinations, &gt;2 weeks.<br><br><b>Diagnosis and treatment?</b>",
      "Postpartum depression → SSRI + psychotherapy (not an emergency).",
      "Ego-DYSTONIC thoughts + intact reality testing = PPD. &gt;2 weeks rules out self-limited baby blues.",
      "Postpartum PSYCHOSIS is the contrast — hallucinations/delusions, lost reality testing, ego-syntonic risk = psychiatric emergency. Don't over-call it.",
      "postpartum_mood"),

    C("Corpus luteum removed/lost at 9 weeks (e.g., cystectomy).<br><br>"
      "<b>What do you supplement, and what's the timing rule?</b>",
      "Vaginal progesterone — because it's before the luteal-placental shift (~8–10 wks).",
      "Early pregnancy runs on CL progesterone until the placenta takes over at ~10–12 wks.",
      "Estrogen alone won't hold it. After ~10–12 wks the placenta covers it and you can be expectant.",
      "luteal_placental_shift"),

    C("First-trimester ultrasound (CRL) dates the pregnancy 10 days off from the LMP.<br><br>"
      "<b>Which date wins, and what's calculated off it?</b>",
      "The ultrasound redates the pregnancy — discard the LMP. Everything downstream (20-wk survey, etc.) is calculated off the US date.",
      "First-tri US is the most accurate dating; redate when LMP and US disagree by &gt;5–7 days in the 1st tri.",
      "The trap is sticking with the LMP.",
      "pregnancy_dating"),

    C("Genital ulcer: SOLITARY, PAINLESS, clean-based, firm indurated borders, with non-tender "
      "(rubbery) lymphadenopathy.<br><br><b>Organism?</b>",
      "Treponema pallidum (primary syphilis chancre).",
      "PainLESS is the separator. PainFUL ulcers = HSV (multiple, vesicular) or chancroid (H. ducreyi, ragged, painful buboes).",
      "Don't call a painless clean ulcer HPV (warts, not ulcers) or LGV (painful suppurative buboes). (Missed 2×.)",
      "syphilis_chancre"),

    C("Pregnant woman with an established acute DVT/PE, normal renal function.<br><br>"
      "<b>Anticoagulant and dose intensity?</b>",
      "THERAPEUTIC-dose LMWH (enoxaparin).",
      "LMWH doesn't cross the placenta, predictable dosing. An established clot needs therapeutic, not prophylactic, dosing.",
      "Don't under-dose. Warfarin is teratogenic, DOACs are contraindicated; UFH only for renal failure/near-term.",
      "vte_pregnancy"),

    C("Active-phase arrest: 9 cm for 4.5 hours, MVU 190 (inadequate), reassuring tracing.<br><br>"
      "<b>Next step?</b>",
      "Augment with oxytocin (inadequate power, MVU &lt;200).",
      "The fork is POWER: if contractions are inadequate, augment before calling it a cesarean.",
      "Carboprost is a PPH uterotonic, NOT a labor-augmentation agent. Vacuum is contraindicated before full dilation.",
      "labor_arrest_oxytocin", extra=["source::NBME"]),

    C("Transverse or breech lie noted at 32 weeks.<br><br>"
      "<b>Management now?</b>",
      "Expectant — schedule follow-up and reassess; most convert to vertex with room to move.",
      "The discriminator is gestational age: a malpresentation BEFORE term is managed expectantly.",
      "ECV is offered at ≥37 weeks (not before). A preterm malpresentation is not a cesarean and not a membrane sweep.",
      "malpresentation_preterm"),

    C("Pregnant woman with HTN 156/92 + headache + visual changes. She has a migraine history.<br><br>"
      "<b>Is this her migraine or preeclampsia?</b>",
      "Preeclampsia with severe features — the cerebral/visual symptoms ARE a severe feature.",
      "When the BP is up, don't blame the migraine history. Severe-range BP + epigastric pain + proteinuria → the feared complication is hemorrhagic stroke (treat severe BP urgently).",
      "This is the REVERSE of the eclampsia-mimics reflex: here the HTN is present, so it IS preE — don't talk yourself out of it.",
      "eclampsia_real_vs_migraine"),

    # ===================== second-angle / additional sourced cards =====================
    C("3rd-trimester bleeding that starts WITH membrane rupture, followed immediately by fetal "
      "bradycardia.<br><br><b>Diagnosis and management?</b>",
      "Vasa previa → emergent cesarean.",
      "Fetal vessels over the os tear at ROM → fetal exsanguination (the blood is FETAL). Painless previa = maternal bleed, no fetal brady at onset.",
      "Bleeding + ROM + fetal brady is the triad — don't confuse with previa (no ROM trigger, no immediate fetal distress).",
      "vasa_previa"),

    C("Pregnant woman &gt;20 weeks, BP 164/112 on two readings, no other findings yet.<br><br>"
      "<b>Does this alone qualify as severe, and what's the immediate concern?</b>",
      "Yes — BP ≥160/110 alone = preeclampsia with severe features.",
      "Severe-range BP by itself meets severe criteria (don't wait for proteinuria/labs). Other severe features: cerebral/visual sx, epigastric pain, ↑LFTs, low platelets, ↑Cr.",
      "Urgently lower severe-range BP (labetalol or hydralazine) to prevent maternal stroke — the feared complication.",
      "preeclampsia_severe"),

    C("Eclampsia (or preeclampsia with severe features) diagnosed.<br><br>"
      "<b>Two pillars of management?</b>",
      "MgSO4 (seizure prophylaxis/treatment) + delivery. Add an antihypertensive (labetalol/hydralazine) for severe-range BP.",
      "Mg prevents/treats seizures; delivery is the only cure. Antihypertensives protect against stroke but don't treat the disease.",
      "Don't give an antihypertensive INSTEAD of Mg, and don't delay delivery for severe disease at term.",
      "preeclampsia_mgmt"),

    C("Severe postpartum hemorrhage. Days later she can't lactate, then develops fatigue, "
      "hypotension, and cold intolerance.<br><br><b>Diagnosis?</b>",
      "Sheehan syndrome — postpartum pituitary infarction → panhypopituitarism.",
      "Failure to lactate (low prolactin) is the early tell; then secondary hypothyroidism/adrenal insufficiency.",
      "Tie the inability to lactate back to the antecedent hemorrhage — don't work it up as primary thyroid/adrenal disease.",
      "sheehan"),

    C("Rh-negative mom, Kleihauer-Betke shows 60 mL of fetal blood.<br><br>"
      "<b>How many RhoGAM doses?</b>",
      "3 doses. 60 ÷ 30 = 2, plus 1 safety dose.",
      "Each 300-µg vial covers ~30 mL of fetal whole blood (15 mL fetal RBCs). Always round up and add one.",
      "Routine RhoGAM is also given at 28 weeks and within 72h postpartum if the baby is Rh-positive.",
      "rhogam_dosing"),

    C("Placenta accreta suspected (prior cesareans + anterior previa). At delivery the placenta "
      "won't separate.<br><br><b>What must you NOT do?</b>",
      "Do NOT attempt manual placental extraction — plan for cesarean hysterectomy.",
      "Accreta = abnormal invasion; forcing separation triggers catastrophic hemorrhage.",
      "Manual extraction is the contraindicated maneuver here. Anticipate it antenatally with prior C/S + previa.",
      "placenta_accreta"),

    C("Prior CLASSICAL cesarean (or a cavity-entering myomectomy). She's asymptomatic at term.<br><br>"
      "<b>Delivery plan?</b>",
      "Scheduled repeat cesarean at 36–37 weeks — before labor starts.",
      "A classical scar can rupture even ANTEPARTUM; avoid labor entirely. Same rule for a myomectomy that entered the cavity.",
      "Don't allow a TOLAC with a classical scar. Deliver abdominally before labor.",
      "rupture_scheduled_delivery"),

    C("Routine GDM screening sequence in a woman at 26 weeks.<br><br>"
      "<b>What's the first test, and when is the next one done?</b>",
      "1-hour 50g glucose challenge FIRST; the 3-hour 100g GTT is only confirmatory if the 1-hour is elevated.",
      "Two-step screening: screen with the 1-hr, confirm with the 3-hr. Screen everyone at 24–28 weeks.",
      "Don't jump straight to the 3-hour test. Screen EARLY at the first visit if risk factors (prior macrosomia ≥4.5 kg, obesity) to catch overt T2DM.",
      "GDM_screening_sequence"),

    C("A 20-year-old asks about a Pap and HPV testing. She's had several partners and smokes.<br><br>"
      "<b>When does cervical cytology start, and does her history change it?</b>",
      "Cytology starts at age 21. History (partners, smoking, sexual debut) does NOT change the start age.",
      "Pap at 21; HPV co-testing not until 30. Age-based, not risk-based.",
      "Don't order an early Pap for 'high-risk' history. Separately: HPV vaccine catch-up runs through 26 — vaccinate (don't HPV-test before vaccinating).",
      "cervical_screening_ages"),

    C("Benign endometrial cells reported on a Pap.<br><br>"
      "<b>Same finding, opposite action — how does menopausal status decide?</b>",
      "POSTmenopausal → endometrial biopsy (no normal shedding). PREmenopausal with regular menses → no workup (just menstrual shedding).",
      "Report endometrial cells if ≥45; evaluate only if postmenopausal or there's abnormal bleeding.",
      "Don't biopsy a premenopausal woman whose LMP was a few days ago — that's normal shedding.",
      "endometrial_cells_pap"),

    C("Older woman with acute new urinary frequency/urgency/incontinence; urinalysis leukocyte "
      "esterase positive (nitrite negative).<br><br><b>What do you do before classifying her incontinence?</b>",
      "Treat the UTI first — it's a transient, reversible cause.",
      "The 'I' (infection) in DIAPPERS. A nitrite-negative UA doesn't exclude it (S. saprophyticus).",
      "Don't classify her as stress vs urge incontinence until the transient cause is treated.",
      "transient_incontinence"),

    C("Woman with bilateral breast pain that's worse premenstrually and eases after menses. No "
      "discrete mass.<br><br><b>Management?</b>",
      "Reassurance — cyclic (fibrocystic) mastalgia.",
      "Bilateral + cyclic + no dominant mass = benign hormonal pattern.",
      "Don't image or biopsy reflexively. (This is the 'trust normal' skill again — you get it when the stem is obvious.)",
      "cyclic_mastalgia"),

    C("Twins (or polyhydramnios) with a sudden gush at ROM, then painful bleeding + a firm tender "
      "uterus.<br><br><b>Mechanism of the abruption?</b>",
      "Sudden uterine decompression at ROM → shearing → placental separation.",
      "The firm tender uterus rules out vasa previa; rapid decompression is the specific trigger here.",
      "Don't call it vasa previa just because it followed ROM — vasa previa gives fetal brady, abruption gives a firm tender uterus.",
      "abruption_decompression"),

    C("Stable ectopic, β-hCG low and not too high, small mass, NO fetal cardiac activity, no free "
      "fluid, no rupture.<br><br><b>Treatment, and the absolute contraindications to it?</b>",
      "Methotrexate. Contraindications: fetal cardiac activity, large size/high hCG, free fluid/rupture, hemodynamic instability.",
      "MTX needs a stable patient and a small, quiet ectopic. Otherwise → surgery (salpingostomy/salpingectomy).",
      "Don't offer MTX when cardiac activity, free fluid, or instability is present — that's a surgical ectopic.",
      "ectopic_methotrexate"),

    C("Imminent preterm delivery before 32 weeks.<br><br>"
      "<b>Besides steroids, what do you give specifically for the fetal brain?</b>",
      "Magnesium sulfate — for fetal neuroprotection (↓ cerebral palsy) at &lt;32 weeks.",
      "Two separate Mg roles: seizure prophylaxis in preeclampsia, and fetal neuroprotection in early preterm birth.",
      "Don't conflate it with tocolysis — Mg's neuroprotection benefit is distinct from buying time.",
      "magnesium_neuroprotection"),

    C("Otherwise normal pregnancy reaching 41 weeks.<br><br>"
      "<b>What's the move, and why not keep waiting?</b>",
      "Offer induction of labor around 41 weeks (by 42 at the latest).",
      "Post-term risk (stillbirth, macrosomia, meconium, placental insufficiency) climbs after 41 weeks.",
      "Don't keep expectantly managing a confirmed 41-weeker — induce.",
      "postterm_induction"),

    C("Preterm labor at 30 weeks, mother hemodynamically normal, needs tocolysis to complete steroids.<br><br>"
      "<b>First-line tocolytic?</b>",
      "Nifedipine (or indomethacin if &lt;32 weeks).",
      "Tocolytics just buy ~48h for steroids. Choose by maternal status: hypotension/tachycardia rules out nifedipine/terbutaline → indomethacin.",
      "Tocolysis is a means to give steroids, not an end — don't expect it to 'stop' preterm birth.",
      "tocolytic_choice"),

    C("Chronic hypertension in pregnancy, now with worsening control near term.<br><br>"
      "<b>Most likely course?</b>",
      "Indicated (medically necessary) preterm delivery.",
      "Chronic HTN raises superimposed preeclampsia risk and often drives an indicated preterm delivery.",
      "Don't confuse this with spontaneous preterm labor or a PPROM distractor.",
      "chronic_htn_complication"),

    C("HTN newly &gt;20 weeks. How do you separate gestational hypertension from preeclampsia?<br><br>"
      "<b>The dividing finding?</b>",
      "Proteinuria (or other end-organ involvement) → preeclampsia. Its absence with new HTN &gt;20 wks = gestational hypertension.",
      "Both are new after 20 weeks; the organ damage (proteinuria, ↑LFTs, low platelets, ↑Cr, cerebral sx) is what upgrades it.",
      "Severe-range BP alone now also counts as severe even without proteinuria.",
      "gestational_vs_preeclampsia"),

    C("PPROM at 31 weeks, no infection, reassuring.<br><br>"
      "<b>Management, and the delivery timing?</b>",
      "Latency antibiotics + antenatal steroids (± Mg neuroprotection); deliver at 34 weeks.",
      "Expectant management to gain maturity, with abx to prolong latency and reduce infection.",
      "But if chorioamnionitis, abruption, or non-reassuring status develops → deliver now (and vaginal/induction is preferred in chorio).",
      "PPROM_management"),

    C("Postpartum thyrotoxic phase from destructive thyroiditis is resolving.<br><br>"
      "<b>What phase often follows, and the long-term watch?</b>",
      "A transient HYPOthyroid phase — most recover, but some stay permanently hypothyroid.",
      "Destructive thyroiditis: thyrotoxic (leak) → hypothyroid (depleted) → usually euthyroid. Monitor TSH.",
      "Don't treat the thyrotoxic phase with a thionamide (no synthesis to block) — β-blocker only; then watch for the hypothyroid swing.",
      "postpartum_thyroiditis_phases"),

    C("Thyrotoxicosis with a PAINFUL, tender goiter after a recent viral URI; low radioiodine uptake.<br><br>"
      "<b>Diagnosis, and how it differs from postpartum thyroiditis?</b>",
      "Subacute (de Quervain) thyroiditis — post-viral, PAINFUL gland.",
      "Both are destructive (low uptake), but de Quervain is painful/post-viral; postpartum thyroiditis is painless and TPO-positive.",
      "Pain + recent virus is the separator. Exogenous thyrotoxicosis = no goiter + low thyroglobulin.",
      "subacute_thyroiditis"),

    # ===================== b13 (2026-06-22) — new weak clusters =====================
    C("First prenatal visit, low-risk woman. You're ordering the routine serologies.<br><br>"
      "<b>Which test screens for syphilis — treponemal or not?</b>",
      "Nontreponemal test first — RPR or VDRL.",
      "Universal screen at the first visit regardless of risk; reactive RPR/VDRL is then confirmed with a treponemal test (FTA-ABS / MHA-TP).",
      "Don't start with the treponemal test (MHA-TP), and don't add Toxo/HSV/CMV — those aren't routine prenatal screens.",
      "prenatal_syphilis_screen"),

    C("Term pregnancy, AFI 3 cm (oligohydramnios). Bladder, growth, and Dopplers all normal. "
      "She denies any medications.<br><br><b>Most likely cause?</b>",
      "Rupture of membranes (amniotic fluid leakage).",
      "ROM is the most common cause of new-onset oligohydramnios at term; normal bladder/growth/Doppler argue against renal agenesis and placental insufficiency.",
      "NSAIDs (indomethacin) also drop fluid — but she denies meds. With everything else normal, leakage is the answer by elimination.",
      "oligohydramnios_term"),

    C("Prior DVT, current smoker, wants a method that also stops her periods.<br><br>"
      "<b>Best contraceptive?</b>",
      "Levonorgestrel IUD (LNG-IUD).",
      "Estrogen methods are MEC Category 4 with a VTE history; the LNG-IUD is safe AND causes amenorrhea — hits both goals.",
      "Not the copper IUD — it increases bleeding, the opposite of her amenorrhea goal. After a clot: progestin/IUD, never estrogen.",
      "contraception_vte"),

    C("5 days after cesarean: fever, a boggy and exquisitely tender uterus, lochia present. "
      "Incision clean and intact.<br><br><b>Diagnosis?</b>",
      "Postpartum endometritis.",
      "Fever + uterine tenderness after delivery (esp. post-cesarean) = endometritis; the clean incision rules out a surgical-site infection.",
      "Not retained placenta — that's a hemorrhage problem (boggy + bleeding). Fever + tenderness = infection. Tx: clindamycin + gentamicin.",
      "postpartum_endometritis", misses="n4", extra=["source::NBME"]),

    C("After prolonged high lithotomy: 1/5 knee extension, absent patellar reflex, numb anterior "
      "thigh. Hip ADDUCTION is 5/5.<br><br><b>Mechanism?</b>",
      "Femoral nerve compression from excessive hip flexion (under the inguinal ligament).",
      "Knee-extension weakness + lost patellar reflex + anterior-thigh sensory loss = femoral nerve; preserved hip adduction (5/5) rules out the obturator nerve.",
      "It's hip FLEXION, not abduction/adduction, that pins the femoral nerve beneath the inguinal ligament in stirrups.",
      "femoral_nerve_lithotomy", extra=["source::NBME"]),

    C("Maternal rash + arthralgia; now fetal hydrops with MCA peak systolic velocity 1.7 MoM. "
      "Fetal heart is structurally normal.<br><br><b>Mechanism of the hydrops?</b>",
      "High-output cardiac failure from severe fetal anemia (parvovirus B19).",
      "Parvovirus B19 → fetal RBC aplasia → anemia → high-output failure → hydrops; MCA PSV >1.5 MoM = anemia/hyperdynamic flow, heart structurally normal.",
      "Not an outflow obstruction — the heart is normal. It's pump-overload from anemia, not a structural lesion.",
      "parvovirus_hydrops"),

    # ===================== b14 (2026-06-24, UWorld) new content-gap cards =====================

    C("Postpartum (or post-pelvic-surgery) woman passing GAS and STOOL through the vagina, "
      "malodorous discharge. External anal skin intact.<br><br><b>Diagnosis?</b>",
      "Rectovaginal fistula — an abnormal rectum↔vagina tract (often after 3rd/4th-degree laceration or surgery).",
      "Flatus/feces per vagina = a fistulous tract bypassing the sphincter — not incontinence (sphincter/skin intact).",
      "Don't call it a urinary fistula (that's urine, not stool) or an anal sphincter defect (that's incontinence, not gas/stool per vagina).",
      "rectovaginal_fistula"),

    C("Days after ovulation induction / egg retrieval: abdominal distension, enlarged ovaries, "
      "ascites, hemoconcentration.<br><br><b>Diagnosis?</b>",
      "Ovarian hyperstimulation syndrome (OHSS).",
      "Post-ovulation-induction enlarged ovaries + third-spacing/ascites + hemoconcentration = OHSS.",
      "It follows fertility treatment specifically — don't chase other causes of ascites/distension that don't track with ovulation induction.",
      "ohss", extra=["source::NBME"]),

    C("2nd/3rd-trimester pruritic urticarial plaques starting AROUND THE UMBILICUS, progressing "
      "to TENSE BULLAE.<br><br><b>Diagnosis?</b>",
      "Pemphigoid gestationis — autoimmune subepidermal blistering dermatosis of pregnancy.",
      "Periumbilical onset + tense blisters = pemphigoid gestationis.",
      "PUPPP spares the umbilicus, lives in the striae, and does NOT blister — the umbilicus + bullae are the split.",
      "pemphigoid_gestationis"),

    C("Amenorrhea, low BMI, intense exercise / restrictive eating. Pregnancy excluded.<br><br>"
      "<b>Best next step?</b>",
      "Evaluate for an underlying eating disorder (functional hypothalamic amenorrhea from low energy availability).",
      "Low weight + restrictive/over-exercise + amenorrhea → suppressed GnRH = FHA; screen for the eating disorder driving it.",
      "Don't run the structural/endocrine amenorrhea workup first when the behavioral/low-energy picture is staring at you.",
      "functional_hypothalamic_amenorrhea"),

    C("Cervical workup shows a POSITIVE endocervical curettage / high-grade endocervical lesion "
      "(e.g., CIN 3).<br><br><b>Next step?</b>",
      "Diagnostic excisional procedure — cervical conization (cold-knife or LEEP).",
      "A positive ECC / high-grade endocervical disease needs EXCISION — see the whole lesion + exclude invasion.",
      "Ablation destroys tissue without a specimen → can't exclude invasive cancer; observation is inadequate for high-grade endocervical disease.",
      "ecc_conization"),

    C("Pregnant patient, any trimester, during flu season.<br><br><b>Which influenza vaccine?</b>",
      "Inactivated influenza vaccine — recommended in ANY trimester.",
      "Inactivated flu vaccine is safe and recommended throughout pregnancy; protects mother + neonate.",
      "The LIVE attenuated (intranasal) flu vaccine is CONTRAINDICATED in pregnancy — and don't defer the inactivated one either.",
      "influenza_vaccine_pregnancy"),

    C("POSTMENOPAUSAL woman with an adnexal mass on imaging.<br><br><b>Next step to stratify "
      "malignancy risk?</b>",
      "Serum CA-125.",
      "In a postmenopausal adnexal mass, CA-125 stratifies malignancy risk and guides gyn-onc referral.",
      "CA-125 is far more specific postmenopausally — premenopausally it's falsely raised by endometriosis, fibroids, PID.",
      "ca125_adnexal_mass"),

    C("Type O mother, type A/B infant, mild neonatal jaundice — in a FIRST pregnancy, no prior "
      "sensitization.<br><br><b>Explanation?</b>",
      "ABO incompatibility — can affect a first pregnancy and is usually MILD.",
      "Mom's preformed anti-A/anti-B (IgG) cross the placenta → mild hemolysis, even in pregnancy #1.",
      "Unlike Rh disease, ABO needs NO prior sensitization and is typically mild — don't expect Rh-like severity or 'only later pregnancies.'",
      "abo_incompatibility"),

    C("Recurrent pregnancy loss; imaging shows a SUBMUCOSAL fibroid distorting the uterine "
      "cavity.<br><br><b>Best treatment?</b>",
      "Hysteroscopic myomectomy.",
      "A submucosal (intracavitary) fibroid impairs implantation → recurrent loss; resect hysteroscopically (cavity access, no abdominal incision).",
      "Abdominal/laparoscopic myomectomy is for intramural/subserosal; medical therapy doesn't fix the mechanical cavity distortion.",
      "leiomyoma_submucosal_rpl"),

    C("Months after cervical CONIZATION (LEEP/CKC): cyclic pelvic pain, scant/absent menses, "
      "possible hematometra.<br><br><b>Complication?</b>",
      "Cervical stenosis — a scarred, narrowed os obstructing menstrual outflow.",
      "Post-cone cyclic pain + obstructed/absent flow = stenosis; outflow obstruction backs blood up (hematometra).",
      "Don't confuse with cervical INSUFFICIENCY (the other post-cone risk — painless dilation/preterm loss, the opposite problem).",
      "cervical_stenosis_post_cone"),

    C("Woman with HIV (or otherwise immunocompromised). Question is the cervical cancer "
      "screening interval.<br><br><b>Approach?</b>",
      "More frequent cervical cancer screening than the general population.",
      "Immunocompromise (esp. HIV) accelerates HPV persistence → higher cervical cancer risk → intensified, more frequent screening.",
      "Don't apply the standard general-population interval (or defer) — immunosuppression changes the schedule.",
      "cervical_screening_hiv"),

    C("Woman UNDER 45 with abnormal uterine bleeding that FAILED medical management (e.g., OCPs). "
      "Hgb normal.<br><br><b>Next step?</b>",
      "Endometrial biopsy.",
      "AUB failing medical management warrants endometrial sampling for hyperplasia/cancer — even under 45.",
      "US is insensitive for the premenopausal endometrium; coag studies are for a bleeding-disorder picture (Hgb normal here); ablation/HSG are wrong before a tissue diagnosis.",
      "aub_under45_biopsy"),
]

# Attach mnemonics by cluster (leaves cards without one blank — the template hides it).
for _card in TEXT_CARDS:
    if _card["cluster"] in MNEM:
        _card["mnem"] = MNEM[_card["cluster"]]
