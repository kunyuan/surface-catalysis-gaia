"""BEEF-vdW Bayesian error estimation — DFT uncertainty quantification."""

from gaia.lang import claim

beef_ensemble_method = claim(
    "The Bayesian Error Estimation Functional with van der Waals "
    "correlation (BEEF-vdW) generates, from a single self-consistent "
    "DFT calculation, a finite ensemble of N = 2000 alternative "
    "exchange-correlation parameterizations that span the space of "
    "plausible semi-local exchange-correlation functionals, providing "
    "a systematic method to estimate the exchange-correlation "
    "contribution to the uncertainty in DFT-predicted adsorption energies.",
    lkm_id="gcn_d3e5e6d8aa5b4459",
    provenance_source="lkm",
)

beef_ensemble_spread = claim(
    "Analysis using the BEEF-vdW ensemble of 2000 exchange-correlation "
    "parameterizations yields a one-standard-deviation spread of "
    "approximately 0.20 eV for binding-energy differences on a "
    "representative surface model, quantifying the intrinsic "
    "exchange-correlation uncertainty of semi-local DFT for "
    "chemisorption energetics — an uncertainty that is larger than "
    "the ~0.02 eV claimed precision of the Mason correction.",
    lkm_id="gcn_ad94a0ff0aaa4c54",
    provenance_source="lkm",
)

beef_uncertainty_propagation = claim(
    "A general procedure to estimate and propagate uncertainty from "
    "the DFT exchange-correlation approximation into composite "
    "materials properties is: (i) construct an ensemble of plausible "
    "exchange-correlation functionals using BEEF-vdW, (ii) compute "
    "the property of interest for each ensemble member, and (iii) use "
    "the ensemble spread as the exchange-correlation uncertainty "
    "estimate — this approach reveals that DFT errors in chemisorption "
    "can propagate nonlinearly into predicted catalytic rates and "
    "selectivities.",
    lkm_id="gcn_88122b04a11943b7",
    provenance_source="lkm",
)

beef_consistent_with_rpa = claim(
    "BEEF-vdW, applied non-self-consistently to compute the "
    "potential-energy curve for adsorption on metal surfaces, yields "
    "results qualitatively consistent with high-level RPA calculations, "
    "validating the BEEF ensemble as a computationally affordable proxy "
    "for higher-level benchmarks when RPA calculations are too expensive.",
    lkm_id="gcn_ceadf42e2a7a4293",
    provenance_source="lkm",
)
