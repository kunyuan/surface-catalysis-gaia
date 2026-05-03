from .paper_mason2003 import (
    prem_linear_mapping,
    prem_benchmark_valid,
    prem_extrapolation_valid,
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

PRIORS = {
    # Decomposed atomic claims — gga_failure_origin
    gga_2pi_too_low: (
        0.88,
        "The GGA self-interaction error placing CO 2pi* too low is a robust, "
        "well-characterized electronic-structure finding confirmed by direct "
        "comparison of GGA orbital energies with GW and hybrid functional "
        "calculations across multiple transition metals."
    ),
    gga_back_donation_overestimated: (
        0.82,
        "The causal link from 2pi* too low → overestimated back-donation is "
        "supported by the Blyholder model and charge-decomposition analysis, "
        "though the quantitative contribution of back-donation relative to "
        "sigma-donation varies by metal and adsorption site."
    ),
    # Decomposed atomic claims — hybrid_limitation
    hybrid_magnitude_nonuniform: (
        0.82,
        "The metal-dependent magnitude of the hybrid correction (Cu ~0.2 eV, "
        "Pt ~0.4 eV, Ru ~0.25-0.45 eV) is directly computed and reported in "
        "systematic DFT studies comparing GGA to hybrid functionals."
    ),
    hybrid_direction_inconsistent: (
        0.78,
        "The direction reversal between Cu and Pt is a computed finding but "
        "could partly depend on the reference experimental data used for "
        "comparison and on the specific hybrid mixing parameter."
    ),
    # Decomposed atomic claims — gga_oxide_error_parallel
    gga_o2_sie_error: (
        0.80,
        "The O2 self-interaction error in GGA is a well-established analogue "
        "of the CO singlet-triplet error; both arise from GGA's incorrect "
        "description of frontier orbital gaps in diatomic molecules."
    ),
    gga_oxide_gap_error: (
        0.75,
        "GGA underestimation of oxide HOMO-LUMO gaps is well-documented but "
        "the quantitative contribution of this error to oxidation energies "
        "relative to the O2 reference error is less well characterized."
    ),
    # Mason et al. premises
    prem_linear_mapping: (
        0.80,
        "Linear relation between chemisorption energy and gas-phase singlet-triplet "
        "splitting is a physically motivated but empirically tested assumption; "
        "supported by DFT-GGA data over [5.35, 5.84] eV for several metal surfaces."
    ),
    prem_benchmark_valid: (
        0.75,
        "CC/CI benchmark value 6.095 eV is accurate for gas-phase CO, but the "
        "assumption that environmental effects do not substantially shift the "
        "required reference energy in the chemisorbed geometry is a significant "
        "approximation that needs experimental validation."
    ),
    prem_extrapolation_valid: (
        0.70,
        "Linear extrapolation from [5.35, 5.84] eV to 6.095 eV is a modest ~4% "
        "extrapolation beyond the sampled range, but the absence of nonlinearity "
        "in this region is an assumption that depends on the specific functional "
        "and pseudopotential used."
    ),
    # S2 findings — independent claims
    gga_failure_origin: (
        0.85,
        "GGA self-interaction error placing CO 2pi* too low is a well-documented "
        "and physically well-understood mechanism; confirmed by multiple studies "
        "across different GGA functionals and metal substrates."
    ),
    co_2pi_mechanism: (
        0.82,
        "The relationship between gas-phase DeltaE_ST, 2pi* orbital position "
        "relative to Fermi level, and surface chemisorption error is supported "
        "by electronic structure analysis across late transition metals."
    ),
    correction_site_reordering: (
        0.78,
        "Site reordering after correction is directly observed in the application "
        "of the Mason method to Pt, Rh, Pd, Cu surfaces; the effect is real but "
        "its physical correctness depends on the accuracy of site-specific m values."
    ),
    hybrid_limitation: (
        0.80,
        "Multiple systematic DFT studies confirm that hybrid functionals do not "
        "uniformly improve adsorption energies; the metal-dependent behavior is a "
        "robust finding reflecting fundamental limitations of single-determinant "
        "DFT for chemisorption."
    ),
    correction_reduces_site_spread: (
        0.65,
        "The narrowing of site-energy spread is a plausible consistency check but "
        "does not independently validate the correction; a wrong correction could "
        "also spuriously reduce spread."
    ),
    gga_oxide_error_parallel: (
        0.80,
        "The parallel between CO/metal and O2/oxide GGA errors is well-established; "
        "both arise from GGA's incorrect description of the frontier orbital gap "
        "in diatomic molecules, suggesting a generic GGA deficiency."
    ),
    # Upstream findings
    pbe_pw91_rpbe_comparison: (
        0.75,
        "PBE and PW91 give similar chemisorption energies while RPBE gives "
        "systematically weaker binding; this is a well-known functional trend "
        "but the magnitude depends on the specific adsorbate and metal."
    ),
    vdw_effect_co: (
        0.82,
        "The ~116 meV vdW contribution to CO adsorption is a well-established "
        "finding; dispersion interactions are significant for molecular "
        "adsorbates and are not captured by semi-local GGA functionals."
    ),
    vdw_geometry_issues: (
        0.70,
        "The observation that vdW-inclusive functionals can alter adsorption "
        "geometries is documented but the magnitude and system-dependence of "
        "the effect requires further systematic study."
    ),
    mason_validation_pt_al2o3: (
        0.65,
        "The validation on Pt/alpha-Al2O3 is a promising demonstration but "
        "a single validation case does not establish universal applicability; "
        "the ~0.02 eV uncertainty claim should be tested on other supported "
        "catalyst systems."
    ),
    method_cross_comparison: (
        0.72,
        "Multi-method testing of the linear mapping hypothesis across a wide "
        "range of DeltaE_ST values provides stronger evidence than the original "
        "single-functional study, but the Pd-only focus limits generalizability "
        "to other metals."
    ),
    experimental_site_methods: (
        0.78,
        "RAIRS and SFG are established techniques for CO site determination, "
        "and the observation that they give method-dependent coverage "
        "dependences is a documented experimental subtlety that complicates "
        "direct comparison between theory and experiment."
    ),
}
