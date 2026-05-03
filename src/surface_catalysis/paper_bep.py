"""BEP scaling relations — universality and limitations across reaction classes."""

from gaia.lang import claim

# ============================================================
# BEP for NO dissociation — extends beyond CO
# ============================================================

bep_no_dissociation = claim(
    "A Brønsted-Evans-Polanyi (BEP)-type linear relation between "
    "activation energy E_a = E_TS - E_slab - E_NO_gas and coadsorption "
    "energy E_coads = E_(N+O):slab - E_slab - E_NO_gas was obtained "
    "by linear regression on four computed data points for NO "
    "dissociation on transition metal surfaces, extending the BEP "
    "framework from CO-related reactions to NO activation.",
    lkm_id="gcn_6c6da7019b224972",
    provenance_source="lkm",
)

# ============================================================
# Multi-class BEP — not a single universal line
# ============================================================

bep_multiclass = claim(
    "Multiple well-resolved empirical linear BEP relationships — an "
    "overall average line plus class-specific lines for Classes I-III "
    "— have been identified for elementary surface dissociation "
    "reactions, meaning that the slope alpha_BEP and intercept beta_BEP "
    "are not universal but depend systematically on the reaction class "
    "(e.g., diatomic dissociation vs. C-H vs. O-H bond breaking).",
    lkm_id="gcn_d5ae469fc8ef4ebc",
    provenance_source="lkm",
)

# ============================================================
# BEP universality across catalyst families
# ============================================================

bep_catalyst_family = claim(
    "For a reaction pathway decomposed into N elementary steps on "
    "catalysts j chosen from a family of analogous materials, the "
    "activation energy of each step k on catalyst j is correlated "
    "with the reaction energy of that step via a BEP relation — "
    "but the BEP parameters (slope, intercept) may differ between "
    "catalyst families (e.g., metals vs. oxides vs. sulfides), "
    "limiting the transferability of BEP relations parameterized "
    "on one class of materials to another.",
    lkm_id="gcn_39909864d20f4830",
    provenance_source="lkm",
)

# ============================================================
# BEP for CO formation from C+O
# ============================================================

bep_co_formation = claim(
    "For the elementary reaction class of CO formation from adsorbed "
    "C and O on transition metal surfaces, the electronic activation "
    "energy DeltaE_Act (transition-state electronic energy relative "
    "to the coadsorbed C+O initial state) scales approximately linearly "
    "with the reaction energy of the C+O -> CO step via a BEP relation, "
    "connecting the CO dissociation/formation energetics — a key "
    "catalytic descriptor — to a single DFT-computed reaction energy.",
    lkm_id="gcn_2aa99d023c334b83",
    provenance_source="lkm",
)
