"""O2/CO2 dissociation barriers and DFT+U corrections — extending the error analysis."""

from gaia.lang import claim

# ============================================================
# CO2 dissociation barriers across 10 metals
# ============================================================

co2_dissociation_10metals = claim(
    "For ten transition-metal facets — Au(111), Ag(111), Pd(111), Cu(111), "
    "Ni(111), Co(0001), Ru(0001), Fe(110), Mo(110), and W(110) — "
    "DFT-computed activation barriers for CO2 dissociation, computed "
    "for both the direct dissociative adsorption pathway and the "
    "hydrogen-assisted pathway, span a range that depends sensitively "
    "on the exchange-correlation functional and the surface model, "
    "extending the known GGA error problem from CO chemisorption "
    "energetics to CO2 activation barriers on a much broader set of "
    "transition metals.",
    lkm_id="gcn_98cf2d3a990840c5",
    provenance_source="lkm",
)

# ============================================================
# O2 dissociation barriers — large error sensitivity
# ============================================================

o2_barrier_model_sensitive = claim(
    "DFT transition-state calculations on Fe-porphyrin and FeN4 cluster "
    "models produce O2 dissociation energy barriers that vary by nearly "
    "a factor of 2 depending on the computational model (1.34 eV for "
    "isolated FeN4 vs. 0.66 eV for the extended model), demonstrating "
    "that computed activation barriers for diatomic dissociation — a "
    "key catalytic descriptor — are far more sensitive to the "
    "computational setup (functional, basis, model size) than "
    "adsorption energies, with uncertainties exceeding the entire "
    "magnitude of the Mason correction.",
    lkm_id="gcn_10181e83c1ae4625",
    provenance_source="lkm",
)

# ============================================================
# DFT+U corrections — another source of functional uncertainty
# ============================================================

dft_plus_u_uncertainty = claim(
    "In spin-polarized plane-wave DFT with an on-site Hubbard U "
    "correction (DFT+U) applied to transition-metal oxide slab models, "
    "the choice of the effective on-site Coulomb parameter U_eff = U-J "
    "significantly changes computed adsorption energies — for Fe 3d "
    "electrons U_eff = 3.0 eV is typically used, but the optimal value "
    "varies with the oxidation state and coordination environment — "
    "introducing an additional functional parameter whose uncertainty "
    "is comparable to the GGA exchange-correlation error.",
    lkm_id="gcn_859c7cebb69441a0",
    provenance_source="lkm",
)

dft_u_vdw_formalism = claim(
    "A combined computational formalism coupling DFT+Hubbard U "
    "corrections with van der Waals treatment (DFT+U+vdW) has been "
    "developed for transition-metal oxide surfaces, highlighting that "
    "for correlated oxide catalysts, THREE independent corrections "
    "(self-interaction via +U, dispersion via vdW, and molecular "
    "reference errors via methods like the Mason correction) are needed "
    "simultaneously, and their uncertainties may compound rather than "
    "cancel.",
    lkm_id="gcn_112df63862b94e15",
    provenance_source="lkm",
)

# ============================================================
# ACBN0 — self-consistent Hubbard U
# ============================================================

acbn0_self_consistent_u = claim(
    "The extended ACBN0 self-consistent procedure, applied to MnO and "
    "NiO at experimental lattice constants, produces converged scalar "
    "Hubbard U parameters from first principles without empirical "
    "fitting — but the computed U values (NiO: U_Ni ~5-7 eV, MnO: "
    "U_Mn ~4-6 eV) depend on the exchange-correlation functional "
    "used in the underlying DFT calculation, showing that even "
    "'first-principles' Hubbard parameters inherit functional "
    "uncertainty.",
    lkm_id="gcn_8d9ff5a5962845c7",
    provenance_source="lkm",
)
