"""Iteration 2: Expanded metal set, correction hypothesis, and validation."""

from gaia.lang import claim

# ============================================================
# CO adsorption on 6 group-VIII 4d/5d metals — extends beyond original Mason set
# ============================================================

co_adsorption_6_metals = claim(
    "For CO adsorption on the most favorable close-packed sites of "
    "group-VIII 4d/5d metal surfaces — Ru(0001), Rh(111), Pd(111), "
    "Os(0001), Ir(111), and Pt(111) — DFT total-energy calculations "
    "with the RPBE functional (Dmol3 code, double-numeric-plus-polarization "
    "basis) yield a consistent set of chemisorption energies, extending "
    "the Mason correction's original Pt/Rh/Pd/Cu dataset to include "
    "Os and Ir surfaces for the first systematic comparison.",
    lkm_id="gcn_52fcedda87c64878",
    provenance_source="lkm",
)

# ============================================================
# The extrapolation hypothesis — directly about prem_extrapolation_valid
# ============================================================

extrapolation_hypothesis_stated = claim(
    "The hypothesis underlying the Mason extrapolation correction is "
    "that a single horizontal shift in the gas-phase CO singlet-triplet "
    "excitation energy — replacing the DFT-GGA value DeltaE_ST^GGA by "
    "the high-level CC/CI reference DeltaE_ST^CI — combined with "
    "site-and-facet-specific slopes m derived from DFT-GGA sampling "
    "over [5.35, 5.84] eV, provides an accurate correction to the "
    "DFT-GGA chemisorption energy even though the correction extrapolates "
    "beyond the sampled range to 6.095 eV.",
    lkm_id="gcn_ee3ed147a9014ec8",
    provenance_source="lkm",
)

# ============================================================
# Mason/Abild-Pedersen vibrational correction extension
# ============================================================

mason_abildpedersen_vibrational = claim(
    "The Mason/Abild-Pedersen linear adsorption-energy correction takes "
    "the form DeltaE = A - B * nu_CO, where nu_CO is the computed DFT "
    "CO stretching frequency (in cm^-1) and B = 0.0008 eV·cm is a "
    "universal slope parameter adopted from the literature, with the "
    "intercept A fitted for the PBE functional — this extends the "
    "original Mason correction from singlet-triplet splitting to "
    "vibrational frequency as the linear predictor.",
    lkm_id="gcn_f91a8f8303904ff5",
    provenance_source="lkm",
)

# ============================================================
# CO on extended metal set — single-atom catalysts
# ============================================================

co_on_single_atom_11metals = claim(
    "For CO oxidation on single-atom catalysts consisting of one "
    "transition-metal atom M embedded in a support, DFT calculations "
    "of CO adsorption energies and activation barriers were performed "
    "for M = Fe, Co, Ni, Cu, Ru, Rh, Pd, Ag, Os, Ir, Pt — covering "
    "all three rows of group-VIII and group-IB transition metals and "
    "extending CO chemisorption energetics comparisons far beyond "
    "the original Mason method's 4-metal (Pt/Rh/Pd/Cu) parameterization.",
    lkm_id="gcn_672c8eb10ce44b73",
    provenance_source="lkm",
)

# ============================================================
# CO on Fe, Co, Ni — 3d metals not in original Mason set
# ============================================================

co_on_3d_metals = claim(
    "The computed per-metal scalar bonding parameters for group-VIII "
    "metals evaluated from DFT calculations — reported as A * 10^2 "
    "values — are: Fe 11.47, Co 14.19, Ni 15.99, indicating that "
    "CO chemisorption energetics on the 3d series (Fe, Co, Ni) follow "
    "a systematically different trend from the 4d/5d metals (Ru, Rh, "
    "Pd, Os, Ir, Pt) that were the focus of the original Mason "
    "correction method.",
    lkm_id="gcn_143b83513dc148ca",
    provenance_source="lkm",
)

# ============================================================
# CO adsorption on Pt coordination-dependent
# ============================================================

co_pt_coordination_dependent = claim(
    "The DFT-computed trend of increasing CO chemisorption energy "
    "with decreasing local Pt coordination number is correlated with "
    "the local electronic structure: as the mean nearest-neighbor Pt "
    "coordination number n of a surface Pt atom is reduced, the "
    "center of the Pt d-band shifts toward the Fermi level, increasing "
    "the CO adsorption strength — this implies that the Mason correction "
    "parameterized on flat (111) and (100) surfaces may not transfer "
    "directly to undercoordinated step, edge, or nanoparticle sites.",
    lkm_id="gcn_adefb8887eef41e2",
    provenance_source="lkm",
)
