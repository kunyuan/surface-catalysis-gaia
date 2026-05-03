"""Surface Catalysis DFT-GGA Chemisorption Energy Correction (Mason et al., 2003)."""

from gaia.lang import claim, deduction, support, contradiction, equivalence

# ============================================================
# Premises (leaf claims)
# ============================================================

prem_linear_mapping = claim(
    "For CO chemisorption on a metal surface at a given adsorption site and "
    "substrate, the DFT-GGA chemisorption energy E_chem^GGA and the DFT-GGA "
    "gas-phase CO singlet-triplet splitting DeltaE_ST^GGA obey a linear "
    "relation E_chem^GGA = E_0 + m * DeltaE_ST^GGA over the sampled interval "
    "DeltaE_ST^GGA in [5.35, 5.84] eV, and the electronic-structure "
    "discrepancy between DFT-GGA and high-level wavefunction theory (CC/CI) "
    "that manifests in the gas-phase DeltaE_ST maps linearly onto the "
    "bonding descriptors that control surface chemisorption for the "
    "adsorption geometry considered.",
    lkm_id="gcn_2ca0860e6ab04204",
    source_paper="paper:867767318044738213",
    provenance_source="lkm",
)

prem_benchmark_valid = claim(
    "The gas-phase CO singlet-triplet excitation energy benchmark value "
    "DeltaE_ST^CI = 6.095 eV, obtained from coupled-cluster and large "
    "configuration-interaction (CC/CI) calculations that reproduce the "
    "experimental value, is the appropriate target for correcting DFT-GGA "
    "surface chemisorption energies — that is, metal-induced polarization, "
    "image-charge stabilization, substrate screening, and chemical shifts "
    "of molecular excitation energies in the chemisorbed geometry do not "
    "substantially change the reference singlet-triplet energy needed for "
    "the linear correction along the DFT-GGA mapping.",
    lkm_id="gcn_8d243509098748dd",
    source_paper="paper:867767318044738213",
    provenance_source="lkm",
)

prem_extrapolation_valid = claim(
    "The empirical linear relation E_chem^GGA = E_0 + m * DeltaE_ST^GGA "
    "obtained from DFT-GGA pseudopotential sampling over the interval "
    "DeltaE_ST^GGA in [5.35, 5.84] eV remains valid when the independent "
    "variable is shifted to the CC/CI benchmark value "
    "DeltaE_ST^CI = 6.095 eV — i.e., no significant nonlinearity or change "
    "in slope m occurs between the sampled DFT-GGA points and the CI target.",
    lkm_id="gcn_ccf34f7408b040d7",
    source_paper="paper:867767318044738213",
    provenance_source="lkm",
)

# ============================================================
# Root claim (conclusion)
# ============================================================

root_correction_method = claim(
    "The DFT-GGA chemisorption energy for CO on a metal surface at a given "
    "adsorption site and substrate can be corrected to a first-principles "
    "benchmark using a linear extrapolation based on the gas-phase CO "
    "singlet-triplet excitation energy [@mason2003]: "
    "E_chem^corr = E_chem^GGA + (DeltaE_ST^CI - DeltaE_ST^GGA) * m, "
    "where DeltaE_ST^CI = 6.095 eV is the CC/CI benchmark singlet-triplet "
    "splitting, DeltaE_ST^GGA is the DFT-GGA value computed with the same "
    "pseudopotential set used for the surface calculation, and "
    "m = dE_chem^GGA / dDeltaE_ST^GGA is the slope of the DFT-GGA linear "
    "fit determined for that specific adsorption site and metal surface.",
    lkm_id="gcn_244409c845cd4a6d",
    source_paper="paper:867767318044738213",
    provenance_source="lkm",
)

# ============================================================
# Deduction — three premises jointly imply the correction method
# ============================================================

deduction_mason2003 = deduction(
    [prem_linear_mapping, prem_benchmark_valid, prem_extrapolation_valid],
    root_correction_method,
    reason=(
        "1. Establish that DFT-GGA chemisorption energy E_chem^GGA and "
        "gas-phase singlet-triplet splitting DeltaE_ST^GGA are linearly "
        "related for a given adsorption site and substrate, with the "
        "electronic-structure discrepancy mapping linearly from gas phase "
        "to surface bonding.\n"
        "2. Establish the CC/CI benchmark DeltaE_ST^CI = 6.095 eV — which "
        "reproduces the experimental value — as the appropriate "
        "extrapolation target, and assert that environmental effects in "
        "the chemisorbed geometry do not substantially shift the required "
        "reference singlet-triplet energy.\n"
        "3. Assert that the empirical linear fit from the DFT-GGA sampled "
        "interval [5.35, 5.84] eV remains valid — no significant "
        "nonlinearity or slope change — up to the CI target at 6.095 eV.\n"
        "4. Therefore the corrected chemisorption energy is "
        "E_chem^corr = E_chem^GGA + (DeltaE_ST^CI - DeltaE_ST^GGA) * m."
    ),
    prior=0.85,
)
