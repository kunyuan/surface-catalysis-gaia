"""Coverage-dependent adsorption energetics and DFT lateral interactions."""

from gaia.lang import claim

# ============================================================
# Coverage effects — critical gap in the Mason correction
# ============================================================

coverage_dft_vs_exp_rh = claim(
    "For CO adsorbed on Rh(111), replacing the raw DFT adsorption energy "
    "and its computed coverage dependence with an experimentally derived "
    "CO desorption energy and its coverage dependence from the literature "
    "significantly changes the predicted surface phase behavior — the "
    "DFT-computed coverage dependence does not reproduce the experimental "
    "coverage variation of the CO desorption energy quantitatively.",
    lkm_id="gcn_1c2b5818c8f642ba",
    provenance_source="lkm",
)

co_ru_lattice_gas = claim(
    "For CO adsorbed on Ru(0001), a lattice-gas Hamiltonian whose "
    "on-site adsorption energies and lateral CO-CO interactions are "
    "obtained from plane-wave DFT calculations predicts coverage-dependent "
    "phase behavior, indicating that CO-CO lateral interactions "
    "substantially modify the effective adsorption energy as coverage "
    "increases — an effect not accounted for in the zero-coverage-limit "
    "Mason correction.",
    lkm_id="gcn_00c51ba2f4024064",
    provenance_source="lkm",
)

coverage_site_dependent_pd_au = claim(
    "For CO adsorbed on Pd dimer sites in a Au(111) surface, DFT-computed "
    "adsorption energies per CO molecule depend on both the adsorption "
    "site (bridge vs. atop) and the CO coverage, with bridge-bonded "
    "configurations spanning two Pd atoms showing coverage-dependent "
    "energy changes that are not captured by single-molecule, "
    "zero-coverage DFT calculations.",
    lkm_id="gcn_8d944f3acdce4407",
    provenance_source="lkm",
)

# ============================================================
# TPD experimental methods for coverage-dependent energetics
# ============================================================

tpd_coverage_dependent_energetics = claim(
    "Temperature-programmed desorption (TPD) measurements analyzed via "
    "Arrhenius/King-method evaluation yield experimental, "
    "coverage-dependent desorption activation energies that differ from "
    "the zero-coverage-limit DFT adsorption energies typically used to "
    "parameterize and validate correction methods such as the Mason "
    "extrapolation.",
    lkm_id="gcn_10c1cec732af42e5",
    provenance_source="lkm",
)
