"""Upstream support findings — functional comparison, vdW, experimental site determination."""

from gaia.lang import claim

# ============================================================
# Functional comparison
# ============================================================

pbe_pw91_rpbe_comparison = claim(
    "Comparisons among exchange-correlation functionals for CO "
    "chemisorption on transition-metal surfaces show that PBE GGA "
    "yields chemisorption energies and energy barriers very close "
    "to PW91 GGA (the functional used in the original Mason "
    "extrapolation method), while the revised PBE (RPBE) functional "
    "systematically gives weaker (less negative, ~0.2-0.3 eV smaller "
    "in magnitude) chemisorption energies than both PBE and PW91.",
    lkm_id="gcn_d56d3b8b11ec45f3",
    provenance_source="lkm",
)

vdw_effect_co = claim(
    "For CO adsorption on metal surfaces at 0.1 ML coverage, "
    "dispersion-inclusive exchange-correlation treatments predict "
    "significantly larger adsorption energies than semi-local GGA: "
    "vdW-DF predicts 363 meV versus PBE (dispersion-free) at 247 meV "
    "for the C-bound adsorption geometry — a difference of ~116 meV "
    "from van der Waals interactions alone, which is comparable in "
    "magnitude to the GGA singlet-triplet correction and represents "
    "a separate, additive source of DFT error not addressed by the "
    "Mason extrapolation method.",
    lkm_id="gcn_3f527cabb5d24ccb",
    provenance_source="lkm",
)

vdw_geometry_issues = claim(
    "The nonlocal van der Waals density functional variant optB86b-vdW "
    "predicts larger CO adsorption energies than semi-local GGA but "
    "can yield adsorption geometries that differ markedly from "
    "experiment and from GGA-predicted geometries, indicating that "
    "vdW-inclusive functionals do not simply add a uniform attractive "
    "correction but can alter the potential-energy surface and site "
    "preferences in ways that are not yet fully understood.",
    lkm_id="gcn_2e28ab98b84446b3",
    provenance_source="lkm",
)

# ============================================================
# Mason method validation
# ============================================================

mason_validation_pt_al2o3 = claim(
    "Applying the Mason et al. extrapolation correction for known DFT "
    "errors in CO chemisorption energies to Pt/alpha-Al2O3 slab "
    "calculations reduces the systematic DFT error to an estimated "
    "uncertainty of approximately 0.02 eV, demonstrating that the "
    "correction method is effective for supported-metal catalyst "
    "models beyond the single-crystal surfaces on which it was "
    "originally parameterized.",
    lkm_id="gcn_55369fd80a854d1e",
    provenance_source="lkm",
)

method_cross_comparison = claim(
    "Across a set of electronic-structure calculations yielding pairs "
    "(DeltaE_T-S, E_CO^a) for CO on Pd model systems computed with "
    "diverse methods spanning plane-wave slab PBE, plane-wave slab "
    "HSE06, plane-wave cluster PBE, plane-wave cluster HSE06, "
    "localized-basis HF, PBE, PBE0, and CR-CC(2,3) on finite Pd "
    "clusters, the linear correlation between the gas-phase CO "
    "singlet-triplet splitting and the chemisorption energy is "
    "tested across a much wider range of DeltaE_ST values than in "
    "the original Mason study, providing a multi-method validation "
    "of the fundamental linear-mapping hypothesis.",
    lkm_id="gcn_558594a5333e473b",
    provenance_source="lkm",
)

# ============================================================
# Experimental determination of adsorption sites
# ============================================================

experimental_site_methods = claim(
    "Reflection-absorption infrared spectroscopy (RAIRS) and "
    "sum-frequency generation (SFG) spectroscopy give qualitatively "
    "different coverage dependences for the C-O stretch of CO "
    "adsorbed in atop sites on transition-metal surfaces, meaning "
    "that experimental determination of the most stable CO "
    "adsorption site — the quantity that DFT site-preference "
    "predictions aim to reproduce — depends on the spectroscopic "
    "method used and on the coverage regime probed.",
    lkm_id="gcn_9ee7d42644ac4146",
    provenance_source="lkm",
)
