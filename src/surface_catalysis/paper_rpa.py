"""RPA benchmarks — gold-standard reference for CO chemisorption."""

from gaia.lang import claim

rpa_method = claim(
    "The random phase approximation (RPA) total-energy method evaluates "
    "the exact Hartree-Fock exchange energy together with the RPA "
    "correlation energy non-self-consistently on Kohn-Sham orbitals "
    "obtained from a PBE GGA calculation (EXX+RPA@PBE), providing a "
    "higher-level first-principles benchmark for surface energetics "
    "that eliminates the self-interaction error present in GGA.",
    lkm_id="gcn_897be232ecb24f8f",
    provenance_source="lkm",
)

rpa_co_benchmark = claim(
    "RPA calculations of CO chemisorption energies on metal surfaces "
    "provide a first-principles benchmark that is free of GGA "
    "self-interaction error and includes nonlocal correlation effects "
    "beyond semi-local functionals — RPA chemisorption energies are "
    "closer to experimental values than GGA for CO on transition metals, "
    "but RPA itself has residual errors and is not a perfect reference.",
    lkm_id="gcn_9171eace9fe94dcb",
    provenance_source="lkm",
)

rpa_optimized = claim(
    "The optimized random phase approximation is defined as "
    "E_optRPA = E_HF + 1.17 * E_c,RPA, where E_HF is the Hartree-Fock "
    "exact-exchange energy evaluated on DFT orbitals and E_c,RPA is the "
    "RPA correlation energy, with the empirical factor 1.17 correcting "
    "for the systematic undercorrelation of bare RPA.",
    lkm_id="gcn_6efddfbab3114451",
    provenance_source="lkm",
)

rpa_deviates_from_experiment = claim(
    "RPA (random phase approximation) reference adsorption energies "
    "from benchmark datasets deviate from experimental measurements "
    "for some systems, indicating that even the RPA — the current "
    "gold-standard first-principles method for surface adsorption — "
    "has a residual error of several tens of meV that limits its use "
    "as an absolute benchmark for validating DFT correction methods "
    "like the Mason extrapolation.",
    lkm_id="gcn_1d90485dd9ac4ed3",
    provenance_source="lkm",
)
