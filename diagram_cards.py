# -*- coding: utf-8 -*-
"""Diagram-back cards (the NBME format): the explanation is an arrow-chart, not
a paragraph. Each card carries a `diagram` spec that build_deck renders to PNG
via diagram.discriminator_svg(). Front is a tight vignette; the back is the
answer line + the chart (Tell/Beats text fields stay empty -> hidden).

Started n2 (2026-06-29). New cards go here in diagram form; old text/image cards
are untouched.
"""


def D(front, answer, cluster, diagram, extra=None, misses=""):
    return dict(front=front, answer=answer, discrim="", trap="", mnem="",
                cluster=cluster, diagram=diagram, extra=extra, misses=misses)


_NBME = ["source::NBME"]
_NBME_ONLY = ["source::NBME", "nbme-only"]

DIAGRAM_CARDS = [

    # ===================== n2 (2026-06-29, NBME) =====================
    D("Primigravid 28 wk, uncomplicated. Hb 9.1, Hct 29, MCV 69.<br><br>"
      "<b>Most appropriate next step to CONFIRM the diagnosis?</b>",
      "Serum ferritin.", "iron_deficiency_pregnancy", extra=_NBME,
      diagram={
          "title": "Microcytic anemia in pregnancy → confirm how?",
          "cues": ["healthy gravida, 28 wk", "Hb 9.1, *MCV 69* (microcytic)",
                   "no hemolysis / no GI-loss clues"],
          "tell": "microcytic + low pretest prob of a hemoglobinopathy",
          "answer": "SERUM FERRITIN", "answer_sub": "cheap, confirms iron deficiency",
          "ruled_out": [("Hgb electrophoresis", "only with thalassemia/variant clues — none here"),
                        ("blood smear", "for unexplained anemia or hemolysis signs"),
                        ("reticulocyte count", "gauges marrow response, not needed"),
                        ("stool occult blood", "GI loss — wrong population")]}),

    D("16 wk: MSAFP 5 MoM; US shows an omphalocele.<br><br><b>Next step in evaluation?</b>",
      "Fetal karyotype.", "omphalocele_karyotype", extra=_NBME_ONLY, misses="n2",
      diagram={
          "title": "↑MSAFP + omphalocele → next step?",
          "cues": ["16 wk, *MSAFP 5 MoM*", "US: *omphalocele* — cause already seen"],
          "tell": "omphalocele = high aneuploidy / Beckwith-Wiedemann association",
          "answer": "FETAL KARYOTYPE", "answer_sub": "escalate to genetic workup",
          "ruled_out": [("amniotic AChE", "confirms NTD when US is UNrevealing — but the cause is already seen"),
                        ("amniotic AFP", "redundant, cause already found"),
                        ("fetal HLA type", "no link to abdominal-wall defects"),
                        ("β-hCG + estriol", "ectopic/GTD follow-up, not this")]}),

    D("23F, +preg test, LMP 8 wk ago, bleeding ×10d. Closed os. US: fetal pole, "
      "NO cardiac activity.<br><br><b>Dx?</b>",
      "Missed abortion.", "missed_abortion", extra=_NBME,
      diagram={
          "title": "Bleeding + US demise → which abortion?",
          "cues": ["+preg test, LMP 8 wk", "bleeding ×10d, *closed os*",
                   "US: fetal pole, *NO cardiac activity*"],
          "tell": "demise on US + products retained + os CLOSED",
          "answer": "MISSED ABORTION",
          "ruled_out": [("incomplete abortion", "OPEN os + tissue passing"),
                        ("hydatidiform mole", "hyperemesis, size>dates, snowstorm"),
                        ("submucous fibroid", "AUB/pain, no demise pattern"),
                        ("endometrial carcinoma", "age ≥45 / postmenopausal")]}),

    D("IVF (2 embryos), 10 wk, acute right pelvic pain. US: intrauterine pregnancy AND a "
      "separate 3-cm adnexal mass (ovary normal).<br><br><b>Dx?</b>",
      "Heterotopic pregnancy.", "heterotopic_pregnancy", extra=_NBME,
      diagram={
          "title": "IVF + IUP + adnexal mass → dx?",
          "cues": ["*IVF*, 2 embryos transferred", "US: *intrauterine* pregnancy",
                   "+ a *separate* adnexal mass (not in ovary)"],
          "tell": "an IUP AND a separate ectopic in an ART patient",
          "answer": "HETEROTOPIC PREGNANCY",
          "ruled_out": [("corpus luteum cyst", "WITHIN the ovary, not separate"),
                        ("hydatidiform mole", "snowstorm uterus, theca-lutein cysts"),
                        ("hydrosalpinx", "dilated fluid-filled tube (PID)"),
                        ("OHSS", "bilaterally enlarged ovaries, not a discrete mass")]}),

    D("Primigravid 34 wk, postictal after a tonic-clonic seizure. BP 170/108, 3+ proteinuria, "
      "reassuring FHR.<br><br><b>In addition to magnesium, next step?</b>",
      "IV labetalol (acute BP control).", "eclampsia_bp_labetalol", extra=_NBME,
      diagram={
          "title": "After mag for the seizure — next?",
          "cues": ["seized, now postictal", "*BP 170/108*, 3+ protein", "reassuring FHR, 34 wk"],
          "tell": "seizure is covered by mag → next priority is the severe BP",
          "answer": "IV LABETALOL", "answer_sub": "treat severe-range HTN",
          "ruled_out": [("betamethasone", "lung maturity can wait until stabilized"),
                        ("oxytocin / delivery", "after stabilization, not the immediate step"),
                        ("biophysical profile", "nonemergent, no acute value"),
                        ("phenobarbital", "for refractory status — she's no longer seizing")]}),

    D("POD 6 after C-section: profuse serosanguineous drainage from the midline incision, "
      "minimal erythema. Probing the defect meets NO resistance.<br><br><b>Most likely explanation?</b>",
      "Fascial dehiscence.", "fascial_dehiscence", extra=_NBME_ONLY, misses="n2",
      diagram={
          "title": "Post-op incision drainage → what is it?",
          "cues": ["POD 6, after C-section", "*serosanguineous* drainage (not pus)",
                   "minimal erythema, afebrile", "probe → *NO resistance*"],
          "tell": "probe slides in freely + serosanguineous (not pus)",
          "answer": "FASCIAL DEHISCENCE", "answer_sub": "the fascia is open — surgical emergency",
          "ruled_out": [("wound infection", "needs pus + fever + erythema, none here"),
                        ("subfascial abscess", "probe meets RESISTANCE + purulent"),
                        ("subcutaneous hematoma", "palpable, probe returns blood"),
                        ("enterocutaneous fistula", "drains GI contents, not serosanguineous")]}),

    D("Primigravid 38 wk in labor. Treated for a first HSV-2 episode 3 mo ago; now "
      "asymptomatic, NO lesions on exam.<br><br><b>Method of delivery?</b>",
      "Vaginal delivery.", "hsv_delivery_mode", extra=_NBME,
      diagram={
          "title": "HSV history, in labor → delivery mode?",
          "cues": ["38 wk, in labor", "first HSV-2 episode *3 mo ago*", "*NO lesions* / no prodrome now"],
          "tell": "delivery mode hinges on lesions AT LABOR, not on history",
          "answer": "VAGINAL DELIVERY",
          "ruled_out": [("C-section (active earlier this preg)", "past activity irrelevant without lesions now"),
                        ("C-section (no acyclovir ppx)", "ppx suppresses but isn't required if asymptomatic"),
                        ("vaginal after 1 acyclovir dose", "one dose doesn't treat an active outbreak")]}),

    # ===================== n3 (2026-06-29, NBME) =====================
    D("Reassuring tracing, then 15 min after epidural: BP 88/50 and FHR 90.<br><br>"
      "<b>Cause of the bradycardia?</b>",
      "Maternal hypotension → uteroplacental insufficiency.", "epidural_hypotension_brady", extra=_NBME,
      diagram={
          "title": "Fetal brady right after epidural → why?",
          "cues": ["reassuring tracing before", "*BP 88/50* 15 min post-epidural",
                   "*FHR 90* at the same time"],
          "tell": "the fetal change parallels the maternal BP fall (temporal link)",
          "answer": "MATERNAL HYPOTENSION", "answer_sub": "uteroplacental insufficiency",
          "ruled_out": [("congenital AV block", "needs anti-Ro/La (SLE/Sjögren), not abrupt"),
                        ("cord compression", "variable decels — transient, not persistent brady"),
                        ("head compression", "early decels — benign/normal"),
                        ("vasovagal", "would recover spontaneously")]}),

    D("In labor at 36 wk, no prenatal records / unknown GBS status, meconium fluid.<br><br>"
      "<b>Most appropriate step re: GBS?</b>",
      "Intrapartum penicillin G.", "gbs_unknown_preterm", extra=_NBME_ONLY, misses="n3",
      diagram={
          "title": "Unknown GBS status in labor → prophylaxis?",
          "cues": ["*unknown* GBS status", "*36 wk* = preterm (a risk factor)",
                   "no negative screen on record"],
          "tell": "unknown status + a risk factor (preterm/PPROM/fever) → treat",
          "answer": "INTRAPARTUM PENICILLIN G", "answer_sub": "no culture needed",
          "ruled_out": [("expectant / no abx", "only if term AND no risk factors, or a negative screen"),
                        ("LFTs or platelets", "that's a preeclampsia/HELLP workup"),
                        ("oxytocin", "for induction/protraction, not GBS"),
                        ("cesarean", "not a GBS-prevention strategy")]}),

    D("FHR strip: a single deceleration paralleling a contraction, otherwise normal baseline "
      "and variability.<br><br><b>Management?</b>",
      "Expectant management.", "variable_decel_observe", extra=_NBME,
      diagram={
          "title": "Single variable decel, reassuring strip → do what?",
          "cues": ["one decel mirrors a contraction", "normal baseline + variability",
                   "no recurrent / late pattern"],
          "tell": "an isolated variable (cord compression) on a reassuring strip is benign",
          "answer": "EXPECTANT MANAGEMENT", "answer_sub": "ID the decel type before acting",
          "ruled_out": [("cesarean", "for recurrent LATE decels / Cat III"),
                        ("oxytocin", "contractions/cervix already adequate"),
                        ("magnesium", "no eclampsia (BP/end-organ normal)"),
                        ("forceps", "2nd-stage tool — she's not fully dilated")]}),

    D("Post-C-section endometritis treated, but fever persists 3 days on broad-spectrum "
      "antibiotics. Patient otherwise well, normal UA.<br><br><b>Dx?</b>",
      "Septic pelvic thrombophlebitis.", "septic_pelvic_thrombophlebitis", extra=_NBME,
      diagram={
          "title": "Postpartum fever that won't break on abx → dx?",
          "cues": ["endometritis treated", "*fever persists* 3d on broad-spectrum abx",
                   "*well-appearing*, normal UA"],
          "tell": "fever REFRACTORY to appropriate abx + looks well = the pivot",
          "answer": "SEPTIC PELVIC THROMBOPHLEBITIS", "answer_sub": "diagnosis of exclusion",
          "ruled_out": [("salpingitis", "would respond to the antibiotics"),
                        ("aspiration pneumonia", "needs lung findings (lungs are clear)"),
                        ("systemic candidiasis", "rare if immunocompetent"),
                        ("UTI", "excluded by the normal UA")]}),

    D("Postpartum day 12: vaginal discharge transitioning red → yellow/white, no fever, no "
      "laceration.<br><br><b>Management?</b>",
      "Reassurance / self-care.", "normal_lochia", extra=_NBME,
      diagram={
          "title": "Day-12 discharge red→yellow → worry?",
          "cues": ["day 12 postpartum", "discharge *red → yellow/white*",
                   "afebrile, no laceration, no bleeding"],
          "tell": "lochia rubra → serosa → alba over weeks is physiologic",
          "answer": "REASSURANCE", "answer_sub": "normal involution",
          "ruled_out": [("antibiotics", "need infection signs (none)"),
                        ("ergometrine", "for atony/PPH — no significant bleeding"),
                        ("suction curettage", "for retained products — none"),
                        ("bath restriction 6–8 wk", "unnecessary")]}),

    D("Pregnant, vomiting, no BM ×2 days, distension, hypoactive bowel sounds, prior abdominal "
      "surgery.<br><br><b>First diagnostic step?</b>",
      "Upright abdominal X-ray.", "sbo_pregnancy_xray", extra=_NBME,
      diagram={
          "title": "Suspected SBO in pregnancy → first test?",
          "cues": ["vomiting, no BM ×2d, distension", "hypoactive bowel sounds",
                   "*prior abdominal surgery* (adhesions)"],
          "tell": "an adhesive SBO picture → safest informative first image",
          "answer": "UPRIGHT ABDOMINAL X-RAY", "answer_sub": "limits fetal radiation",
          "ruled_out": [("CT", "more radiation — reserve if x-ray nondiagnostic"),
                        ("colonoscopy", "no role in SBO"),
                        ("EGD", "upper GI — exam points lower"),
                        ("laparoscopy", "surgical risk too high before a diagnosis")]}),

    D("Pregnant: median-distribution numbness worse after typing, +Tinel, thumb abduction "
      "weakness 4/5.<br><br><b>Initial management?</b>",
      "Wrist splints (conservative).", "carpal_tunnel_pregnancy", extra=_NBME,
      diagram={
          "title": "Carpal tunnel in pregnancy → first move?",
          "cues": ["median numbness, worse with typing", "*+Tinel*, thumb weakness 4/5",
                   "pregnancy-related"],
          "tell": "pregnancy CTS usually resolves postpartum → start conservative",
          "answer": "WRIST SPLINTS", "answer_sub": "even with mild motor signs",
          "ruled_out": [("steroid injection", "only after a splint trial"),
                        ("NSAIDs", "no better than placebo + avoided in pregnancy"),
                        ("surgical release", "for refractory/severe only"),
                        ("observation alone", "insufficient for this pain")]}),

    D("72F: firm, minimally tender breast mass after steering-wheel chest trauma. Mammogram "
      "shows calcifications; biopsy benign.<br><br><b>Dx?</b>",
      "Fat necrosis.", "breast_fat_necrosis", extra=_NBME,
      diagram={
          "title": "Firm breast mass after trauma → dx?",
          "cues": ["72yo, mass after *chest trauma*", "firm, minimally tender",
                   "calcifications on mammo, *biopsy benign*"],
          "tell": "antecedent trauma + benign biopsy + calcifications",
          "answer": "FAT NECROSIS",
          "ruled_out": [("duct ectasia", "periareolar, subareolar duct dilation"),
                        ("fibroadenoma", "young (<35), mobile rubbery"),
                        ("intraductal papilloma", "bloody nipple discharge, usually nonpalpable"),
                        ("sclerosing adenosis", "mammographic/microscopic, rarely a big mass")]}),

    # ===================== n4 (2026-06-29, NBME) =====================
    D("29F: bilateral breast swelling/tenderness timed ~1 wk before menses ×3 mo, exam normal "
      "(family hx of breast cancer).<br><br><b>Dx?</b>",
      "Fibrocystic change.", "fibrocystic_breast", extra=_NBME,
      diagram={
          "title": "Cyclic bilateral breast tenderness → dx?",
          "cues": ["bilateral, *premenstrual* (~1 wk before)", "resolves after menses",
                   "exam NORMAL — no discrete mass"],
          "tell": "symptoms are LINKED to the menstrual cycle",
          "answer": "FIBROCYSTIC CHANGE",
          "ruled_out": [("fibroadenoma", "unilateral discrete mobile mass — none here"),
                        ("mastitis", "warm tender area, breastfeeding, S. aureus"),
                        ("abscess", "fluctuant erythematous, breastfeeding"),
                        ("the family history", "a distractor — the cyclic bilateral pattern outweighs it")]}),

    D("52F perimenopausal: a discrete 1-cm palpable breast mass in dense fibronodular tissue."
      "<br><br><b>Most appropriate step?</b>",
      "Tissue biopsy.", "palpable_breast_mass_biopsy", extra=_NBME, misses="n4",
      diagram={
          "title": "Discrete PALPABLE breast mass → what step?",
          "cues": ["52yo, perimenopausal", "*discrete 1-cm palpable mass*", "dense fibronodular tissue"],
          "tell": "a palpable mass demands TISSUE — imaging can't rule out cancer",
          "answer": "BIOPSY (tissue)", "answer_sub": "regardless of imaging",
          "ruled_out": [("MRI", "clarifies equivocal imaging / high-risk screen — mass already palpable"),
                        ("6-month follow-up", "unsafe with a palpable mass"),
                        ("CA-125", "ovarian marker, no breast role"),
                        ("BRCA testing", "risk assessment, not a diagnosis of this mass")]}),

    D("New partner, dysuria + lower abdominal pain, whitish cervical discharge, adnexal "
      "tenderness.<br><br><b>Which structure is primarily involved?</b>",
      "Fallopian tube (salpingitis).", "pid_site_fallopian", extra=_NBME,
      diagram={
          "title": "PID — which structure?",
          "cues": ["new partner, cervical discharge", "lower abdominal + *adnexal* tenderness",
                   "ascending infection"],
          "tell": "PID ascends cervix → uterus → FALLOPIAN TUBE",
          "answer": "FALLOPIAN TUBE (salpingitis)",
          "ruled_out": [("appendix", "periumbilical→RLQ migration, no cervical discharge"),
                        ("bladder", "isolated dysuria/frequency, no adnexal findings"),
                        ("Bartholin gland", "introital swelling, normal internal exam"),
                        ("vagina", "discharge/erythema, not adnexal tenderness")]}),

    D("Healthy 19F, sexually active, first gyn visit, normal exam.<br><br>"
      "<b>Most appropriate screening test?</b>",
      "Chlamydia (+ gonorrhea) screen.", "chlamydia_screening_under25", extra=_NBME,
      diagram={
          "title": "Sexually active 19yo → what to screen?",
          "cues": ["*age <25* + sexually active", "asymptomatic, normal exam"],
          "tell": "USPSTF: annual chlamydia/GC screen for sexually active women <25",
          "answer": "CHLAMYDIA / GC SCREEN",
          "ruled_out": [("annual Pap", "Pap starts at 21, q3y — not annual, not now"),
                        ("HPV vaccine", "prevention (9–26), but the asked SCREEN is chlamydia"),
                        ("TSH", "not screened in asymptomatic patients"),
                        ("pneumococcal vaccine", "high-risk / ≥65 only")]}),

    D("Sexual assault 3 h ago, motile sperm on wet mount, worried about infection.<br><br>"
      "<b>Which agent must be in the prophylaxis?</b>",
      "IM ceftriaxone (gonorrhea).", "sexual_assault_gc_prophylaxis", extra=_NBME,
      diagram={
          "title": "Post-assault STI prophylaxis → core agent?",
          "cues": ["assault 3h ago", "empiric STI prophylaxis bundle"],
          "tell": "ceftriaxone covers N. gonorrhoeae — the required core",
          "answer": "IM CEFTRIAXONE",
          "answer_sub": "+ azithro/doxy, metronidazole, HIV PEP, emergency contraception",
          "ruled_out": [("penicillin", "narrower / duplicative vs ceftriaxone"),
                        ("fluconazole", "yeast — not STI-transmitted"),
                        ("TMP-SMX", "UTI/cellulitis, not STI prophylaxis"),
                        ("immune globulin", "no role if previously vaccinated")]}),

    D("62F: large central pelvic mass, heterogeneous myometrial masses on US, para-aortic "
      "adenopathy on CT.<br><br><b>Dx?</b>",
      "Uterine sarcoma.", "uterine_sarcoma_clinical", extra=_NBME,
      diagram={
          "title": "Postmeno enlarging uterine mass + nodes → dx?",
          "cues": ["*postmenopausal*", "large heterogeneous myometrial mass", "*para-aortic adenopathy*"],
          "tell": "postmenopausal + lymphadenopathy → think MALIGNANT, not a fibroid",
          "answer": "UTERINE SARCOMA",
          "ruled_out": [("leiomyomata", "benign, SHRINK after menopause, no adenopathy"),
                        ("adenomyosis", "boggy uterus, no discrete mass / nodes"),
                        ("cervical cancer", "exophytic cervical lesion — cervix is normal"),
                        ("endometriosis", "dysmenorrhea/dyspareunia, not a big mass")]}),

    D("67F: 1-yr pruritic/painful vulvar lump; DM + prior cervical CIS. Large cauliflower-like "
      "mass.<br><br><b>Dx?</b>",
      "Vulvar (squamous cell) carcinoma.", "vulvar_carcinoma", extra=_NBME, misses="n4",
      diagram={
          "title": "Chronic large exophytic vulvar mass → dx?",
          "cues": ["67yo, *1-yr* lump, pruritic/painful", "risk factors: DM, *prior cervical CIS*",
                   "large *cauliflower-like* mass"],
          "tell": "a chronic exophytic vulvar MASS + risk factors",
          "answer": "VULVAR CARCINOMA (SCC)",
          "ruled_out": [("granuloma inguinale", "painless friable ULCER, not a mass"),
                        ("herpes", "painful vesicles/ulcers, not a large mass"),
                        ("metastatic cervical ca", "nodules/rash, a single big mass is uncommon"),
                        ("vulvar abscess", "acute tender cystic, not present 1 yr")]}),

    D("Healthy 45F, asymptomatic, one 2nd-degree relative (aunt) with ovarian cancer, requests "
      "screening.<br><br><b>Most appropriate?</b>",
      "No screening — routine exam only.", "ovarian_cancer_no_screening", extra=_NBME, misses="n4",
      diagram={
          "title": "Average-risk woman wants ovarian screening → ?",
          "cues": ["asymptomatic, healthy 45yo", "only a *2nd-degree* relative affected",
                   "= average risk, NOT high-risk"],
          "tell": "no test screens average-risk ovarian ca (USPSTF: against)",
          "answer": "NO SCREENING — routine exam",
          "answer_sub": "the family-history anxiety is the trap",
          "ruled_out": [("CA-125", "tumor marker for trending/dx, not screening"),
                        ("CA-125 + US", "the combo still isn't a screening test"),
                        ("transvaginal US", "case-finding/dx, not screening the asymptomatic"),
                        ("abdominal US", "not a screening tool")]}),

    # ===================== n5 (2026-06-29, NBME) =====================
    D("5 days post-laparoscopic adhesiolysis (stage IV endometriosis): fever, tachycardia, "
      "diffuse rebound/guarding, AIR under the diaphragm on CXR.<br><br><b>Dx?</b>",
      "Iatrogenic bowel perforation.", "bowel_perforation_laparoscopy", extra=_NBME,
      diagram={
          "title": "Acute abdomen after adhesiolysis → dx?",
          "cues": ["5d post-laparoscopic *adhesiolysis*", "fever, diffuse rebound/guarding",
                   "*free air* under the diaphragm"],
          "tell": "free subdiaphragmatic air + recent adhesiolysis",
          "answer": "BOWEL PERFORATION", "answer_sub": "peritonitis — needs surgery",
          "ruled_out": [("bladder perforation", "free FLUID without free air; dysuria/hematuria"),
                        ("bacterial overgrowth", "malabsorption picture, not an acute free-air abdomen"),
                        ("skin-flora contamination", "a blood-culture artifact, not this"),
                        ("opportunistic infection", "needs immunocompromise")]}),

    D("32F: 3-mo amenorrhea + dark spotting. LNG IUD placed 1 yr ago, string visible at the os."
      "<br><br><b>Mechanism of the amenorrhea?</b>",
      "LNG-IUD endometrial atrophy.", "lng_iud_endometrial_atrophy", extra=_NBME, misses="n5",
      diagram={
          "title": "Amenorrhea + spotting with an LNG IUD → why?",
          "cues": ["LNG IUD *in place 1 yr*, string at os", "3-mo amenorrhea + dark spotting",
                   "32yo, otherwise well"],
          "tell": "local progestin thins the lining → endometrial ATROPHY",
          "answer": "ENDOMETRIAL ATROPHY (from the LNG IUD)", "answer_sub": "an expected, benign effect",
          "ruled_out": [("menopause transition", "she's 32, no vasomotor/GU menopause signs"),
                        ("Asherman", "needs prior endometrial trauma — absent"),
                        ("PCOS", "no androgen excess / obesity / polycystic ovaries"),
                        ("prolactinoma", "no galactorrhea / headache / visual change")]}),

    D("72F, advanced metastatic ovarian cancer, pain 10/10 on fixed-dose oxycodone. She chooses "
      "hospice / stops chemo.<br><br><b>Most appropriate next step?</b>",
      "Increase the scheduled opioid.", "hospice_opioid_escalation", extra=_NBME, misses="n5",
      diagram={
          "title": "Hospice + progressive cancer pain → next step?",
          "cues": ["advanced metastatic ovarian ca", "pain *10/10* on fixed oxycodone",
                   "goals: *comfort*, hospice, no invasive measures"],
          "tell": "align the next step with the stated comfort goals",
          "answer": "INCREASE THE OPIOID (≥25%)", "answer_sub": "match care to goals — don't escalate invasiveness",
          "ruled_out": [("surgical resection", "ineffective in advanced disease + against her wishes"),
                        ("more IV chemo", "she declined chemo"),
                        ("intraperitoneal chemo", "too invasive for hospice goals"),
                        ("palliative radiation", "slow onset (days–wks) — less appropriate for acute 10/10 pain")]}),
]
