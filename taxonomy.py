# -*- coding: utf-8 -*-
"""
Tag taxonomy for the Step-2 / rotations Anki deck.

Three independent axes (Anki hierarchical tags via `::`) so any slice is studyable:
  rotation::<Rotation>           the shelf / clerkship the card came from
  system::<OrganSystem>          NBME organ-system axis
  discipline::<BasicScience>     path / physio / pharm / micro(::bacteria) / nutrition ...

Every card also keeps:
  cluster::<name>   stable identity (drives the guid — do NOT rename casually)
  weak              flagged from the QLog miss list

As the deck grows: classify each new cluster here. Unclassified clusters fall back
to (Reproductive, Pathology) and print a warning at build time so nothing slips through
untagged. New rotations: pass rotation="Medicine" (etc.) when building that deck/batch.
"""

# --- controlled vocabulary (reference; extend as new rotations/subjects appear) ---
ROTATIONS = [
    "OBGYN", "Medicine", "Surgery", "Pediatrics", "Psychiatry",
    "FamilyMedicine", "Neurology", "EmergencyMedicine",
]
SYSTEMS = [
    "Reproductive", "Endocrine", "Renal_Urinary", "Nervous", "Psychiatric",
    "Heme_Onc", "Cardiovascular", "Pulmonary", "GI", "MSK_Skin", "Multisystem",
]
DISCIPLINES = [
    "Pathology", "Physiology", "Pharmacology",
    "Microbiology", "Microbiology::Bacteria", "Microbiology::Virology",
    "Microbiology::Mycology", "Microbiology::Parasitology",
    "Immunology", "Biochemistry", "Nutrition", "Genetics", "Embryology",
    "Anatomy", "Behavioral_Science", "Biostatistics_Ethics",
]

DEFAULT = ("Reproductive", "Pathology")

# --- per-cluster classification: cluster -> (system(s), discipline(s)) ---
# a value may be a single string or a list when the card genuinely spans axes.
CLUSTER_TAX = {
    # ---- b14 (2026-06-24, UWorld) ----
    "rectovaginal_fistula": ("Reproductive", "Pathology"),
    "ohss": ("Reproductive", "Pathology"),
    "pemphigoid_gestationis": (["Reproductive", "Multisystem"], "Pathology"),
    "functional_hypothalamic_amenorrhea": (["Reproductive", "Psychiatric"], "Pathology"),
    "ecc_conization": ("Reproductive", "Pathology"),
    "influenza_vaccine_pregnancy": ("Multisystem", "Pharmacology"),
    "ca125_adnexal_mass": (["Reproductive", "Heme_Onc"], "Pathology"),
    "abo_incompatibility": (["Reproductive", "Heme_Onc"], "Pathology"),
    "leiomyoma_submucosal_rpl": ("Reproductive", "Pathology"),
    "cervical_stenosis_post_cone": ("Reproductive", "Pathology"),
    "cervical_screening_hiv": ("Reproductive", "Pathology"),
    "aub_under45_biopsy": ("Reproductive", "Pathology"),

    # OB — bleeding / peripartum emergencies
    "abruptio_placentae": ("Reproductive", "Pathology"),
    "abruption_decompression": ("Reproductive", "Pathology"),
    "placenta_previa": ("Reproductive", "Pathology"),
    "vasa_previa": ("Reproductive", "Pathology"),
    "placenta_accreta": ("Reproductive", "Pathology"),
    "uterine_inversion": ("Reproductive", "Pathology"),
    "pph_puerperium": ("Reproductive", "Pathology"),
    "normal_involution_vs_atony": ("Reproductive", "Physiology"),
    "cord_prolapse": ("Reproductive", "Pathology"),
    "amniotic_fluid_embolism": ("Reproductive", "Pathology"),
    "rupture_scheduled_delivery": ("Reproductive", "Pathology"),

    # OB — hypertensive / neuro
    "eclampsia_mimics": (["Reproductive", "Nervous"], "Pathology"),
    "eclampsia_real_vs_migraine": (["Reproductive", "Nervous"], "Pathology"),
    "preeclampsia_severe": ("Reproductive", "Pathology"),
    "preeclampsia_mgmt": ("Reproductive", "Pharmacology"),
    "chronic_htn_pregnancy": ("Reproductive", "Pathology"),
    "chronic_htn_complication": ("Reproductive", "Pathology"),
    "gestational_vs_preeclampsia": ("Reproductive", "Pathology"),
    "magnesium_kidney": ("Reproductive", "Pharmacology"),
    "magnesium_neuroprotection": (["Reproductive", "Nervous"], "Pharmacology"),

    # OB — preterm / labor / tocolysis
    "PPROM": ("Reproductive", ["Pathology", "Microbiology::Bacteria"]),
    "PPROM_management": ("Reproductive", "Pharmacology"),
    "indomethacin_tocolysis": ("Reproductive", "Pharmacology"),
    "tocolytic_choice": ("Reproductive", "Pharmacology"),
    "antenatal_corticosteroids": ("Reproductive", "Pharmacology"),
    "cervical_insufficiency": ("Reproductive", "Pathology"),
    "second_stage_arrest_OVD": ("Reproductive", "Physiology"),
    "labor_arrest_oxytocin": ("Reproductive", "Pharmacology"),
    "malpresentation_preterm": ("Reproductive", "Physiology"),
    "obesity_postterm": ("Reproductive", "Physiology"),
    "postterm_induction": ("Reproductive", "Physiology"),

    # OB — infection
    "GBS_prophylaxis": (["Reproductive", "Multisystem"], ["Pharmacology", "Microbiology::Bacteria"]),
    "chorioamnionitis": (["Reproductive", "Multisystem"], ["Pathology", "Microbiology::Bacteria"]),
    "pyelonephritis_pregnancy": (["Renal_Urinary", "Multisystem"], ["Pathology", "Microbiology::Bacteria"]),

    # OB — heme / immune
    "Rh_kleihauer": (["Reproductive", "Heme_Onc"], ["Pathology", "Immunology"]),
    "rhogam_dosing": (["Reproductive", "Heme_Onc"], "Pharmacology"),
    "vte_pregnancy": (["Reproductive", "Heme_Onc"], "Pharmacology"),

    # OB — liver / GI
    "third_tri_liver": (["Reproductive", "GI"], "Pathology"),
    "ICP": (["Reproductive", "GI"], "Pathology"),

    # OB — endocrine / metabolic / misc physiology
    "GDM": ("Endocrine", ["Pathology", "Pharmacology"]),
    "GDM_screening_sequence": ("Endocrine", "Pathology"),
    "postpartum_thyroiditis": ("Endocrine", "Pathology"),
    "postpartum_thyroiditis_phases": ("Endocrine", "Pathology"),
    "subacute_thyroiditis": ("Endocrine", "Pathology"),
    "wernicke": ("Nervous", ["Nutrition", "Pharmacology"]),
    "sheehan": ("Endocrine", "Pathology"),
    "luteal_placental_shift": ("Reproductive", "Physiology"),
    "pregnancy_dating": ("Reproductive", "Physiology"),
    "twin_chorionicity": ("Reproductive", "Embryology"),

    # OB — demise / communication / psych
    "IUFD": ("Reproductive", ["Pathology", "Biostatistics_Ethics"]),
    "communication_bad_news": ("Psychiatric", "Biostatistics_Ethics"),
    "postpartum_mood": ("Psychiatric", "Pathology"),
    "well_patient_observe": ("Multisystem", "Biostatistics_Ethics"),

    # GYN — repro / endocrine
    "pregnancy_first": ("Reproductive", "Physiology"),
    "galactorrhea_hyperprolactinemia": ("Endocrine", ["Pathology", "Pharmacology"]),
    "POI_POF": (["Reproductive", "Endocrine"], "Pathology"),
    "atrophic_vaginitis_GSM": (["Reproductive", "Renal_Urinary"], "Pathology"),
    "aromatase_deficiency": ("Endocrine", ["Genetics", "Pathology"]),
    "postmenopausal_bleeding": ("Reproductive", "Pathology"),
    "GTD_surveillance": (["Reproductive", "Heme_Onc"], "Pathology"),
    "PCOS_pathophys": ("Endocrine", "Physiology"),
    "progestin_challenge": (["Reproductive", "Endocrine"], "Physiology"),
    "endometrial_ablation": ("Reproductive", "Pharmacology"),
    "endometriosis": ("Reproductive", "Pathology"),
    "infertility_tubal_hsg": ("Reproductive", "Pathology"),

    # b15 (2026-06-28, UWorld) — new content gaps
    "lactational_amenorrhea": (["Reproductive", "Endocrine"], "Physiology"),
    "leiomyoma_menopause_regression": ("Reproductive", "Pathology"),
    "spinal_epidural_abscess": ("Nervous", "Pathology"),
    "tamoxifen_adverse_effects": (["Reproductive", "Heme_Onc"], "Pharmacology"),
    "obstetric_anal_sphincter_injury": (["Reproductive", "GI"], "Pathology"),
    "pseudocyesis": (["Psychiatric", "Reproductive"], "Behavioral_Science"),
    "shoulder_dystocia_simulation": ("Reproductive", "Biostatistics_Ethics"),
    "substituted_judgment": ("Multisystem", "Biostatistics_Ethics"),

    # b16 (2026-06-29, Ora) — new content gaps (real misses only; lucky guesses not carded)
    "complete_mole": (["Reproductive", "Endocrine"], "Pathology"),
    "symptomatic_hyponatremia_3pct": (["Renal_Urinary", "Nervous"], "Physiology"),
    "mullerian_agenesis_mrkh": (["Reproductive", "Endocrine"], "Embryology"),
    "sinusoidal_fhr_anemia": ("Reproductive", "Physiology"),
    "pyelonephritis_persistent_imaging": (["Renal_Urinary", "Reproductive"], "Pathology"),
    "hellp_hemolysis_maha": (["Reproductive", "Heme_Onc"], "Pathology"),
    "neonatal_lupus_heart_block": (["Reproductive", "Cardiovascular"], "Immunology"),
    "interstitial_cystitis": (["Renal_Urinary", "Reproductive"], "Pathology"),
    "tubo_ovarian_abscess": ("Reproductive", "Pathology"),
    "congenital_toxoplasmosis": (["Nervous", "Multisystem"], "Microbiology::Parasitology"),
    "alpha_thalassemia_hydrops": (["Reproductive", "Heme_Onc"], ["Genetics", "Pathology"]),
    "uterine_carcinosarcoma": ("Reproductive", "Pathology"),

    # n1 (2026-06-29, NBME) — card every concept
    "pyelo_pregnancy_urine_culture": (["Renal_Urinary", "Reproductive"], "Pathology"),
    "cyclophosphamide_hemorrhagic_cystitis": ("Renal_Urinary", "Pharmacology"),
    "urge_incontinence_detrusor": ("Renal_Urinary", "Physiology"),
    "ureteral_injury_hysterectomy": (["Renal_Urinary", "Reproductive"], "Anatomy"),
    "pregestational_dm_cardiac": (["Reproductive", "Cardiovascular"], "Pathology"),
    "cf_carrier_screen_partner": ("Reproductive", "Genetics"),
    "rh_prevention_screening": (["Reproductive", "Heme_Onc"], "Pathology"),
    "exercise_pregnancy_no_risk": ("Reproductive", "Physiology"),

    # n2 (2026-06-29, NBME) — diagram-back cards
    "iron_deficiency_pregnancy": (["Reproductive", "Heme_Onc"], "Pathology"),
    "omphalocele_karyotype": ("Reproductive", "Genetics"),
    "missed_abortion": ("Reproductive", "Pathology"),
    "heterotopic_pregnancy": ("Reproductive", "Pathology"),
    "eclampsia_bp_labetalol": (["Reproductive", "Cardiovascular"], "Pharmacology"),
    "fascial_dehiscence": ("Reproductive", "Pathology"),
    "hsv_delivery_mode": ("Reproductive", "Microbiology::Virology"),

    # n3 (2026-06-29, NBME) — diagram-back cards
    "epidural_hypotension_brady": ("Reproductive", "Physiology"),
    "gbs_unknown_preterm": ("Reproductive", "Microbiology"),
    "variable_decel_observe": ("Reproductive", "Physiology"),
    "septic_pelvic_thrombophlebitis": (["Reproductive", "Heme_Onc"], "Pathology"),
    "normal_lochia": ("Reproductive", "Physiology"),
    "sbo_pregnancy_xray": (["GI", "Reproductive"], "Pathology"),
    "carpal_tunnel_pregnancy": (["Nervous", "Reproductive"], "Pathology"),
    "breast_fat_necrosis": ("Reproductive", "Pathology"),

    # n4 (2026-06-29, NBME) — diagram-back cards
    "fibrocystic_breast": ("Reproductive", "Pathology"),
    "palpable_breast_mass_biopsy": ("Reproductive", "Pathology"),
    "pid_site_fallopian": ("Reproductive", "Microbiology"),
    "chlamydia_screening_under25": ("Reproductive", "Microbiology"),
    "sexual_assault_gc_prophylaxis": ("Reproductive", "Pharmacology"),
    "uterine_sarcoma_clinical": ("Reproductive", "Pathology"),
    "vulvar_carcinoma": ("Reproductive", "Pathology"),
    "ovarian_cancer_no_screening": ("Reproductive", "Biostatistics_Ethics"),

    # n5 (2026-06-29, NBME) — diagram-back cards
    "bowel_perforation_laparoscopy": (["GI", "Reproductive"], "Pathology"),
    "lng_iud_endometrial_atrophy": ("Reproductive", "Pharmacology"),
    "hospice_opioid_escalation": ("Multisystem", "Biostatistics_Ethics"),
    "leiomyoma_iud": ("Reproductive", "Pathology"),
    "age_sti_screening": (["Reproductive", "Multisystem"], ["Microbiology::Bacteria", "Biostatistics_Ethics"]),
    "HSIL_colposcopy": ("Reproductive", ["Pathology", "Microbiology::Virology"]),
    "cervical_screening_ages": ("Reproductive", ["Biostatistics_Ethics", "Microbiology::Virology"]),
    "granulosa_cell_tumor": (["Reproductive", "Endocrine"], "Pathology"),
    "androgen_insensitivity": ("Reproductive", "Genetics"),
    "vaginal_foreign_body": ("Reproductive", "Pathology"),
    "mixed_mets": ("Heme_Onc", "Pathology"),
    "cornual_ectopic": ("Reproductive", "Pathology"),
    "ectopic_overcall": ("Reproductive", "Pathology"),
    "ectopic_methotrexate": ("Reproductive", "Pharmacology"),
    "ovarian_torsion_vs_corpus_luteum": ("Reproductive", "Pathology"),
    "breast_differential": ("Reproductive", ["Pathology", "Microbiology::Bacteria"]),
    "cyclic_mastalgia": ("Reproductive", "Pathology"),
    "syphilis_chancre": ("Multisystem", "Microbiology::Bacteria"),
    "pid_fitzhugh": (["Reproductive", "Multisystem"], ["Microbiology::Bacteria", "Pathology"]),
    "migraine_repro": (["Nervous", "Reproductive"], "Pharmacology"),

    # GYN — urinary
    "urinary_leakage": ("Renal_Urinary", "Pathology"),
    "transient_incontinence": ("Renal_Urinary", ["Pathology", "Microbiology::Bacteria"]),
    "endometrial_cells_pap": ("Reproductive", ["Pathology", "Biostatistics_Ethics"]),

    # --- b13 (2026-06-22) new clusters ---
    "prenatal_syphilis_screen": (["Reproductive", "Multisystem"], ["Microbiology::Bacteria", "Biostatistics_Ethics"]),
    "oligohydramnios_term": ("Reproductive", "Physiology"),
    "contraception_vte": (["Reproductive", "Heme_Onc"], "Pharmacology"),
    "postpartum_endometritis": (["Reproductive", "Multisystem"], ["Pathology", "Microbiology::Bacteria"]),
    "femoral_nerve_lithotomy": ("Nervous", "Anatomy"),
    "parvovirus_hydrops": (["Reproductive", "Heme_Onc"], ["Microbiology::Virology", "Pathology"]),
    "birth_injury_facial_palsy": (["Nervous", "Reproductive"], ["Anatomy", "Pathology"]),
    "condyloma_hpv": (["Reproductive", "Multisystem"], ["Microbiology::Virology", "Pharmacology"]),
}

_warned = set()


def _as_list(v):
    return [v] if isinstance(v, str) else list(v)


def tags_for(cluster, rotation="OBGYN", extra=None):
    """Full tag list for a card: cluster + weak + rotation + system(s) + discipline(s) + extra."""
    if cluster in CLUSTER_TAX:
        syss, discs = CLUSTER_TAX[cluster]
    else:
        syss, discs = DEFAULT
        if cluster not in _warned:
            print(f"  [taxonomy] WARNING: '{cluster}' unclassified -> default {DEFAULT}; add it to CLUSTER_TAX")
            _warned.add(cluster)
    tags = [f"cluster::{cluster}", "weak", f"rotation::{rotation}"]
    tags += [f"system::{s}" for s in _as_list(syss)]
    tags += [f"discipline::{d}" for d in _as_list(discs)]
    tags += list(extra or [])
    return tags
