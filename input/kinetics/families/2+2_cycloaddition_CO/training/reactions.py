#!/usr/bin/env python
# encoding: utf-8

name = "2+2_cycloaddition_CO/training"
shortDesc = u"Kinetics used to train group additivity values"
longDesc = u"""
Put kinetic parameters for reactions to use as a training set for fitting
group additivity values in this file.
"""
entry(
    index = 1,
    label = "CH2O + C2H3O <=> C3H5O2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (0.2319, 'cm^3/(mol*s)', '*|/', 5),
        n = 3.416,
        Ea = (322.616, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (600, 'K'),
        Tmax = (2000, 'K'),
        comment = 'MRH CBS-QB3 calculations for the reverse of the reaction sequence *CH2-cycle(CH-CH2-O-O) => *CH2-O-O-CH=CH2 ==> CH2O + CH2CHO\n\nPrevious RMG estimate for this reaction was an "Average of average" estimate, in addition to RMG needing\nto increase the estimated Ea by ~20 kcal/mol because the barrier was not greater than the endothermicity.\nThis reaction was of interest to MRH/MHS because the butanol model was sensitive to allyl+O2 => CH2O+CH2CHO.\nThe high-p limit kinetics were necessary to estimate a k(T,P) for this PES.\n\nThe kinetics correspond to the reaction CH2O+CH2CHO => *CH2-cycle(CH-CH2-O-O)\n\nReactant: 0 hindered rotors\nTS: 0 hindered rotors were considered (the only low-frequency torisonal mode corresponded to\n\ta hindered rotation within the cycle; MRH did not think treating this as a 1-d separable\n\thindered rotor was accurate)\nProduct: 1 hindered rotor was considered (the *CH2 torsion)\n\nAll external symmetry numbers were set equal to one, except for CH2O which was set to two.\nMRH could not find a stable geometry for *CH2-O-O-CH=CH2 at the B3LYP/6-31G(d) level (the method/basis\nused in the CBS-QB3 method), it would always optimize to CH2O + CH2CHO.  Furthermore, MRH did not run an\nIRC for the TS, to confirm the TS would fall apart to CH2O + CH2CHO (instead of CH2-OO-CH=CH2), hence the lowest\nranking of "5" assigned to this rate coefficient.\n\nThe k(T) was calculated from 600 - 2000 K, in 200 K intervals, and the fitted Arrhenius expression from CanTherm was:\nk(T) = 2.319e-01 * (T/1K)^3.416 * exp(-77.107 kcal/mol / RT) cm3/mol/s.\n\nConverted to training reaction from rate rule: CH2CHO;mb_CO_2H',
    ),
    rank = 11,
    shortDesc = u"""MRH CBS-QB3 calculations with 1d h.r. corrections""",
)

