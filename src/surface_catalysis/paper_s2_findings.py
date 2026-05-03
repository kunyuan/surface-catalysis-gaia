"""Contradiction-search findings for Mason et al. (2003) correction method."""

from gaia.lang import claim

# ============================================================
# Physical mechanism: why GGA fails for CO chemisorption
# ============================================================

# ============================================================
# DECOMPOSED: gga_failure_origin broken into cause + effect
# ============================================================

gga_2pi_too_low = claim(
    "The GGA self-interaction error in plane-wave DFT calculations on "
    "transition-metal surfaces places the unoccupied CO 2pi* orbital too "
    "low in energy with respect to the substrate Fermi level, and this "
    "orbital energy misplacement is the principal electronic-structure "
    "origin of the GGA error in CO chemisorption energies.",
    lkm_id="gcn_80526abae33f4039",
    provenance_source="lkm",
)

gga_back_donation_overestimated = claim(
    "Because the GGA places the CO 2pi* orbital too low in energy relative "
    "to the substrate Fermi level, it causes spuriously strong back-donation "
    "of electrons from the metal d states into the unoccupied CO 2pi* "
    "orbital, which overestimates the chemisorption strength at adsorption "
    "sites where back-donation dominates the metal-CO bonding.",
    lkm_id="gcn_80526abae33f4039",
    provenance_source="lkm",
)

gga_failure_origin = claim(
    "The principal reason that GGA exchange-correlation functionals in "
    "plane-wave DFT produce incorrect adsorption-site energy differences "
    "for CO on transition-metal surfaces (including Ru(0001)) is that GGA "
    "inadequately predicts the relative energy of the unoccupied CO 2pi* "
    "orbital with respect to the substrate Fermi level — the GGA "
    "self-interaction error places the CO 2pi* orbital too low in energy, "
    "causing spuriously strong back-donation from the metal d states into "
    "2pi* and therefore overestimating the chemisorption strength at sites "
    "where back-donation dominates.",
    lkm_id="gcn_80526abae33f4039",
    provenance_source="lkm",
    lkm_original=(
        "The principal reason that generalized-gradient-approximation (GGA) "
        "exchange-correlation functionals in plane-wave DFT calculations "
        "produce incorrect adsorption-site energy differences for CO on "
        "transition-metal surfaces (including Ru(0001)) is that these "
        "functionals inadequately predict the relative energy of the "
        "unoccupied CO 2pi* orbital with respect to the substrate Fermi level."
    ),
)

co_2pi_mechanism = claim(
    "For CO chemisorption on late transition-metal surfaces, the gas-phase "
    "CO singlet-triplet excitation energy DeltaE_ST (5sigma → 2pi* "
    "excitation, experimentally benchmarked at 6.095 eV) is closely related "
    "to the energetic position of the CO 2pi* orbital relative to the "
    "substrate Fermi level — the GGA functional underestimates DeltaE_ST "
    "because it places the 2pi* orbital too low, and this gas-phase error "
    "correlates with the GGA overbinding error on the surface through the "
    "proportionality between DeltaE_ST and 2pi*-Fermi-level alignment.",
    lkm_id="gcn_951b103f255d4432",
    provenance_source="lkm",
)

# ============================================================
# Correction method: what it actually does
# ============================================================

correction_site_reordering = claim(
    "Applying the Mason linear-extrapolation correction to DFT-GGA "
    "chemisorption energies for CO on Pt(111), Rh(111), Pd(111), Cu(111) "
    "and the corresponding (100) surfaces changes the DFT-GGA predicted "
    "energetic ordering of high-symmetry adsorption sites — that is, the "
    "correction is site-specific and can alter which adsorption site is "
    "predicted to be most stable on a given metal surface.",
    lkm_id="gcn_5ceccdc16e3c4317",
    provenance_source="lkm",
)

# ============================================================
# Contradiction: hybrid functionals don't uniformly fix the problem
# ============================================================

# ============================================================
# DECOMPOSED: hybrid_limitation broken into magnitude + direction
# ============================================================

hybrid_magnitude_nonuniform = claim(
    "The magnitude of the shift in CO adsorption energy caused by "
    "switching from GGA to hybrid functionals (PBE0, HSE03) varies "
    "significantly across transition-metal substrates: for Cu(111) the "
    "shift is only ~0.2 eV, for Pt(111) it reaches up to ~0.4 eV, and "
    "for Ru(0001) it is ~0.25-0.45 eV — meaning the hybrid correction "
    "is not a uniform shift across metals.",
    lkm_id="gcn_edc27c0d6ea44e07",
    provenance_source="lkm",
)

hybrid_direction_inconsistent = claim(
    "Hybrid functionals (PBE0, HSE03) shift the CO adsorption energy "
    "toward weaker binding on Pt(111) but toward stronger binding on "
    "Cu(111), revealing that the direction of the hybrid correction "
    "relative to GGA is not consistent across different transition metals.",
    lkm_id="gcn_edc27c0d6ea44e07",
    provenance_source="lkm",
)

hybrid_limitation = claim(
    "The inclusion of a fraction of exact nonlocal exchange via the PBE0 "
    "and HSE03 hybrid functionals in plane-wave periodic-slab DFT "
    "calculations does not produce a uniform improvement in agreement "
    "with experimental CO adsorption energies across different "
    "transition-metal substrates: for Cu(111) the hybrid functionals give "
    "adsorption energies that differ from the GGA result by only ~0.2 eV "
    "(on-top vs. hollow), whereas for Pt(111) and Ru(0001) the hybrid-GGA "
    "differences can reach 0.4 eV and 0.25-0.45 eV respectively, and the "
    "direction of the correction is not consistent across metals — hybrid "
    "functionals shift the CO/Pt(111) adsorption energy toward weaker "
    "binding but shift CO/Cu(111) toward stronger binding.",
    lkm_id="gcn_edc27c0d6ea44e07",
    provenance_source="lkm",
    lkm_original=(
        "The inclusion of a fraction of exact nonlocal exchange via the "
        "PBE0 and HSE03 hybrid functionals does not produce a uniform "
        "improvement in agreement with experimental CO adsorption energies "
        "across the three transition-metal substrates studied."
    ),
)

# ============================================================
# Additional supporting claim
# ============================================================

correction_reduces_site_spread = claim(
    "Applying the post-DFT singlet-triplet extrapolation correction to "
    "the set of high-symmetry adsorption-site chemisorption energies for "
    "CO on a given metal surface reduces the computed energetic spread "
    "(range) of chemisorption energies across sites, systematically "
    "narrowing the site-energy distribution compared to uncorrected GGA.",
    lkm_id="gcn_7a6a4cea8c864a06",
    provenance_source="lkm",
)

# ============================================================
# DECOMPOSED: gga_oxide_error_parallel broken into two error sources
# ============================================================

gga_o2_sie_error = claim(
    "A systematic contribution to errors in GGA-calculated oxidation "
    "energies for 3d transition metal oxides arises from the GGA "
    "self-interaction error in the O2 molecule binding energy — this "
    "is the same physical mechanism (GGA frontier-orbital error in a "
    "diatomic molecule) that produces the CO chemisorption energy error "
    "on metal surfaces, establishing that the problem is general to "
    "diatomic adsorbates.",
    lkm_id="gcn_af70e8a16f224591",
    provenance_source="lkm",
)

gga_oxide_gap_error = claim(
    "A second, independent systematic contribution to errors in "
    "GGA-calculated oxidation energies for 3d transition metal oxides "
    "arises from the GGA underestimation of the HOMO-LUMO gap in the "
    "oxide itself — this error is distinct from the molecular-reference "
    "(O2) error and reflects GGA's fundamental band-gap problem in "
    "strongly correlated oxide materials.",
    lkm_id="gcn_af70e8a16f224591",
    provenance_source="lkm",
)

gga_oxide_error_parallel = claim(
    "Two separate and systematic contributions to errors in GGA "
    "density-functional calculated oxidation energies for 3d transition "
    "metal oxides are identified: (a) an error from the GGA self-interaction "
    "error in the O2 molecule binding energy (analogous to the CO "
    "singlet-triplet error), and (b) an error from the GGA underestimation "
    "of the HOMO-LUMO gap in the oxide — establishing that the GGA "
    "molecular reference error problem extends beyond CO to other "
    "diatomic adsorbates and their surface reactions.",
    lkm_id="gcn_af70e8a16f224591",
    provenance_source="lkm",
    lkm_original=(
        "Two separate and systematic contributions to errors in generalized "
        "gradient approximation (GGA) density-functional calculated oxidation "
        "energies for 3d transition metal oxides are identified: (a) an error "
        "from the GGA self-interaction error in the O2 molecule binding energy, "
        "and (b) an error from the GGA underestimation of the HOMO-LUMO gap "
        "in the oxide."
    ),
)
