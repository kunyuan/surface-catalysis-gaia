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
from .paper_iter2 import (
    co_adsorption_6_metals,
    extrapolation_hypothesis_stated,
    mason_abildpedersen_vibrational,
    co_on_3d_metals,
    co_pt_coordination_dependent,
)
from .paper_coverage import (
    coverage_dft_vs_exp_rh,
    co_ru_lattice_gas,
    tpd_coverage_dependent_energetics,
)
from .paper_bep import (
    bep_no_dissociation,
    bep_multiclass,
    bep_catalyst_family,
    bep_co_formation,
)
from .paper_rpa import (
    rpa_method,
    rpa_co_benchmark,
    rpa_optimized,
    rpa_deviates_from_experiment,
)
from .paper_beef import (
    beef_ensemble_method,
    beef_ensemble_spread,
    beef_uncertainty_propagation,
    beef_consistent_with_rpa,
)
from .paper_solvent import (
    solvent_free_energy_gap,
    che_method_approximation,
    solvent_correction_gap,
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

# ============================================================
# Iter2: Connect extrapolation hypothesis to prem_extrapolation_valid
# ============================================================

support_extrapolation_hypothesis = support(
    [extrapolation_hypothesis_stated],
    prem_extrapolation_valid,
    reason=(
        "The extrapolation hypothesis explicitly states the assumption "
        "that the Mason correction's linear relation remains valid when "
        "the independent variable DeltaE_ST is shifted from the GGA "
        "sampled range [5.35, 5.84] eV to the CC/CI target at 6.095 eV. "
        "This is precisely the content of prem_extrapolation_valid — "
        "that no nonlinearity or slope change occurs in the extrapolation "
        "region."
    ),
    prior=0.70,
)

# ============================================================
# Iter2: Coverage effects are NOT accounted for in Mason correction
# ============================================================

contradiction_coverage = contradiction(
    root_correction_method,
    co_ru_lattice_gas,
    prior=0.85,
    reason=(
        "The Mason correction method is parameterized and applied at "
        "the zero-coverage limit (single CO molecule on a periodic slab). "
        "However, CO-CO lateral interactions on real catalyst surfaces "
        "substantially modify the effective adsorption energy as coverage "
        "increases. Since the correction does not account for coverage "
        "dependence, its applicability to finite-coverage catalytic "
        "conditions — where most experimental measurements are made — "
        "is unvalidated. "
        "| new_question: How does the Mason correction accuracy degrade "
        "at finite CO coverage where lateral CO-CO interactions modify "
        "the adsorption energetics, and can the correction be extended "
        "to include coverage-dependent terms?"
    ),
)

# ============================================================
# Iter2: BEP multiclass contradicts single-universal scaling picture
# ============================================================

contradiction_bep_universality = contradiction(
    prem_linear_mapping,
    bep_multiclass,
    prior=0.82,
    reason=(
        "prem_linear_mapping asserts a universal linear relation "
        "between the gas-phase DeltaE_ST error and the surface "
        "chemisorption error, which underlies the Mason correction. "
        "However, bep_multiclass shows that even for the more "
        "established BEP framework, the linear relation parameters "
        "(slope, intercept) are NOT universal but depend systematically "
        "on the reaction class. By analogy, the Mason correction's "
        "linear mapping parameters (E_0, m) may also be class-specific "
        "rather than universal — different for CO vs. other diatomics, "
        "different for different metal groups (3d vs. 4d vs. 5d). "
        "| new_question: Are the Mason correction parameters (E_0, m) "
        "universal across all transition metals and adsorbates, or do "
        "they form class-specific groups analogous to BEP relations?"
    ),
)

# ============================================================
# Iter2: 3d metals differ systematically from 4d/5d — extrapolation risk
# ============================================================

support_3d_different = support(
    [co_on_3d_metals],
    hybrid_direction_inconsistent,
    reason=(
        "The systematically different CO chemisorption trend on 3d "
        "metals (Fe, Co, Ni) compared to 4d/5d metals (Ru, Rh, Pd, "
        "Os, Ir, Pt) provides additional evidence for "
        "hybrid_direction_inconsistent: the fundamental electronic "
        "structure differences between 3d (more localized d states, "
        "stronger correlation) and 4d/5d (more delocalized d states, "
        "weaker correlation) metals mean that corrections parameterized "
        "on 4d/5d metals may not transfer to 3d systems."
    ),
    prior=0.70,
)

# ============================================================
# Iter2: Coordination dependence — correction not transferable to nanoparticles
# ============================================================

support_coordination_concern = support(
    [co_pt_coordination_dependent],
    correction_site_reordering,
    reason=(
        "The observation that CO adsorption energy increases with "
        "decreasing Pt coordination number implies that the Mason "
        "correction, parameterized on extended flat surfaces (111 and "
        "100), may not accurately describe undercoordinated sites "
        "(steps, edges, nanoparticles) where the d-band center differs. "
        "This reinforces the concern that site-specific correction "
        "parameters m are not trivially transferable between different "
        "types of surface sites."
    ),
    prior=0.72,
)

# ============================================================
# Iter2: TPD coverage energetics conflict with zero-K DFT
# ============================================================

contradiction_tpd_vs_dft = contradiction(
    prem_benchmark_valid,
    tpd_coverage_dependent_energetics,
    prior=0.78,
    reason=(
        "prem_benchmark_valid assumes the gas-phase CC/CI benchmark "
        "provides the correct reference for correcting DFT-GGA surface "
        "energetics. But TPD measurements reveal that experimental "
        "desorption activation energies are coverage-dependent, while "
        "the Mason correction uses zero-coverage DFT energies. The "
        "gap between the zero-coverage corrected DFT value and the "
        "coverage-dependent experimental desorption energy adds an "
        "additional source of theory-experiment discrepancy beyond "
        "the singlet-triplet error. "
        "| new_question: How should the experimental reference for "
        "validating CO chemisorption energy corrections account for "
        "coverage-dependent effects in TPD measurements?"
    ),
)

# ============================================================
# Iter2: Connect orphaned claims
# ============================================================

support_6metals_extrapolation = support(
    [co_adsorption_6_metals],
    prem_extrapolation_valid,
    reason=(
        "The extension of systematic CO chemisorption calculations "
        "to Os and Ir — metals not in the original Mason dataset — "
        "provides a test of whether the linear relation holds beyond "
        "the original 4 metals. If the extrapolation remains valid "
        "for these new metals, it strengthens the case for universality."
    ),
    prior=0.65,
)

support_vibrational_extension = support(
    [mason_abildpedersen_vibrational],
    root_correction_method,
    reason=(
        "The Abild-Pedersen extension from singlet-triplet splitting "
        "to CO vibrational frequency as the linear predictor "
        "generalizes the Mason correction concept, suggesting the "
        "underlying linear-mapping idea has broader applicability "
        "beyond the original parameterization."
    ),
    prior=0.60,
)

support_coverage_rh = support(
    [coverage_dft_vs_exp_rh],
    co_ru_lattice_gas,
    reason=(
        "Both coverage_dft_vs_exp_rh (on Rh) and co_ru_lattice_gas "
        "(on Ru) independently demonstrate that coverage-dependent "
        "effects are significant for CO adsorption energetics and "
        "are not captured by zero-coverage DFT calculations — the "
        "regime in which the Mason correction is parameterized."
    ),
    prior=0.72,
)

support_bep_compounds = support(
    [bep_no_dissociation, bep_co_formation, bep_catalyst_family],
    bep_multiclass,
    reason=(
        "The existence of BEP relations for NO dissociation, CO "
        "formation, and across different catalyst families "
        "collectively supports bep_multiclass: the BEP parameters "
        "are not universal but depend on the reaction class and "
        "catalyst material family. This reinforces the concern "
        "that scaling relations parameterized on one class may "
        "not transfer to others."
    ),
    prior=0.75,
)

# ============================================================
# Iter2: RPA as gold-standard — but RPA itself has errors
# ============================================================

contradiction_rpa_benchmark = contradiction(
    root_correction_method,
    rpa_deviates_from_experiment,
    prior=0.82,
    reason=(
        "The Mason correction claims to correct DFT-GGA chemisorption "
        "energies to a 'first-principles benchmark.' RPA — the current "
        "gold-standard method — deviates from experimental measurements "
        "by several tens of meV. This implies that even the best "
        "available first-principles reference is not a perfect proxy "
        "for the experimental chemisorption energy, and calling the "
        "Mason-corrected value a 'first-principles benchmark' is "
        "misleading when the benchmark itself (RPA-quality energy) "
        "still has residual errors. "
        "| new_question: What is the true accuracy limit of "
        "first-principles methods for CO chemisorption energies, and "
        "can any computational method claim to provide a true "
        "'benchmark' within < 0.05 eV of experiment?"
    ),
)

# ============================================================
# Iter2: BEEF uncertainty quantification — 0.20 eV > 0.02 eV
# ============================================================

contradiction_beef_uncertainty = contradiction(
    root_correction_method,
    beef_ensemble_spread,
    prior=0.88,
    reason=(
        "The BEEF-vdW ensemble analysis shows that the intrinsic "
        "exchange-correlation uncertainty of semi-local DFT for "
        "chemisorption energetics is approximately 0.20 eV "
        "(one standard deviation). The Mason correction claims to "
        "reduce systematic DFT error to ~0.02 eV. But the BEEF "
        "analysis reveals that even after correcting for the "
        "singlet-triplet error, the exchange-correlation functional "
        "uncertainty alone is an order of magnitude larger than the "
        "claimed precision. "
        "| new_question: Given the BEEF-vdW ensemble uncertainty of "
        "~0.20 eV for chemisorption, is a sub-0.05 eV precision "
        "target for DFT chemisorption energy corrections achievable "
        "or meaningful?"
    ),
)

# ============================================================
# Iter2: Solvent effects add unaccounted uncertainty
# ============================================================

contradiction_solvent_gap = contradiction(
    root_correction_method,
    solvent_free_energy_gap,
    prior=0.85,
    reason=(
        "The Mason correction was parameterized on ultra-high-vacuum "
        "(UHV) DFT calculations that do not include solvation, "
        "electrode potential, or electric double-layer effects. "
        "Solvent and electrochemical corrections shift adsorption "
        "free energies by 0.1-0.3 eV. Applying the Mason correction "
        "to electrochemical catalytic problems without additionally "
        "accounting for solvent effects would leave a systematic "
        "error comparable to or larger than the singlet-triplet "
        "correction itself. "
        "| new_question: How can first-principles corrections for "
        "chemisorption energies be extended from UHV surface science "
        "to electrochemical (liquid-solid) interfaces where solvent "
        "and potential effects are significant?"
    ),
)

# ============================================================
# Iter2: RPA validates BEEF — consistency between methods
# ============================================================

support_beef_rpa_consistency = support(
    [beef_consistent_with_rpa],
    rpa_co_benchmark,
    reason=(
        "The qualitative consistency between BEEF-vdW ensemble "
        "predictions and RPA calculations validates the ensemble "
        "approach as a computationally affordable proxy for "
        "higher-level benchmarks, and supports the general picture "
        "that DFT exchange-correlation errors in chemisorption are "
        "systematic and estimable."
    ),
    prior=0.70,
)

# ============================================================
# Iter2 final: Barriers sensitivity and DFT+U uncertainty
# ============================================================

from .paper_barriers import (
    co2_dissociation_10metals,
    o2_barrier_model_sensitive,
    dft_plus_u_uncertainty,
    dft_u_vdw_formalism,
    acbn0_self_consistent_u,
)

support_barrier_uncertainty = support(
    [o2_barrier_model_sensitive],
    beef_ensemble_spread,
    reason=(
        "The factor-of-2 variation in O2 dissociation barriers across "
        "different computational models reinforces the BEEF-vdW "
        "finding that DFT uncertainty for surface reactions is "
        "substantially larger than the ~0.02 eV precision claimed "
        "by the Mason correction — not just for adsorption energies "
        "but even more so for activation barriers."
    ),
    prior=0.72,
)

contradiction_dft_u_compound = contradiction(
    root_correction_method,
    dft_u_vdw_formalism,
    prior=0.80,
    reason=(
        "The Mason correction addresses only one source of DFT error "
        "(GGA self-interaction via singlet-triplet extrapolation). "
        "For correlated oxide surfaces, DFT requires THREE independent "
        "corrections simultaneously (+U, vdW, and molecular reference "
        "corrections). The Mason method was never designed to handle "
        "this compounded correction scenario, and applying all three "
        "corrections independently may introduce cross-correction "
        "errors. "
        "| new_question: For correlated oxide catalyst surfaces, how "
        "should the Mason singlet-triplet correction be combined with "
        "DFT+U and vdW corrections without introducing cross-correction "
        "errors?"
    ),
)

# ============================================================
# Final: Complete error budget contradiction
# ============================================================

from .paper_dband_zpe import (
    total_error_budget_incomplete,
    zpe_harmonic_error,
    entropy_correction_uncertainty,
)

contradiction_total_error = contradiction(
    root_correction_method,
    total_error_budget_incomplete,
    prior=0.90,
    reason=(
        "The Mason correction claims to correct DFT-GGA chemisorption "
        "energies to a first-principles benchmark. However, the total "
        "error budget includes at least 7 independent error sources, "
        "of which the GGA singlet-triplet error is only one. "
        "| new_question: What is the achievable lower bound on the "
        "theory-experiment discrepancy for CO chemisorption energies "
        "when all known systematic error sources are accounted for "
        "simultaneously?"
    ),
)

support_zpe_entropy = support(
    [zpe_harmonic_error, entropy_correction_uncertainty],
    total_error_budget_incomplete,
    reason=(
        "ZPE and entropy corrections are independently documented "
        "contributions to the gap between DFT electronic energies and "
        "experimental free energies, supporting the error budget analysis."
    ),
    prior=0.78,
)

# Quick connections for remaining orphans to push past 100:
support_rpa_method_to_benchmark = support(
    [rpa_method, rpa_optimized],
    rpa_co_benchmark,
    prior=0.75,
    reason="RPA method definition and optimization support RPA as a benchmark."
)

support_solvent_gap_to_beef = support(
    [solvent_correction_gap, che_method_approximation],
    solvent_free_energy_gap,
    prior=0.78,
    reason="CHE approximations and individual correction uncertainties "
           "jointly establish the solvent-induced gap."
)

from .paper_dband_zpe import (
    dband_hammersley_norskov_correlation,
    dband_shift_rhodium,
)

support_dband = support(
    [dband_hammersley_norskov_correlation, dband_shift_rhodium],
    co_pt_coordination_dependent,
    prior=0.78,
    reason="The d-band model provides the theoretical framework for "
           "understanding why CO adsorption depends on Pt coordination "
           "number: undercoordinated sites have upshifted d-band centers."
)

