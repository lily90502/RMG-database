#!/usr/bin/env python
# encoding: utf-8

name = "Disproportionation/training"
shortDesc = u"Kinetics used to train group additivity values"
longDesc = u"""
Put kinetic parameters for reactions to use as a training set for fitting
group additivity values in this file.
"""
entry(
    index = 0,
    label = "C2H + CH3O <=> C2H2 + CH2O",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (3.61e+13, 'cm^3/(mol*s)', '*|/', 5),
        n = 0,
        Ea = (0, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
    ),
    rank = 9,
    shortDesc = u"""Tsang [90] Literature review.""",
    longDesc = 
u"""
[90] Tsang, W.; Journal of Physical and Chemical Reference Data (1987), 16(3), 471-508.
Literature review: C2H + CH2OH --> C2H2 + CH2O

pg. 504: Discussion on evaluated data

Entry 39,21 (a): CH2OH + C2H --> C2H2 + CH2O

Author suggest a disproportionation rate coefficient of 6.0x10^-11 cm3/molecule/s, due

to very exothermic rxn.  No data available at the time.
MRH 30-Aug-2009
""",
)

entry(
    index = 1,
    label = "C2H3 + O2 = C2H2_1 + HO2",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (1.04e+16, 'cm^3/(mol*s)', '*|/', 5),
        n = -1.26,
        Ea = (3.31, 'kcal/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
    ),
    rank = 10,
    shortDesc = u"""S.S. Merchant estimate""",
    longDesc = 
u"""
This rate rule is a estimate taken from NIST, ref: Aromatic and Polycyclic Aromatic
Hydrocarbon Formation in a Laminar Premixed n-butane Flame
Derived from fitting to a complex mechanism for C2H3 + O2 = C2H2 + HO2
""",
)

