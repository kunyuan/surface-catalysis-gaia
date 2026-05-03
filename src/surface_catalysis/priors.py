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
from .paper_dband_zpe import (
    dband_hammersley_norskov_correlation,
    dband_shift_rhodium,
    zpe_harmonic_error,
    entropy_correction_uncertainty,
    total_error_budget_incomplete,
)
from .paper_barriers import (
    co2_dissociation_10metals,
    o2_barrier_model_sensitive,
    dft_plus_u_uncertainty,
    dft_u_vdw_formalism,
    acbn0_self_consistent_u,
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
    # Iter2 — expanded metal set, coverage, BEP
    co_adsorption_6_metals: (
        0.78,
        "DFT calculations on 6 group-VIII metals using consistent methodology "
        "provide a reliable dataset; the inclusion of Os and Ir extends the "
        "original Mason parameterization but the use of a single functional "
        "(RPBE) limits generalizability."
    ),
    extrapolation_hypothesis_stated: (
        0.65,
        "The extrapolation hypothesis is clearly stated in the literature but "
        "has not been independently tested across a systematic range of metals "
        "and functionals; the assumption of linearity beyond the sampled region "
        "is the core weakness."
    ),
    mason_abildpedersen_vibrational: (
        0.68,
        "Extending the Mason correction to CO vibrational frequency as the "
        "linear predictor is a creative generalization, but the universal "
        "slope B = 0.0008 eV·cm has only been validated on a limited set of "
        "systems."
    ),
    co_on_3d_metals: (
        0.72,
        "The different CO chemisorption trend on 3d metals is a plausible "
        "finding consistent with d-band theory, but the bonding parameter "
        "values are from a single computational study."
    ),
    co_pt_coordination_dependent: (
        0.80,
        "The coordination-dependence of CO adsorption energy on Pt is "
        "well-established by DFT and consistent with d-band center theory; "
        "the implication for Mason correction transferability is real."
    ),
    coverage_dft_vs_exp_rh: (
        0.75,
        "The discrepancy between DFT-computed and experimental coverage "
        "dependence on Rh(111) is a documented finding but may depend on "
        "the specific functional and coverage model used."
    ),
    co_ru_lattice_gas: (
        0.78,
        "Lattice-gas models with DFT lateral interactions for CO/Ru(0001) "
        "are a well-established approach, and the importance of CO-CO "
        "interactions for coverage-dependent energetics is well-known."
    ),
    tpd_coverage_dependent_energetics: (
        0.82,
        "TPD is a mature experimental technique and the coverage-dependence "
        "of desorption energies is experimentally well-documented; the gap "
        "between zero-coverage DFT and finite-coverage experiment is a "
        "recognized issue in surface science."
    ),
    bep_no_dissociation: (
        0.70,
        "A BEP relation for NO dissociation on only four data points is "
        "suggestive but not statistically robust; needs validation on a "
        "larger dataset across more metals."
    ),
    bep_multiclass: (
        0.82,
        "The existence of class-specific BEP relations is well-documented "
        "in the literature; the non-universality of BEP parameters is a "
        "key insight for understanding the limits of scaling relations."
    ),
    bep_catalyst_family: (
        0.78,
        "The catalyst-family dependence of BEP parameters is a logical "
        "extension of the multi-class BEP concept but has not been "
        "systematically quantified across a wide range of materials classes."
    ),
    bep_co_formation: (
        0.74,
        "BEP for CO formation from C+O is a specific reaction class with "
        "moderate evidence; the linear scaling between activation energy "
        "and reaction energy for this step is supported by DFT calculations."
    ),
    # Iter2 — RPA, BEEF, solvent
    rpa_method: (
        0.85,
        "EXX+RPA@PBE is a well-established computational protocol; "
        "the method is systematically improvable and provides the "
        "current gold-standard for surface adsorption energetics."
    ),
    rpa_co_benchmark: (
        0.78,
        "RPA is demonstrably more accurate than GGA for CO chemisorption, "
        "but RPA calculations for surface adsorption are computationally "
        "expensive and limited to a small number of benchmark systems."
    ),
    rpa_optimized: (
        0.72,
        "The empirical factor 1.17 in optRPA is fitted to a limited "
        "dataset; its transferability to chemisorption systems is "
        "not systematically validated."
    ),
    rpa_deviates_from_experiment: (
        0.75,
        "The residual RPA error of several tens of meV is documented "
        "from benchmark dataset comparisons; this represents the current "
        "practical accuracy limit of first-principles surface energetics."
    ),
    beef_ensemble_method: (
        0.82,
        "BEEF-vdW ensemble method is well-established and published; "
        "the 2000-member ensemble approach is a standard tool for "
        "DFT error estimation in the surface catalysis community."
    ),
    beef_ensemble_spread: (
        0.80,
        "The ~0.20 eV ensemble spread for binding energies is a "
        "representative value for typical chemisorption systems; "
        "the exact value depends on the specific system and property."
    ),
    beef_uncertainty_propagation: (
        0.78,
        "BEEF ensemble uncertainty propagation is a general method; "
        "the nonlinear propagation of exchange-correlation errors into "
        "catalytic rates is an active research area."
    ),
    beef_consistent_with_rpa: (
        0.72,
        "BEEF-vdW consistency with RPA is a validation point but the "
        "comparison has only been made for a limited set of systems."
    ),
    solvent_free_energy_gap: (
        0.80,
        "Solvent effects of 0.1-0.3 eV are well-documented in "
        "electrocatalysis literature; the gap between UHV DFT and "
        "electrochemical conditions is a recognized challenge."
    ),
    che_method_approximation: (
        0.82,
        "The computational hydrogen electrode is the standard method "
        "in computational electrocatalysis; its limitations are "
        "well-characterized and its typical uncertainty of ~0.1-0.3 eV "
        "is accepted in the field."
    ),
    solvent_correction_gap: (
        0.76,
        "Each correction term (ZPE, entropy, solvation, potential) "
        "carries independent uncertainties that compound; the total "
        "uncertainty is likely larger than individual contributions."
    ),
    # Iter2 final — barriers and DFT+U
    co2_dissociation_10metals: (
        0.74,
        "DFT barriers for CO2 dissociation on 10 metals provide a "
        "useful benchmark dataset; the functional-sensitivity of "
        "barriers is well-known but the specific error magnitudes "
        "are less systematically characterized than for adsorption energies."
    ),
    o2_barrier_model_sensitive: (
        0.76,
        "The model-sensitivity of O2 dissociation barriers is a known "
        "issue in computational catalysis; barrier errors exceeding "
        "0.5 eV due to model choice are documented across multiple systems."
    ),
    dft_plus_u_uncertainty: (
        0.78,
        "The U_eff parameter dependence of DFT+U adsorption energies "
        "is well-documented; the optimal U value is system-dependent "
        "and introduces an additional source of functional uncertainty."
    ),
    dft_u_vdw_formalism: (
        0.72,
        "Combining +U, vdW, and molecular reference corrections is a "
        "practical necessity for oxide catalysts but the cross-correction "
        "errors have not been systematically quantified."
    ),
    acbn0_self_consistent_u: (
        0.70,
        "Self-consistent Hubbard U from ACBN0 removes empiricism but "
        "the computed U values still depend on the underlying functional; "
        "this is an improvement over empirical U but not a complete solution."
    ),
    # Final layer — d-band and ZPE
    dband_hammersley_norskov_correlation: (
        0.85,
        "The Hammer-Norskov d-band model is one of the most well-established "
        "concepts in computational surface catalysis, but its quantitative "
        "limitations are increasingly recognized."
    ),
    dband_shift_rhodium: (
        0.78,
        "The d-band shift correlation for Rh is consistent with the HN model "
        "but the metal-specific coupling matrix element introduces deviations "
        "from a universal scaling relation."
    ),
    zpe_harmonic_error: (
        0.74,
        "Harmonic ZPE errors of 0.05-0.1 eV are a systematic uncertainty "
        "in DFT-based adsorption free energies; anharmonic effects are "
        "typically neglected due to computational cost."
    ),
    entropy_correction_uncertainty: (
        0.72,
        "The hindered translator/rotator approximation for adsorbate entropy "
        "is a recognized source of error, particularly for weakly bound "
        "molecules where the harmonic oscillator model is inaccurate."
    ),
    total_error_budget_incomplete: (
        0.88,
        "The enumeration of independent error sources in DFT-experiment "
        "comparison is a systematic exercise; the conclusion that the Mason "
        "correction addresses only 1 of ~7 error sources is robust."
    ),
}
