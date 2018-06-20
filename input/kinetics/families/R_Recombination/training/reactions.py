#!/usr/bin/env python
# encoding: utf-8

name = "R_Recombination/training"
shortDesc = u"Kinetics used to train group additivity values"
longDesc = u"""
Put kinetic parameters for reactions to use as a training set for fitting
group additivity values in this file.
"""
entry(
    index = 0,
    label = "CH3O2 <=> O2 + CH3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.09e+14, 's^-1'), n=0.25, Ea=(33.3, 'kcal/mol'), T0=(1, 'K')),
    rank = 10,
    shortDesc = u"""Method CBS-QB3 w/ 1-d Hindered rotor corrections""",
    longDesc = 
u"""
High-Pressure Rate Rules for Alkyl + O2 Reactions. 1. The Dissociation, Concerted Elimination, and Isomerization Channels of the Alkyl Peroxy Radical
Stephanie M. Villano, Lam K. Huynh, Hans-Heinrich Carstensen, and Anthony M. Dean
The Journal of Physical Chemistry A 2011 115 (46), 13425-13442
dx.doi.org/10.1021/jp2079204

Method CBS-QB3 w/ 1-d Hindered rotor corrections
""",
)

entry(
    index = 1,
    label = "C2H5O2 <=> O2 + C2H5",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9.49e+21, 's^-1'), n=-2.41, Ea=(35.8, 'kcal/mol'), T0=(1, 'K')),
    rank = 10,
    shortDesc = u"""Method CBS-QB3 w/ 1-d Hindered rotor corrections""",
    longDesc = 
u"""
High-Pressure Rate Rules for Alkyl + O2 Reactions. 1. The Dissociation, Concerted Elimination, and Isomerization Channels of the Alkyl Peroxy Radical
Stephanie M. Villano, Lam K. Huynh, Hans-Heinrich Carstensen, and Anthony M. Dean
The Journal of Physical Chemistry A 2011 115 (46), 13425-13442
dx.doi.org/10.1021/jp2079204

Method CBS-QB3 w/ 1-d Hindered rotor corrections
""",
)

entry(
    index = 2,
    label = "C3H7O2 <=> O2 + C3H7",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.52e+23, 's^-1'), n=-2.71, Ea=(36.4, 'kcal/mol'), T0=(1, 'K')),
    rank = 10,
    shortDesc = u"""Method CBS-QB3 w/ 1-d Hindered rotor corrections""",
    longDesc = 
u"""
High-Pressure Rate Rules for Alkyl + O2 Reactions. 1. The Dissociation, Concerted Elimination, and Isomerization Channels of the Alkyl Peroxy Radical
Stephanie M. Villano, Lam K. Huynh, Hans-Heinrich Carstensen, and Anthony M. Dean
The Journal of Physical Chemistry A 2011 115 (46), 13425-13442
dx.doi.org/10.1021/jp2079204

Method CBS-QB3 w/ 1-d Hindered rotor corrections
""",
)

entry(
    index = 3,
    label = "1-hydroxybutyl + O2 <=> 1-hydroxybutylO2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (8.36e+12, 'cm^3/(mol*s)'),
        n = -0.085,
        Ea = (-567.2, 'cal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 10,
    shortDesc = u"""CBS-QB3 w/ 1-d HR""",
    longDesc = 
u"""
Reference: Low-Temperature Combustion Chemistry of n-Butanol: Principal Oxidation Pathways of Hydroxybutyl Radicals 
DOI: 10.1021/jp403792t
""",
)

entry(
    index = 4,
    label = "NO2 + NO2 <=> N2O4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.63e+08, 'm^3/(mol*s)', '+|-', 3.16e+07),
        n = -1.1,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (600, 'K'),
        Pmin = (101000, 'Pa'),
        Pmax = (2.09e+07, 'Pa'),
    ),
    reference = Article(
        authors = ["'Borrell, P.'", "'Cobos, C.J.'", "'Luther, K.'"],
        title = 'Falloff curve and specific rate constants for the reaction NO2 + NO2 N2O4',
        journal = "'J. Phys. Chem.'",
        volume = "'92'",
        pages = "'4377-4384'",
        year = "'1988'",
        url = "'http://kinetics.nist.gov/kinetics/Detail?id=1988BOR/COB4377-4384:1'",
    ),
    referenceType = "experiment",
    rank = 10,
    shortDesc = u"""High or low pressure extrapolation""",
    longDesc = 
u"""
Bath gas: N2
Excitation technique: Flash photolysis (laser or conventional)
Analytical technique: Vis-UV absorption
""",
)

entry(
    index = 5,
    label = "NO + O2 <=> NO3",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (117000, 'm^3/(mol*s)', '*|/', -1),
        n = 0,
        Ea = (13.386, 'kJ/mol', '+|-', -0.001),
        T0 = (1, 'K'),
        Tmin = (473, 'K'),
        Tmax = (703, 'K'),
        Pmin = (1333, 'Pa'),
        Pmax = (33600, 'Pa'),
    ),
    reference = Article(
        authors = ["'Ashmore, P.G.'", "'Burnett, M.G.'"],
        title = 'Concurrent molecular and free radical mechanisms in the thermal decomposition of nitrogen dioxide',
        journal = "'J. Chem. Soc. Faraday Trans. 2'",
        volume = "'58'",
        pages = "'253'",
        year = "'1962'",
        url = "'http://kinetics.nist.gov/kinetics/Detail?id=1962ASH/BUR253:5'",
    ),
    referenceType = "experiment",
    rank = 10,
    shortDesc = u"""Derived from fitting to a complex mechanism""",
    longDesc = 
u"""
Uncertainty: 3.0
Bath gas: NO2
Excitation technique: Thermal
Analytical technique: Pressure measurement
""",
)

entry(
    index = 6,
    label = "NO2 + NO3-2 <=> N2O5",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (366000, 'm^3/(mol*s)', '+|-', 57700),
        n = 0.2,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (400, 'K'),
        Pmin = (100000, 'Pa'),
        Pmax = (9e+07, 'Pa'),
    ),
    reference = Article(
        authors = ["'Hahn, J.'", "'Luther, K.'", "'Troe, J.'"],
        title = 'Experimental and Theoretical Study of the Temperature and Pressure Dependences of the Recombination Reactions O+NO2(+M) = NO3(+M) and NO2+NO3(+M)=N2O5(+M)',
        journal = "'Phys. Chem. Chem. Phys.'",
        pages = "'5098-5104'",
        year = "'2000'",
        url = "'http://kinetics.nist.gov/kinetics/Detail?id=2000HAH/LUT5098-5104:4'",
    ),
    referenceType = "experiment",
    rank = 10,
    shortDesc = u"""Absolute value measured directly""",
    longDesc = 
u"""
Pressure dependence: Rate constant is high pressure limit
Experimental procedure: Static or low flow - Data taken vs time
Excitation technique: Flash photolysis (laser or conventional)
Time resolution: In real time
Analytical technique: Vis-UV absorption

Theoretical modeling of k0, k and Fc=0.38 exp(-T/4900K) led to consistency with the experimental data.
""",
)

entry(
    index = 7,
    label = "C5H5 + C2H5 <=> C7H10",
    degeneracy = 5.0,
    kinetics = Arrhenius(
        A = (8.34e+15, 'cm^3/(mol*s)'),
        n = -0.7,
        Ea = (-0.5, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: vinylCPD_H""",
    longDesc = 
u"""
Taken from entry: ethyl + CPDyl <=> ethylCPD
""",
)

entry(
    index = 8,
    label = "CH3NO2 <=> CH3 + NO2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.88e+24, 's^-1'),
        n = -2.35,
        Ea = (62398, 'cal/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Training reaction from kinetics library: primaryNitrogenLibrary""",
    longDesc = 
u"""
R.S. Zhu, P. Raghunath, M.C. Lin, J. Phys. Chem. A, 2013, 117, 7308-7313, doi: 10.1021/jp401148q
p. 7311
calculations done at the UCCSD(T)/CBS//UB3LYP/6-311+G(3df,2p) level of theory
The high pressure limit rate is giving here. A 1 atm rate is also available from the same source.

Also available (experimental) from:
P. Glarborg, A.B. Bendtsen, J.A. Miller
Nitromethane Dissociation: Implications for the CH3 + NO2 Reaction
International Journal of Chemical Kinetics Volume 31, Issue 9, pages 591-602, 1999
DOI: 10.1002/(SICI)1097-4601(1999)31:9<591::AID-KIN1>3.0.CO;2-E
    kinetics = Arrhenius(A=(1.8e+16, 's^-1'), n=0, Ea=(58500, 'cal/mol'), T0=(1, 'K')),

Also appears in the Nitrogen_Glarborg_Zhang_et_al library (index 671)
and in the Nitrogen_Glarborg_Gimenez_et_al library (index 953)
""",
)

entry(
    index = 9,
    label = "CH3 + CH3 <=> C2H6",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (9.45e+14, 'cm^3/(mol*s)'),
        n = -0.538,
        Ea = (135.1, 'cal/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 4,
    shortDesc = u"""CASPT2/cc-pvdz""",
    longDesc = 
u"""
S.J. Klippenstein, Y. Georgievskiia, L.B. Hardingb
Predictive theory for the combination kinetics of two alkyl radicals
Phys. Chem. Chem. Phys., 2006, 8, 1133-1147
doi: 10.1039/B515914H
""",
)

entry(
    index = 10,
    label = "CH3 + C2H5 <=> C3H8",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.23e+15, 'cm^3/(mol*s)'),
        n = -0.562,
        Ea = (20.5, 'cal/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 4,
    shortDesc = u"""CASPT2/cc-pvdz""",
    longDesc = 
u"""
S.J. Klippenstein, Y. Georgievskiia, L.B. Hardingb
Predictive theory for the combination kinetics of two alkyl radicals
Phys. Chem. Chem. Phys., 2006, 8, 1133-1147
doi: 10.1039/B515914H
""",
)

entry(
    index = 11,
    label = "C2H5 + C2H5 <=> C4H10",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (8.73e+14, 'cm^3/(mol*s)'),
        n = -0.699,
        Ea = (-3.2, 'cal/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 4,
    shortDesc = u"""CASPT2/cc-pvdz""",
    longDesc = 
u"""
S.J. Klippenstein, Y. Georgievskiia, L.B. Hardingb
Predictive theory for the combination kinetics of two alkyl radicals
Phys. Chem. Chem. Phys., 2006, 8, 1133-1147
doi: 10.1039/B515914H
""",
)

entry(
    index = 12,
    label = "C5H5 + CH3 <=> C6H8",
    degeneracy = 5.0,
    kinetics = Arrhenius(
        A = (1.623e+17, 'cm^3/(mol*s)'),
        n = -1.07,
        Ea = (0.002, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ["'Krasnoukhov, V. S.'", "'Porfiriev, D. P.'", "'Zavershinskiy, I. P.'", "'Azyazov, V. N.'", "'Mebel, A. M.'"],
        title = 'Kinetics of the CH3 + C5H5 Reaction: A Theoretical Study',
        journal = "'The Journal of Physical Chemistry A'",
        volume = "'121 (48)'",
        pages = "'9191-9200'",
        year = "'2017'",
    ),
    referenceType = "theory",
    rank = 4,
    longDesc = 
u"""
CCSD(T)-F12/cc-pVTZ-f12//B2PLYPD3/aug-cc-pVDZ
""",
)

entry(
    index = 13,
    label = "C6H7 + H <=> C6H8-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.62e+13, 'cm^3/(mol*s)'),
        n = 0.228,
        Ea = (-0.022, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ["'Krasnoukhov, V. S.'", "'Porfiriev, D. P.'", "'Zavershinskiy, I. P.'", "'Azyazov, V. N.'", "'Mebel, A. M.'"],
        title = 'Kinetics of the CH3 + C5H5 Reaction: A Theoretical Study',
        journal = "'The Journal of Physical Chemistry A'",
        volume = "'121 (48)'",
        pages = "'9191-9200'",
        year = "'2017'",
    ),
    referenceType = "theory",
    rank = 4,
    longDesc = 
u"""
CCSD(T)-F12/cc-pVTZ-f12//B2PLYPD3/aug-cc-pVDZ
""",
)

entry(
    index = 14,
    label = "C6H7-2 + H <=> C6H8-3",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.884e+13, 'cm^3/(mol*s)'),
        n = 0.408,
        Ea = (0.002, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ["'Krasnoukhov, V. S.'", "'Porfiriev, D. P.'", "'Zavershinskiy, I. P.'", "'Azyazov, V. N.'", "'Mebel, A. M.'"],
        title = 'Kinetics of the CH3 + C5H5 Reaction: A Theoretical Study',
        journal = "'The Journal of Physical Chemistry A'",
        volume = "'121 (48)'",
        pages = "'9191-9200'",
        year = "'2017'",
    ),
    referenceType = "theory",
    rank = 4,
    longDesc = 
u"""
CCSD(T)-F12/cc-pVTZ-f12//B2PLYPD3/aug-cc-pVDZ
""",
)

entry(
    index = 15,
    label = "C6H7-3 + H <=> C6H8-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.156e+12, 'cm^3/(mol*s)'),
        n = 0.461,
        Ea = (-0.001, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ["'Krasnoukhov, V. S.'", "'Porfiriev, D. P.'", "'Zavershinskiy, I. P.'", "'Azyazov, V. N.'", "'Mebel, A. M.'"],
        title = 'Kinetics of the CH3 + C5H5 Reaction: A Theoretical Study',
        journal = "'The Journal of Physical Chemistry A'",
        volume = "'121 (48)'",
        pages = "'9191-9200'",
        year = "'2017'",
    ),
    referenceType = "theory",
    rank = 4,
    longDesc = 
u"""
CCSD(T)-F12/cc-pVTZ-f12//B2PLYPD3/aug-cc-pVDZ
""",
)

entry(
    index = 16,
    label = "C6H7-4 + H <=> C6H8-5",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (5.871e+13, 'cm^3/(mol*s)'),
        n = 0.158,
        Ea = (-0.004, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ["'Krasnoukhov, V. S.'", "'Porfiriev, D. P.'", "'Zavershinskiy, I. P.'", "'Azyazov, V. N.'", "'Mebel, A. M.'"],
        title = 'Kinetics of the CH3 + C5H5 Reaction: A Theoretical Study',
        journal = "'The Journal of Physical Chemistry A'",
        volume = "'121 (48)'",
        pages = "'9191-9200'",
        year = "'2017'",
    ),
    referenceType = "theory",
    rank = 4,
    longDesc = 
u"""
CCSD(T)-F12/cc-pVTZ-f12//B2PLYPD3/aug-cc-pVDZ
""",
)

entry(
    index = 17,
    label = "C6H7-5 + H <=> C6H8-6",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (7.09e+12, 'cm^3/(mol*s)'),
        n = 0.412,
        Ea = (0.009, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ["'Krasnoukhov, V. S.'", "'Porfiriev, D. P.'", "'Zavershinskiy, I. P.'", "'Azyazov, V. N.'", "'Mebel, A. M.'"],
        title = 'Kinetics of the CH3 + C5H5 Reaction: A Theoretical Study',
        journal = "'The Journal of Physical Chemistry A'",
        volume = "'121 (48)'",
        pages = "'9191-9200'",
        year = "'2017'",
    ),
    referenceType = "theory",
    rank = 4,
    longDesc = 
u"""
CCSD(T)-F12/cc-pVTZ-f12//B2PLYPD3/aug-cc-pVDZ
""",
)

entry(
    index = 18,
    label = "C6H7-6 + H <=> C6H8-7",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.48677e-12, 'cm^3/(molecule*s)'),
        n = 0.6,
        Ea = (-0.8, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: 2009_Sharma_C5H5_CH3_highP""",
    longDesc = 
u"""
Taken from entry: R4 + H <=> C5H5CH3-5
""",
)

entry(
    index = 19,
    label = "CH3ONO <=> CH3O + NO",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (7.9e+22, 's^-1'),
        n = -2.18,
        Ea = (41930, 'cal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (3000, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Training reaction from kinetics library: primaryNitrogenLibrary""",
    longDesc = 
u"""
R.S. Zhu, P. Raghunath, M.C. Lin, J. Phys. Chem. A, 2013, 117, 7308-7313, doi: 10.1021/jp401148q
p. 7311
calculations done at the UCCSD(T)/CBS//UB3LYP/6-311+G(3df,2p) level of theory
The high pressure limit rate is giving here. A 1 atm rate is akso available from the same source.
Reported rate was divided by 2 due to a 50% branching ratio (Fig. 7 in the manuscript).
""",
)

entry(
    index = 20,
    label = "CN + NCN <=> NCNCN",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.01e+09, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-34691, 'cal/mol'),
        T0 = (1, 'K'),
        Tmin = (2000, 'K'),
        Tmax = (4000, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Training reaction from kinetics library: primaryNitrogenLibrary""",
    longDesc = 
u"""
See Table 1 on p. 2397 in L.V Moskaleva, M.C. Lin, Proceedings of the Combustion Institute, 2000, 28(2), 2393-2401, doi: 10.1016/S0082-0784(00)80652-9
Done at the G2M(RCC2)//B3LYP/6-311G(d,p) level of theory
""",
)

entry(
    index = 21,
    label = "HSOO <=> SH + O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.41e+18, 's^-1'),
        n = -1.07,
        Ea = (7750, 'cal/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Training reaction from kinetics library: primarySulfurLibrary""",
    longDesc = 
u"""
A. Goumri, J-D.R. Rocha, D. Laakso, C.E. Smith, P. Marshall, J. Phys. Chem. A, 1999, 103(51), 11328-11335 doi: 10.1021/jp9924070
Table 7 on p. 11333
calculations done at the QCISD(T)/6-311+G(3df,2p)//MP2=FULL/6-31G(d) level of theory

Troe expression given, only k_inf taken here:
kinetics = Troe(
        arrheniusHigh = Arrhenius(A=(4.41e+18, 's^-1'), n=-1.07, Ea=(7750, 'cal/mol'), T0=(1, 'K'), Tmin = (200, 'K'), Tmax = (2000, 'K')),
        arrheniusLow = Arrhenius(A=(1.56e+23, 'cm^3/(mol*s)'), n=-2.82, Ea=(-7450, 'cal/mol'), T0=(1, 'K'), Tmin = (200, 'K'), Tmax = (2000, 'K')),
        alpha=1, T3=(1e-30, 'K'), T1=(1e+30, 'K'), efficiencies={}),
""",
)

entry(
    index = 22,
    label = "OH + NO2-2 <=> HOONO",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.03e+14, 'cm^3/(mol*s)'),
        n = -0.24,
        Ea = (-200, 'cal/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: primaryNitrogenLibrary""",
    longDesc = 
u"""
R.S. Zhu, M.C. Lin, J. Chem. Phys., 2003, 119, 10667, doi: 10.1063/1.1619373

Lindemann expression given, only k_inf taken here:
    kinetics = Lindemann(
        arrheniusHigh = Arrhenius(A=(1.03e+14, 'cm^3/(mol*s)'), n=-0.24, Ea=(-200, 'cal/mol'), T0=(1, 'K'), Tmin=(200, 'K'), Tmax=(2000, 'K')),
        arrheniusLow = Arrhenius(A=(1.14e+50, 'cm^6/(mol^2*s)'), n=-12.3, Ea=(1163, 'cal/mol'), T0=(1, 'K'), Tmin=(200, 'K'), Tmax=(2000, 'K'))),
        
A low T (200-400 K) kinetics from a different source is:
    kinetics = Arrhenius(
        A = (2.41e+07, 'm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (400, 'K'),
    ),
    reference = Article(
        authors = ["Williams, C.F.", "Pogrebnya, S.K.", "Clary, D.C."],
        title = u'Quantum study on the branching ratio of the reaction NO2+OH',
        journal = "J. Chem. Phys.",
        volume = "126",
        pages = "154321",
        year = "2007",
        url = "http://kinetics.nist.gov/kinetics/Detail?id=2007WIL/POG154321:2",
    ),
""",
)

entry(
    index = 23,
    label = "N2H4 <=> NH2 + NH2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.57e+21, 's^-1'),
        n = -1.04,
        Ea = (66565, 'cal/mol'),
        T0 = (1, 'K'),
        Tmin = (700, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Training reaction from kinetics library: primaryNitrogenLibrary""",
    longDesc = 
u"""
P. Raghunath, N.T. Nghia, M.C. Lin, Advances in Quantum Chemistry, 2014, 69, 253-301, doi: 10.1016/B978-0-12-800345-9.00007-6
p. 264
Calculations done at the RCCSD(T)/6-311+G(3df,2p)//B3LYP/6-311G(d,p) level of theoty
Only High Pressure Limit rate was taken; low limit and 1 atm rate are also available from the same source
Also available from [Klippenstein2009] in reverse:
label = "NH2 + NH2 <=> N2H4",
    kinetics = Troe(
       arrheniusHigh = Arrhenius(A=(9.33e-10, 's^-1'), n=-0.414, Ea=(66, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(2500, 'K')),
       arrheniusLow = Arrhenius(A=(2.7e+10, 'cm^3/(mol*s)'), n=-5.49, Ea=(1987, 'cal/mol'), T0=(1, 'K'), Tmin=(300, 'K'), Tmax=(2500, 'K')),
       alpha=0.31, T3=(1e-30, 'K'), T1=(1e+30, 'K'), efficiencies={}),
Table 3, p. 10245, T range: 300-2500 K, calculated at the (CCSD(T) and CAS+1+2+QC level
""",
)

entry(
    index = 24,
    label = "H + NJCO <=> HNCO",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.8e+12, 'cm^3/(mol*s)'),
        n = 0.493,
        Ea = (-294, 'cal/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Training reaction from kinetics library: primaryNitrogenLibrary""",
    longDesc = 
u"""
S.J. Klippenstein, L.B. Harding, Proc. Comb. Inst., 2009, 32, 149-155, doi: 10.1016/j.proci.2008.06.135
Table 2, p. 154
The reported branching ratio is 80% HNCO 20% NCOH; the original rates were multiplied here by 80%.
calculated at the multi-reference configuration interaction (MR-CI) CASSCF level
The isomerization barrier between HNCO and HOCN is well below the H + NCO asymptote. Thus, a rapid isomerization between
the initial adducts is expected and the distinction between the initial addition sites should be largely irrelevant to
the overall kinetics. The contributions from the triplet additions are quite minor, increasing to only 10% at 2500 K.
""",
)

entry(
    index = 25,
    label = "H + NCOJ <=> NCOH",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (7e+11, 'cm^3/(mol*s)'),
        n = 0.493,
        Ea = (-294, 'cal/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Training reaction from kinetics library: primaryNitrogenLibrary""",
    longDesc = 
u"""
S.J. Klippenstein, L.B. Harding, Proc. Comb. Inst., 2009, 32, 149-155, doi: 10.1016/j.proci.2008.06.135
Table 2, p. 154
The reported branching ratio is 80% HNCO 20% NCOH; the original rates were multiplied here by 20%.
calculated at the multi-reference configuration interaction (MR-CI) CASSCF level
The isomerization barrier between HNCO and HOCN is well below the H + NCO asymptote. Thus, a rapid isomerization between
the initial adducts is expected and the distinction between the initial addition sites should be largely irrelevant to
the overall kinetics. The contributions from the triplet additions are quite minor, increasing to only 10% at 2500 K.
""",
)

entry(
    index = 26,
    label = "NH2 + HO2 <=> NH2OOH",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.5e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'cal/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (1900, 'K'),
    ),
    rank = 9,
    shortDesc = u"""QRRK""",
    longDesc = 
u"""
J.W. Bozzeli, A.M Dean, J. Phys. Chem., 1989, 93, 1058-1065, doi: 10.1021/j100340a009
Table 1, k1
P range: 0.001-10 atm
""",
)

entry(
    index = 27,
    label = "NH2 + O2 <=> NH2OO",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.6e+19, 'cm^3/(mol*s)'),
        n = -3.683,
        Ea = (1630, 'cal/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (1900, 'K'),
    ),
    rank = 9,
    shortDesc = u"""QRRK""",
    longDesc = 
u"""
J.W. Bozzeli, A.M Dean, J. Phys. Chem., 1989, 93, 1058-1065, doi: 10.1021/j100340a009
Table 1, k1
P range: 0.001-10 atm
Calculated with N2 as third body. Data for He, CH4, and Ar as third body colliders is also available
""",
)

entry(
    index = 28,
    label = "CH3NHNH2 <=> NH2 + CH3NH",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.55e+23, 'cm^3/(mol*s)'),
        n = -2.147,
        Ea = (64703, 'cal/mol'),
        T0 = (1, 'K'),
        Tmin = (400, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""QRRK""",
    longDesc = 
u"""
P. Zhang, S.J. Klippenstein, H. Sun, C.K. Law, Proc. Comb. Inst., 2011, 33(1), 425-432, doi: 10.1016/j.proci.2010.05.010
R1
Calculated at the QCISD(T)/CBS//B3LYP/6-311++G(d,p) level
""",
)

entry(
    index = 29,
    label = "CH3NHNH2 <=> CH3 + NHNH2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.65e+19, 'cm^3/(mol*s)'),
        n = -1.12,
        Ea = (65677, 'cal/mol'),
        T0 = (1, 'K'),
        Tmin = (400, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 4,
    shortDesc = u"""QRRK""",
    longDesc = 
u"""
P. Zhang, S.J. Klippenstein, H. Sun, C.K. Law, Proc. Comb. Inst., 2011, 33(1), 425-432, doi: 10.1016/j.proci.2010.05.010
R2
Calculated at the QCISD(T)/CBS//B3LYP/6-311++G(d,p) level
""",
)

entry(
    index = 30,
    label = "HSSH <=> SH + SH",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.59e+18, 'cm^3/(mol*s)'),
        n = -0.957,
        Ea = (267, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Sendt2009b""",
    longDesc = 
u"""
C.R. Zhou, K. Sendt, B.S. Haynes, J. Phys. Chem. A, 2009, 113, 8299-8306, doi: 10.1021/jp903185k
Table 1, R2
calculations done at the MRCI/aug-cc-pV(Q+d)Z//CASSCF/cc-pVTZ level of theory
""",
)

entry(
    index = 31,
    label = "HSSH <=> HSS + H",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (4.7e+17, 'cm^3/(mol*s)'),
        n = -0.076,
        Ea = (310, 'kJ/mol'),
        T0 = (1, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Sendt2009b""",
    longDesc = 
u"""
C.R. Zhou, K. Sendt, B.S. Haynes, J. Phys. Chem. A, 2009, 113, 8299-8306, doi: 10.1021/jp903185k
Table 1, R3
calculations done at the MRCI/aug-cc-pV(Q+d)Z//CASSCF/cc-pVTZ level of theory
""",
)

entry(
    index = 32,
    label = "C10H9 <=> C10H8 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1.89e+16, 's^-1'), n=-0.28, Ea=(68.378, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2016_Mebel_C10H9_highP""",
    longDesc = 
u"""
Taken from entry: W111 <=> P114 + H
""",
)

entry(
    index = 33,
    label = "C3H3 + C7H7 <=> C10H10",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.781e+17, 'cm^3/(mol*s)'),
        n = -1.568,
        Ea = (0.4547, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2012_Matsugi_C3H3_C7H7_highP""",
    longDesc = 
u"""
Taken from entry: C3H3 + C7H7 <=> W1
""",
)

entry(
    index = 34,
    label = "C3H3-2 + C7H7 <=> C10H10-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.144e+19, 'cm^3/(mol*s)'),
        n = -2.163,
        Ea = (1.195, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2012_Matsugi_C3H3_C7H7_highP""",
    longDesc = 
u"""
Taken from entry: C3H3 + C7H7 <=> W2
""",
)

entry(
    index = 35,
    label = "C10H10-3 <=> C10H9-2 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(9.431e+15, 's^-1'), n=-0.34, Ea=(77.615, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2012_Matsugi_C3H3_C7H7_highP""",
    longDesc = 
u"""
Taken from entry: W10 <=> P5 + H
""",
)

entry(
    index = 36,
    label = "C10H10-4 <=> C10H9-3 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(5.081e+15, 's^-1'), n=-0.263, Ea=(86.584, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2012_Matsugi_C3H3_C7H7_highP""",
    longDesc = 
u"""
Taken from entry: W17 <=> P9 + H
""",
)

entry(
    index = 37,
    label = "C10H10-5 <=> C10H9-4 + H",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(2.899e+16, 's^-1'), n=-0.42, Ea=(88.738, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: First_to_Second_Aromatic_Ring/2012_Matsugi_C3H3_C7H7_highP""",
    longDesc = 
u"""
Taken from entry: W17 <=> P10 + H
""",
)

entry(
    index = 38,
    label = "C6H5 + C3H3 <=> C9H8",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: kislovB""",
    longDesc = 
u"""
Taken from entry: phenyl_16 + C3H3_9 <=> C9H8_20
""",
)

entry(
    index = 39,
    label = "C6H5 + C3H3-2 <=> C9H8-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: kislovB""",
    longDesc = 
u"""
Taken from entry: phenyl_16 + C3H3_9 <=> C9H8_21
""",
)

entry(
    index = 40,
    label = "C9H7 + H <=> C9H8-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(A=(1e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'kcal/mol'), T0=(1, 'K')),
    rank = 5,
    shortDesc = u"""Training reaction from kinetics library: kislovB""",
    longDesc = 
u"""
Taken from entry: C9H7_19 + H_15 <=> indene_25
""",
)

entry(
    index = 41,
    label = "C3H3 + O2 <=> C3H3O2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (47800, 'cm^3/(mol*s)'),
        n = 2.243,
        Ea = (-1.064, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ["'Hahn, D. K.'", "'Klippenstein, S. J.'", "'Miller, J. A.'"],
        title = 'A theoretical analysis of the reaction between propargyl and molecular oxygen',
        journal = "'Faraday Discussions'",
        volume = "'119 (0)'",
        pages = "'79-100'",
        year = "'2002'",
    ),
    referenceType = "theory",
    rank = 5,
    longDesc = 
u"""
approximate QCISD(T,Full)/6-311&&G(3df,2pd)//B3LYP
""",
)

entry(
    index = 42,
    label = "C3H3-2 + O2 <=> C3H3O2-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (8270, 'cm^3/(mol*s)'),
        n = 2.525,
        Ea = (1.989, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ["'Hahn, D. K.'", "'Klippenstein, S. J.'", "'Miller, J. A.'"],
        title = 'A theoretical analysis of the reaction between propargyl and molecular oxygen',
        journal = "'Faraday Discussions'",
        volume = "'119 (0)'",
        pages = "'79-100'",
        year = "'2002'",
    ),
    referenceType = "theory",
    rank = 5,
    longDesc = 
u"""
approximate QCISD(T,Full)/6-311&&G(3df,2pd)//B3LYP
""",
)

entry(
    index = 43,
    label = "C3H3 + H <=> C3H4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.398e+13, 'cm^3/(mol*s)'),
        n = 0.102,
        Ea = (-130.54, 'J/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ["'Harding, L. B.'", "'Klippenstein, S. J.'", "'Georgievskii, Y.'"],
        title = 'On the Combination Reactions of Hydrogen Atoms with Resonance-Stabilized Hydrocarbon Radicals',
        journal = "'The Journal of Physical Chemistry A'",
        volume = "'111 (19)'",
        pages = "'3789-3801'",
        year = "'2007'",
    ),
    referenceType = "theory",
    rank = 9,
    longDesc = 
u"""
CASPT2/cc-pvdz (VRC-TST)
""",
)

entry(
    index = 44,
    label = "C3H3-2 + H <=> C3H4-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.048e+13, 'cm^3/(mol*s)'),
        n = 0.206,
        Ea = (-724.19, 'J/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ["'Harding, L. B.'", "'Klippenstein, S. J.'", "'Georgievskii, Y.'"],
        title = 'On the Combination Reactions of Hydrogen Atoms with Resonance-Stabilized Hydrocarbon Radicals',
        journal = "'The Journal of Physical Chemistry A'",
        volume = "'111 (19)'",
        pages = "'3789-3801'",
        year = "'2007'",
    ),
    referenceType = "theory",
    rank = 9,
    longDesc = 
u"""
CASPT2/cc-pvdz (VRC-TST)
""",
)

entry(
    index = 45,
    label = "C3H3-2 + C3H3-2 <=> C6H6",
    degeneracy = 0.5,
    kinetics = Arrhenius(
        A = (4.288e+09, 'cm^3/(mol*s)'),
        n = 0.795,
        Ea = (-4303.6, 'J/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ["'Georgievskii, Y.'", "'Miller, J. A.'", "'Klippenstein, S. J.'"],
        title = 'Association rate constants for reactions between resonance-stabilized radicals: C3H3 + C3H3, C3H3 + C3H5, and C3H5 + C3H5',
        journal = "'Physical Chemistry Chemical Physics'",
        volume = "'9 (31)'",
        pages = "'4259-4268'",
        year = "'2007'",
    ),
    referenceType = "theory",
    rank = 9,
    longDesc = 
u"""
CASPT2/cc-pvdz (VRC-TST)
""",
)

entry(
    index = 46,
    label = "C3H3 + C3H3-2 <=> C6H6-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.307e+12, 'cm^3/(mol*s)'),
        n = 0.192,
        Ea = (-2807, 'J/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ["'Georgievskii, Y.'", "'Miller, J. A.'", "'Klippenstein, S. J.'"],
        title = 'Association rate constants for reactions between resonance-stabilized radicals: C3H3 + C3H3, C3H3 + C3H5, and C3H5 + C3H5',
        journal = "'Physical Chemistry Chemical Physics'",
        volume = "'9 (31)'",
        pages = "'4259-4268'",
        year = "'2007'",
    ),
    referenceType = "theory",
    rank = 9,
    longDesc = 
u"""
CASPT2/cc-pvdz (VRC-TST)
""",
)

entry(
    index = 47,
    label = "C3H3 + C3H3 <=> C6H6-3",
    degeneracy = 0.5,
    kinetics = Arrhenius(
        A = (2.945e+13, 'cm^3/(mol*s)'),
        n = -0.278,
        Ea = (-1268.8, 'J/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ["'Georgievskii, Y.'", "'Miller, J. A.'", "'Klippenstein, S. J.'"],
        title = 'Association rate constants for reactions between resonance-stabilized radicals: C3H3 + C3H3, C3H3 + C3H5, and C3H5 + C3H5',
        journal = "'Physical Chemistry Chemical Physics'",
        volume = "'9 (31)'",
        pages = "'4259-4268'",
        year = "'2007'",
    ),
    referenceType = "theory",
    rank = 9,
    longDesc = 
u"""
CASPT2/cc-pvdz (VRC-TST)
""",
)

entry(
    index = 48,
    label = "CH3 + C3H3-2 <=> C4H6",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.705e+09, 'cm^3/(mol*s)'),
        n = 1.07,
        Ea = (-2.268, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ["'Huang, C.'", "'Yang, B.'", "'Zhang, F.'"],
        title = 'Initiation mechanism of 1,3-butadiene combustion and its effect on soot precursors',
        journal = "'Combustion and Flame'",
        volume = "'184'",
        pages = "'167-175'",
        year = "'2017'",
    ),
    referenceType = "theory",
    rank = 4,
    longDesc = 
u"""
CCSD(T)-F12/cc-pVTZ-F12//QCISD/6-311++G(2df,2p)
""",
)

entry(
    index = 49,
    label = "C4H5 + H <=> C4H6-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.117e+14, 'cm^3/(mol*s)'),
        n = -0.152,
        Ea = (1.003, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ["'Huang, C.'", "'Yang, B.'", "'Zhang, F.'"],
        title = 'Initiation mechanism of 1,3-butadiene combustion and its effect on soot precursors',
        journal = "'Combustion and Flame'",
        volume = "'184'",
        pages = "'167-175'",
        year = "'2017'",
    ),
    referenceType = "theory",
    rank = 4,
    longDesc = 
u"""
CCSD(T)-F12/cc-pVTZ-F12//QCISD/6-311++G(2df,2p)
""",
)

entry(
    index = 50,
    label = "C4H5-2 + H <=> C4H6-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.25e+14, 'cm^3/(mol*s)'),
        n = -0.119,
        Ea = (-1.012, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ["'Huang, C.'", "'Yang, B.'", "'Zhang, F.'"],
        title = 'Initiation mechanism of 1,3-butadiene combustion and its effect on soot precursors',
        journal = "'Combustion and Flame'",
        volume = "'184'",
        pages = "'167-175'",
        year = "'2017'",
    ),
    referenceType = "theory",
    rank = 4,
    longDesc = 
u"""
CCSD(T)-F12/cc-pVTZ-F12//QCISD/6-311++G(2df,2p)
""",
)

entry(
    index = 51,
    label = "C6H5 + CH3 <=> C7H8",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.87e-10, 'cm^3/(molecule*s)'),
        n = -0.283,
        Ea = (-0.191, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ["'Klippenstein, S. J.'", "'Harding, L. B.'", "'Georgievskii, Y.'"],
        title = 'On the formation and decomposition of C7H8',
        journal = "'Proceedings of the Combustion Institute'",
        volume = "'31 (1)'",
        pages = "'221-229'",
        year = "'2007'",
    ),
    referenceType = "theory",
    rank = 5,
    longDesc = 
u"""
CCSD(T)/aug-cc-pvdz//B3LYP/6-31G* (VRC-TST)
""",
)

entry(
    index = 52,
    label = "C7H7 + H <=> C7H8-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.2e-10, 'cm^3/(molecule*s)'),
        n = 0.062,
        Ea = (-0.044, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ["'Klippenstein, S. J.'", "'Harding, L. B.'", "'Georgievskii, Y.'"],
        title = 'On the formation and decomposition of C7H8',
        journal = "'Proceedings of the Combustion Institute'",
        volume = "'31 (1)'",
        pages = "'221-229'",
        year = "'2007'",
    ),
    referenceType = "theory",
    rank = 5,
    longDesc = 
u"""
CCSD(T)/aug-cc-pvdz//B3LYP/6-31G* (VRC-TST)
""",
)

entry(
    index = 53,
    label = "C7H7-2 + H <=> C7H8-3",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (8.28e-13, 'cm^3/(molecule*s)'),
        n = 0.611,
        Ea = (-0.436, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ["'Klippenstein, S. J.'", "'Harding, L. B.'", "'Georgievskii, Y.'"],
        title = 'On the formation and decomposition of C7H8',
        journal = "'Proceedings of the Combustion Institute'",
        volume = "'31 (1)'",
        pages = "'221-229'",
        year = "'2007'",
    ),
    referenceType = "theory",
    rank = 5,
    longDesc = 
u"""
CCSD(T)/aug-cc-pvdz//B3LYP/6-31G* (VRC-TST)
""",
)

entry(
    index = 54,
    label = "C7H7-3 + H <=> C7H8-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.07e-11, 'cm^3/(molecule*s)'),
        n = 0.245,
        Ea = (-0.333, 'kcal/mol'),
        T0 = (1, 'K'),
    ),
    reference = Article(
        authors = ["'Klippenstein, S. J.'", "'Harding, L. B.'", "'Georgievskii, Y.'"],
        title = 'On the formation and decomposition of C7H8',
        journal = "'Proceedings of the Combustion Institute'",
        volume = "'31 (1)'",
        pages = "'221-229'",
        year = "'2007'",
    ),
    referenceType = "theory",
    rank = 5,
    longDesc = 
u"""
CCSD(T)/aug-cc-pvdz//B3LYP/6-31G* (VRC-TST)
""",
)

entry(
    index = 55,
    label = "H + H <=> H2",
    degeneracy = 0.5,
    kinetics = Arrhenius(
        A = (5e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
        comment = '\n\nConverted to training reaction from rate rule: Y_rad;Y_rad',
    ),
    rank = 0,
    shortDesc = u"""Default""",
)

entry(
    index = 56,
    label = "H + H <=> H2",
    degeneracy = 0.5,
    kinetics = Arrhenius(
        A = (5.45e+10, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (6.276, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (278, 'K'),
        Tmax = (372, 'K'),
        comment = '[167] Dingle, J.R.; Le Roy, D.J.; J. Chem. Phys. 1950, 18, 1632.\n\nAbsolute value measured directly. Excitation: thermal. H + H --> H2 Bath gas: C2H2\n\nNIST record: http://kinetics.nist.gov/kinetics/Detail?id=1950DIN/LER1632-1637:1\n***high probability of inaccuracy***\nChecked by Greg Magoon; I suspect the parameters in the paper come from a different reaction (maybe H + C2H2 -> products?); (even if it was the correct reaction, the parameters used by NIST and RMG appear to be based off of values from the abstract, but p. 1637 seems to suggest that it may be more complicated, perhaps a collision theory-type form as alluded to in the abstract...p. 1637 states "In calculating E1 allowance was made for the term T^1/2 appearing in the frequency factor.";if this is the case, then the NIST record is inaccurate; almost all the other papers in NIST database report 3rd order rate constant, which is proportional to [M]; the best assessment I have found is Stace and Murrell, IJCK, v. 10, p. 197-212, which seems to suggest bimolecular rate constant of at least ~10^14 at high pressure (over 3 orders of magnitude higher than this value); this paper and Troe, Ann. Rev. Phys. Chem. 1978. 29: 223-250. make reference to "diffusion" limitations at very high pressure; another (relatively minor) consideration is that we will probably want to divide the reported rate coefficient by 2 to correctly account for stoichiometry\n\nConverted to training reaction from rate rule: H_rad;H_rad',
    ),
    rank = 11,
    shortDesc = u"""Dingle et al. [167]""",
)

entry(
    index = 57,
    label = "H + CH3 <=> CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.93e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (1.12968, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
        comment = "[168] Takahashi, J.; Momose, T.; Shida, T. Bull. Chem. Soc. Jpn. 1994, 67, 74.\n\nH + CH3 --> CH4\n\nCVTST calculation\nNIST record: http://kinetics.nist.gov/kinetics/Detail?id=1994TAK/MOM74-85:2\nVerified by Greg Magoon: RMG value agrees with NIST record, and the points in the NIST record agree with the values in Table 3 in the paper within 10%; note that a 3000K data point is also available in the paper, but doesn't seem to be considered in the NIST fit; also, note that a lot of other data for this reaction is available on the NIST site and in the paper\n\nConverted to training reaction from rate rule: H_rad;C_methyl",
    ),
    rank = 6,
    shortDesc = u"""Takahashi et al. [168] Transition state theory.""",
)

entry(
    index = 58,
    label = "H + C2H5 <=> C2H6-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1e+14, 'cm^3/(mol*s)', '+|-', 1e+13),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        comment = '[169] Sillesen , A.; Ratajczak, E.; Pagsberg, P. Chem. Phys. Lett. 1993, 201, 171.\nData derived from fitting to a complex mechanism. Excitation: radiolysis, analysis: IR absroption. Pressure 0.10 bar\n\nH + C2H5 (+ M) --> C2H6 (+ M) (Rxn. 2b)\n\n***NHP***\nVerified by Greg Magoon; I changed the DA uncertainty from (times/divide)1.1 to (+/-)1E13, as this is what the abstract reports (also, Table 3 mentions uncertainties in the range of 10%-20%)\n\nConverted to training reaction from rate rule: H_rad;C_rad/H2/Cs',
    ),
    rank = 11,
    shortDesc = u"""Sillensen et al [169]""",
)

entry(
    index = 59,
    label = "H + C3H7-2 <=> C3H8-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2e+13, 'cm^3/(mol*s)', '*|/', 3.16),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
        comment = '[134] Warnatz, J. Rate coefficeints in the C/H/O system. In Combustion Chemistry, 1984; pp 197.\n\nConverted to training reaction from rate rule: H_rad;C_rad/H/NonDeC',
    ),
    rank = 10,
    shortDesc = u"""Warnatz [134] literature review.""",
)

entry(
    index = 60,
    label = "H + C2H3 <=> C2H4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.21e+14, 'cm^3/(mol*s)', '+|-', 4.82e+13),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        comment = '[171] Fahr, A.; Laufer, A.; Klein, R.; Braun, W. J. Phys. Chem. 1991, 95, 3218.\nAbsolute value measured directly. Excitation: flash photolysis, analysis : Vis-UV absorption. Pressure 0.13 atm. Original uncertainty 4.8E+13\n\nH + C2H3 -> C2H4 (Rxn. VIIC)\n\n***NHP***\nVerified by Greg Magoon; note that the value in rateLibrary agrees with value reported in abstract, the value in Table III also includes contribution from Rxn. VIID, which apparently dominates at low pressures (p. 3222); DA uncertainty updated, as I have done elsewhere; also, for k, I calculate 1.2044E14 (which is very slightly different from 1.21 used here)\n\nConverted to training reaction from rate rule: H_rad;Cd_pri_rad',
    ),
    rank = 6,
    shortDesc = u"""Fahr et al. [171]""",
)

entry(
    index = 61,
    label = "H + C2H <=> C2H2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.81e+14, 'cm^3/(mol*s)', '*|/', 3),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = '[89] Tsang, W.; Hampson, R. F. J. Phys. Chem. Ref. Data 1986, 15, 1087.\nH + C2H --> C2H2\n\npg 1101, Chemical Kinetic Database For Combustion Chemistry, 2. Index of Reactions and Summary of Recommended Rate Expressions. No. 21,4.\n\nVerified by Karma James\n\nNOTE: Reported rate coefficients are for k_inf (MRH 11Aug2009)\n\npg. 1218-1219: Discussion on evaluated data\n\nRecommended data (k_inf) based on reverse rate and equilibrium constant\n\nFall-off and collisional efficiencies are available in reference\n(although we do not store them in RMG_database)\nMRH 28-Aug-2009\n\nConverted to training reaction from rate rule: H_rad;Ct_rad/Ct',
    ),
    rank = 10,
    shortDesc = u"""Tsang [89] literature review.""",
)

entry(
    index = 62,
    label = "H + C6H5 <=> C6H6-4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.2e+14, 'cm^3/(mol*s)', '+|-', 8e+13),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1200, 'K'),
        comment = '[172] Davis, S. G.; Wang, H.; Brezinsky K.; Law C. K. Symp. Int. Combust. Proc. 1996, 26, 1025.\n(1000-1200K, excitation : thermal, pressure 1.0 atm)\n\n[173] Ackerman, L.; Hippler, H.; Pagsberg, P.; Reihs, C.; Troe, J. J. Phys. Chem. 1990, 94, 5247. \n(300K, absolute value measured directly, excitation : flash photolysis, analysis : VIS-UV absorption, pressure 0.01-0.99 atm) \n\n[172b] Emdee, J. L., Brezinsky, K., and Glassman, I., J. Phys. Chem. 96:21512161 (1992) DOI: 10.1021/j100184a025\nH + phenyl --> benzene (R1 in [172]) (Reaction 1 in [172b])\nVerified by Greg Magoon\n[172]: reported rate coefficient is for k_inf (see Table 1); temperature range considered is 1000-1200 K; this paper cites: Emdee, J. L., Brezinsky, K., and Glassman, I., J. Phys. Chem. 96:21512161 (1992) DOI: 10.1021/j100184a025 (included as 172b, above), which, in turn, references [173] (Troe) paper...conditions for this paper are 1100 K - 1200 K\n[173]: this contains the uncertainty estimate (see Table 2); I updated the DA uncertainty as I have done elsewhere; this seems to be the actual raw value that was subsequently interpreted/used in the paper cited by Ref. 172; conditions are 300 K and 1 bar, so apparently, the paper cited by Ref. 172 and/or Ref. 172 itself has assumed that it is in high-pressure limit and that it is temperature independent\n[172b]: see Table III\n\nConverted to training reaction from rate rule: H_rad;Cb_rad',
    ),
    rank = 6,
    shortDesc = u"""Davis et al. [172] Ackermann et al. [173] Emdee et al. [172b]""",
)

entry(
    index = 63,
    label = "H + CHO <=> CH2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.68e+10, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-18.9535, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1500, 'K'),
        Tmax = (1900, 'K'),
        comment = '[174] Tsuboi, T.; Katoh, M.; Kikuchi, S.; Hashimoto, K. Jpn J. Appl. Phys. 1981, 20, 985.\nData is estimated. Pressure 7.0 atm. \n\nH + HCO (+M) --> H2CO (+M) (Rxn -9)\n\n***NHP*** possible improvement for A (for rho = 1E-4): 6.61E10\nVerified by Greg Magoon; three A factors have been reported (for 3 different densities); the value currently used in the rateLibrary appears to come from the middle density: 5E-5 (mol/cm^3, I think);I have assumed that the 2nd two columns in Table II are for the reverse reaction reference for this value is apparently in Japanese (see *** note in Table 2); minor issue: I calculate -19/4.184 = -4.54 kcal/mol (vs. -4.53 in rateLibrary)\n\nConverted to training reaction from rate rule: H_rad;CO_pri_rad',
    ),
    rank = 10,
    shortDesc = u"""Tsuboi et al. [174]""",
)

entry(
    index = 64,
    label = "H + OH <=> H2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.62e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0.6276, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2100, 'K'),
        comment = '[106] Cobos, C. J.; Troe, J. J. Chem. Phys. 1985, 83, 1010. \nTransition State Theory\n\nH + OH --> H2O\n\nConverted to training reaction from rate rule: H_rad;O_pri_rad',
    ),
    rank = 6,
    shortDesc = u"""Cobos et al. [106]""",
)

entry(
    index = 65,
    label = "CH3 + CH3 <=> C2H6-3",
    degeneracy = 0.5,
    kinetics = Arrhenius(
        A = (4.13e+17, 'cm^3/(mol*s)'),
        n = -1.4,
        Ea = (4.184, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
        comment = "[175] Pesa, M. ; Pilling, M. J.; Robertson, S. H.; Wardlaw. J. Phys. Chem. A 1998, 102, 8526.\nCanonical Flexible Transition State Theory \n\nCH3 + CH3 --> C2H6 (Same as 438) (Rxn. R1)\n\nNIST record: http://kinetics.nist.gov/kinetics/Detail?id=1998PES/PIL8526-8536:1\nVerified by Greg Magoon; NIST record has slightly different parameters than RMG (it doesn't seem like best-fit parameters are reported in the paper); paper values for k_inf with alpha = 1 appear in Tables 5/11 and values for alpha = 0.7 appear in Tables 6/12; NIST parameters agree within 10% of k_inf values in the paper with alpha = 1 A^-1 (Tables 11) (though in paper, they seem to suggest that alpha = 0.7 A^-1 (Table 6/12) matches experimental data better); I am assuming that their k is for the reaction, as written, so that no factor of two correction is needed; RMG parameters seem to agree with Table 5 values within 10% (agreement may not be quite as good as NIST fit, though it is not immediately obvious which fit is better without looking closer/doing calculations)\n\nConverted to training reaction from rate rule: C_methyl;C_methyl",
    ),
    rank = 6,
    shortDesc = u"""Pesa et al. [175]""",
)

entry(
    index = 66,
    label = "CH3 + C2H5 <=> C3H8-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.37e+13, 'cm^3/(mol*s)', '*|/', 2),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
        comment = '[94] Baulch, D. L.; Cobos, C. J.; Cox, R. A.; Frank, P.; Hayman, G.; Just, T.; Kerr, J. A.;\nMurrells, T.; Pilling, M. J.; Troe, J.; Walker, R. W.; Warnatz, J. J. Phys. Chem. Ref. Data 1994, 23, 847.\n\nCH3 + C2H5 --> C3H8\n\npg 871 Evaluated Kinetic Data for Combustion Modelling Supplement 1, Table 3. Combination reactions.\n\nRMG data matches reference data for k(infinity).\n\nVerified by Karma James\n\npg.991: Discussion on evaluated data\n\nCH3+C2H5(+m) --> C3H8(+m): RMG stores the recommended high-pressure limit rate coefficient,\n\nk_inf.  "The recommended value for k_inf is a weighted average of earlier experiments\nin agreement with SACM calculations following Ref.10.  A temperature independent value\nof k_inf is assumed until more definite experimental information is available."\nMRH 31-Aug-2009\n\nConverted to training reaction from rate rule: C_methyl;C_rad/H2/Cs',
    ),
    rank = 10,
    shortDesc = u"""Baulch et al. [94] literature review.""",
)

entry(
    index = 67,
    label = "CH3 + C3H7-2 <=> C4H10-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.64e+14, 'cm^3/(mol*s)'),
        n = -0.57,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (713, 'K'),
        Tmax = (1800, 'K'),
        comment = '[176] Tsang, W. Combust. Flame 1989, 78, 71. \nRRK(M) extrapolation. \n\nCH3 + iso-C3H7 --> iso-C4H10 \n\nVerified by Greg Magoon; high-pressure rate constants are reported here; \nI don\'t immediately see an explicit temperature range for the polynomial fits, \nbut the domain of the graphs agrees pretty well with the range in the rateLibrary \n(though the graphs seem to go slightly higher, to 2000 K); the abstract says \n"from room to combustion temperatures", so if anything, the range specified in \nthe rateLibrary is probably too narrow; minor: I calculate 1.1E-9*6.022141E23=6.624E14, \nbut rateLibrary has slightly different value of 6.64E14\n\nConverted to training reaction from rate rule: C_methyl;C_rad/H/NonDeC',
    ),
    rank = 10,
    shortDesc = u"""Tsang [176] RRK(M) extrapolation.""",
)

entry(
    index = 68,
    label = "CH3 + C4H9 <=> C5H12",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.88e+15, 'cm^3/(mol*s)', '*|/', 2),
        n = -1,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = "[92] Tsang, W. J. Phys. Chem. Ref. Data 1990, 19, 1.\n\nCH3 + tert-C4H9 --> neo-C5H12\n\npg 7, Chemical Kinetic Database For Combustion Chemistry, Part 4 - Isobutane. \n\nIndex of Reactions and Summary of Recommended Rate Expressions. No. 44,16.\nVerified by Karma James\n\nNOTE: Data entry was not consistent w/recommended value in reference (pg. 36)\n\nMRH computes A=4.88E+15, n=-1, E=0, dA=*2.0 (11Aug2009)\n\nMRH interprets data in reference as 2.7E-11*(300/T)^-1, NOT 2.7E-11*exp(300/T)\n\nNOTE: kinetics.nist.gov has 2.7E-11*exp(300/T) expression in database\n\nkinetics.nist.gov also has A/n/E from 2006 paper by Klippenstein et al.;\nthe new rate expression matches Klippenstein's value better across the valid T range\npg.36: Discussion on evaluated data\n\nEntry 44,16(b)\n\nMRH computed geometric mean of CH3+CH3-->adduct (1.68x10^-9 * T^-0.64) and tC4H9+tC4H9-->adduct\n\n(4x10^-12 * (300/T)^1.5) to obtain: 5.909x10^-9 * T^-1.07.  Setting the temperature\nexponent equal to one and multiplying by 1 (*300/300) results in: 1.970x10^-11 * (300/T)\nwhich is somewhat in agreement with the value recommended by Tsang.\nMRH 31-Aug-2009\n\nConverted to training reaction from rate rule: C_methyl;C_rad/Cs3",
    ),
    rank = 10,
    shortDesc = u"""Tsang [92] literature review.""",
)

entry(
    index = 69,
    label = "CH3 + C2H3 <=> C3H6",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (7.23e+13, 'cm^3/(mol*s)', '+|-', 1.81e+13),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        comment = '[171] Fahr, A.; Laufer, A.; Klein, R.; Braun, W. J. Phys. Chem. 1991, 95, 3218.\nAbsolute value measured directly. Excitation: flash photolysis, analysis : Vis-UV absorption. Pressure 0.13 atm. Original Uncertainty 1.8E+13\n\nCH3. + .HC=CH2 --> CH3HC=CH2 (Rxn. IIIC)\n\n***NHP***\nVerified by Greg Magoon; DA uncertainty updated, as I have done elsewhere\n\nConverted to training reaction from rate rule: C_methyl;Cd_pri_rad',
    ),
    rank = 6,
    shortDesc = u"""Fahr et al. [171]""",
)

entry(
    index = 70,
    label = "CH3 + C6H5 <=> C7H8-5",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.38e+13, 'cm^3/(mol*s)', '+|-', 8e+11),
        n = 0,
        Ea = (0.192464, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (980, 'K'),
        comment = "[177] Tokmakov, I. V.; Park, J.; Gheyas, S. I.; Lin, M. C. J. Phys. Chem. A. 1999, 103, 3636.\nData Derived from detailed balance/reverse rate. Uncertainty 8.0E-2. \n\nCH3 + phenyl --> C6H5CH3 (Rxn. 2) (cf. #444, below)\n\n***NHP***\nVerified by Greg Magoon; 0.05 kcal barrier changed to 0.046 as reported in paper; uncertainties are in abstract; more precise values appear in Tables 3,4; however, note: in text on p. 3639, A factor uncertainty is expressed as additive on log scale...value is relatively small, so it probably doesn't make that much of a difference; DA uncertainty was added and DE0 uncertainty was refined\n\nConverted to training reaction from rate rule: C_methyl;Cb_rad",
    ),
    rank = 6,
    shortDesc = u"""Tokmakov et al. [177]""",
)

entry(
    index = 71,
    label = "CH3 + CHO <=> C2H4O",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.81e+13, 'cm^3/(mol*s)', '*|/', 2),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = '[89] Tsang, W.; Hampson, R. F. J. Phys. Chem. Ref. Data 1986, 15, 1087.\nCH3 + HCO --> CH3CHO \n\npg 1095, Chemical Kinetic Database For Combustion Chemistry, 2. Index of Reactions and Summary of Recommended Rate Expressions. No. 16,15.\n\nVerified by Karma James\n\npg. 1167: Discussion on evaluated data\n\nRecommended data calculated using reverse rate and equilibrium constant\n\nAuthors note that their RRKM calculations suggest that rxn is very close\nto high-P limit at low temperatures.\nMRH 28-Aug-2009\n\nConverted to training reaction from rate rule: C_methyl;CO_pri_rad',
    ),
    rank = 10,
    shortDesc = u"""Tsang [89] literature review.""",
)

entry(
    index = 72,
    label = "CH3 + C2H3O <=> C3H6O",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.2e+13, 'cm^3/(mol*s)', '+|-', 8.4e+12),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        comment = '[179] Hassinen, E.; Kalliorinne, K; Koskikallio, J. Int. J. Chem. Kinet. 1990, 22, 741\nData derived from fitting to a complex mechanism. Excitation : direct photolysis, analysis : GC. Pressure 96? and 99 kPa with He, 5.5 kPa and 25 kPa with CO2. \n\nCH3CO. + .CH3 --> (CH3)2CO (Rxn. 6)\n\npaper states reaction occurs close to high pressure limit (p. 742)\nVerified by Greg Magoon; Note that the paper cites 4 other values for k6 from literature; perhaps uncertainty could be assigned based on these values; also, page 744 discusses "relatively large value of k6" potentially due to other reactions; p. 744: uncertainty estimated to be 20% -> I changed DA uncertainty from 0 to 8.4E+12\n\nConverted to training reaction from rate rule: C_methyl;CO_rad/NonDe',
    ),
    rank = 10,
    shortDesc = u"""Hassinen et al [179]""",
)

entry(
    index = 73,
    label = "CH3 + OH <=> CH4O",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.03e+13, 'cm^3/(mol*s)', '*|/', 2),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
        comment = '[94] Baulch, D. L.; Cobos, C. J.; Cox, R. A.; Frank, P.; Hayman, G.; Just, T.; Kerr, J. A.;\nMurrells, T.; Pilling, M. J.; Troe, J.; Walker, R. W.; Warnatz, J. J. Phys. Chem. Ref. Data 1994, 23, 847.\n\nCH3 + .OH --> CH3OH\n\npg 871 Evaluated Kinetic Data for Combustion Modelling Supplement 1, Table 3. Combination reactions.\n\nRMG data matches reference data for k(infinity).\n\nVerified by Karma James\n\npg.933-934: Discussion of evaluated data\n\nOH+CH3(+m) --> CH3OH(+m): RMG stores the recommended high-pressure limit rate coefficient,\n\nk_inf.  "The available database is still limited and more measurements are needed.\n... The preferred k_inf is consistent with SACM estimates ..."\nMRH 31-Aug-2009\n\nConverted to training reaction from rate rule: C_methyl;O_pri_rad',
    ),
    rank = 10,
    shortDesc = u"""Baulch et al. [94] literature review.""",
)

entry(
    index = 74,
    label = "CH3 + CH3O <=> C2H6O",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.21e+13, 'cm^3/(mol*s)', '*|/', 5),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = '[89] Tsang, W.; Hampson, R. F. J. Phys. Chem. Ref. Data 1986, 15, 1087.\nCH3 + CH3O --> (CH3)2O\n\npg 1104, Chemical Kinetic Database For Combustion Chemistry, 2. Index of Reactions and Summary of Recommended Rate Expressions. No. 24,16.\n\nVerified by Karma James\n\npg. 1247: Discussion on evaluated data\n\nRecommended data from study by Gray, Shaw, and Thynne (1967).  Expression was\n\nestimated from rates of CH3+CH3=C2H6 and CH3O+CH3O=CH3OOCH3.\nMRH 28-Aug-2009\n\nConverted to training reaction from rate rule: C_methyl;O_rad/NonDe',
    ),
    rank = 10,
    shortDesc = u"""Tsang [89] literature review.""",
)

entry(
    index = 75,
    label = "C2H5 + C2H5 <=> C4H10-3",
    degeneracy = 0.5,
    kinetics = Arrhenius(
        A = (5.75e+12, 'cm^3/(mol*s)', '*|/', 2),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1200, 'K'),
        comment = '[95] Baulch, D. L.; Cobos, C. J.; Cox, R. A.; Esser, C.; Frank, P.; Just, T.; Kerr, \nJ. A.; Pilling, M. J.; Troe, J.; Walker, R. W.; Warnatz, J. J. Phys. Chem. Ref. Data 1992, 21, 411.\n\n.C2H5 + .C2H5 --> n-C4H10 \n\npg.707: Discussion on evaluated data\n\nC2H5+C2H5 --> nC4H10: "The preferred rate coefficient is the mean of the results of\n\nParkes and Quinn, Adachi et al., Demissy and Lesclaux, Pacey and Wimalasena,\nMunk et al., Arthur, and Anastasi and Arthur which are all in substantial \nagreement."\nMRH 31-Aug-2009\n\nConverted to training reaction from rate rule: C_rad/H2/Cs;C_rad/H2/Cs',
    ),
    rank = 10,
    shortDesc = u"""Baulch et al. [95] literature review.""",
)

entry(
    index = 76,
    label = "C2H5 + C3H7-2 <=> C5H12-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.15e+14, 'cm^3/(mol*s)', '*|/', 2),
        n = -0.35,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = '[91] Tsang, W. J. Phys. Chem. Ref. Data 1988, 17, 887.\nC2H5 + iso-C3H7 --> iso-C5H12\n\npg 894, Chemical Kinetic Database For Combustion Chemistry, Part 3. Index of Reactions and Summary of Recommended Rate Expressions. No. 42,17.\n\nVerified by Karma James\n\npg. 937-938: Discussion on evaluated data\n\nEntry 42,17 (a): No data available at the time.  The author obtains the recommended\n\nrate coefficient expression by using the geometric mean rule (using the rxn rates\nof C2H5+C2H5-->adduct and i-C3H7+i-C3H7-->adduct).\nMRH 30-Aug-2009\n\nConverted to training reaction from rate rule: C_rad/H2/Cs;C_rad/H/NonDeC',
    ),
    rank = 10,
    shortDesc = u"""Tsang [91] literature review.""",
)

entry(
    index = 77,
    label = "C2H5 + C4H9 <=> C6H14",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.91e+14, 'cm^3/(mol*s)', '*|/', 2),
        n = -0.75,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = '[92] Tsang, W. J Phys. Chem. Ref. Data 1990, 19, 1.\nC2H5 + tert-C4H9 --> (CH3)3CCH2CH3\n\n//DOES NOT MATCH! Reference: A = 9.6E+12, E0 = 0, n = -0.75, Database: A = 6.91E+14, E0 = 0, n = -0.75\n\n//pg 7, Chemical Kinetic Database For Combustion Chemistry, Part 4 - Isobutane. \n\n//Index of Reactions and Summary of Recommended Rate Expressions. No. 44,17.\n\n//Verified by Karma James\n\npg. 37\n\nData reported as kc = 1.6e-11 * (300/T)^0.75\n\nWhen lumping the 1.6e-11 * 300^0.75, attain A=6.94e+14\nNo experimental data, at the time\n\nVerified by MRH on 10Aug2009\n\npg.37: Discussion on evaluated data\n\nEntry 44,17(c): Recommended rate calculated by taking geometric mean of C2H5+C2H5-->adduct\n\nand tC4H9+tC4H9-->adduct rxns.\nMRH 31-Aug-2009\n\nConverted to training reaction from rate rule: C_rad/H2/Cs;C_rad/Cs3',
    ),
    rank = 10,
    shortDesc = u"""Tsang [92] literature review.""",
)

entry(
    index = 78,
    label = "C2H5 + CHO <=> C3H6O-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.81e+13, 'cm^3/(mol*s)', '*|/', 3),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = '[89] Tsang, W.; Hampson, R. F. J. Phys. Chem. Ref. Data 1986, 15, 1087.\nC2H5 + HCO --> C2H5CHO\n\npg 1097, Chemical Kinetic Database For Combustion Chemistry, 2. Index of Reactions and Summary of Recommended Rate Expressions. No. 17,15.\n\nVerified by Karma James\n\npg. 1179: Discussion on evaluated data\n\nRecommended data is based on the rate expression for CH3+CHO-->H3CCHO\n\nMRH 28-Aug-2009\n\nConverted to training reaction from rate rule: C_rad/H2/Cs;CO_pri_rad',
    ),
    rank = 10,
    shortDesc = u"""Tsang [89] literature review.""",
)

entry(
    index = 79,
    label = "C2H5 + C2H3O <=> C4H8O",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.12e+14, 'cm^3/(mol*s)', '*|/', 3),
        n = -0.5,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = '[89] Tsang, W.; Hampson, R. F. J. Phys. Chem. Ref. Data 1986, 15, 1087.\nC2H5 + CH3CO --> C2H5COCH3\n\npg 1103, Chemical Kinetic Database For Combustion Chemistry, 2. Index of Reactions and Summary of Recommended Rate Expressions. No. 22,17.\n\nVerified by Karma James\n\npg. 1234: Discussion on evaluated data\n\nRecommended data is based on the rate expression for CH3+CH3CO-->(CH3)2CO\n\nMRH 28-Aug-2009\n\nConverted to training reaction from rate rule: C_rad/H2/Cs;CO_rad/NonDe',
    ),
    rank = 10,
    shortDesc = u"""Tsang [89] literature review.""",
)

entry(
    index = 80,
    label = "C2H5 + OH <=> C2H6O-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (7.7e+13, 'cm^3/(mol*s)', '+|-', 1e+13),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (400, 'K'),
        comment = "[180] Fagerstrom, K.; Lund, A.; Mahmoud, G.; Jodkowski, J. T.; Ratajczak, E. Chem. Phys. Lett. 1993, 208, 321\nExcitation : radiolysis, analysis : VIS-UV absorption. Pressure 0.25-0.99 bar SF6. Original Uncertainty 1.0E+13. \n\nC2H5 + OH (+M) --> C2H5OH (+M) (Rxn. 1a)\n\nVerified by Greg Magoon; value reported for k1a,Infinity (high-pressure) appears to be theoretical rather than experimentally based; value in paper is 7.7+/-1.0E13 (rateLibrary originally had 7.69E13 with uncertainty of *1.1, so I changed it to match paper values); there doesn't seem to be an experimental value for k1a, but k(1a+1b) is slightly lower (6.5E13); experimentally, they say no pressure dependence observed in studied pressure range (p. 326)\n\nConverted to training reaction from rate rule: C_rad/H2/Cs;O_pri_rad",
    ),
    rank = 10,
    shortDesc = u"""Fagerstrom et al. [180]""",
)

entry(
    index = 81,
    label = "C3H7-2 + C3H7-2 <=> C6H14-2",
    degeneracy = 0.5,
    kinetics = Arrhenius(
        A = (1.625e+14, 'cm^3/(mol*s)', '*|/', 2),
        n = -0.7,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = '[91] Tsang, W. J. Phys. Chem. Ref. Data 1988, 17, 887.\nIso-C3H7 + iso-C3H7 --> (CH3)2CHCH(CH3)2\n\npg 895, Chemical Kinetic Database For Combustion Chemistry, Part 3. Index of Reactions and Summary of Recommended Rate Expressions. No. 42,42.\n\n//NOTE: For A value, Database value = 3.25E+14 and Reference value = 6.023E+12\n\nVerified by Karma James\n\nMRH computes reference A value = 3.26E+14 (11Aug2009)\n\npg. 946-947: Discussion on evaluated data\n\nEntry 42,42 (a): Multiple data available at low T.  Author fit experimentally reported\n\ndata to obtain recommended rate coefficient expression.  Note: the author states\nthat more high-Temperature data points are necessary (to ensure a reasonable\nfit at high-T).\nMRH 30-Aug-2009\n\nConverted to training reaction from rate rule: C_rad/H/NonDeC;C_rad/H/NonDeC',
    ),
    rank = 10,
    shortDesc = u"""Tsang [91] literature review.""",
)

entry(
    index = 82,
    label = "C3H7-2 + C4H9 <=> C7H16",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.12e+15, 'cm^3/(mol*s)', '*|/', 1.5),
        n = -1.1,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = '[92] Tsang, W. J Phys. Chem. Ref. Data 1990, 19, 1.\nIso-C3H7 + tert-C4H9 --> 2,2,3-trimethyl-butane\n\n//DOES NOT MATCH! Reference: A = 7.83E+12, E0 = 0, n = -1.1, Database: A = 4.12E+15, E0 = 0, n = -1.1\n\n//pg 8, Chemical Kinetic Database For Combustion Chemistry, Part 4 - Isobutane. \n\n//Index of Reactions and Summary of Recommended Rate Expressions. No. 44,42.\n\n//Verified by Karma James\n\npg. 46\n\nData reported as kc = 1.3e-11 * (300/T)^1.1\n\nWhen lumping the 1.3e-11 * 300^1.1, attain A=4.15e+15\nNo experimental data, at the time\n\nVerified by MRH on 10Aug2009\n\nEntry 44,42(c): Recommended rate computed using geometric mean of iC3H7+iC3H7-->adduct\n\nand tC4H9+tC4H9-->adduct rxns.\nMRH 31-Aug-2009\n\nConverted to training reaction from rate rule: C_rad/H/NonDeC;C_rad/Cs3',
    ),
    rank = 10,
    shortDesc = u"""Tsang [92] literature review.""",
)

entry(
    index = 83,
    label = "C3H7-2 + C2H3O <=> C5H10O",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.64e+13, 'cm^3/(mol*s)', '*|/', 2),
        n = -0.35,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = '[91] Tsang, W. J. Phys. Chem. Ref. Data 1988, 17, 887.\nIso-C3H7 + CH3CO --> iso-C3H7COCH3\n\npg 895, Chemical Kinetic Database For Combustion Chemistry, Part 3. Index of Reactions and Summary of Recommended Rate Expressions. No. 42,22.\n\n//NOTE: For A value, Database value = 6.64E+13 and Reference value = 9.03E+12\n\nVerified by Karma James\n\nMRH computes reference A value = 6.65E+13 (11Aug2009)\n\npg. 943: Discussion on evaluated data\n\nEntry 42,22: No data available at the time.  Author uses the geometrical mean rule\n\n(for the rxns i-C3H7+i-C3H7-->adduct and CH3CO+CH3CO-->adduct) to obtain \nrecommended rate coefficient expression\nMRH 30-Aug-2009\n\nConverted to training reaction from rate rule: C_rad/H/NonDeC;CO_rad/NonDe',
    ),
    rank = 10,
    shortDesc = u"""Tsang [91] literature review.""",
)

entry(
    index = 84,
    label = "C3H7-2 + CH3O <=> C4H10O",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.03e+12, 'cm^3/(mol*s)', '*|/', 5),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = '[91] Tsang, W. J. Phys. Chem. Ref. Data 1988, 17, 887.\nIso-C3H7 + CH3O --> i-C3H7OCH3\n\npg 895, Chemical Kinetic Database For Combustion Chemistry, Part 3. Index of Reactions and Summary of Recommended Rate Expressions. No. 42,24.\n\nVerified by Karma James\n\npg. 943: Discussion on evaluated data\n\nEntry 42,24 (b): No data available at the time.  Author recommends rate coefficient\n\nbased on CH3+CH3O-->adduct.\nMRH 30-Aug-2009\n\nConverted to training reaction from rate rule: C_rad/H/NonDeC;O_rad/NonDe',
    ),
    rank = 10,
    shortDesc = u"""Tsang [91] literature review.""",
)

entry(
    index = 85,
    label = "C4H9 + C4H9 <=> C8H18",
    degeneracy = 0.5,
    kinetics = Arrhenius(
        A = (6.2e+15, 'cm^3/(mol*s)', '*|/', 2),
        n = -1.5,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = '[92] Tsang, W. J Phys. Chem. Ref. Data 1990, 19, 1.\nTert-C4H9 + tert- C4H9 --> (CH3)3CC(CH3)3\n\n//DOES NOT MATCH! Reference: A = 2.4E+12, E0 = 0, n = -1.5, Database: A = 1.24E+16, E0 = 0, n = -1.5\n\n//pg 8, Chemical Kinetic Database For Combustion Chemistry, Part 4 - Isobutane. \n\n//Index of Reactions and Summary of Recommended Rate Expressions. No. 44,44.\n\n//Verified by Karma James\n\npg. 47\n\nData reported as ka = 4e-12 * (300/T)^1.5\n\nWhen lumping the 4e-12 * 300^1.5, attain A=1.25e+16\nRecommended data taken from expression computed by Parkes, Quinn (1976)\n\nVerified by MRH on 10Aug2009\n\nEntry 44,44(a)\n\nMRH 31-Aug-2009\n\nConverted to training reaction from rate rule: C_rad/Cs3;C_rad/Cs3',
    ),
    rank = 10,
    shortDesc = u"""Tsang [92] literature review.""",
)

entry(
    index = 86,
    label = "C4H9 + CHO <=> C5H10O-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.21e+13, 'cm^3/(mol*s)', '*|/', 5),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = '[92] Tsang, W. J Phys. Chem. Ref. Data 1990, 19, 1.\nTert-C4H9 + HCO --> tert-C4H9CHO\n\npg 7, Chemical Kinetic Database For Combustion Chemistry, Part 4 - Isobutane. \n\nIndex of Reactions and Summary of Recommended Rate Expressions. No. 44,15.\n\nVerified by Karma James\n\npg.36: Discussion on evaluated data\n\nEntry 44,15(b): No data available at the time.  Recommended rate coefficient is based\n\non rate of rxn tC4H9+CH3-->adduct, but "slightly smaller"\nMRH 31-Aug-2009\n\nConverted to training reaction from rate rule: C_rad/Cs3;CO_pri_rad',
    ),
    rank = 10,
    shortDesc = u"""Tsang [92] literature review.""",
)

entry(
    index = 87,
    label = "C4H9 + C2H3O <=> C6H12O",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (7.75e+14, 'cm^3/(mol*s)', '*|/', 2),
        n = -0.75,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = '[92] Tsang, W. J Phys. Chem. Ref. Data 1990, 19, 1.\nTert-C4H9 + CH3CO --> tert-C4H9COCH3\n\n//DOES NOT MATCH! Reference: A = 1.08E+13, E0 = 0, n = -0.75, Database: A = 7.75E+14, E0 = 0, n = -0.75\n\n//pg 7, Chemical Kinetic Database For Combustion Chemistry, Part 4 - Isobutane. \n\n//Index of Reactions and Summary of Recommended Rate Expressions. No. 44,22.\n\n//Verified by Karma James\n\npg. 42\n\nData reported as k = 1.8e-11 * (300/T)^0.75\n\nWhen lumping the 1.8e-11 * 300^0.75, attain A=7.81e+14\nNo experimental data, at the time\n\nVerified by MRH on 10Aug2009\n\nEntry 44,22: Recommended rate coefficient computed using geometric mean rule of\n\ntC4H9+tC4H9-->adduct and CH3CO+CH3CO-->adduct rxns\nMRH 31-Aug-2009\n\nConverted to training reaction from rate rule: C_rad/Cs3;CO_rad/NonDe',
    ),
    rank = 10,
    shortDesc = u"""Tsang [92] literature review.""",
)

entry(
    index = 88,
    label = "C4H9 + CH3O <=> C5H12O",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (9.04e+12, 'cm^3/(mol*s)', '*|/', 3),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = '[92] Tsang, W. J Phys. Chem. Ref. Data 1990, 19, 1.\nTert-C4H9 + CH3O --> tert-C4H9OCH3\n\npg 8, Chemical Kinetic Database For Combustion Chemistry, Part 4 - Isobutane. \n\nIndex of Reactions and Summary of Recommended Rate Expressions. No. 44,24.\n\nVerified by Karma James\n\npg.42-43: Discussion on evaluated data\n\nEntry 44,24(b): Rate coefficient calculated using geometric mean rule of tC4H9+tC4H9-->adduct\n\nand CH3O+CH3O-->adduct rxns\nMRH 31-Aug-2009\n\nConverted to training reaction from rate rule: C_rad/Cs3;O_rad/NonDe',
    ),
    rank = 10,
    shortDesc = u"""Tsang [92] literature review.""",
)

entry(
    index = 89,
    label = "C2H3 + C2H3 <=> C4H6-4",
    degeneracy = 0.5,
    kinetics = Arrhenius(
        A = (3.615e+13, 'cm^3/(mol*s)', '+|-', 1.2e+13),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        comment = '[171] Fahr, A.; Laufer, A.; Klein, R.; Braun, W. J. Phys. Chem. 1991, 95, 3218.\nAbsolute value measured directly. Excitation: flash photolysis, analysis : Vis-UV absorption. Original Uncertainty 1.2E+13. \n\nC2H3 + C2H3 --> (E)-CH2=CHCH=CH2 (Rxn. IIC)\n\nVerified by Greg Magoon; DA uncertainty updated, as I have done elsewhere; based on Eqs. 3, 6, it looks like a factor of two correction is not needed\n\nConverted to training reaction from rate rule: Cd_pri_rad;Cd_pri_rad',
    ),
    rank = 10,
    shortDesc = u"""Fahr et al. [171]""",
)

entry(
    index = 90,
    label = "C2H3 + C2H <=> C4H4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (700, 'K'),
        Tmax = (1300, 'K'),
        comment = '[165] Duran, R. P.; Amorebieta, V. T.; Colussi, A. J. J. Phys. Chem. 1988, 92, 636.\nAb initio. Pressure 0.10-1.0 atm. \n\nC2H3 +.C2H --> CH2=CHC=CH (Rxn. 25)\n\nNIST record: http://kinetics.nist.gov/kinetics/Detail?id=1988DUR/AMO636:4\nVerified by Greg Magoon; value confirmed from paper data in Table III; this is presumably high-pressure limit since no pressure-dependence is indicated in the table\n\nConverted to training reaction from rate rule: Cd_pri_rad;Ct_rad/Ct',
    ),
    rank = 6,
    shortDesc = u"""Duran et al. [165]""",
)

entry(
    index = 91,
    label = "C2H3 + CHO <=> C3H4O",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.81e+13, 'cm^3/(mol*s)', '*|/', 3),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = '[89] Tsang, W.; Hampson, R. F. J. Phys. Chem. Ref. Data 1986, 15, 1087.\nC2H3 + HCO --> CH2=CHCHO\n\npg 1099, Chemical Kinetic Database For Combustion Chemistry, 2. Index of Reactions and Summary of Recommended Rate Expressions. No. 19,15.\n\nVerified by Karma James\n\npg. 1199: Discussion on evaluated data\n\nRecommended data based on rate expression for CH3+HCO-->CH3CHO\n\nAuthors note that rate expression will be in fall-off region at high temperatures\nMRH 28-Aug-2009\n\nConverted to training reaction from rate rule: Cd_pri_rad;CO_pri_rad',
    ),
    rank = 10,
    shortDesc = u"""Tsang [89] literature review.""",
)

entry(
    index = 92,
    label = "C6H5 + C6H5 <=> C12H10",
    degeneracy = 0.5,
    kinetics = Arrhenius(
        A = (2.85e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (1100, 'K'),
        Tmax = (1400, 'K'),
        comment = '[124] Heckmann, E.; Hippler, H.; Troe, J. Symp. Int. Combust. Proc.1996, 26, 543.\nAbsolute value measured directly. Excitation : thermal, analysis : Vis-UV absorption. \n\nPhenyl + Phenyl --> Biphenyl\n\nConverted to training reaction from rate rule: Cb_rad;Cb_rad',
    ),
    rank = 6,
    shortDesc = u"""Heckmann et al. [124]""",
)

entry(
    index = 93,
    label = "CHO + CHO <=> C2H2O2",
    degeneracy = 0.5,
    kinetics = Arrhenius(
        A = (7.55e+12, 'cm^3/(mol*s)', '+|-', 6.02e+12),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        comment = '[182] Stoeckel, F.; Schuh, M. D.; Goldstein, N.; Atkinson, G.H. Chem. Phys. 1985, 95, 135\nAbsolute value measured directly. Excitation : flash photolysis, abalysis : VIS-UV absorption. Original uncertainty 1.2E+13. Pressure: 10 Torr (this is total pressure; see p. 141)\n\nHCO + HCO --> (CHO)2 \n\n***NHP***\nVerified by Greg Magoon: the existing k in the rateLibrary appeared to be off by a factor of two, since the paper uses d[HCO]/dt=-k*[HCO]^2; they report k=(5+/-2)*10^-11 molecules^-1*cm^3/s (references 9, 19, and 20 in this paper could have better data); I think in rateLibrary, we should have half of this (2.5 +/- 1), so I have changed the value in the rateLibrary accordingly (with 2nd opinion to confirm from MRH)\n\nConverted to training reaction from rate rule: CO_pri_rad;CO_pri_rad',
    ),
    rank = 6,
    shortDesc = u"""Stoeckel et al. [182]""",
)

entry(
    index = 94,
    label = "CHO + C2H3O <=> C3H4O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.81e+13, 'cm^3/(mol*s)', '*|/', 3),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = '[89] Tsang, W.; Hampson, R. F. J. Phys. Chem. Ref. Data 1986, 15, 1087.\nHCO + CH3CO --> CH3COCHO\n\npg 1102, Chemical Kinetic Database For Combustion Chemistry, 2. Index of Reactions and Summary of Recommended Rate Expressions. No. 22,15.\n\nVerified by Karma James\n\npg. 1232: Discussion on evaluated data\n\nRecommended data is assigned a value of 3x10^-11 cm3/molecule*s (This appears to be\n\nthe default value the authors assign for recombination rxns)\nMRH 28-Aug-2009\n\nConverted to training reaction from rate rule: CO_pri_rad;CO_rad/NonDe',
    ),
    rank = 10,
    shortDesc = u"""Tsang [89] literature review.""",
)

entry(
    index = 95,
    label = "C2H3O + C2H3O <=> C4H6O2",
    degeneracy = 0.5,
    kinetics = Arrhenius(
        A = (6.05e+12, 'cm^3/(mol*s)', '*|/', 2),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = '[89] Tsang, W.; Hampson, R. F. J. Phys. Chem. Ref. Data 1986, 15, 1087.\nCH3CO + CH3CO --> (CH3CO)2\n\npg 1103, Chemical Kinetic Database For Combustion Chemistry, 2. Index of Reactions and Summary of Recommended Rate Expressions. No. 22,22.\n\nVerified by Karma James\n\npg. 1234-1235: Discussion on evaluated data\n\nRecommended data is assigned based on 5 reported direct measurements of rate coefficient\n\nMRH 28-Aug-2009\n\nConverted to training reaction from rate rule: CO_rad/NonDe;CO_rad/NonDe',
    ),
    rank = 10,
    shortDesc = u"""Tsang [89] literature review.""",
)

entry(
    index = 96,
    label = "OH + OH <=> H2O2",
    degeneracy = 0.5,
    kinetics = Arrhenius(
        A = (7.85e+12, 'cm^3/(mol*s)', '+|-', 6.02e+12),
        n = (0, '', '+|-', 0.5),
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (400, 'K'),
        comment = '[183] DeMore, W. B.; Sander, S. P.; Golden, D. M.; Hampson, R. F.; Kurylo, M.J.; \nHoward, C. J.; Ravishankara, A. R.; Kolb, C. E.; Molina, M .J. JPL publication 97-4 1997, 1.\n\n(Rate constant is high pressure limit, original uncertainty 6.0E+12) \n\n[97] Atkinson, R.; Baulch, D. L.; Cox, R. A.; Hampson, R. F., jr.; Kerr, J. A.; Rossi, M. J.; Troe, J. \n\nJ. Phys. Chem. Ref. Data 1997, 26, 1329\n\nOH + OH --> H2O2\n\nLiterature review: OH + OH (+m) --> H2OH\n\npg.126: Recommended low-pressure and high-pressure limit rate coefficient\n\npg.130 B2: Discussion on evaluated data.\n\nAuthors recommend the fits by Zellner et al. in N2 and by Forster et al.\nin 1-150kbar He scaled to N2.  RMG stores the high-pressure limit (k_inf)\nrate coefficient.\n*** High-pressure rate coefficient. ***\n\nMRH 1-Sept-2009\n\nConverted to training reaction from rate rule: O_pri_rad;O_pri_rad',
    ),
    rank = 10,
    shortDesc = u"""DeMore et al. [183] literature review.""",
)

entry(
    index = 97,
    label = "CH3O + CH3O <=> C2H6O2",
    degeneracy = 0.5,
    kinetics = Arrhenius(
        A = (9.05e+11, 'cm^3/(mol*s)', '*|/', 5),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = '[89] Tsang, W.; Hampson, R. F. J. Phys. Chem. Ref. Data 1986, 15, 1087.\nCH3O + CH3O --> CH3OOCH3\n\npg 1105, Chemical Kinetic Database For Combustion Chemistry, 2. Index of Reactions and Summary of Recommended Rate Expressions. No. 24,24.\n\nVerified by Karma James\n\npg. 1251: Discussion on evaluated data (in theory)\n\nOnline reference does not contain pg. 1251.  The following discussion is based\non the information provided in the table on pg. 1105\nEntry 24,24 (b)\n\nMRH 28-Aug-2009\n\nConverted to training reaction from rate rule: O_rad/NonDe;O_rad/NonDe',
    ),
    rank = 10,
    shortDesc = u"""Tsang [89] literature review.""",
)

entry(
    index = 98,
    label = "H + CH3 <=> CH4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
        comment = "[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253. \nCurran's estimation, based on half that recommended by Allara and Shaw [146] for H (rad) and R (rad) recombination reactions\n\nConverted to training reaction from rate rule: H_rad;Cs_rad",
    ),
    rank = 11,
    shortDesc = u"""Curran's [8] estimation.""",
)

entry(
    index = 99,
    label = "CH3 + C4H9 <=> C5H12",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.63e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (2.49366, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
        comment = "[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.\nCurran's estimation, based on recommendations of Tsang [92] for CH3 + tC4H9\n\nConverted to training reaction from rate rule: C_methyl;C_ter_rad",
    ),
    rank = 11,
    shortDesc = u"""Curran's [8] estimation.""",
)

entry(
    index = 100,
    label = "CH3 + C3H7-2 <=> C4H10-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.8e+14, 'cm^3/(mol*s)'),
        n = -0.68,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
        comment = "[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.\nCurran's estimation based on half Tsang's [91] recommendation for CH3 + iC3H7\n\nConverted to training reaction from rate rule: C_methyl;C_sec_rad",
    ),
    rank = 11,
    shortDesc = u"""Curran's [8] estimation.""",
)

entry(
    index = 101,
    label = "C2H5 + C3H7-2 <=> C5H12-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.79e+14, 'cm^3/(mol*s)'),
        n = -0.75,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
        comment = "[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.\nCurran's estimation for neoC5H11 + iC3H7, similar to tC4H9 + iC4H9\n\nConverted to training reaction from rate rule: C_pri_rad;C_sec_rad",
    ),
    rank = 11,
    shortDesc = u"""Curran's [8] estimation.""",
)

entry(
    index = 102,
    label = "C2H5 + C4H9 <=> C6H14",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.59e+14, 'cm^3/(mol*s)'),
        n = -0.75,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
        comment = "[8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. Combust. Flame 2002, 129, 253.\nCurran's estimation based on Tsang's [92] reccomendation for tC4H9 Curran's estimation. About a factor of 2 slower than other \n\nvalues from literature for smaller alkyl, based upon the consideration that rate constants decrease with the increasing size of R radical.\n\nConverted to training reaction from rate rule: C_pri_rad;C_ter_rad",
    ),
    rank = 11,
    shortDesc = u"""Curran's [8] estimation.""",
)

entry(
    index = 103,
    label = "OH + CH3O <=> CH4O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
        comment = "[159] Curran, H.J.; Pitz, W.J.; Westbrook, C.K.; Dagaut, P.; Boettner, J.-C.; Cathonnet, M. Int. J. Chem. Kinet. 1998, 30, 229.\nCurran's estimation in DME modeling for ketohydroperoxide decomposition \n\nApparently the number comes from estimate for reverse of Rxn. 337: HO2CH2OCHO -> .OCH2OCHO + .OH (2E13) (p. 234); reverse of Rxn. 191 (p. 238) would also be informative, but it doesn't seem to be disucussed in paper\nVerified by Greg Magoon; it is not immediately clear whether this rate constant is for high pressure limit, but based on other references to high pressure limit in the paper, I suspect that it is a high pressure limit value\n\n*NHP = Not necessarily at high pressure limit\n\nConverted to training reaction from rate rule: O_pri_rad;O_sec_rad",
    ),
    rank = 11,
    shortDesc = u"""Curran's [159] estimation.""",
)

entry(
    index = 104,
    label = "O2 + H <=> HO2-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (8.79e+10, 'cm^3/(mol*s)'),
        n = 1,
        Ea = (1.8828, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        Tmax = (6000, 'K'),
        comment = '[142] Duchovic,R.J; Pettigrew,J D; Welling B; Shipchandler,T. *J. Chem Phys.* **105**, 10367 (1996) http://dx.doi.org/10.1063/1.472992\n\nRRK(M) extrapolation. H + O2 --> OH + O\n\nC.D.W. divided rate expression by 2, to get rate of addition per site.\n\nValues (4.395E+10\t1.00\t0\t0.45) confirmed to fit table (divided by 2) \nby rwest@mit.edu  7-Sep-2009\n\nAgreement with experimental data from Cobos et al. \n(C. J. Cobos, H. Hippler, and J. Troe, *J. Phys. Chem.* 89, 342, 1985)\nwas promising **at low pressures**, but \n"Significant deviations are observed between theory and experiment as the \nhigh-pressure limit is approached."\n    \nE.g., at 298 K\n\n    "However, the value of \n    the high-pressure limit rate coefficient at 298.15 K for the\n    termolecular process computed with TST, model I, and \n    model II does not agree with the estimated high-pressure \n    limit value of Cobos et al. at that temperature. TST, \n    model I, and model II agree with one another, predicting a \n    value of Log10(k)=-10.7 where the value of the limiting \n    high-pressure rate coefficient k=2E-11 cm3/molecule/s at 298.15 K, \n    while Cobos et al. estimate a value of Log10(k)=-10.12 \n    (that is, k=7.5E-11 cm3/molecule/s)"\n    \nThe calculations used the *ab initio* PES of Walch et al., which was the best available in 1991.\n(63) Walch, S. P.; Rohlfing, C. M.; Melius, C. F.; Bauschlicher, C. W. J. Chem. Phys. 1988, 88, 6273. \n(64) Walch, S. P.; Rohlfing, C. M. J. Chem. Phys. 1989, 91, 2373. \n(67) Walch, S. P.; Duchovic, R. J. J. Chem. Phys. 1991, 94, 7068. \n\nMany extensions and improvements are suggested for future work, which may well \nhave happened since the paper was published in 1996. Revision of this rate is recommended.\n\nMoved from R_Addition_MultipleBond on 3-Jun-2010, JDM.\n\nConverted to training reaction from rate rule: O2_birad;H_rad',
    ),
    rank = 10,
    shortDesc = u"""Duchovic et al. [142] RRK(M) extrapolation. Probably could do better.""",
)

entry(
    index = 105,
    label = "HSS + CH3 <=> CH4S2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.94e+09, 'cm^3/(mol*s)'),
        n = 1.25,
        Ea = (-3.09616, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
        comment = '\n\nConverted to training reaction from rate rule: SsJ-S2s;C_methyl',
    ),
    rank = 2,
    shortDesc = u"""A.G. Vandeputte""",
)

entry(
    index = 106,
    label = "CH3S + CH3S <=> C2H6S2",
    degeneracy = 0.5,
    kinetics = Arrhenius(
        A = (5.3e+10, 'cm^3/(mol*s)'),
        n = 1.21,
        Ea = (-3.9748, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
        comment = '\n\nConverted to training reaction from rate rule: SsJ-Cs;SsJ-Cs',
    ),
    rank = 2,
    shortDesc = u"""A.G. Vandeputte""",
)

entry(
    index = 107,
    label = "CH3S-2 + H <=> CH4S",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5e+11, 'cm^3/(mol*s)'),
        n = 0.65,
        Ea = (-1.54808, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
        comment = '\n\nConverted to training reaction from rate rule: C_rad/H2/S;H_rad',
    ),
    rank = 2,
    shortDesc = u"""A.G. Vandeputte""",
)

entry(
    index = 108,
    label = "O2 + CH3 <=> CH3O2-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (4.52e+12, 'cm^3/(mol*s)', '+|-', 4.2e+11),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
        comment = 'We are using a primary R. radical as a methyl radical. The rate comes from n-butyl.\n\n[8]   Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. *Combust. Flame* 2002, 129, 253-280. http://dx.doi.org/10.1016/S0010-2180(01)00373-X\n\nIn their study modelling iso-octane oxidation, Curran et al [8] chose to use the rate measured by Lenhardt et al [143] described below.\n\n[143] Lenhardt, T.M.; McDade, C.E.; Bayes, K.D.; *J. Chem. Phys.* 1980, 72,304 http://dx.doi.org/10.1063/1.438848\n\nRates measurement of **n-butyl** + O2 at 300 K. High pressure limit from flash photolysis experiments.\n\nC.D.W. divided rate expression by 2, to get rate of addition rate per site,\ngiving  (2.260.42)E12 cm3/mole/sec.\n\n    Rate constants for the reaction of four different butyl radicals with molecular oxygen \n    have been measured **at room temperature**. The radicals were generated by flash photolysis \n    and their time decay was followed with a photoionization mass spectrometer. The radical \n    concentrations were kept low to avoid complications from radicalradical reactions. \n    Radical lifetimes were long, up to 50 msec, thus assuring that thermalized radicals were being studied. \n    \n    The rate constants, in units of 10E11 cm3/molecule/sec, are:\n    \n     * **n-butyl (0.750.14); (gives (2.260.42)E12 cm3/mole/sec when divided by 2 to get rate per site)**\n     * s-butyl (1.660.22); (gives (5.000.66)E12 cm3/mole/sec when divided by 2 to get rate per site)\n     * t-butyl (2.340.39); (gives (7.051.17)E12 cm3/mole/sec when divided by 2 to get rate per site)\n     * 3-hydroxy s-butyl (2.81.8). (gives (8.435.42)E12 cm3/mole/sec when divided by 2 to get rate per site)\n     \n    No pressure dependence of the rate constants was observed over the range 1 to 4 Torr. \n\nBecause radical addition to a double bond is probably barrierless, the temperature range 300-1500K\nhas been assigned although the rate was only measured at 300K. \nrwest@mit.edu  7-Sep-2009\n\nMoved from R_Addition_MultipleBond on 3-Jun-2010, JDM.\n\nConverted to training reaction from rate rule: O2_birad;C_methyl',
    ),
    rank = 11,
    shortDesc = u"""Curran et al. [8] From Lenhardt et al. [143]. (Measured at 300K) (n-butyl not methyl)""",
)

entry(
    index = 109,
    label = "SH + H <=> H2S",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (7.07e+12, 'cm^3/(mol*s)'),
        n = 0.56,
        Ea = (-0.33472, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
        comment = '\n\nConverted to training reaction from rate rule: SsJ-H;H_rad',
    ),
    rank = 2,
    shortDesc = u"""A.G. Vandeputte""",
)

entry(
    index = 110,
    label = "O2 + C2H5 <=> C2H5O2-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (4.52e+12, 'cm^3/(mol*s)', '+|-', 4.2e+11),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
        comment = '[8]   Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. *Combust. Flame* 2002, 129, 253-280. http://dx.doi.org/10.1016/S0010-2180(01)00373-X\n\nIn their study modelling iso-octane oxidation, Curran et al [8] chose to use the rate measured by Lenhardt et al [143] described below.\n\n[143] Lenhardt, T.M.; McDade, C.E.; Bayes, K.D.; *J. Chem. Phys.* 1980, 72,304 http://dx.doi.org/10.1063/1.438848\n\nRates measurement of **n-butyl** + O2 at 300 K. High pressure limit from flash photolysis experiments.\nC.D.W. divided rate expression by 2, to get rate of addition rate per site, \ngiving  (2.260.42)E12 cm3/mole/sec.\n\n    Rate constants for the reaction of four different butyl radicals with molecular oxygen \n    have been measured **at room temperature**. The radicals were generated by flash photolysis \n    and their time decay was followed with a photoionization mass spectrometer. The radical \n    concentrations were kept low to avoid complications from radicalradical reactions. \n    Radical lifetimes were long, up to 50 msec, thus assuring that thermalized radicals were being studied. \n    \n    The rate constants, in units of 10E11 cm3/molecule/sec, are:\n    \n     * n-butyl (0.750.14); (gives (2.260.42)E12 cm3/mole/sec when divided by 2 to get rate per site)\n     * s-butyl (1.660.22); (gives (5.000.66)E12 cm3/mole/sec when divided by 2 to get rate per site)\n     * t-butyl (2.340.39); (gives (7.051.17)E12 cm3/mole/sec when divided by 2 to get rate per site)\n     * 3-hydroxy s-butyl (2.81.8). (gives (8.435.42)E12 cm3/mole/sec when divided by 2 to get rate per site)\n     \n    No pressure dependence of the rate constants was observed over the range 1 to 4 Torr. \n\nBecause radical addition to a double bond is probably barrierless, the temperature range 300-1500K\nhas been assigned although the rate was only measured at 300K. \n\nrwest@mit.edu  7-Sep-2009\n\nMoved from R_Addition_MultipleBond on 3-Jun-2010, JDM.\n\nConverted to training reaction from rate rule: O2_birad;C_pri_rad',
    ),
    rank = 11,
    shortDesc = u"""Curran et al. [8] From Lenhardt et al. [143]. (Measured at 300K)""",
)

entry(
    index = 111,
    label = "HSS + C4H9 <=> C4H10S2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.94e+09, 'cm^3/(mol*s)'),
        n = 1.25,
        Ea = (-3.09616, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
        comment = '\n\nConverted to training reaction from rate rule: SsJ-S2s;C_rad/Cs3',
    ),
    rank = 2,
    shortDesc = u"""A.G. Vandeputte""",
)

entry(
    index = 112,
    label = "O2 + C3H7-2 <=> C3H7O2-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (7.54e+12, 'cm^3/(mol*s)', '+|-', 1e+12),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
        comment = 'Lenhardt [143] measured (10.01.3)E12 cm3/mole/sec (at 300K, high pressure limit, from flash photolysis experiments.)\nAtkinson [96], in their review, recommend 6.62E12 cm3/mole/sec. (according to Curran [8]).\nCurran [8], in their modelling paper, refer to both these and chose and "intermediate" value of 7.54E12 cm3/mol/sec.\n\nCurran [8] is the rate adopted here, giving 3.77E+12 cm3/mole/sec when divided by two to give the rate of addition per site.\nThe uncertainty of 1E12 cm3/mole/sec was estimated from these values\n\n * [8] Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. *Combust. Flame* 2002, 129, 253-280. http://dx.doi.org/10.1016/S0010-2180(01)00373-X\n * [96] Atkinson,R; Baulch,D. L.; Cox R.A.;Hampson,R.F.,Jr.;Kerr,J.A;Rossi,M.J.;Troe,J. *J Phys. Chem. Ref. Data* 1997,26,521.\n * [143] Lenhardt,T.M.;McDade,C.E.;Bayes,K.D.; *J. Chem Phys* 1980, 72,304 http://dx.doi.org/10.1063/1.438848\n\nBecause radical addition to a double bond is probably barrierless, the temperature range 300-1500K\nhas been assigned although the rate was only measured/estimated at 300K. \n\nrwest@mit.edu  7-Sep-2009\n\nMoved from R_Addition_MultipleBond on 3-Jun-2010, JDM.\n\nConverted to training reaction from rate rule: O2_birad;C_sec_rad',
    ),
    rank = 11,
    shortDesc = u"""Curran et al. [8]. (Estimated at 300K)""",
)

entry(
    index = 113,
    label = "CH3S + C2H5 <=> C3H8S",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (8.94e+07, 'cm^3/(mol*s)'),
        n = 1.54,
        Ea = (-5.52288, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
        comment = '\n\nConverted to training reaction from rate rule: SsJ-Cs;C_rad/H2/Cs',
    ),
    rank = 2,
    shortDesc = u"""A.G. Vandeputte, calculated""",
)

entry(
    index = 114,
    label = "O2 + C4H9 <=> C4H9O2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.41e+13, 'cm^3/(mol*s)', '+|-', 1.17e+12),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
        comment = '[8]   Curran, H.J.; Gaffuri, P.; Pit z, W.J.; Westbrook, C.K. *Combust. Flame* 2002, 129, 253-280. http://dx.doi.org/10.1016/S0010-2180(01)00373-X\n\nIn their study modelling iso-octane oxidation, Curran et al [8] chose to use the rate measured by Lenhardt et al [143] described below.\n\n[143] Lenhardt, T.M.; McDade, C.E.; Bayes, K.D.; *J. Chem. Phys.* 1980, 72,304 http://dx.doi.org/10.1063/1.438848\n\nRates measurement of **t-butyl** + O2 at 300 K. High pressure limit from flash photolysis experiments.\nC.D.W. divided rate expression by 2, to get rate of addition rate per site, \ngiving  (7.051.17)E12 cm3/mole/sec.\n\n    Rate constants for the reaction of four different butyl radicals with molecular oxygen \n    have been measured **at room temperature**. The radicals were generated by flash photolysis \n    and their time decay was followed with a photoionization mass spectrometer. The radical \n    concentrations were kept low to avoid complications from radicalradical reactions. \n    Radical lifetimes were long, up to 50 msec, thus assuring that thermalized radicals were being studied. \n    \n    The rate constants, in units of 10E11 cm3/molecule/sec, are:\n    \n     * n-butyl (0.750.14); (gives (2.260.42)E12 cm3/mole/sec when divided by 2 to get rate per site)\n     * s-butyl (1.660.22); (gives (5.000.66)E12 cm3/mole/sec when divided by 2 to get rate per site)\n     * **t-butyl (2.340.39); (gives (7.051.17)E12 cm3/mole/sec when divided by 2 to get rate per site)**\n     * 3-hydroxy s-butyl (2.81.8). (gives (8.435.42)E12 cm3/mole/sec when divided by 2 to get rate per site)\n     \n    No pressure dependence of the rate constants was observed over the range 1 to 4 Torr. \n\nBecause radical addition to a double bond is probably barrierless, the temperature range 300-1500K\nhas been assigned although the rate was only measured at 300K. \n\nrwest@mit.edu  7-Sep-2009\n\nMoved from R_Addition_MultipleBond on 3-Jun-2010, JDM.\n\nConverted to training reaction from rate rule: O2_birad;C_ter_rad',
    ),
    rank = 11,
    shortDesc = u"""Curran et al. [8] From Lenhardt et al. [143]. (Measured at 300K)""",
)

entry(
    index = 115,
    label = "CH3S + CH3 <=> C2H6S",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (8.94e+07, 'cm^3/(mol*s)'),
        n = 1.54,
        Ea = (-5.52288, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
        comment = '\n\nConverted to training reaction from rate rule: SsJ-Cs;C_methyl',
    ),
    rank = 2,
    shortDesc = u"""A.G. Vandeputte, calculated""",
)

entry(
    index = 116,
    label = "O2 + C2H3 <=> C2H3O2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (6e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
        comment = '[144] Bozzelli,J.W. J phys. Chem 1993, 97,4427.\nRRKM extrapolation (adjusted to match data).O2 +CH = CH2CHOO. C.D.W. divided rate expression by 2, to get rate of addition per site\n\nMoved from R_Addition_MultipleBond on 3-Jun-2010, JDM.\n\nConverted to training reaction from rate rule: O2_birad;Cd_pri_rad',
    ),
    rank = 10,
    shortDesc = u"""Bozzelli et al. [144] RRKM extrapolation ( adjusted to match data).""",
)

entry(
    index = 117,
    label = "CH3S + C4H9 <=> C5H12S",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (8.94e+07, 'cm^3/(mol*s)'),
        n = 1.54,
        Ea = (-5.52288, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
        comment = '\n\nConverted to training reaction from rate rule: SsJ-Cs;C_rad/Cs3',
    ),
    rank = 2,
    shortDesc = u"""A.G. Vandeputte, calculated""",
)

entry(
    index = 118,
    label = "O2 + C6H5 <=> C6H5O2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (6.03e+12, 'cm^3/(mol*s)', '*|/', 1.2),
        n = 0,
        Ea = (1.33888, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (297, 'K'),
        Tmax = (473, 'K'),
        comment = '[145] Yu,T.; Lin, M.C.J. Am. Chem.Soc.1994,116,9571.\nO2+ phenyl --> phenyl dioxy. Absolute value measured directly. Pressure 0.03-0.11 atm. Excitation: Flash photolysis, analysis: Vis- UV absorption. C.D.W. divided rate epxression by 2, to get rate of addition per site\n\nMoved from R_Addition_MultipleBond on 3-Jun-2010, JDM.\n\nConverted to training reaction from rate rule: O2_birad;Cb_rad',
    ),
    rank = 6,
    shortDesc = u"""Yu, T. and Lin, M.C. [145]""",
)

entry(
    index = 119,
    label = "O2 + CHO <=> CHO3",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (7e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = '[144] Bozzelli,J.W. J Phys. Chem. 1993, 97 , 4427.\nRRKM extrapolation. O2 +HCO -->HC(O)O2. C.D.W. divided rate expression by 2, to get rate of addition per site\n\nMoved from R_Addition_MultipleBond on 3-Jun-2010, JDM.\n\nConverted to training reaction from rate rule: O2_birad;CO_pri_rad',
    ),
    rank = 10,
    shortDesc = u"""Bozzelli et al. [144] RRKM extrapolation.""",
)

entry(
    index = 120,
    label = "O2 + C2H3O <=> C2H3O3",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (3.01e+12, 'cm^3/(mol*s)', '*|/', 3.16),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (300, 'K'),
        comment = '[96] Atkinson,R; Baulch,D. L.; Cox R.A.;Hampson,R.F.,Jr.;Kerr,J.A;Rossi,M.J.;Troe,J.J Phys. Chem. Ref. Data 1997,26,521.\nliterature review. Rate constant is high pressure limit. O2+ CH3CO --> CH3C(O)OO C.D.W. divided rate expression by 2, to get rate of addition per site\n\nMoved from R_Addition_MultipleBond on 3-Jun-2010, JDM.\n\nConverted to training reaction from rate rule: O2_birad;CO_rad/NonDe',
    ),
    rank = 10,
    shortDesc = u"""Atkinson et al [96] literature review.""",
)

entry(
    index = 121,
    label = "H + C3H5 <=> C3H6-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (5.84e+13, 'cm^3/(mol*s)'),
        n = 0.18,
        Ea = (0.518816, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (2000, 'K'),
        comment = '\n\nConverted to training reaction from rate rule: H_rad;C_rad/H2/Cd',
    ),
    rank = 6,
    shortDesc = u"""Harding et al. (2007HAR/KLI3789-3801), value devided by 2 to account for two addition sites""",
)

entry(
    index = 122,
    label = "H + C4H7 <=> C4H8",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.92e+13, 'cm^3/(mol*s)'),
        n = 0.18,
        Ea = (0.518816, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (2000, 'K'),
        comment = '\n\nConverted to training reaction from rate rule: H_rad;C_rad/H/OneDeC',
    ),
    rank = 11,
    shortDesc = u"""Estimated by 495""",
)

entry(
    index = 123,
    label = "H + C5H9 <=> C5H10",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.92e+13, 'cm^3/(mol*s)'),
        n = 0.18,
        Ea = (0.518816, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (2000, 'K'),
        comment = '\n\nConverted to training reaction from rate rule: H_rad;C_rad/OneDe',
    ),
    rank = 11,
    shortDesc = u"""Estimated by 495""",
)

entry(
    index = 124,
    label = "H + C6H9 <=> C6H10",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.92e+13, 'cm^3/(mol*s)'),
        n = 0.18,
        Ea = (0.518816, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (200, 'K'),
        Tmax = (2000, 'K'),
        comment = '\n\nConverted to training reaction from rate rule: H_rad;C_rad/TwoDe',
    ),
    rank = 11,
    shortDesc = u"""Estimated by 495""",
)

entry(
    index = 125,
    label = "C3H5 + C3H5 <=> C6H10-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (2.04e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-1.08784, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = '\n\nConverted to training reaction from rate rule: C_rad/H2/Cd;C_rad/H2/Cd',
    ),
    rank = 10,
    shortDesc = u"""Tsang (1991) Chemical kinetic data base for combustion chemistry. Part V. Propene Literature review""",
)

entry(
    index = 126,
    label = "C3H5 + C2H5 <=> C5H10-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (4.1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-0.54392, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = '\n\nConverted to training reaction from rate rule: C_rad/H2/Cd;C_rad/H2/Cs',
    ),
    rank = 10,
    shortDesc = u"""Tsang (1991) Chemical kinetic data base for combustion chemistry. Part V. Propene Literature review""",
)

entry(
    index = 127,
    label = "C3H5 + CH3 <=> C4H8-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (2.04e+14, 'cm^3/(mol*s)'),
        n = -0.32,
        Ea = (-0.54392, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = '\n\nConverted to training reaction from rate rule: C_rad/H2/Cd;C_methyl',
    ),
    rank = 10,
    shortDesc = u"""Tsang (1991) Chemical kinetic data base for combustion chemistry. Part V. Propene Literature review""",
)

entry(
    index = 128,
    label = "C3H5 + C3H7-2 <=> C6H12",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (2.3e+14, 'cm^3/(mol*s)'),
        n = -0.35,
        Ea = (-0.54392, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = '\n\nConverted to training reaction from rate rule: C_rad/H2/Cd;C_rad/H/NonDeC',
    ),
    rank = 10,
    shortDesc = u"""Tsang (1991) Chemical kinetic data base for combustion chemistry. Part V. Propene Literature review""",
)

entry(
    index = 129,
    label = "C3H5 + C4H9 <=> C7H14",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.448e+15, 'cm^3/(mol*s)'),
        n = -0.75,
        Ea = (-0.54392, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = '\n\nConverted to training reaction from rate rule: C_rad/H2/Cd;C_rad/Cs3',
    ),
    rank = 10,
    shortDesc = u"""Tsang (1991) Chemical kinetic data base for combustion chemistry. Part V. Propene Literature review""",
)

entry(
    index = 130,
    label = "C3H5 + C5H7 <=> C8H12",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (2.04e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-1.08784, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = '\n\nConverted to training reaction from rate rule: C_rad/H2/Cd;C_rad/H/CdCd',
    ),
    rank = 11,
    shortDesc = u"""Better estimate then averaging out, Tsang (1991) Chemical kinetic data base for combustion chemistry. Part V. Propene Literature review""",
)

entry(
    index = 131,
    label = "C3H3-2 + C3H3-2 <=> C6H6",
    degeneracy = 0.5,
    kinetics = Arrhenius(
        A = (2.145e+09, 'cm^3/(mol*s)'),
        n = 0.8,
        Ea = (-4.30952, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = 'A. G. Vandeputte\nSome estimated values for propyne recombination reactions\n\nConverted to training reaction from rate rule: Cd_allenic;Cd_allenic',
    ),
    rank = 6,
    shortDesc = u"""2007GEO/MIL4259-4268""",
)

entry(
    index = 132,
    label = "C3H3-2 + CH3 <=> C4H6-5",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Estimated value, agrees with 1987WU/KER6291\n\nConverted to training reaction from rate rule: Cd_allenic;C_methyl',
    ),
    rank = 11,
    shortDesc = u"""1987WU/KER6291""",
)

entry(
    index = 133,
    label = "C3H3-2 + H <=> C3H4-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = '\n\nConverted to training reaction from rate rule: Cd_allenic;H_rad',
    ),
    rank = 11,
    shortDesc = u"""A. G. Vandeputte estimated value""",
)

entry(
    index = 134,
    label = "C5H5 + H <=> C5H6",
    degeneracy = 5.0,
    kinetics = Arrhenius(
        A = (2.5e+15, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = '\n\nConverted to training reaction from rate rule: C_rad_cyclopentadiene;H_rad',
    ),
    rank = 6,
    shortDesc = u"""From 2001 Roy IJCK high-P value""",
)

entry(
    index = 135,
    label = "C5H5 + CH3 <=> C6H8",
    degeneracy = 5.0,
    kinetics = Arrhenius(
        A = (4.17e+16, 'cm^3/(mol*s)'),
        n = -0.7,
        Ea = (2.092, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
        comment = '\n\nConverted to training reaction from rate rule: C_rad_cyclopentadiene;C_methyl',
    ),
    rank = 6,
    shortDesc = u"""Sharma J. Phys. Chem. A 113 8871 - 8882 (2009)""",
)

entry(
    index = 136,
    label = "C5H5 + C5H5 <=> C10H10-6",
    degeneracy = 12.5,
    kinetics = Arrhenius(
        A = (6.25e+14, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
        comment = '\n\nConverted to training reaction from rate rule: C_rad_cyclopentadiene;C_rad_cyclopentadiene',
    ),
    rank = 11,
    shortDesc = u"""A. G. Vandeputte estimated value""",
)

entry(
    index = 137,
    label = "H + C5H7 <=> C5H8",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = '\n\nConverted to training reaction from rate rule: H_rad;C_rad/H/CdCd',
    ),
    rank = 11,
    shortDesc = u"""A. G. Vandeputte estimated value""",
)

entry(
    index = 138,
    label = "NO2 + OH <=> HNO3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.5e+12, 'cm^3/(mol*s)'),
        n = 0.24,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = "J. Hahn, K. Luther and J. Troe\nExperimental and theoretical study of the temperature and pressure dependences of the recombination reactions O + NO2 (+M) = NO2 (+M) and NO2 + NO3 (+M) = N2O5 (+M)\nPhys. Chem. Chem. Phys., 2000, 2, 5098-5104\nDOI: 10.1039/B005756H\n\nNO2 + O < = > NO3\n\nAlso appears in the Nitrogen_Glarborg_Zhang_et_al library (index 712)\nand in the Nitrogen_Glarborg_Gimenez_et_al library (index 936)\n\nThe high-pressure limit kinetics was taken. Troe coefficients are:\n    kinetics = Troe(\n        arrheniusHigh = Arrhenius(A=(3.5e+12, 'cm^3/(mol*s)'), n=0.24, Ea=(0, 'cal/mol'), T0=(1, 'K')),\n        arrheniusLow = Arrhenius(A=(2.5e+20, 'cm^6/(mol^2*s)'), n=-1.5, Ea=(0, 'cal/mol'), T0=(1, 'K')),\n        alpha = 0.71,\n        T3 = (1e-30, 'K'),\n        T1 = (1700, 'K'),\n        T2 = (1e+30, 'K'),\n        efficiencies = {},\n    ),\n\nConverted to training reaction from rate rule: N5dc-OdOs;O_rad",
    ),
    rank = 2,
    shortDesc = u"""Experimental, J. Hahn, K. Luther and J. Troe""",
)

entry(
    index = 139,
    label = "NO2 + OH <=> HNO3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = "J. Troe\nAnalysis of the temperature and pressure dependence of the reaction HO + NO2 + M = HONO2 + M\nInternational Journal of Chemical Kinetics, Volume 33, Issue 12 December 2001 Pages 878-889\nDOI: 10.1002/kin.10019\n\nNO2 + OH <=> HONO2; T range: 50 to 1400 K, P range: 10E-4 to 10E3 bar\n\nAlso appears in the Nitrogen_Glarborg_Zhang_et_al library (index 713)\nand in the Nitrogen_Glarborg_Gimenez_et_al library (index 937)\n\nThe high-pressure limit kinetics was taken. Troe coefficients are:\n    kinetics = Troe(\n        arrheniusHigh = Arrhenius(A=(3e+13, 'cm^3/(mol*s)'), n=0, Ea=(0, 'cal/mol'), T0=(1, 'K')),\n        arrheniusLow = Arrhenius(A=(2.938e+25, 'cm^6/(mol^2*s)'), n=-3, Ea=(0, 'cal/mol'), T0=(1, 'K')),\n        alpha = 0.4,\n        T3 = (1e-30, 'K'),\n        T1 = (1e+30, 'K'),\n        T2 = (1e+30, 'K'),\n        efficiencies = {},\n    ),\n\nConverted to training reaction from rate rule: N5dc-OdOs;O_pri_rad",
    ),
    rank = 6,
    shortDesc = u"""J. Troe""",
)

entry(
    index = 140,
    label = "H + SH <=> H2S-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.77e+15, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (1.79912, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
        comment = '\n\nConverted to training reaction from rate rule: H_rad;SsJ-H',
    ),
    rank = 6,
    shortDesc = u"""GA Jonas x 3 for spinorbit""",
)

