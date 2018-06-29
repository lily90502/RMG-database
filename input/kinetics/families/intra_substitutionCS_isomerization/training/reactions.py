#!/usr/bin/env python
# encoding: utf-8

name = "intra_substitutionCS_isomerization/training"
shortDesc = u"Kinetics used to train group additivity values"
longDesc = u"""
Put kinetic parameters for reactions to use as a training set for fitting
group additivity values in this file.
"""
entry(
    index = 1,
    label = "C2H5S <=> C2H5S-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.03e+09, 's^-1'),
        n = 1.057,
        Ea = (190.372, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
        comment = '\n\nConverted to training reaction from rate rule: XSR3J_S;C-HHH;CsJ-HH',
    ),
    rank = 6,
    shortDesc = u"""A. G. Vandeputte""",
)

entry(
    index = 2,
    label = "C3H7S <=> C3H7S-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.76e+10, 's^-1'),
        n = 0.394,
        Ea = (191.209, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
        comment = '\n\nConverted to training reaction from rate rule: XSR4J_SS_Cs;C-HHH;CsJ-HH',
    ),
    rank = 6,
    shortDesc = u"""A. G. Vandeputte""",
)

entry(
    index = 3,
    label = "C2H5S2 <=> C2H5S2-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.51e+11, 's^-1'),
        n = 0.327,
        Ea = (230.538, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
        comment = '\n\nConverted to training reaction from rate rule: XSR4J_SS_Ss;C-HHH;CsJ-HH',
    ),
    rank = 6,
    shortDesc = u"""A. G. Vandeputte""",
)

