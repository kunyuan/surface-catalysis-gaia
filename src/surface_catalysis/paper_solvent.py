"""Solvent and electrochemical environment effects on DFT adsorption."""

from gaia.lang import claim

solvent_free_energy_gap = claim(
    "DFT slab calculations of adsorption energies on metal surfaces "
    "performed in vacuum or with only a few explicit water molecules "
    "omit significant electrochemical-environment contributions — "
    "including solvation, electrode potential, and electric double-layer "
    "effects — that can shift effective adsorption free energies by "
    "several tenths of an eV, creating a gap between ultra-high-vacuum "
    "DFT benchmarks and electrochemical catalytic conditions.",
    lkm_id="gcn_987040dd170c4a3e",
    provenance_source="lkm",
)

che_method_approximation = claim(
    "The computational hydrogen electrode (CHE) method, which is the "
    "standard approach for modeling electrocatalytic reactions with DFT, "
    "approximates the free energy of a proton-electron pair as half the "
    "chemical potential of H2 gas at standard conditions and typically "
    "neglects explicit solvent effects beyond a few water molecules, "
    "introducing an additional uncertainty of ~0.1-0.3 eV in predicted "
    "adsorption free energies relative to experimental electrochemical "
    "measurements.",
    lkm_id="gcn_1d48eecde11f41bb",
    provenance_source="lkm",
)

solvent_correction_gap = claim(
    "For aqueous electrochemical conditions, the difference between "
    "DFT-computed hydrogen adsorption energy DeltaE_H in vacuum and "
    "the Gibbs free adsorption energy DeltaG_H* under operating "
    "conditions involves corrections for zero-point energy, entropy, "
    "solvation stabilization, and electrode potential — each correction "
    "carries its own uncertainty, and these uncertainties are comparable "
    "in magnitude to the GGA exchange-correlation error that the Mason "
    "correction aims to fix.",
    lkm_id="gcn_9ae635a05aac48a2",
    provenance_source="lkm",
)
