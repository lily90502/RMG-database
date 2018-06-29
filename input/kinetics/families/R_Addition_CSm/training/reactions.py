#!/usr/bin/env python
# encoding: utf-8

name = "R_Addition_CSm/training"
shortDesc = u"Kinetics used to train group additivity values"
longDesc = u"""
Put kinetic parameters for reactions to use as a training set for fitting
group additivity values in this file.
"""
entry(
    index = 1,
    label = "H + CS <=> CHS",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (20.92, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
        comment = '\n\nConverted to training reaction from rate rule: CSm;Y_rad',
    ),
    rank = 0,
    shortDesc = u"""Default""",
)

entry(
    index = 2,
    label = "H + CS <=> CHS",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.18e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (11.3386, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
        comment = '\n\nConverted to training reaction from rate rule: CSm;H_rad',
    ),
    rank = 11,
    shortDesc = u"""Guessed from CO+H_rad""",
)

entry(
    index = 3,
    label = "CH3 + CS <=> C2H3S",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.2e+13, 'cm^3/(mol*s)'),
        n = 2.11,
        Ea = (10.2926, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
        comment = '\n\nConverted to training reaction from rate rule: CSm;C_methyl',
    ),
    rank = 5,
    shortDesc = u"""CAC CBS-QB3 calc (using methyl group), HO Approx""",
)

entry(
    index = 4,
    label = "C2H5 + CS <=> C3H5S",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.01e+10, 'cm^3/(mol*s)'),
        n = 2.22,
        Ea = (1.63176, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
        comment = '\n\nConverted to training reaction from rate rule: CSm;CH2CH3',
    ),
    rank = 5,
    shortDesc = u"""CAC CBS-QB3 calc (using ethyl group), HO approx""",
)

