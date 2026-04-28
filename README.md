# Electron mean free paths and photon attenuation lengths

__Electron mean free paths and photon attenuation lengths in various materials calculated with `XTANT-3` code__

[![DOI](https://zenodo.org/badge/1221780769.svg)](https://doi.org/10.5281/zenodo.19811711)


XTANT-3 code: [https://github.com/N-Medvedev/XTANT-3](https://github.com/N-Medvedev/XTANT-3).


## What's inside

The directories contain the following files:

> 1) OUTPUT_[material]_Electron_EMFP.dat - electron elastic mean free path vs. electron energy

> 2) OUTPUT_[material]_Electron_IMFP.dat - electron inelastic mean free path vs. electron energy 

> 3) OUTPUT_[material]_Photon_IMFP.dat - photon attenuation length vs. photon energy 

> 4) OUTPUT_MFP_electron.png - plot of electron mean free paths vs. electron energy

> 5) OUTPUT_MFP_photon.png - plot of photon attenuation length vs. photon energy

> 6) OUTPUT_MFP_electron.py - script to plot the electron mean free paths vs. electron energy

> 7) OUTPUT_MFP_photon.py - script to plot the photon attenuation length vs. photon energy

> 8) !OUTPUT_[material]_parameters.txt - basic parameters used in XTANT-3 calculations (including material's composition, density, ionization potentials, Auger decay times, etc.)


## Electron mean free paths

The inelastic electron mean free paths are calculated within the single-pole approximation for the linear response function (loss function; complex dielectric function) in the Ritchie-Howie algorithm [1]. Electron elastic mean free paths are calculated with the screened Rutherford cross section using modified Molier screening parameter [1,2]. The elastic cross section for a compound is constructed from the atomic ones using Bragg additivity rule, accounting for the stoicheometry of the chemical composition.


## Photon attenuation lengths

The photoabsorption cross sections for each shell of each element are extracted from EPICS2025 database [3]. The photon attenuation length of a compound is constructed from the atomic ones using Bragg additivity rule.


## Caution

The data are only reliable at electron and photon energies above some 50 eV. Although the files and plots contain the data for lower energies, one must keep in mind that for electrons, the single-pole approximation (as well as the linear response theory itself) is not meant for slow particles, and the data may only be used with extreme caution - in an absence of better data. For photons, the data are atomic, so at energies below some 30-50 eV, the collective effects of the solids are missing (in particular, plasmon peak in the photoabsorption cross sections), and thus the data become completely unreliable at low energies.


## List of materials present

Ag, Al, Al2O3, Al2O3 in kappa phase (k-Al2O3), Al2S3, AlAs, AlCrCuFeNi, AlCu, AlP, Aluminum, Al on Si, Amorphous Carbon, Overdence amorphous C (Overdence_aC), Angiotensin_II, As2Se3, amorphous Si (aSi), Au, Au2O3, AuH, gold nanoparticle (Au_NP), Au on C layer, B4C, Ba, Bi, Bi2O3, BiO2, Biphenylene, BN, C, C60, C60_2, C60_3, C60_Pa3_2, Ca, CaF2, Caffeine, Cd, CdO, CdS, CdTe, carbon nanotube (CNT), Co, Copper, CrMnFeCoNi, Cr, Cr in Pm3n phase (Cr_Pm3n), Cu, Cu2O, Cu on Si, C-dimer, C-layer, C-mobius strip, Diamond, DNA (TAACCGATGG fragment), Fe, Fe2O3, Ga, Ga2O3, GaAs, GaP, GaSb, Ge, Gold, Graphene, Graphene on SiC, Graphite, H, H2O, HAl, Hf, HfNbTaTiZr, HgO, I, In, In2O3, In2O3 in R3c phase (In2O3_R3c), Ir, ITO, K2TiO3, KTO, Li, LiBr, LiCl, LiF, LiI, Mg, Mg2SiO4, MgAl2O4, MgCoNiCuZnO, MgO, Mn, Mo, MoNbTaVW, MoS2, MoS2 layer on Al2O3, MoSi2, Multilayer AlCu, Multilayer AlSi, Multilayer AuC, NaBr, NaCl, NaF, NaI, Nb, NC, Nickel, O, Os, Pb, Pb2O3, PbI2, PbO, PbO2, PbS, PbWO4, Pd, Pentaheptite, PET, Phlogopite, PMMA, Polyethylene, Polybutylene, Polypropylene, Polystyrene, Pt, PTFE, PVDF, Quartz (crystalline), Re, Rh, Ru, Ruthenium, Ru in bcc phase (Ru_bcc), Ru nanoparticle (Ru_NP), Sc, Se, Si, Si3N4, SiAl, SiAu3, SiC, Silicon, silicon in tin phase (Si_tin), Sn, SnO, Sr, Stainless steel, STO, Ta, Tc, Te, Te2Pd, TiO2, TiO2 in beta phase (TiO2_beta), Titanium, Tl2O, Tl2O3, V, VO2, W, Y, YAG, YBCO, Zn, ZnO, ZnS, ZnSe, Zr.


## Disclaimer

Although we endeavour to ensure that the code XTANT and results delivered are correct, no warranty is given as to their accuracy. We assume no responsibility for possible errors or omissions. We shall not be liable for any damage arising from the use of these dataset, or from any action or decision taken as a result of using it or any related material.
This dataset is distributed _as is_ for non-commercial peaceful purposes only, such as research and education (for details, see GPL-3.0 license). 


## References

[1] N. Medvedev, F. Akhmetov, R.A. Rymzhanov, R. Voronkov, A.E. Volkov, "_Modeling Time‐Resolved Kinetics in Solids Induced by Extreme Electronic Excitation_", Advanced Theory and Simulations 5, 2200091 (2022)

[2] "_Monte Carlo Transport of Electrons and Photons_" 1988, Edited by T.M. Jenkins, W.R. Nelson, A. Rindi

[3] https://nuclear.llnl.gov/EPICS/
