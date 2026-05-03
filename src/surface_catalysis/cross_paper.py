"""Cross-paper operators for surface-catalysis-gaia."""

from gaia.lang import contradiction, equivalence, support

from .paper_mason2003 import (
    prem_linear_mapping,
    prem_benchmark_valid,
    prem_extrapolation_valid,
    root_correction_method,
)
from .paper_s2_findings import (
    gga_failure_origin,
    gga_2pi_too_low,
    gga_back_donation_overestimated,
    co_2pi_mechanism,
    correction_site_reordering,
    hybrid_limitation,
    hybrid_magnitude_nonuniform,
    hybrid_direction_inconsistent,
    correction_reduces_site_spread,
    gga_oxide_error_parallel,
    gga_o2_sie_error,
    gga_oxide_gap_error,
)
from .paper_upstream import (
    pbe_pw91_rpbe_comparison,
    vdw_effect_co,
    vdw_geometry_issues,
    mason_validation_pt_al2o3,
    method_cross_comparison,
    experimental_site_methods,
)

# ============================================================
# DECOMPOSITION 1: gga_failure_origin ≡ causal chain
#   gga_2pi_too_low → gga_back_donation_overestimated
#   together they support the compound claim
# ============================================================

causal_2pi_to_backdonation = support(
    [gga_2pi_too_low],
    gga_back_donation_overestimated,
    reason=(
        "If GGA places the CO 2pi* orbital too low, then — by the "
        "established Blyholder model of CO chemisorption — metal d "
        "electrons can back-donate into the artificially stabilized "
        "2pi* acceptor orbital, causing the back-donation contribution "
        "to the chemisorption bond to be overestimated."
    ),
    prior=0.90,
)

decomp_gga_failure = support(
    [gga_2pi_too_low, gga_back_donation_overestimated],
    gga_failure_origin,
    reason=(
        "The compound claim gga_failure_origin states that GGA places "
        "CO 2pi* too low (captured by gga_2pi_too_low) AND that this "
        "causes spuriously strong back-donation overestimating "
        "chemisorption strength (captured by gga_back_donation_"
        "overestimated). The two atomic claims together capture the "
        "full causal chain asserted by the compound claim."
    ),
    prior=0.85,
)

# ============================================================
# DECOMPOSITION 2: hybrid_limitation ≡ two independent aspects
#   magnitude non-uniformity + direction inconsistency
# ============================================================

decomp_hybrid = support(
    [hybrid_magnitude_nonuniform, hybrid_direction_inconsistent],
    hybrid_limitation,
    reason=(
        "The compound claim hybrid_limitation asserts that hybrid "
        "functionals do NOT produce uniform improvement, which "
        "manifests in two distinct ways: the magnitude of the correction "
        "varies across metals (captured by hybrid_magnitude_nonuniform) "
        "AND the direction of the correction is inconsistent — stronger "
        "binding on Cu but weaker on Pt (captured by "
        "hybrid_direction_inconsistent). Both aspects are required to "
        "fully capture the non-uniformity."
    ),
    prior=0.85,
)

# ============================================================
# DECOMPOSITION 3: gga_oxide_error_parallel ≡ two error sources
#   O2 SIE error + oxide HOMO-LUMO gap error
# ============================================================

decomp_oxide = support(
    [gga_o2_sie_error, gga_oxide_gap_error],
    gga_oxide_error_parallel,
    reason=(
        "The compound claim gga_oxide_error_parallel enumerates two "
        "separate and systematic error sources: the GGA O2 "
        "self-interaction error (captured by gga_o2_sie_error) and "
        "the GGA oxide HOMO-LUMO gap underestimation (captured by "
        "gga_oxide_gap_error). The two atomic claims are independent "
        "and each identifies a distinct physical mechanism for GGA "
        "errors in oxide energetics."
    ),
    prior=0.85,
)

# ============================================================
# Support: physical mechanism explains correction
# ============================================================

support_mechanism = support(
    [gga_failure_origin, co_2pi_mechanism],
    prem_linear_mapping,
    reason=(
        "The physical mechanism identified in gga_failure_origin and "
        "co_2pi_mechanism provides a theoretical justification for the "
        "linear mapping assumed in prem_linear_mapping: GGA places the "
        "CO 2pi* orbital too low due to self-interaction error, which "
        "manifests as an underestimated gas-phase DeltaE_ST and an "
        "overestimated surface chemisorption energy, and the correlation "
        "between these two errors makes a linear correction plausible."
    ),
    prior=0.85,
)

# ============================================================
# Support: correction reduces site spread (validation)
# ============================================================

support_site_reduction = support(
    [correction_reduces_site_spread],
    root_correction_method,
    reason=(
        "The observation that applying the correction systematically "
        "narrows the spread of chemisorption energies across adsorption "
        "sites is a consistency check: a physically meaningful correction "
        "should not introduce random noise but should bring the energies "
        "closer to the true (first-principles benchmark) values."
    ),
    prior=0.60,
)

# ============================================================
# Contradiction: Mason method vs hybrid functional failure
# ============================================================

contradiction_hybrid = contradiction(
    root_correction_method,
    hybrid_limitation,
    prior=0.88,
    reason=(
        "The Mason correction method assumes that the GGA error in CO "
        "chemisorption can be corrected by a single-parameter horizontal "
        "shift in the gas-phase singlet-triplet energy. However, hybrid "
        "functionals (PBE0, HSE03) — which incorporate exact exchange and "
        "should partially correct the singlet-triplet / 2pi* orbital energy "
        "problem — do NOT produce a uniform improvement in CO adsorption "
        "energies across metals: the correction magnitude and even direction "
        "vary with the metal (Cu vs Pt vs Ru). This implies that the "
        "gas-phase-to-surface error mapping is not universal and may depend "
        "on metal-specific factors beyond the singlet-triplet splitting. "
        "| new_question: Is the gas-phase singlet-triplet extrapolation "
        "correction universally applicable across all transition metals, or "
        "does it fail for specific metal substrates where metal d-band "
        "hybridization with CO 2pi* is fundamentally different from the "
        "molecular orbital picture?"
    ),
)

# ============================================================
# Contradiction: site reordering challenges the method's precision
# ============================================================

contradiction_site_ordering = contradiction(
    prem_extrapolation_valid,
    correction_site_reordering,
    prior=0.82,
    reason=(
        "prem_extrapolation_valid assumes the linear relation remains valid "
        "when extrapolated from the GGA range [5.35, 5.84] eV to the CI "
        "target at 6.095 eV. However, the correction changes the energetic "
        "ordering of adsorption sites on the same surface. This site "
        "reordering implies that the correction is sensitive to the "
        "site-specific slope m, and if m varies significantly between "
        "on-top, bridge, and hollow sites on the same metal, then a small "
        "error in m for one site could incorrectly change the predicted "
        "most-stable site. "
        "| new_question: How reliable is the site-specific slope m of the "
        "E_chem vs DeltaE_ST linear relation, and what is the uncertainty "
        "in site preference prediction after applying the Mason correction?"
    ),
)

# ============================================================
# Equivalence: correction broadens to oxide systems
# ============================================================

equiv_oxide_parallel = equivalence(
    gga_failure_origin,
    gga_oxide_error_parallel,
    prior=0.70,
    reason=(
        "Both claims identify GGA self-interaction error in the molecular "
        "(diatomic) reference as a systematic source of error in surface "
        "energetics: gga_failure_origin describes the CO/metal "
        "chemisorption problem via the 2pi* orbital error, while "
        "gga_oxide_error_parallel identifies the same mechanism for O2 "
        "in oxide formation energies and additionally identifies the "
        "HOMO-LUMO gap error in the oxide itself as a second systematic "
        "error source. The two mechanisms are analogous and suggest the "
        "problem is general to GGA descriptions of diatomic adsorbates."
    ),
)

# ============================================================
# Support: Mason method validated on Pt/alpha-Al2O3
# ============================================================

support_validation = support(
    [mason_validation_pt_al2o3],
    root_correction_method,
    reason=(
        "The successful application of the Mason extrapolation "
        "correction to a supported-metal catalyst model "
        "(Pt/alpha-Al2O3), reducing the systematic DFT error to "
        "~0.02 eV, demonstrates that the method works beyond the "
        "ideal single-crystal surfaces used for its original "
        "parameterization, strengthening the case for its practical "
        "utility in more realistic catalyst models."
    ),
    prior=0.70,
)

# ============================================================
# Support: multi-method validation of linear mapping
# ============================================================

support_multi_method = support(
    [method_cross_comparison],
    prem_linear_mapping,
    reason=(
        "The testing of the (DeltaE_ST, E_CO^a) linear correlation "
        "across a much wider range of DeltaE_ST values using diverse "
        "methods (PBE, HSE06, PBE0, HF, CR-CC(2,3)) provides a more "
        "stringent test of the linear-mapping hypothesis than the "
        "original Mason study alone, and the persistence of the "
        "linear relation across this multi-method dataset supports "
        "the generality of the underlying physical mechanism."
    ),
    prior=0.75,
)

# ============================================================
# Contradiction: Mason correction does not address vdW errors
# ============================================================

contradiction_vdw_gap = contradiction(
    root_correction_method,
    vdw_effect_co,
    prior=0.90,
    reason=(
        "The Mason correction addresses only the GGA self-interaction "
        "error in the CO singlet-triplet excitation energy. However, "
        "the vdW contribution to the CO adsorption energy (~116 meV "
        "difference between vdW-DF and PBE at 0.1 ML) represents an "
        "independent, additive source of DFT error of comparable "
        "magnitude. Since the Mason correction does not account for "
        "missing dispersion interactions, its claim to correct the "
        "full DFT-GGA chemisorption energy to a 'first-principles "
        "benchmark' is incomplete — the corrected energy may still "
        "have a systematic error from the neglected vdW contribution. "
        "| new_question: What is the complete list of independent "
        "sources of systematic error in DFT predictions of CO "
        "chemisorption energies, and can a single correction method "
        "address all of them simultaneously?"
    ),
)

# ============================================================
# Contradiction: experiment-theory site comparison is
# methodologically ambiguous
# ============================================================

# ============================================================
# Support: RPBE functional dependence reinforces site-specific
# slope uncertainty
# ============================================================

support_rpbe_uncertainty = support(
    [pbe_pw91_rpbe_comparison],
    correction_site_reordering,
    reason=(
        "The systematic difference between RPBE and PW91/PBE "
        "chemisorption energies (~0.2-0.3 eV) shows that the "
        "adsorption energy depends sensitively on the choice of "
        "GGA functional. Since the Mason correction slope m is "
        "derived from a specific GGA functional's linear fit, the "
        "correction is functional-dependent, and the magnitude of "
        "the correction — and hence the site reordering effect — "
        "will vary with the functional used."
    ),
    prior=0.75,
)

# ============================================================
# Support: vdW geometry issues reinforce vdW contradiction
# ============================================================

support_vdw_geometry = support(
    [vdw_geometry_issues],
    vdw_effect_co,
    reason=(
        "vdw_geometry_issues documents that vdW-inclusive functionals "
        "can alter adsorption geometries compared to both GGA and "
        "experiment, which strengthens vdw_effect_co: the vdW "
        "contribution is not merely a uniform energy shift but "
        "affects the potential-energy surface shape, meaning "
        "it cannot be trivially added to the Mason-corrected GGA "
        "energy as a simple post-hoc correction."
    ),
    prior=0.70,
)

contradiction_experiment_ambiguity = contradiction(
    correction_site_reordering,
    experimental_site_methods,
    prior=0.75,
    reason=(
        "correction_site_reordering asserts that the Mason correction "
        "changes the predicted energetic ordering of adsorption sites, "
        "which is a significant effect that should be experimentally "
        "verifiable. However, experimental_site_methods reveals that "
        "RAIRS and SFG — the two primary experimental techniques for "
        "determining CO adsorption sites — give qualitatively different "
        "coverage dependences. This means the experimental reference "
        "against which DFT site predictions are judged is itself "
        "methodologically uncertain, making it difficult to determine "
        "whether the correction improves or degrades agreement with "
        "experiment. "
        "| new_question: Given the methodological ambiguity in "
        "experimental site determination (RAIRS vs SFG), how can "
        "the accuracy of DFT site-preference predictions — including "
        "post-Mason-correction predictions — be rigorously validated?"
    ),
)
