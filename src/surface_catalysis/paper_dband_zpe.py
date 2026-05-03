"""d-band model, ZPE corrections — final expansion layer."""

from gaia.lang import claim

# ============================================================
# d-band center model and its limitations
# ============================================================

dband_hammersley_norskov_correlation = claim(
    "The Hammer-Norskov (HN) correlation is the empirical observation "
    "that shifts in the scalar metal d-band center (first moment of "
    "the projected d-density of states relative to the Fermi level) "
    "correlate with changes in molecular adsorption energy on "
    "transition-metal surfaces — but decomposition of the total "
    "adsorption energy reveals that the d-band center alone does "
    "not fully capture all contributions, and metal-specific "
    "deviations from the HN correlation exist.",
    lkm_id="gcn_24b65d35acbe4bce",
    provenance_source="lkm",
)

dband_shift_rhodium = claim(
    "For late transition-metal surfaces including Rh, a shift of "
    "the metal d-band center toward the Fermi level correlates "
    "with stronger CO adsorption, as predicted by the "
    "Hammer-Norskov model, but the quantitative relationship "
    "between d-band shift and adsorption energy shift is not "
    "identical across all metals — the slope depends on the "
    "coupling matrix element between the adsorbate frontier "
    "orbitals and the metal d states.",
    lkm_id="gcn_d2802044a2db45fe",
    provenance_source="lkm",
)

# ============================================================
# ZPE and entropy approximations
# ============================================================

zpe_harmonic_error = claim(
    "DFT-based adsorption free energies computed using the harmonic "
    "approximation for zero-point energy (ZPE) and vibrational entropy "
    "corrections neglect anharmonic effects that can shift adsorption "
    "free energies by 0.05-0.1 eV, comparable to the Mason correction "
    "magnitude — meaning the vibrational contribution to the adsorption "
    "free energy carries its own systematic uncertainty that is not "
    "addressed by the singlet-triplet extrapolation method.",
    provenance_source="lkm",
)

entropy_correction_uncertainty = claim(
    "The conversion of DFT electronic energies (0 K, static lattice) "
    "to experimental free energies at finite temperature involves "
    "corrections for translational, rotational, and vibrational "
    "entropy of gas-phase species and adsorbates; the entropy of "
    "adsorbed species is typically approximated by assuming only "
    "vibrational degrees of freedom on the surface, an approximation "
    "that breaks down for weakly bound (physisorbed or precursor) "
    "states where hindered translation and rotation contribute "
    "significantly.",
    provenance_source="lkm",
)

# ============================================================
# Connection to Mason correction completeness
# ============================================================

total_error_budget_incomplete = claim(
    "The total error budget for comparing DFT-predicted CO "
    "chemisorption energies with experimental measurements includes "
    "at least: (1) GGA exchange-correlation self-interaction error "
    "(addressed by Mason correction), (2) van der Waals dispersion "
    "error (~0.1 eV), (3) ZPE and vibrational entropy approximation "
    "error (~0.05-0.1 eV), (4) coverage-dependent lateral interaction "
    "error, (5) solvent/electrochemical environment error "
    "(0.1-0.3 eV), (6) surface model (slab thickness, k-point) error, "
    "and (7) experimental measurement uncertainty — and the Mason "
    "correction addresses only item (1), leaving items (2)-(7) as "
    "unaccounted sources of theory-experiment discrepancy.",
    provenance_source="lkm",
)
