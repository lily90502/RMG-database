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
        pages = """'4377-4384'""",
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
        pages = """'253'""",
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
        title = 'Experimental and Theoretical Study of the Temperature and Pressure Dependences of the Recombination Reactions O+NO2(+M)\xe2\x86\x92\xc2\x92NO3(+M) and NO2+NO3(+M)\xe2\x86\x92\xc2\x92N-2O5(+M)',
        journal = "'Phys. Chem. Chem. Phys.'",
        pages = """'5098-5104'""",
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
        pages = """'9191-9200'""",
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
        pages = """'9191-9200'""",
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
        pages = """'9191-9200'""",
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
        pages = """'9191-9200'""",
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
        pages = """'9191-9200'""",
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
        pages = """'9191-9200'""",
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
        pages = """'79-100'""",
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
        pages = """'79-100'""",
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
        pages = """'3789-3801'""",
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
        pages = """'3789-3801'""",
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
        pages = """'4259-4268'""",
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
        pages = """'4259-4268'""",
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
        pages = """'4259-4268'""",
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
        pages = """'167-175'""",
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
        pages = """'167-175'""",
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
        pages = """'167-175'""",
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
        pages = """'221-229'""",
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
        pages = """'221-229'""",
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
        pages = """'221-229'""",
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
        pages = """'221-229'""",
        year = "'2007'",
    ),
    referenceType = "theory",
    rank = 5,
    longDesc = 
u"""
CCSD(T)/aug-cc-pvdz//B3LYP/6-31G* (VRC-TST)
""",
)

