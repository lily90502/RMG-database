#!/usr/bin/env python
# encoding: utf-8

name = "1+2_Cycloaddition/rules"
shortDesc = u""
longDesc = u"""

"""
entry(
    index = 576,
    label = "elec_def;multiplebond",
    kinetics = ArrheniusEP(
        A = (1e+12, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
    ),
    rank = 0,
    shortDesc = u"""Default""",
)

entry(
    index = 577,
    label = "carbene;mb_db_unsub",
    kinetics = ArrheniusEP(
        A = (1.98e+12, 'cm^3/(mol*s)', '*|/', 3.2),
        n = 0,
        alpha = 0,
        E0 = (5.29, 'kcal/mol', '+|-', 0.26),
        Tmin = (296, 'K'),
        Tmax = (728, 'K'),
    ),
    rank = 5,
    shortDesc = u"""Frey et al [192]""",
)

entry(
    index = 579,
    label = "o_atom_singlet;mb_db_unsub",
    kinetics = ArrheniusEP(
        A = (7e+11, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
    ),
    rank = 9,
    shortDesc = u"""Gaedtke et al [194]""",
    longDesc = 
u"""
[194] Gaedtke, H. Symp. Int. Combust. Proc. 1973, 14, 295. 
Excitation: direct photolysis, analysis: UV-Vis absorption, Pressure 0.1 - 1000 atm. O + C2H4 --> Oxirane
""",
)

entry(
    index = 580,
    label = "o_atom_singlet;mb_db_monosub_Nd",
    kinetics = ArrheniusEP(
        A = (2.9e+12, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (300, 'K'),
    ),
    rank = 9,
    shortDesc = u"""Gaedtke et al [194]""",
    longDesc = 
u"""
[194] Gaedtke, H. Symp. Int. Combust. Proc. 1973, 14, 295. 
Excitation: direct photolysis, analysis: UV-Vis absorption, Pressure 0.1 - 1000 atm. O + CH3CH=CH2 --> methyloxirane
""",
)

entry(
    index = 581,
    label = "o_atom_singlet;mb_db_monosub_Nd",
    kinetics = ArrheniusEP(
        A = (4.2e+12, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (0.5, 'kcal/mol'),
        Tmin = (275, 'K'),
        Tmax = (360, 'K'),
    ),
    rank = 9,
    shortDesc = u"""Herbrechtsmeier et al [195]""",
    longDesc = 
u"""
[195] Herbrechtsmeier, P. Reactions of O(3P) Atoms with Unsaturated C3 Hydrocarbons. In Combust. Inst. European Symp., 1973; pp13.
Absolute values measured directly. Excitation: discharge, analysis :GC, Pressure 0.01 atm. O + CH3CH=CH2 --> methyloxirane
""",
)

entry(
    index = 582,
    label = "o_atom_singlet;mb_db_monosub_Nd",
    kinetics = ArrheniusEP(
        A = (1.9e+12, 'cm^3/(mol*s)', '*|/', 1.2),
        n = 0,
        alpha = 0,
        E0 = (0.8, 'kcal/mol', '+|-', 0.4),
        Tmin = (298, 'K'),
        Tmax = (410, 'K'),
    ),
    rank = 9,
    shortDesc = u"""Smith [196]""",
    longDesc = 
u"""
[196] Smith, I.W.M. Trans. Faraday Soc. 1968, 64, 378.
Data derived from fitting to a complex mechanism. Excitation: flash photolysis, analysis : UV-Vis absorption. Pressure 0.13 atm

O + 1-C4H8 --> ethyloxirane. Original uncertainty 3.0E+11
""",
)

entry(
    index = 583,
    label = "o_atom_singlet;mb_db_onecdisub_Nd",
    kinetics = ArrheniusEP(
        A = (7.6e+12, 'cm^3/(mol*s)', '*|/', 1.2),
        n = 0,
        alpha = 0,
        E0 = (0.1, 'kcal/mol', '+|-', 0.4),
        Tmin = (298, 'K'),
        Tmax = (410, 'K'),
    ),
    rank = 9,
    shortDesc = u"""Smith [196]""",
    longDesc = 
u"""
[196] Smith, I.W.M. Trans. Faraday Soc. 1968, 64, 378.
Data derived from fitting to a complex mechanism. Excitation: flash photolysis, analysis : UV-Vis absorption. Pressure 0.13 atm

O + iso-C4H8 --> 2,2- dimethyloxirane. Original uncertainty 1.2E+12
""",
)

entry(
    index = 584,
    label = "o_atom_singlet;mb_db_twocdisub_Nd",
    kinetics = ArrheniusEP(
        A = (1.54e+13, 'cm^3/(mol*s)'),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (298, 'K'),
    ),
    rank = 9,
    shortDesc = u"""Cvetanovic [197]""",
    longDesc = 
u"""
[197] Cvetanovic, R. J. Chem. Phys. 1959, 30, 19.
Relative value measured (O + (Z)-2-C4H8 --> cis-2,3-dimethyloxirane/O + C2H4 = Oxirane --> 2.2E+01) 

Pressure 0.39 atm. Excitation : sensitized photolysis, analysis :GC.
""",
)

entry(
    index = 585,
    label = "o_atom_singlet;mb_db_tetrasub_Nd",
    kinetics = ArrheniusEP(
        A = (3.18e+13, 'cm^3/(mol*s)', '*|/', 1.2),
        n = 0,
        alpha = 0,
        E0 = (0, 'kcal/mol'),
        Tmin = (298, 'K'),
    ),
    rank = 9,
    shortDesc = u"""Cvetanovic [197]""",
    longDesc = 
u"""
[197] Cvetanovic, R. J. Chem. Phys. 1959, 30, 19.
Relative value measured (O + (CH3)2C=C(CH3)2 --> tetramethyl-oxirane/O + iso-C4H8 --> 2,2-Dimethyloxirane = 4.18)  

Pressure 0.39 atm. Excitation : sensitized photolysis, analysis :GC.
""",
)

entry(
    index = 586,
    label = "carbene;mb_tb_unsub",
    kinetics = ArrheniusEP(
        A = (1.77e+15, 'cm^3/(mol*s)'),
        n = -0.662,
        alpha = 0,
        E0 = (0.0377, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Polino [carbene,acetylene]""",
)

entry(
    index = 587,
    label = "carbene;mb_db_unsub",
    kinetics = ArrheniusEP(
        A = (1.24e+15, 'cm^3/(mol*s)'),
        n = -0.684,
        alpha = 0,
        E0 = (-0.0805, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Polino [carbene,ethene]""",
)

entry(
    index = 588,
    label = "carbene;mb_tb_monosub_Nd",
    kinetics = ArrheniusEP(
        A = (4.5e+15, 'cm^3/(mol*s)'),
        n = -0.708,
        alpha = 0,
        E0 = (-0.0267, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Polino [carbene,propyne]""",
)

entry(
    index = 589,
    label = "carbene;mb_db_monosub_Nd",
    kinetics = ArrheniusEP(
        A = (5e+15, 'cm^3/(mol*s)'),
        n = -0.826,
        alpha = 0,
        E0 = (-0.09, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Polino [carbene,propene]""",
)

entry(
    index = 590,
    label = "carbene;mb_db_dbSub",
    kinetics = ArrheniusEP(
        A = (6.38e+14, 'cm^3/(mol*s)'),
        n = -0.562,
        alpha = 0,
        E0 = (-0.133, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Polino [carbene,propadiene]""",
)

entry(
    index = 591,
    label = "carbene;mb_tb_disub_twoNd",
    kinetics = ArrheniusEP(
        A = (4.7e+15, 'cm^3/(mol*s)'),
        n = -0.823,
        alpha = 0,
        E0 = (0.023, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Polino [carbene,2-butyne]""",
)

entry(
    index = 592,
    label = "carbene;mb_db_monosub_De",
    kinetics = ArrheniusEP(
        A = (1.85e+15, 'cm^3/(mol*s)'),
        n = -0.7,
        alpha = 0,
        E0 = (-0.0672, 'kcal/mol'),
        Tmin = (200, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 4,
    shortDesc = u"""Polino [carbene,1,3-butadiene]""",
)

