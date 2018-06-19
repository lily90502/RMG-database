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

entry(
    index = 2,
    label = "C2H5 + O2 <=> HO2 + C2H4",
    degeneracy = 6.0,
    kinetics = Arrhenius(
        A = (4.338e+13, 'cm^3/(mol*s)', '*|/', 3),
        n = 0,
        Ea = (66.9022, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (700, 'K'),
        Tmax = (2500, 'K'),
        comment = '[91] Tsang, W.; Journal of Physical and Chemical Reference Data (1988), 17(2), 887-951.\nLiterature review: i-C3H7 + O2 = HO2 + C3H6\n\npg. 931-932: Discussion on evaluated data\n\nEntry 42,3 (a): Author appears to be skeptical of the only experimentally reported\n\nvalue.  Author notes that more recent work on C2H5+O2 suggested that the\naddition and disproportionation rxns may be coupled through a common intermediate.\nFor the time being, the author decided to recommend the only experimentally\nreported rate coefficient, only for temperatures above 700K, as they note the\naddition rxn should be the predominant rxn at lower temperatures.\nMRH 30-Aug-2009\n\nDivide the rate constant by 12 to account for symmetry of 2 (O2) and 6 (i-C3H7, carbons #1 and 3).  The final result is 1.05833e+10 cm3/mol/s.\nJDM 31-Mar-2010\n\nConverted to training reaction from rate rule: O2b;Cmethyl_Csrad',
    ),
    rank = 10,
    shortDesc = u"""[AJ] Miyoshi 2011 (Table 4, Node 'sp') dx.doi.org/10.1021/jp112152n""",
)

entry(
    index = 3,
    label = "CH2 + C2H5 <=> CH3 + C2H4",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (9.03e+13, 'cm^3/(mol*s)', '*|/', 2),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = '[91] Tsang, W.; Journal of Physical and Chemical Reference Data (1988), 17(2), 887-951.\nLiterature review.  CH2(triplet) + i-C3H7 --> C3H6 + CH3\n\npg. 944: Discussion on evaluated data\n\nEntry 42,26: No data available at the time.  Author suggests this is a minor channel,\n\nstating the main process should be combination, leading to chemically activated\ni-butyl radical.  Rate coefficient is estimate.\nMRH 30-Aug-2009\n\nConverted to training reaction from rate rule: CH2_triplet;Cmethyl_Csrad',
    ),
    rank = 10,
    shortDesc = u"""Tsang [91] Literature review.""",
)

entry(
    index = 4,
    label = "H + C2H5 <=> H2 + C2H4",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (1.083e+13, 'cm^3/(mol*s)', '*|/', 2),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = '[91] Tsang, W.; Journal of Physical and Chemical Reference Data (1988), 17(2), 887-951.\nLiterature review.  H + i-C3H7 --> C3H6 + H2\n\npg. 932: Discussion on evaluated data\n\nEntry 42,4 (a): No data available at the time.  Author recommends a rate coefficient\n\nexpression equal to double the rate expression of H+C2H5=H2+C2H4.\nMRH 30-Aug-2009\n\nConverted to training reaction from rate rule: H_rad;Cmethyl_Csrad',
    ),
    rank = 10,
    shortDesc = u"""Tsang [91] Literature review.""",
)

entry(
    index = 5,
    label = "CH3 + C2H5 <=> CH4 + C2H4",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (6.57e+14, 'cm^3/(mol*s)', '*|/', 1.1),
        n = -0.68,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = '[91] Tsang, W.; Journal of Physical and Chemical Reference Data (1988), 17(2), 887-951.\nLiterature review.  CH3 + i-C3H7 --> C3H6 + CH4\n\npg. 937: Discussion on evaluated data\n\nEntry 42,16 (b): Author notes that measurements performed by Arthur and Anastasi on\n\nthe rate coefficient of total CH3+i-C3H7 decomposition matches very well with\nthe coefficient derived from the recommended rate of CH3+CH3 decomposition, the \nrecommended rate of i-C3H7+i-C3H7 decomposition, and the geometric rule.  The author\nrecommends a high-pressure rate expression of 4.7x10^-11*(300/T)^0.68 cm3/molecule/s\nfor the addition rexn (based on the geometric mean rule???) and recommends the \nbranching ratio of 0.16 reported by Gibian and Corley (1973).\nNOTE: Previous data entry appeared to compute A and n as such:\n\nA = 0.16 * 4.7x10^-11 * (1/300)^0.68\nn = 0.68\nHowever, MRH would compute A and n:\n\nA = 0.16 * 4.7x10^-11 * (300)^0.68\nn = -0.68\nThese are the values that now reside in the database.  The online NIST database\n\n(kinetics.nist.gov) agree with what I have calculated.\nMRH 30-Aug-2009\n\nConverted to training reaction from rate rule: C_methyl;Cmethyl_Csrad',
    ),
    rank = 10,
    shortDesc = u"""Tsang [91] Literature review.""",
)

entry(
    index = 6,
    label = "C2H5 + C2H5-2 <=> C2H6 + C2H4",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (6.9e+13, 'cm^3/(mol*s)', '*|/', 1.1),
        n = -0.35,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = '[91] Tsang, W.; Journal of Physical and Chemical Reference Data (1988), 17(2), 887-951.\nLiterature review.  C2H5 + i-C3H7 --> C3H6 + C2H6\n\npg. 937-938: Discussion on evaluated data\n\nEntry 42,17 (c): No data available at the time.  The rate coefficient expression for\n\nthe combination rxn is computed using the geometric mean rule and is reported as\n2.6x10^-11 * (300/T)^0.35 cm3/molecule/s.  The recommended branching ratio for \ndisproportionation to addition is that reported by Gibian and Corley (1973).\nMRH 30-Aug-2009\n\nConverted to training reaction from rate rule: C_rad/H2/Cs;Cmethyl_Csrad',
    ),
    rank = 10,
    shortDesc = u"""Tsang [91] Literature review.""",
)

entry(
    index = 7,
    label = "C3H5 + C2H5 <=> C3H6 + C2H4",
    degeneracy = 6.0,
    kinetics = Arrhenius(
        A = (1.374e+14, 'cm^3/(mol*s)', '*|/', 3),
        n = -0.35,
        Ea = (-0.54392, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = '[93] Tsang, W.; Journal of Physical and Chemical Reference Data (1991), 20(2), 221-273.\nLiterature review: C3H5 + iC3H7 --> C3H6 + C3H6\n\npg.268: Discussion on evaluated data\n\nEntry 47,42(a): No data available at the time.  Recommended rate coefficient expression\n\nbased on rxn C3H5+C2H5=C2H4+C3H6 (James, D.G.L. and Troughton, G.E.) and values\nfor "alkyl radicals" (Gibian M.J. and Corley R.C.); this leads to disproportionation-\nto-addition ratio of 0.2.  The addition rate expression was derived using the geometric\nmean rule for the rxns C3H5+C3H5-->adduct and iC3H7+iC3H7-->adduct.\nMRH 31-Aug-2009\n\nConverted to training reaction from rate rule: C_rad/H2/Cd;Cmethyl_Csrad',
    ),
    rank = 10,
    shortDesc = u"""Tsang [93] Literature review.""",
)

entry(
    index = 8,
    label = "CH3O-2 + C2H5 <=> CH4O + C2H4",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (8.67e+12, 'cm^3/(mol*s)', '*|/', 5),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = '[91] Tsang, W.; Journal of Physical and Chemical Reference Data (1988), 17(2), 887-951.\nLiterature review.  CH2OH + i-C3H7 --> C3H6 + CH3OH\n\npg. 945: Discussion on evaluated data\n\nEntry 42,39 (c): No data available at the time.  Author recommends a rate coefficient\n\nof 4.8x10^-12 based on the rate expression of i-C3H7+C2H5=C2H6+C3H6\nMRH 30-Aug-2009\n\nConverted to training reaction from rate rule: C_rad/H2/O;Cmethyl_Csrad',
    ),
    rank = 10,
    shortDesc = u"""Tsang [91] Literature review.""",
)

entry(
    index = 9,
    label = "C2H5 + C3H7 <=> C3H8 + C2H4",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (6.33e+14, 'cm^3/(mol*s)', '*|/', 2),
        n = -0.7,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = '[91] Tsang, W.; Journal of Physical and Chemical Reference Data (1988), 17(2), 887-951.\nLiterature review.  i-C3H7 + i-C3H7 --> C3H6 + C3H8\n\npg. 946-947: Discussion on evaluated data\n\nEntry 42,42 (b): No high-Temperature data available.  Author has fit rate coefficient\n\nexpression for addition rxn to 4 sets of experimental data.  Recommended branching\nratio agrees well with most of the experimental data.\nMRH 30-Aug-2009\n\nConverted to training reaction from rate rule: C_rad/H/NonDeC;Cmethyl_Csrad',
    ),
    rank = 10,
    shortDesc = u"""Tsang [91] Literature review.""",
)

entry(
    index = 10,
    label = "C2H5 + C4H9 <=> C4H10 + C2H4",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (8.58e+15, 'cm^3/(mol*s)', '*|/', 1.7),
        n = -1.1,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = '[92] Tsang, W.; Journal of Physical and Chemical Reference Data (1990), 19(1), 1-68.\nLiterature review: t-C4H9 + i-C3H7 --> C3H6 + i-C4H10\n\npg. 46: Discussion on evaluated data\n\nEntry 44,42 (a): The author computes the combination rate expression using the geometric\n\nmean rule (of the rxns t-C4H9+t-C4H9-->adduct and i-C3H7+i-C3H7-->adduct).  The\ndisproportionation rate coefficient expression was then computed using the\nreported branching ratio.\nMRH 30-Aug-2009\n\nConverted to training reaction from rate rule: C_rad/Cs3;Cmethyl_Csrad',
    ),
    rank = 10,
    shortDesc = u"""Tsang [92] Literature review.""",
)

entry(
    index = 11,
    label = "C2H3-2 + C2H5 <=> C2H4-2 + C2H4",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (4.56e+14, 'cm^3/(mol*s)', '*|/', 1.5),
        n = -0.7,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = '[91] Tsang, W.; Journal of Physical and Chemical Reference Data (1988), 17(2), 887-951.\nLiterature review.  C2H3 + i-C3H7 --> C3H6 + C2H4\n\npg. 939-940: Discussion on evaluated data\n\nEntry 42,19 (a): No data available at the time.  Author recommends the rate coefficient\n\nexpression of C2H5+i-C3H7 for the rate expression for C2H3+i-C3H7.  Author also\nrecommends the branching ratio of disproportionation to addition of the \nC2H5+i-C3H7 system for the C2H3+i-C3H7 system.\nMRH 30-Aug-2009\n\nConverted to training reaction from rate rule: Cd_pri_rad;Cmethyl_Csrad',
    ),
    rank = 10,
    shortDesc = u"""Tsang [91] Literature review.""",
)

entry(
    index = 12,
    label = "C2H + C2H5 <=> C2H2 + C2H4",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (1.083e+13, 'cm^3/(mol*s)', '*|/', 2),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = '[91] Tsang, W.; Journal of Physical and Chemical Reference Data (1988), 17(2), 887-951.\nLiterature review.  C2H + i-C3H7 --> C3H6 + C2H2\n\npg. 941-942: Discussion on evaluated data\n\nEntry 42,21 (a): No data available at the time.  Author recommends a rate coefficient\n\nof 6x10^-12 cm3/molecule/s, a "typical" disproportionation rate.\nMRH 30-Aug-2009\n\nConverted to training reaction from rate rule: Ct_rad/Ct;Cmethyl_Csrad',
    ),
    rank = 10,
    shortDesc = u"""Tsang [91] Literature review.""",
)

entry(
    index = 13,
    label = "HO + C2H5 <=> H2O + C2H4",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (7.23e+13, 'cm^3/(mol*s)', '*|/', 3),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = '[91] Tsang, W.; Journal of Physical and Chemical Reference Data (1988), 17(2), 887-951.\nLiterature review.  OH + i-C3H7 --> C3H6 + H2O\n\npg. 934: Discussion on evaluated data\n\nEntry 42,6: No data available at the time.  Author notes that both a H-atom abstraction\n\nrxn and an addition + hot adduct decomposition rxn will result in the same products.\nMRH 30-Aug-2009\n\nConverted to training reaction from rate rule: O_pri_rad;Cmethyl_Csrad',
    ),
    rank = 10,
    shortDesc = u"""Tsang [91] Literature review.""",
)

entry(
    index = 14,
    label = "H + CH3O-3 <=> H2 + CH2O-2",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (5.43e+13, 'cm^3/(mol*s)', '*|/', 3.16),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1000, 'K'),
        comment = '[95] Baulch, D.L.; Cobos, C.J.; Cox, R.A.; Esser, C.; Frank, P.; Just, T.; Kerr, J.A.; Pilling, M.J.; Troe, J.; Walker, R.W.; Warnatz, J.; Journal of Physical and Chemical Reference Data (1992), 21(3), 411-734.\npg.523: Discussion of evaluated data\n\nH+CH3O --> H2+CH2O: Authors state that no new data have been reported for this reaction.\n\nMRH assumes the recommended value comes from a previous review article published\nby authors.  In any case, recommended data fits the reported data well.\nMRH 31-Aug-2009\n\nConverted to training reaction from rate rule: H_rad;Cmethyl_Orad',
    ),
    rank = 10,
    shortDesc = u"""Baulch et al [95] literature review.""",
)

entry(
    index = 15,
    label = "C3H7-2 + O2 <=> HO2 + C3H6-2",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (1.833e+13, 'cm^3/(mol*s)', '*|/', 3),
        n = 0,
        Ea = (62.1324, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (500, 'K'),
        Tmax = (900, 'K'),
        comment = '[91] Tsang, W.; Journal of Physical and Chemical Reference Data (1988), 17(2), 887-951.\nLiterature review: n-C3H7 + O2 = HO2 + C3H6\n\npg. 914-915: Discussion on evaluated data\n\nEntry 41,3 (a): The author suggests a rate coefficient based on those reported in the\n\nliterature.  The author notes that the data reported in the literature suggests\nthe formation of C3H6 is controlled by the addition rxn.  The author further\nnotes that it is surprising that p-dependence effects are not observed for\nC3H6 formation.\nMRH 30-Aug-2009\n\nDivide the rate constant by 4 to account for symmetry of 2 (O2) and 2 (n-C3H7, carbon #2).  The final result is 2.25825e+10 cm3/mol/s.\nJDM 31-Mar-2010\n\nConverted to training reaction from rate rule: O2b;C/H2/Nd_Csrad',
    ),
    rank = 10,
    shortDesc = u"""[AJ] Miyoshi 2011 (Table 4, Node 'ss') dx.doi.org/10.1021/jp112152n""",
)

entry(
    index = 16,
    label = "CH2 + C3H7-2 <=> CH3 + C3H6-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (3.62e+12, 'cm^3/(mol*s)', '*|/', 5),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = '[91] Tsang, W.; Journal of Physical and Chemical Reference Data (1988), 17(2), 887-951.\nLiterature review.  CH2_triplet + n-C3H7 --> C3H6 + CH3\n\npg. 925: Discussion on evaluated data\n\nEntry 41,26: No data available at the time.  Author estimates the rate coefficient\n\nexpression of the addition rxn.  The author then recommends that the disproportionation\nrate coefficient not exceed 10% of the combination rate.  Thus, the rate coefficient\nis an upper limit.\nMRH 30-Aug-2009\n\nConverted to training reaction from rate rule: CH2_triplet;C/H2/Nd_Csrad',
    ),
    rank = 10,
    shortDesc = u"""Tsang [91] Literature review.""",
)

entry(
    index = 17,
    label = "C2H3S + C3H7-2 <=> C2H4S + C3H6-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.438, 'cm^3/(mol*s)'),
        n = 3.13,
        Ea = (-15.2716, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
        comment = '\n\nConverted to training reaction from rate rule: S_rad/OneDe;C/H2/Nd_Csrad',
    ),
    rank = 6,
    shortDesc = u"""CAC calc CBS-QB3, 1dhr""",
)

entry(
    index = 18,
    label = "H + C3H7-2 <=> H2 + C3H6-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (3.62e+12, 'cm^3/(mol*s)', '*|/', 2),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = '[91] Tsang, W.; Journal of Physical and Chemical Reference Data (1988), 17(2), 887-951.\nLiterature review.  H + n-C3H7 --> C3H6 + H2\n\npg. 915-916: Discussion on evaluated data\n\nEntry 41,4 (a): No data available at the time.  Author recommends the rate coefficient\n\nof the H+C2H5=C2H4+H2 rxn for the H+n-C3H7=C3H6+H2 rxn.\nMRH 30-Aug-2009\n\nConverted to training reaction from rate rule: H_rad;C/H2/Nd_Csrad',
    ),
    rank = 10,
    shortDesc = u"""Tsang [91] Literature review.""",
)

entry(
    index = 19,
    label = "C4H7 + C2H5S <=> C4H8 + C2H4S-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.526e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-2.3012, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
        comment = '[91] Tsang, W.; Journal of Physical and Chemical Reference Data (1988), 17(2), 887-951.\nLiterature review.  CH3 + n-C3H7 --> C3H6 + CH4\n\npg. 920: Discussion on evaluated data\n\nEntry 41,16 (b): No direct measurements for either the addition or disproportionation\n\nrxns.  Author recommends a rate coefficient expression for the addition rxn, based\non the geometric mean rule of the rxns CH3+CH3=>adduct and n-C3H7+n-C3H7=>adduct.\nFurthermore, author recommends a branching ratio for disproportionation to\naddition of 0.06 (which appears to MRH to be consistent with the experimentally\nmeasured branching ratios)\nMRH 30-Aug-2009\n\nConverted to training reaction from rate rule: C_rad/H/OneDeC;C/H2/Nd_Srad',
    ),
    rank = 11,
    shortDesc = u"""Rough estimate based on 1/10 of #3026 in R_Recombination""",
)

entry(
    index = 20,
    label = "CH3 + C3H7-2 <=> CH4 + C3H6-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (2.3e+13, 'cm^3/(mol*s)', '*|/', 1.7),
        n = -0.32,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = '[91] Tsang, W.; Journal of Physical and Chemical Reference Data (1988), 17(2), 887-951.\nLiterature review.  CH3 + n-C3H7 --> C3H6 + CH4\n\npg. 920: Discussion on evaluated data\n\nEntry 41,16 (b): No direct measurements for either the addition or disproportionation\n\nrxns.  Author recommends a rate coefficient expression for the addition rxn, based\non the geometric mean rule of the rxns CH3+CH3=>adduct and n-C3H7+n-C3H7=>adduct.\nFurthermore, author recommends a branching ratio for disproportionation to\naddition of 0.06 (which appears to MRH to be consistent with the experimentally\nmeasured branching ratios)\nMRH 30-Aug-2009\n\nConverted to training reaction from rate rule: C_methyl;C/H2/Nd_Csrad',
    ),
    rank = 10,
    shortDesc = u"""Tsang [91] Literature review.""",
)

entry(
    index = 21,
    label = "C3H7-2 + C2H5-2 <=> C2H6 + C3H6-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (2.9e+12, 'cm^3/(mol*s)', '*|/', 1.4),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = '[91] Tsang, W.; Journal of Physical and Chemical Reference Data (1988), 17(2), 887-951.\nLiterature review.  C2H5 + n-C3H7 --> C3H6 + C2H6\n\npg. 937-938: Discussion on evaluated data\n\nEntry 42,17 (b): No direct measurements for either the addition or disproportionation\n\nrxns.  Author recommends a rate coefficient expression for the addition rxn, based\non the geometric mean rule of the rxns C2H5+C2H5=>adduct and n-C3H7+n-C3H7=>adduct.\nFurthermore, author recommends a branching ratio for disproportionation to\naddition of 0.073 (which is an average of the 2 experimentally determined\nbranching ratios)\nMRH 30-Aug-2009\n\nConverted to training reaction from rate rule: C_rad/H2/Cs;C/H2/Nd_Csrad',
    ),
    rank = 10,
    shortDesc = u"""Tsang [91] Literature review.""",
)

entry(
    index = 22,
    label = "C5H7 + C2H5S <=> C5H8 + C2H4S-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (3.88e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (1.50624, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
        comment = '[91] Tsang, W.; Journal of Physical and Chemical Reference Data (1988), 17(2), 887-951.\nLiterature review.  C2H5 + n-C3H7 --> C3H6 + C2H6\n\npg. 937-938: Discussion on evaluated data\n\nEntry 42,17 (b): No direct measurements for either the addition or disproportionation\n\nrxns.  Author recommends a rate coefficient expression for the addition rxn, based\non the geometric mean rule of the rxns C2H5+C2H5=>adduct and n-C3H7+n-C3H7=>adduct.\nFurthermore, author recommends a branching ratio for disproportionation to\naddition of 0.073 (which is an average of the 2 experimentally determined\nbranching ratios)\nMRH 30-Aug-2009\n\nConverted to training reaction from rate rule: C_rad/H/TwoDe;C/H2/Nd_Srad',
    ),
    rank = 11,
    shortDesc = u"""Rough estimate based on 1/10 of #3027 in R_Recombination""",
)

entry(
    index = 23,
    label = "C3H5 + C3H7-2 <=> C3H6 + C3H6-2",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (5.8e+12, 'cm^3/(mol*s)', '*|/', 3),
        n = 0,
        Ea = (-0.54392, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = '[93] Tsang, W.; Journal of Physical and Chemical Reference Data (1991), 20(2), 221-273.\nLiterature review: C3H5 + nC3H7 --> C3H6 + C3H6\n\npg.268: Discussion on evaluated data\n\nEntry 47,41(a): No data available at the time.  Recommended rate coefficient expression\n\nbased on rxn C3H5+C2H5=C2H4+C3H6 (James, D.G.L. and Troughton, G.E.) and values\nfor "alkyl radicals" (Gibian M.J. and Corley R.C.); this leads to disproportionation-\nto-addition ratio of 0.07.  The addition rate expression was derived using the geometric\nmean rule for the rxns C3H5+C3H5-->adduct and nC3H7+nC3H7-->adduct.\nMRH 31-Aug-2009\n\nConverted to training reaction from rate rule: C_rad/H2/Cd;C/H2/Nd_Csrad',
    ),
    rank = 10,
    shortDesc = u"""Tsang [93] Literature review.""",
)

entry(
    index = 24,
    label = "C2H3S + C4H9-2 <=> C2H4S + C4H8-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (7.63e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-2.3012, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
        comment = '\n\nConverted to training reaction from rate rule: S_rad/OneDe;C/H/NdNd_Csrad',
    ),
    rank = 11,
    shortDesc = u"""VERY Rough estimate based on 1/10 of #3026 in R_Recombination""",
)

entry(
    index = 25,
    label = "CH3O-2 + C3H7-2 <=> CH4O + C3H6-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (9.64e+11, 'cm^3/(mol*s)', '*|/', 3),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = '[91] Tsang, W.; Journal of Physical and Chemical Reference Data (1988), 17(2), 887-951.\nLiterature review.  CH2OH + n-C3H7 --> C3H6 + CH3OH\n\npg. 926: Discussion on evaluated data\n\nEntry 41,39 (c): No data available at the time.  Author estimates the rate coefficient\n\nfor the addition rxn to be similar to the rate for n-C3H7+n-C3H7=>adduct.  Author\nalso estimates the branching ratio of disproportionation to addition as 0.051\nMRH 30-Aug-2009\n\nConverted to training reaction from rate rule: C_rad/H2/O;C/H2/Nd_Csrad',
    ),
    rank = 10,
    shortDesc = u"""Tsang [91] Literature review.""",
)

entry(
    index = 26,
    label = "C4H9-2 + CH3S <=> CH4S + C4H8-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (7.63e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (-2.3012, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
        comment = '[91] Tsang, W.; Journal of Physical and Chemical Reference Data (1988), 17(2), 887-951.\nLiterature review.  CH2OH + n-C3H7 --> C3H6 + CH3OH\n\npg. 926: Discussion on evaluated data\n\nEntry 41,39 (c): No data available at the time.  Author estimates the rate coefficient\n\nfor the addition rxn to be similar to the rate for n-C3H7+n-C3H7=>adduct.  Author\nalso estimates the branching ratio of disproportionation to addition as 0.051\nMRH 30-Aug-2009\n\nConverted to training reaction from rate rule: S_rad/NonDeC;C/H/NdNd_Csrad',
    ),
    rank = 11,
    shortDesc = u"""Rough estimate based on 1/10 of #3026 in R_Recombination""",
)

entry(
    index = 27,
    label = "C3H7-2 + C3H7 <=> C3H8 + C3H6-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (5.13e+13, 'cm^3/(mol*s)', '*|/', 2),
        n = -0.35,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = '[91] Tsang, W.; Journal of Physical and Chemical Reference Data (1988), 17(2), 887-951.\nLiterature review.  i-C3H7 + n-C3H7 --> C3H6 + C3H8\n\npg. 945-946: Discussion on evaluated data\n\nEntry 42,41 (b): No data available at the time.  Author estimates the rate coefficient\n\nexpression of the addition rxn using the rate for i-C3H7+i-C3H7=>adduct, the rate\nfor n-C3H7+n-C3H7=>adduct, and the geometric mean rule.  The author recommends\nthe branching ratio of disproportionation to addition reported by Gibian and\nCorley (1973).\nMRH 30-Aug-2009\n\nDegeneracy not recalculated\n\nConverted to training reaction from rate rule: C_rad/H/NonDeC;C/H2/Nd_Csrad',
    ),
    rank = 10,
    shortDesc = u"""Tsang [91] Literature review.""",
)

entry(
    index = 28,
    label = "C3H7-2 + C4H9 <=> C4H10 + C3H6-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (4.32e+14, 'cm^3/(mol*s)', '*|/', 2),
        n = -0.75,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = '[92] Tsang, W.; Journal of Physical and Chemical Reference Data (1990), 19(1), 1-68.\nLiterature review: t-C4H9 + n-C3H7 --> C3H6 + i-C4H10\n\npg. 45: Discussion on evaluated data\n\nEntry 44,41 (a): No data available at the time.  Author estimates the rate expression\n\nfor the combination rxn using the geometric mean rule (of the rxns t-C4H9+t-C4H9-->adduct\nand n-C3H7+n-C3H7-->adduct).  The author then estimates the disproportionation\nrate expression using the branching ratio; the branching ratio is from "analogous\nprocesses".\nMRH 30-Aug-2009\n\nConverted to training reaction from rate rule: C_rad/Cs3;C/H2/Nd_Csrad',
    ),
    rank = 10,
    shortDesc = u"""Tsang [92] Literature review.""",
)

entry(
    index = 29,
    label = "C2H3-2 + C3H7-2 <=> C2H4-2 + C3H6-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (2.42e+12, 'cm^3/(mol*s)', '*|/', 3),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = '[91] Tsang, W.; Journal of Physical and Chemical Reference Data (1988), 17(2), 887-951.\nLiterature review.  C2H3 + n-C3H7 --> C3H6 + C2H4\n\npg. 922: Discussion on evaluated data\n\nEntry 41,19 (a): No data available at the time.  Author estimates the rate coefficient\n\nbased on the rxn C2H5+n-C3H7=C3H6=C2H6.\nMRH 30-Aug-2009\n\nConverted to training reaction from rate rule: Cd_pri_rad;C/H2/Nd_Csrad',
    ),
    rank = 10,
    shortDesc = u"""Tsang [91] Literature review.""",
)

entry(
    index = 30,
    label = "HS2 + C5H9 <=> H2S2 + C5H8-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.288e+09, 'cm^3/(mol*s)'),
        n = 1.19,
        Ea = (2.13384, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
        comment = '\n\nConverted to training reaction from rate rule: S_rad/NonDeS;C/H2/Nd_Csrad/H/Cd',
    ),
    rank = 11,
    shortDesc = u"""Very rough based on R_Recomb #491""",
)

entry(
    index = 31,
    label = "C2H + C3H7-2 <=> C2H2 + C3H6-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.206e+13, 'cm^3/(mol*s)', '*|/', 3),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = '[91] Tsang, W.; Journal of Physical and Chemical Reference Data (1988), 17(2), 887-951.\nLiterature review.  C2H + n-C3H7 --> C3H6 + C2H2\n\npg. 923: Discussion on evaluated data\n\nEntry 41,21 (a): No data available at the time.  Author notes that the rxn is more exothermic\n\nthan the rxn CH3+n-C3H7=C3H6+CH4 and suggests a rate coefficient 3x larger,\nnamely 1.0x10^-11 cm3/molecule/s.\nMRH 30-Aug-2009\n\nConverted to training reaction from rate rule: Ct_rad/Ct;C/H2/Nd_Csrad',
    ),
    rank = 10,
    shortDesc = u"""Tsang [91] Literature review.""",
)

entry(
    index = 32,
    label = "HS2 + CH3S-2 <=> H2S2 + CH2S",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.44e+08, 'cm^3/(mol*s)'),
        n = 1.19,
        Ea = (2.13384, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
        comment = '\n\nConverted to training reaction from rate rule: S_rad/NonDeS;S_Csrad',
    ),
    rank = 11,
    shortDesc = u"""Very rough based on R_Recomb #491""",
)

entry(
    index = 33,
    label = "HO + C3H7-2 <=> H2O + C3H6-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (4.82e+13, 'cm^3/(mol*s)', '*|/', 3),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = '[91] Tsang, W.; Journal of Physical and Chemical Reference Data (1988), 17(2), 887-951.\nLiterature review.  OH + n-C3H7 --> C3H6 + H2O\n\npg. 917: Discussion on evaluated data\n\nEntry 41,6 (a): No data available at the time.  Author estimates rate coefficient based\n\non the rate coefficient for OH+C2H5=C2H4+H2O, namely 4.0x10^-11 cm3/molecule/s.\nMRH 30-Aug-2009\n\nConverted to training reaction from rate rule: O_pri_rad;C/H2/Nd_Csrad',
    ),
    rank = 10,
    shortDesc = u"""Tsang [91] Literature review.""",
)

entry(
    index = 34,
    label = "C4H9-2 + O2 <=> HO2 + C4H8-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (2.4088e+10, 'cm^3/(mol*s)', '*|/', 5),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (600, 'K'),
        Tmax = (1000, 'K'),
        comment = "[92] Tsang, W.; Journal of Physical and Chemical Reference Data (1990), 19(1), 1-68.\nLiterature review: O2 + iC4H9 --> iC4H8 + HO2\n\npg. 52-53: Discussion on evaluated data\n\nEntry 45,3 (a): The author recommends a rate coefficient based on the experiments performed\n\nby Baker et al. (yielding a disproportionation-to-decomposition ratio) and the\ncurrent (Tsang) study's recommended iC4H9 unimolecular decomposition rate.\nMRH 31-Aug-2009\n\nDivide the rate constant by 2 to account for symmetry of 2 (O2) and 1 (i-C4H9, carbon #2).  The final result is 1.2044e+10 cm3/mol/s.\nJDM 31-Mar-2010\n\nConverted to training reaction from rate rule: O2b;C/H/NdNd_Csrad",
    ),
    rank = 10,
    shortDesc = u"""Tsang [92] Literature review.""",
)

entry(
    index = 35,
    label = "C2H + C4H9-2 <=> C2H2 + C4H8-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.03e+12, 'cm^3/(mol*s)', '*|/', 3),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = '[92] Tsang, W.; Journal of Physical and Chemical Reference Data (1990), 19(1), 1-68.\nLiterature review: C2H + i-C4H9 --> i-C4H8 + C2H2\n\npg. 61: Discussion on evaluated data\n\nEntry 45,21: No data available at the time.  The author estimates the rate of \n\ndisproportionation to be 1x10^-11 cm3/molecule/s.\n*** NOTE: RMG_database previously had CH2_triplet as Y_rad_birad node, not Ct_rad ***\n\nMRH 30-Aug-2009\n\nConverted to training reaction from rate rule: Ct_rad/Ct;C/H/NdNd_Csrad',
    ),
    rank = 10,
    shortDesc = u"""Tsang [92] Literature review.""",
)

entry(
    index = 36,
    label = "H + C4H9-2 <=> H2 + C4H8-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (9.04e+11, 'cm^3/(mol*s)', '*|/', 2),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = '[92] Tsang, W.; Journal of Physical and Chemical Reference Data (1990), 19(1), 1-68.\nLiterature review: H + i-C4H9 --> i-C4H8 + H2\n\npg. 53: Discussion on evaluated data\n\nEntry 45,4 (c): No data available at the time.  The author estimates the disproportionation\n\nrate coefficent as half the rate of H+n-C3H7=C3H6+H2 (due to the presence of 2\nH-atoms on the alpha-carbon in n-C3H7 and only 1 on the alpha-carbon of i-C4H9).\nThe author also states that the branching ratio is pressure-dependent and supplies\nfall-off tables and collisional efficiencies.\nMRH 30-Aug-2009\n\nConverted to training reaction from rate rule: H_rad;C/H/NdNd_Csrad',
    ),
    rank = 10,
    shortDesc = u"""Tsang [92] Literature review.""",
)

entry(
    index = 37,
    label = "CH3 + C4H9-2 <=> CH4 + C4H8-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.02e+12, 'cm^3/(mol*s)', '*|/', 2),
        n = -0.32,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = '[92] Tsang, W.; Journal of Physical and Chemical Reference Data (1990), 19(1), 1-68.\nLiterature review: CH3 + i-C4H9 --> i-C4H8 + CH4\n\npg. 58: Discussion on evaluated data\n\nEntry 45,16 (b): No data available at the time.  The author estimates the disproportionation\n\nrate coefficient as half the rate of CH3+n-C3H7=C3H6+H2 (due to half as many H-atoms\non the alpha-carbon).\nMRH 30-Aug-2009\n\nConverted to training reaction from rate rule: C_methyl;C/H/NdNd_Csrad',
    ),
    rank = 10,
    shortDesc = u"""Tsang [92] Literature review.""",
)

entry(
    index = 38,
    label = "C4H9-2 + C2H5-2 <=> C2H6 + C4H8-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (8.43e+11, 'cm^3/(mol*s)', '*|/', 2),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = '[92] Tsang, W.; Journal of Physical and Chemical Reference Data (1990), 19(1), 1-68.\nLiterature review: C2H5 + i-C4H9 --> i-C4H8 + C2H6\n\npg. 59: Discussion on evaluated data\n\nEntry 45,17 (a): No direct measurements of either the addition or disproportionation rxns.\n\nThe combination rate coefficient was computed using the geometric mean rule (of the\nrxns C2H5+C2H5-->adduct and i-C4H9+i-C4H9-->adduct).  The disproportionation rate\ncoefficient was computed using the disproportionation-to-combination ratio reported\nby Gibian and Corley (1973).\nMRH 30-Aug-2009\n\nConverted to training reaction from rate rule: C_rad/H2/Cs;C/H/NdNd_Csrad',
    ),
    rank = 10,
    shortDesc = u"""Tsang [92] Literature review.""",
)

entry(
    index = 39,
    label = "CH3O-2 + C4H9-2 <=> CH4O + C4H8-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.41e+11, 'cm^3/(mol*s)', '*|/', 3),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = '[92] Tsang, W.; Journal of Physical and Chemical Reference Data (1990), 19(1), 1-68.\nLiterature review: CH2OH + i-C4H9 --> i-C4H8 + CH3OH\n\npg. 64: Discussion on evaluated data\n\nEntry 45,39 (c): No data available at the time.  Author estimates the disproportionation rate\n\ncoefficient as half the rate of CH2OH+n-C3H7=C3H6+CH3OH (due to half as many H-atoms\non the alpha-carbon).\n*** NOTE: Although author states the the rate coefficient of CH2OH+i-C4H9=i-C4H8+CH3OH\n\nis half that of CH2OH+n-C3H7=C3H6+CH3OH, MRH finds them to be equal, both in the electronic\nreferences and the online NIST database (kinetics.nist.gov).  I am therefore\ncutting the A in the RMG_database in two. ***\nMRH 30-Aug-2009\n\nConverted to training reaction from rate rule: C_rad/H2/O;C/H/NdNd_Csrad',
    ),
    rank = 10,
    shortDesc = u"""Tsang [92] Literature review.""",
)

entry(
    index = 40,
    label = "C3H5 + C4H9-2 <=> C3H6 + C4H8-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.566e+12, 'cm^3/(mol*s)', '*|/', 3),
        n = 0,
        Ea = (-0.54392, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = '[93] Tsang, W.; Journal of Physical and Chemical Reference Data (1991), 20(2), 221-273.\nLiterature review: C3H5 + iC4H9 --> iC4H8 + C3H6\n\npg.270: Discussion on evaluated data\n\nEntry 47,45(a): No data available at the time.  Recommended rate coefficient expression\n\nbased on rxn C3H5+C2H5=C2H4+C3H6 (James, D.G.L. and Troughton, G.E.); this leads to disproportionation-\nto-addition ratio of 0.04.  The addition rate expression was derived using the geometric\nmean rule for the rxns C3H5+C3H5-->adduct and iC4H9+iC4H9-->adduct.\nMRH 31-Aug-2009\n\nConverted to training reaction from rate rule: C_rad/H2/Cd;C/H/NdNd_Csrad',
    ),
    rank = 10,
    shortDesc = u"""Tsang [93] Literature review.""",
)

entry(
    index = 41,
    label = "C4H9-2 + C3H7 <=> C3H8 + C4H8-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.56e+13, 'cm^3/(mol*s)', '*|/', 2),
        n = -0.35,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = "[92] Tsang, W.; Journal of Physical and Chemical Reference Data (1990), 19(1), 1-68.\nLiterature review: i-C3H7 + i-C4H9 --> i-C4H8 + C3H8\n\npg. 65: Discussion on evaluated data\n\nEntry 45,42 (b): No data available at the time.  Author estimates the disproportionation rate\n\ncoefficient as half the rate of i-C3H7+n-C3H7=C3H6+C3H8 (due to half as many H-atoms\non the alpha-carbon).\n*** NOTE: MRH computes half the rate of i-C3H7+n-C3H7=C3H6+C3H8 as 0.52x10^-11 * (300/T)^0.35,\n\nnot 0.58x10^-11 * (300/T)^0.35.  However, there may be a reason for the relatively\nsmall discrepancy between the author's stated and implemented calculation. ***\nMRH 30-Aug-2009\n\nConverted to training reaction from rate rule: C_rad/H/NonDeC;C/H/NdNd_Csrad",
    ),
    rank = 10,
    shortDesc = u"""Tsang [92] Literature review.""",
)

entry(
    index = 42,
    label = "C4H9-2 + C4H9 <=> C4H10 + C4H8-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.08e+14, 'cm^3/(mol*s)', '*|/', 2),
        n = -0.75,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = '[92] Tsang, W.; Journal of Physical and Chemical Reference Data (1990), 19(1), 1-68.\nLiterature review: t-C4H9 + i-C4H9 --> i-C4H8 + i-C4H10\n\npg. 66: Discussion on evaluated data\n\nEntry 45,44 (b): No data available at the time.  Author estimates the disproportionation rate\n\ncoefficient as half the rate of t-C4H9+n-C3H7=C3H6+i-C4H10 (due to half as many H-atoms\non the alpha-carbon).\n*** NOTE: Although author states the the rate coefficient of t-C4H9+i-C4H9=i-C4H8+i-C4H10\n\nis half that of t-C4H9+n-C3H7=C3H6+i-C4H10, MRH finds them to be equal, both in the electronic\nreferences and the online NIST database (kinetics.nist.gov).  I am therefore\ncutting the A in the RMG_database in two. ***\nMRH 30-Aug-2009\n\nDegeneracy not recalculated\n\nConverted to training reaction from rate rule: C_rad/Cs3;C/H/NdNd_Csrad',
    ),
    rank = 10,
    shortDesc = u"""Tsang [92] Literature review.""",
)

entry(
    index = 43,
    label = "C2H3-2 + C4H9-2 <=> C2H4-2 + C4H8-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (8.43e+11, 'cm^3/(mol*s)', '*|/', 4),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = '[92] Tsang, W.; Journal of Physical and Chemical Reference Data (1990), 19(1), 1-68.\nLiterature review: C2H3 + i-C4H9 --> i-C4H8 + C2H4\n\npg. 60: Discussion on evaluated data\n\nEntry 45,19 (b): No data available at the time.  Author estimates the disproportionation rate\n\ncoefficient based on the rate of C2H5+i-C4H9=i-C4H8+C2H6.\nMRH 30-Aug-2009\n\nConverted to training reaction from rate rule: Cd_pri_rad;C/H/NdNd_Csrad',
    ),
    rank = 10,
    shortDesc = u"""Tsang [92] Literature review.""",
)

entry(
    index = 44,
    label = "HO + C4H9-2 <=> H2O + C4H8-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.21e+13, 'cm^3/(mol*s)', '*|/', 3),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = '[92] Tsang, W.; Journal of Physical and Chemical Reference Data (1990), 19(1), 1-68.\nLiterature review: OH + i-C4H9 --> i-C4H8 + H2O\n\npg. 55: Discussion on evaluated data\n\nEntry 45,6 (a): No data available at the time.  Author estimates the disproportionation rate\n\ncoefficient as half the rate of OH+n-C3H7=C3H6+H2O (due to half as many H-atoms\non the alpha-carbon).\nMRH 30-Aug-2009\n\nConverted to training reaction from rate rule: O_pri_rad;C/H/NdNd_Csrad',
    ),
    rank = 10,
    shortDesc = u"""Tsang [92] Literature review.""",
)

entry(
    index = 45,
    label = "C3H5-2 + O2 <=> HO2 + C3H4",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.2044e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (56.6932, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = '[93] Tsang, W.; Journal of Physical and Chemical Reference Data (1991), 20(2), 221-273.\nLiterature review: O2 + C3H5 --> H2C=C=CH2 + HO2\n\npg.251: Discussion on evaluated data\n\n*** UPPER LIMIT ***\n\nEntry 47,3(b): The author states that there is uncertainty whether this rxn is appreciable\n\nat high temperatures.  There were conflicting results published regarding the\nsignificance above 461K (Morgan et al. and Slagle and Gutman).  The author thus\ndecides to place an upper limit on the rate coefficient of 2x10^-12 * exp(-6820/T)\ncm3/molecule/s.  The author further notes that this upper limit assumes no\ncontribution from a complex rearrangement of the adduct.  Finally, the author\nnotes that this rxn should not be significant in combustion situations.\nMRH 31-Aug-2009\n\nDivide the rate constant by 2 to account for symmetry of 2 (O2) and 1 (allyl, carbon #2). The final result is 6.022e+11 cm3/mol/s, Ea = 13.55 kcal/mol.\nJDM 31-Mar-2010\n\nConverted to training reaction from rate rule: O2b;Cdpri_Csrad',
    ),
    rank = 10,
    shortDesc = u"""Tsang [93] Literature review.""",
)

entry(
    index = 46,
    label = "CH3 + C3H5-2 <=> CH4 + C3H4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.01e+12, 'cm^3/(mol*s)', '*|/', 3),
        n = 0,
        Ea = (25.104, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = '[93] Tsang, W.; Journal of Physical and Chemical Reference Data (1991), 20(2), 221-273.\nLiterature review: CH3 + C3H5 --> H2C=C=CH2 + CH4\n\npg.257: Discussion on evaluated data\n\nEntry 47,16(a): No data available at the time.  Recommended rate coefficient expression\n\nbased on rxn C3H5+C2H5=C2H4+C3H6 (James, D.G.L. and Troughton, G.E.); this leads to disproportionation-\nto-addition ratio of 0.03.  The addition rate expression was derived using the geometric\nmean rule for the rxns C3H5+C3H5-->adduct and CH3+CH3-->adduct.\nNOTE: The Ea reported in the discussion is Ea/R=-132 Kelvin.  However, in the table near\n\nthe beginning of the review article (summarizing all reported data) and in the NIST\nonline database (kinetics.nist.gov), the reported Ea/R=-66 Kelvin.  MRH took the\ngeometric mean of the allyl combination rxn (1.70x10^-11 * exp(132/T)) and methyl\ncombination rxn (1.68x10^-9 * T^-0.64) to obtain 1.69x10^-11 * T^-0.32 * exp(66/T).\nMultiplying by 0.03 results in the recommended rate coefficient expression.\nMRH 31-Aug-2009\n\nConverted to training reaction from rate rule: C_methyl;Cdpri_Csrad',
    ),
    rank = 11,
    shortDesc = u"""SSM estimate. Original value with 6 kcal barrier""",
)

entry(
    index = 47,
    label = "C3H5-2 + C2H5-2 <=> C2H6 + C3H4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (9.64e+11, 'cm^3/(mol*s)', '*|/', 2),
        n = 0,
        Ea = (25.104, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = '[93] Tsang, W.; Journal of Physical and Chemical Reference Data (1991), 20(2), 221-273.\nLiterature review: C2H5 + C3H5 --> H2C=C=CH2 + C2H6\n\npg.259: Discussion on evaluated data\n\nEntry 47,17(a): The recommended rate expression is derived from the experimentally-\n\ndetermined disproportionation-to-addition ratio of 0.047 (James and Troughton)\nand the addition rate rule (C2H5+C3H5-->adduct) calculated using the geometric\nmean rule of the rxns C2H5+C2H5-->adduct and C3H5+C3H5-->adduct.\nMRH 31-Aug-2009\n\nConverted to training reaction from rate rule: C_rad/H2/Cs;Cdpri_Csrad',
    ),
    rank = 11,
    shortDesc = u"""SSM estimate. Original value with 6 kcal barrier""",
)

entry(
    index = 48,
    label = "C3H5-2 + C3H5 <=> C3H6 + C3H4",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.686e+11, 'cm^3/(mol*s)', '*|/', 2.5),
        n = 0,
        Ea = (25.104, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = '[93] Tsang, W.; Journal of Physical and Chemical Reference Data (1991), 20(2), 221-273.\nLiterature review: C3H5 + C3H5 --> H2C=C=CH2 + C3H6\n\npg.271-272: Discussion on evaluated data\n\nEntry 47,47(b): The recommended rate expression is derived from the experimentally-\n\ndetermined disproportionation-to-addition ratio of 0.008 (James and Kambanis)\nand the addition rate rule (C3H5+C3H5-->adduct) calculated based on the results\nof Tulloch et al.\nMRH 31-Aug-2009\n\nConverted to training reaction from rate rule: C_rad/H2/Cd;Cdpri_Csrad',
    ),
    rank = 11,
    shortDesc = u"""SSM estimate. Original value with 6 kcal barrier""",
)

entry(
    index = 49,
    label = "C3H5-2 + C3H7 <=> C3H8 + C3H4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.58e+12, 'cm^3/(mol*s)', '*|/', 3),
        n = 0,
        Ea = (25.104, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = '[93] Tsang, W.; Journal of Physical and Chemical Reference Data (1991), 20(2), 221-273.\nLiterature review: iC3H7 + C3H5 --> H2C=C=CH2 + C3H8\n\npg.268: Discussion on evaluated data\n\nEntry 47,42(b): No data available at the time.  Recommended rate coefficient expression\n\nbased on rxn C3H5+C2H5=C2H4+C3H6 (James, D.G.L. and Troughton, G.E.) and values\nfor "alkyl radicals" (Gibian M.J. and Corley R.C.); this leads to disproportionation-\nto-addition ratio of 0.04.  The addition rate expression was derived using the geometric\nmean rule for the rxns C3H5+C3H5-->adduct and iC3H7+iC3H7-->adduct.\nMRH 31-Aug-2009\n\nConverted to training reaction from rate rule: C_rad/H/NonDeC;Cdpri_Csrad',
    ),
    rank = 11,
    shortDesc = u"""SSM estimate. Original value with 6 kcal barrier""",
)

entry(
    index = 50,
    label = "C3H5-2 + C4H9 <=> C4H10 + C3H4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.89e+13, 'cm^3/(mol*s)', '*|/', 3),
        n = 0,
        Ea = (25.104, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = '[93] Tsang, W.; Journal of Physical and Chemical Reference Data (1991), 20(2), 221-273.\nLiterature review: tC4H9 + C3H5 --> H2C=C=CH2 + iC4H10\n\npg.269: Discussion on evaluated data\n\nEntry 47,44(b): No data available at the time.  Recommended rate coefficient expression\n\nbased on "allyl and alkyl radicals behaving in similar fashion" (possibly referencing\nGibian M.J. and Corley R.C.); this leads to disproportionation-\nto-addition ratio of 0.04.  The addition rate expression was derived using the geometric\nmean rule for the rxns C3H5+C3H5-->adduct and tC4H9+tC4H9-->adduct.\nMRH 31-Aug-2009\n\nConverted to training reaction from rate rule: C_rad/Cs3;Cdpri_Csrad',
    ),
    rank = 11,
    shortDesc = u"""SSM estimate. Original value with 6 kcal barrier""",
)

entry(
    index = 51,
    label = "C2H3-2 + C3H5-2 <=> C2H4-2 + C3H4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.41e+12, 'cm^3/(mol*s)', '*|/', 3),
        n = 0,
        Ea = (25.104, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = '[93] Tsang, W.; Journal of Physical and Chemical Reference Data (1991), 20(2), 221-273.\nLiterature review: C2H3 + C3H5 --> H2C=C=CH2 + C2H4\n\npg.261-262: Discussion on evaluated data\n\nEntry 47,19(d): No data available at the time.  Author recommends a rate coefficient\n\nof 4x10^-12 cm3/molecule/s for the disproportionation rxn.\nMRH 31-Aug-2009\n\nConverted to training reaction from rate rule: Cd_pri_rad;Cdpri_Csrad',
    ),
    rank = 11,
    shortDesc = u"""SSM estimate. Original value with 6 kcal barrier""",
)

entry(
    index = 52,
    label = "HO + C3H5-2 <=> H2O + C3H4",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (6.03e+12, 'cm^3/(mol*s)', '*|/', 3),
        n = 0,
        Ea = (25.104, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = '[93] Tsang, W.; Journal of Physical and Chemical Reference Data (1991), 20(2), 221-273.\nLiterature review: OH + C3H5 --> H2C=C=CH2 + H2O\n\npg.253: Discussion on evaluated data\n\nEntry 47,6(a): No data available at the time.  Author recommends a rate coefficient\n\nof 1x10^-11 cm3/molecule/s, based on "comparable rxns".\nMRH 31-Aug-2009\n\nConverted to training reaction from rate rule: O_pri_rad;Cdpri_Csrad',
    ),
    rank = 11,
    shortDesc = u"""SSM estimate. Original value with 6 kcal barrier""",
)

entry(
    index = 53,
    label = "CH3O + O2 <=> HO2 + CH2O",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.14418e+13, 'cm^3/(mol*s)', '*|/', 2),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        comment = '[98] Atkinson, R.; Baulch, D.L.; Cox, R.A.; Crowley, J.N.; Hampson, R.F., Jr.; Kerr, J.A.; Rossi, M.J.; Troe, J. "Summary of Evaluated Kinetic and Photochemical Data for Atmospheric Chemistry,", 2001.\nLiterature review: CH3CHOH + O2 --> CH3CHO + HO2\n\nRecommended value is k298.  This reference just gives a table of results,\n\nwith no discussion on how the preferred numbers were arrived at.\nMRH 31-Aug-2009\n\nDivide the rate constant by 2 to account for symmetry of 2 (O2) and 1 (CH3CHOH, oxygen atom). The final result is 5.7209e+12 cm3/mol/s.\nJDM 31-Mar-2010\n\nConverted to training reaction from rate rule: O2b;O_Csrad',
    ),
    rank = 10,
    shortDesc = u"""Atkinson et al [98] literature review.""",
)

entry(
    index = 54,
    label = "CH3O + O <=> HO-2 + CH2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (9.04e+13, 'cm^3/(mol*s)', '+|-', 3.01e+13),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        comment = '[189] Grotheer, H.; Riekert, G.; Walter, D.; Just, T. Symp. Int. Combust. Proc. 1989, 22, 963.\nAbsolute value measured directly. Excitation: discharge, analysis: mass spectroscopy. Original uncertainty 3.0E+13\n\nO + CH2OC --> OH + CH2O, O + CH3CHOH --> OH + CH3CHO\n\nO+CH2OH --> OH+CH2O && O+CH3CHOH --> OH+CH3CHO\n\npg.963: Measured rate coefficients mentioned in abstract as k_2M and k_2E.\n\npg.965-967: Discussion on measured rate coefficients.\n\nMRH 1-Sept-2009\n\nConverted to training reaction from rate rule: O_atom_triplet;O_Csrad',
    ),
    rank = 6,
    shortDesc = u"""Grotheer et al [189].""",
)

entry(
    index = 55,
    label = "CH2 + CH3O <=> CH3 + CH2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.21e+12, 'cm^3/(mol*s)', '*|/', 3),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = '[90] Tsang, W.; Journal of Physical and Chemical Reference Data (1987), 16(3), 471-508.\nLiterature review: CH2 + CH2OH --> CH3 + CH2O\n\npg. 505: Discussion on evaluated data\n\nEntry 39,26 (b): CH2OH + CH2(triplet) --> CH3 + CH2O\n\nAuthor estimates the rate of disproportionation as 2.0x10^-12 cm3/molecule/s.  No data at the time.\n\nMRH 30-Aug-2009\n\nConverted to training reaction from rate rule: CH2_triplet;O_Csrad',
    ),
    rank = 10,
    shortDesc = u"""Tsang [90] Literature review.""",
)

entry(
    index = 56,
    label = "H + CH3O <=> H2 + CH2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2e+13, 'cm^3/(mol*s)', '+|-', 1e+13),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (295, 'K'),
        comment = '[190] Edelbuttel-Einhaus, J.; Hoyermann, K.; Rohde, G.; Seeba, J. Symp. Int. Combust. Proc. 1992, 22, 661.\nData derived from fitting to a complex mechanism. Excitation: discharge, analysis: mass spectroscopy. Original uncertainty 1.0E+13\n\nH + CH3CHOH --> H2 + CH3CHO\n\nH+CH3CHOH --> H2+CH3CHO\n\npg.661: Measured rate coefficient mentioned in abstract as k6.\n\npg.665-666: Discussion on measured rate coefficient.  The reported rate coefficient is\n\nfor H+CH3CHOH --> products, making this an UPPER LIMIT.  The rate coefficient\nwas calculated based on the rate coefficient of the rxn C2H5+H --> CH3+CH3; the\nvalue the authors used was 3.6x10^13 cm3/mol/s.\nMRH 1-Sept-2009\n\nConverted to training reaction from rate rule: H_rad;O_Csrad',
    ),
    rank = 10,
    shortDesc = u"""Edelbuttel-Einhaus et al [190].""",
)

entry(
    index = 57,
    label = "CH3O + CH3 <=> CH4 + CH2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (8.49e+13, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        comment = '[191] Pagsberg, P.; Munk, J.; Sillesen, A.; Anastasi, C. Chem. Phys. Lett. 1988, 146, 375.\nAbsolute value measured directly. Excitatio: electron beam, analysis: Vis-UV absorption.\n\nCH2OH + CH3 --> CH2O + CH4\n\npg.378 Table 2: Formation and decay rates of CH2OH, CH3, and OH observed by pulse radiolysis of\n\ngas mixtures of varying composition.  Chemical composition of systems A-E as in Table 1.\nThe authors note below Table 2 that the reported rate coefficient for CH3+CH2OH is an\n\n"adjustment of model to reproduce the observed decay rates of CH3 and CH2OH".\nMRH is skeptical of data, as this specific rxn is not directly referenced in the article,\n\nnor do the authors address whether other channels besides -->CH4+CH2O exist / are significant.\nThe value of A in the database is consistent with that reported in Table 2.\nMRH 1-Sept-2009\n\nConverted to training reaction from rate rule: C_methyl;O_Csrad',
    ),
    rank = 6,
    shortDesc = u"""Pagsberg et al [191].""",
)

entry(
    index = 58,
    label = "CH3O + C2H5-2 <=> C2H6 + CH2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.41e+12, 'cm^3/(mol*s)', '*|/', 5),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = '[90] Tsang, W.; Journal of Physical and Chemical Reference Data (1987), 16(3), 471-508.\nLiterature review: C2H5 + CH2OH --> C2H6 + CH2O\n\npg. 502: Discussion on evaluated data\n\nEntry 39,17 (b): C2H5 + CH2OH --> C2H6 + CH2O\n\nAuthor estimates the disproportionation rate coefficient as 4x10^-12 cm3/molecule/s.\n\nNo data at the time.\nMRH 30-Aug-2009\n\nConverted to training reaction from rate rule: C_rad/H2/Cs;O_Csrad',
    ),
    rank = 10,
    shortDesc = u"""Tsang [90] Literature review.""",
)

entry(
    index = 59,
    label = "CH3O + C3H5 <=> C3H6 + CH2O",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (3.62e+13, 'cm^3/(mol*s)', '*|/', 2.5),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = '[93] Tsang, W.; Journal of Physical and Chemical Reference Data (1991), 20(2), 221-273.\nLiterature review: C3H5 + CH2OH --> CH2O + C3H6\n\npg.267: Discussion on evaluated data\n\nEntry 47,39: No data available at the time.  Author notes that combination of these two\n\nreactants will form 3-butene-1-ol which should decompose under combustion conditions\nto form C3H6 + CH2O (same products).  The author therefore recommends a rate\ncoefficient of 3x10^-11 cm3/molecule/s.\nMRH 31-Aug-2009\n\nConverted to training reaction from rate rule: C_rad/H2/Cd;O_Csrad',
    ),
    rank = 10,
    shortDesc = u"""Tsang [93] Literature review.""",
)

entry(
    index = 60,
    label = "CH3O-2 + CH3O <=> CH4O + CH2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.82e+12, 'cm^3/(mol*s)', '*|/', 2),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = "[90] Tsang, W.; Journal of Physical and Chemical Reference Data (1987), 16(3), 471-508.\nLiterature review: CH2OH + CH2OH --> CH3OH + CH2O\n\npg. 506: Discussion on evaluated data\n\nEntry 39,39 (b): CH2OH + CH2OH --> CH3OH + CH2O\n\nMeier, et al. (1985) measured the rate of addition + disproportionation.  Tsang estimates\n\na disproportionation to combination ratio of 0.5\nNOTE: Rate coefficient given in table at beginning of reference (summarizing all data\n\npresented) gives k_a+b = 2.4x10^-11, leading to k_b = 8x10^-12.  NIST's online\ndatabase (kinetics.nist.gov) reports this number as well.  However, the discussion\non pg. 506 suggests k_a+b = 1.5x10^-11, leading to k_b = 5x10^-12.\nMRH 30-Aug-2009\n\n*** NEED TO INVESTIGATE ***\n\nConverted to training reaction from rate rule: C_rad/H2/O;O_Csrad",
    ),
    rank = 10,
    shortDesc = u"""Tsang [90] Literature review.""",
)

entry(
    index = 61,
    label = "CH3O + C3H7 <=> C3H8 + CH2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.35e+12, 'cm^3/(mol*s)', '*|/', 5),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = '[91] Tsang, W.; Journal of Physical and Chemical Reference Data (1988), 17(2), 887-951.\nLiterature review: CH2OH + i-C3H7 = C3H8 + CH2O\n\npg. 945: Discussion on evaluated data\n\nEntry 42,39 (b): No data available at the time.  Author suggests rate coefficient based\n\non rxn C2H5+i-C3H7=C3H8+C2H4, namely 3.9x10^-12 cm3/molecule/s\nMRH 30-Aug-2009\n\nConverted to training reaction from rate rule: C_rad/H/NonDeC;O_Csrad',
    ),
    rank = 10,
    shortDesc = u"""Tsang [91] Literature review.""",
)

entry(
    index = 62,
    label = "CH3O + C4H9 <=> C4H10 + CH2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.47e+14, 'cm^3/(mol*s)', '*|/', 3),
        n = -0.75,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = '[92] Tsang, W.; Journal of Physical and Chemical Reference Data (1990), 19(1), 1-68.\nLiterature review: t-C4H9 + CH2OH = CH2O + i-C4H10\n\npg. 44: Discussion on evaluated data\n\nEntry 44,39 (a): No data available at the time.  Author estimates the addition rxn rate\n\ncoefficient based on the rate for t-C4H9+C2H5-->adduct.  The author uses a\ndisproportionation-to-addition ratio of 0.52 to obtain the reported rate coefficient\nexpression.\n*** NOTE: Previous value in RMG was for k_c (the addition rxn).  I have changed it to match\n\nthe rate for the disproportionation rxn. ***\nMRH 30-Aug-2009\n\nConverted to training reaction from rate rule: C_rad/Cs3;O_Csrad',
    ),
    rank = 10,
    shortDesc = u"""Tsang [92] Literature review.""",
)

entry(
    index = 63,
    label = "CH3O + C2H3-2 <=> C2H4-2 + CH2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.01e+13, 'cm^3/(mol*s)', '*|/', 2.5),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = "[90] Tsang, W.; Journal of Physical and Chemical Reference Data (1987), 16(3), 471-508.\nLiterature review: CH2OH + C2H3 --> C2H4 + CH2O\n\npg. 503: Discussion on evaluated data\n\nEntry 39,19 (a): CH2OH + C2H3 --> C2H4 + CH2O\n\nAuthor suggests a disproportionation rate coefficient near the collision limit, due\n\nto rxn's exothermicity.  No data available at the time.\nMRH 30-Aug-2009\n\nConverted to training reaction from rate rule: Cd_pri_rad;O_Csrad",
    ),
    rank = 10,
    shortDesc = u"""Tsang [90] Literature review.""",
)

entry(
    index = 64,
    label = "CHO + CH3O <=> CH2O-3 + CH2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.81e+14, 'cm^3/(mol*s)', '*|/', 3),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = '[90] Tsang, W.; Journal of Physical and Chemical Reference Data (1987), 16(3), 471-508.\nLiterature review: HCO + CH2OH --> CH2O + CH2O\n\npg. 500: Discussion on evaluated data\n\nEntry 39,15 (b): CH2OH + HCO --> 2 CH2O\n\nAuthor estimates a disproportionation rate coefficient of 3x10^-11 cm3/molecule/s.\n\nNo data available at the time.\nMRH 30-Aug-2009\n\nConverted to training reaction from rate rule: CO_pri_rad;O_Csrad',
    ),
    rank = 10,
    shortDesc = u"""Tsang [90] Literature review.""",
)

entry(
    index = 65,
    label = "HO + CH3O <=> H2O + CH2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.41e+13, 'cm^3/(mol*s)', '*|/', 2),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = '[90] Tsang, W.; Journal of Physical and Chemical Reference Data (1987), 16(3), 471-508.\nLiterature review: OH + CH2OH --> H2O + CH2O\n\npg. 497: Discussion on evaluated data\n\nEntry 39,6: CH2OH + OH --> H2O + CH2O\n\nAuthor estimates a disproportionation rate coefficient of 4x10^-11 cm3/molecule/s.\n\nNo data available at the time.\nMRH 30-Aug-2009\n\nConverted to training reaction from rate rule: O_pri_rad;O_Csrad',
    ),
    rank = 10,
    shortDesc = u"""Tsang [90] Literature review.""",
)

entry(
    index = 66,
    label = "CH3O + CH3O-4 <=> CH4O-2 + CH2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.41e+13, 'cm^3/(mol*s)', '*|/', 2),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = '[90] Tsang, W.; Journal of Physical and Chemical Reference Data (1987), 16(3), 471-508.\nLiterature review: CH3O + CH2OH --> CH3OH + CH2O\n\npg. 505: Discussion on evaluated data\n\nEntry 39,24: CH2OH + CH3O --> CH3OH + CH2O\n\nAuthor estimates a disproportionation rate coefficient of 4x10^-11 cm3/molecule/s.\n\nNo data available at the time.\nMRH 30-Aug-2009\n\nDegeneracy not recalculated\n\nConverted to training reaction from rate rule: O_rad/NonDeC;O_Csrad',
    ),
    rank = 10,
    shortDesc = u"""Tsang [90] Literature review.""",
)

entry(
    index = 67,
    label = "HO2-2 + CH3O <=> H2O2 + CH2O",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.21e+13, 'cm^3/(mol*s)', '*|/', 2),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = '[90] Tsang, W.; Journal of Physical and Chemical Reference Data (1987), 16(3), 471-508.\nLiterature review: HO2 + CH2OH --> CH3OH + H2O2\n\npg. 498: Discussion on evaluated data\n\nEntry 39,7: CH2OH + HO2 --> H2O2 + CH2O\n\nAuthor recommends a disproportionation rate coefficient of 2x10^-11 cm3/molecules/s.\n\nNo data available at the time.\nMRH 30-Aug-2009\n\nConverted to training reaction from rate rule: O_rad/NonDeO;O_Csrad',
    ),
    rank = 10,
    shortDesc = u"""Tsang [90] Literature review.""",
)

entry(
    index = 68,
    label = "CH3S + CH3S-3 <=> CH4S + CH2S-2",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (2.937e+12, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (298, 'K'),
        comment = '\n\nConverted to training reaction from rate rule: S_rad/NonDeC;Cmethyl_Srad',
    ),
    rank = 10,
    shortDesc = u"""Tycholiz et al [A].""",
)

entry(
    index = 69,
    label = "C2H5S-2 + C3H7-2 <=> C2H6S + C3H6-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (6.74e-06, 'cm^3/(mol*s)'),
        n = 4.35,
        Ea = (4.76976, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (1500, 'K'),
        comment = '\n\nConverted to training reaction from rate rule: C_rad/H/CsS;C/H2/Nd_Csrad',
    ),
    rank = 6,
    shortDesc = u"""CAC calc CBS-QB3 1dhr""",
)

entry(
    index = 70,
    label = "C4H7-2 + O2 <=> HO2 + C4H6",
    degeneracy = 6.0,
    kinetics = Arrhenius(
        A = (4.338e+13, 'cm^3/(mol*s)', '*|/', 10),
        n = 0,
        Ea = (92.048, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2000, 'K'),
        comment = 'SSM estimate based on Miyoshi rate rule for secondary carbon in dx.doi.org/10.1021/jp112152n, \nmodified to account for allylic stability (+7 kcal)\n\nConverted to training reaction from rate rule: O2b;Cmethyl_Csrad/H/Cd',
    ),
    rank = 11,
    shortDesc = u"""S.S. Merchant estimate""",
)

entry(
    index = 71,
    label = "C4H7-3 + O2 <=> HO2 + C4H6-2",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (4e+10, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = '\n\nConverted to training reaction from rate rule: O2b;C/H2/De_Csrad',
    ),
    rank = 10,
    shortDesc = u"""Estimated value, AG Vandeputte""",
)

entry(
    index = 72,
    label = "C3H7-2 + O2 <=> HO2 + C3H6-2",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (4e+10, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = '\n\nConverted to training reaction from rate rule: O2b;C/H2/Nd_Rrad',
    ),
    rank = 10,
    shortDesc = u"""Estimated value, AG Vandeputte""",
)

entry(
    index = 73,
    label = "C4H7-3 + O2 <=> HO2 + C4H6-2",
    degeneracy = 4.0,
    kinetics = Arrhenius(
        A = (4e+10, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = '\n\nConverted to training reaction from rate rule: O2b;C/H2/De_Rrad',
    ),
    rank = 10,
    shortDesc = u"""Estimated value, AG Vandeputte""",
)

entry(
    index = 74,
    label = "C4H9-2 + O2 <=> HO2 + C4H8-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (2e+10, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = '\n\nConverted to training reaction from rate rule: O2b;C/H/NdNd_Rrad',
    ),
    rank = 10,
    shortDesc = u"""Estimated value, AG Vandeputte""",
)

entry(
    index = 75,
    label = "C5H9-2 + O2 <=> HO2 + C5H8-3",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (2e+10, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = '\n\nConverted to training reaction from rate rule: O2b;C/H/NdDe_Rrad',
    ),
    rank = 10,
    shortDesc = u"""Estimated value, AG Vandeputte""",
)

entry(
    index = 76,
    label = "C6H9 + O2 <=> HO2 + C6H8",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (2e+10, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = '\n\nConverted to training reaction from rate rule: O2b;C/H/DeDe_Rrad',
    ),
    rank = 10,
    shortDesc = u"""Estimated value, AG Vandeputte""",
)

entry(
    index = 77,
    label = "HO2-3 + H2N <=> H3N + O2-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (920000, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (-4.8116, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Added by Beat Buesser, value for reaction: NH2 + HO2 = NH3 + O2 (B&D #14d) in \'Gas-Phase Combustion Chemistry\' (ISBN: 978-1-4612-7088-1), chapter 2, \'Combustion Chemistry of Nitrogen\', Anthony M. Dean, Joseph W. Bozzelli",\n\nDegeneracy not recalculated\n\nConverted to training reaction from rate rule: NH2_rad;O_Orad',
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
)

entry(
    index = 78,
    label = "HN2 + O2 <=> HO2 + N2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (2.4e+12, 'cm^3/(mol*s)'),
        n = -0.34,
        Ea = (0.6276, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Added by Beat Buesser, value for reaction: NNH + O2 = N2 + HO2 (B&D #28b1) in \'Gas-Phase Combustion Chemistry\' (ISBN: 978-1-4612-7088-1), chapter 2, \'Combustion Chemistry of Nitrogen\', Anthony M. Dean, Joseph W. Bozzelli",\n\nConverted to training reaction from rate rule: O2b;N3d/H_d_Nrad',
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
)

entry(
    index = 79,
    label = "H + HN2 <=> H2 + N2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.4e+08, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (-3.72376, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Added by Beat Buesser, value for reaction: NNH + H = N2 + H2 (B&D #28c) in \'Gas-Phase Combustion Chemistry\' (ISBN: 978-1-4612-7088-1), chapter 2, \'Combustion Chemistry of Nitrogen\', Anthony M. Dean, Joseph W. Bozzelli",\n\nConverted to training reaction from rate rule: H_rad;N3d/H_d_Nrad',
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
)

entry(
    index = 80,
    label = "HO + HN2 <=> H2O + N2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.2e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-4.97896, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Added by Beat Buesser, value for reaction: NNH + OH = N2 + H2O (B&D #28d2) in \'Gas-Phase Combustion Chemistry\' (ISBN: 978-1-4612-7088-1), chapter 2, \'Combustion Chemistry of Nitrogen\', Anthony M. Dean, Joseph W. Bozzelli",\n\nConverted to training reaction from rate rule: O_pri_rad;N3d/H_d_Nrad',
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
)

entry(
    index = 81,
    label = "HN2 + O <=> HO-2 + N2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.7e+08, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (-3.72376, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Added by Beat Buesser, value for reaction: NNH + O = N2 + OH (B&D #28e2) in \'Gas-Phase Combustion Chemistry\' (ISBN: 978-1-4612-7088-1), chapter 2, \'Combustion Chemistry of Nitrogen\', Anthony M. Dean, Joseph W. Bozzelli",\n\nConverted to training reaction from rate rule: O_atom_triplet;N3d/H_d_Nrad',
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
)

entry(
    index = 82,
    label = "H2N + HN2 <=> H3N + N2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (920000, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (-4.8116, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Added by Beat Buesser, value for reaction: NNH + NH2 = N2 + NH3 (B&D #28f) in \'Gas-Phase Combustion Chemistry\' (ISBN: 978-1-4612-7088-1), chapter 2, \'Combustion Chemistry of Nitrogen\', Anthony M. Dean, Joseph W. Bozzelli",\n\nConverted to training reaction from rate rule: NH2_rad;N3d/H_d_Nrad',
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
)

entry(
    index = 83,
    label = "HO2-2 + HN2 <=> H2O2 + N2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (14000, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (-6.6944, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Added by Beat Buesser, value for reaction: NNH + HO2 = N2 + H2O2 (B&D #28g1) in \'Gas-Phase Combustion Chemistry\' (ISBN: 978-1-4612-7088-1), chapter 2, \'Combustion Chemistry of Nitrogen\', Anthony M. Dean, Joseph W. Bozzelli",\n\nConverted to training reaction from rate rule: O_rad/NonDeO;N3d/H_d_Nrad',
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
)

entry(
    index = 84,
    label = "HN2 + NO <=> HNO + N2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.2e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-4.97896, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Added by Beat Buesser, value for reaction: NNH + NO = N2 + HNO (B&D #28h) in \'Gas-Phase Combustion Chemistry\' (ISBN: 978-1-4612-7088-1), chapter 2, \'Combustion Chemistry of Nitrogen\', Anthony M. Dean, Joseph W. Bozzelli",\n\nConverted to training reaction from rate rule: N3d_rad/O;N3d/H_d_Nrad',
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
)

entry(
    index = 85,
    label = "H + H2N2 <=> H2 + HN2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (9.6e+08, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (-3.72376, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Added by Beat Buesser, value for reaction: H2NN + H = NNH + H2 (B&D #30c2) in \'Gas-Phase Combustion Chemistry\' (ISBN: 978-1-4612-7088-1), chapter 2, \'Combustion Chemistry of Nitrogen\', Anthony M. Dean, Joseph W. Bozzelli",\n\nConverted to training reaction from rate rule: H_rad;N3s/H2_s_Nbirad',
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
)

entry(
    index = 86,
    label = "H2N2 + O <=> HO-2 + HN2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (6.6e+08, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (-3.72376, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Added by Beat Buesser, value for reaction: H2NN + O = NNH + OH (B&D #30d2) in \'Gas-Phase Combustion Chemistry\' (ISBN: 978-1-4612-7088-1), chapter 2, \'Combustion Chemistry of Nitrogen\', Anthony M. Dean, Joseph W. Bozzelli",\n\nConverted to training reaction from rate rule: O_atom_triplet;N3s/H2_s_Nbirad',
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
)

entry(
    index = 87,
    label = "HO + H2N2 <=> H2O + HN2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (4.8e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-4.97896, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Added by Beat Buesser, value for reaction: H2NN + OH = NNH + H2O (B&D #30e2) in \'Gas-Phase Combustion Chemistry\' (ISBN: 978-1-4612-7088-1), chapter 2, \'Combustion Chemistry of Nitrogen\', Anthony M. Dean, Joseph W. Bozzelli",\n\nConverted to training reaction from rate rule: O_pri_rad;N3s/H2_s_Nbirad',
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
)

entry(
    index = 88,
    label = "CH3 + H2N2 <=> CH4 + HN2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (3.2e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (0.54392, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Added by Beat Buesser, value for reaction: H2NN + CH3 = NNH + CH4 (B&D #30f3) in \'Gas-Phase Combustion Chemistry\' (ISBN: 978-1-4612-7088-1), chapter 2, \'Combustion Chemistry of Nitrogen\', Anthony M. Dean, Joseph W. Bozzelli",\n\nConverted to training reaction from rate rule: C_methyl;N3s/H2_s_Nbirad',
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
)

entry(
    index = 89,
    label = "H2N + H2N2 <=> H3N + HN2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (3.6e+06, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (-4.8116, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Added by Beat Buesser, value for reaction: H2NN + NH2 = NNH + NH3 (B&D #30g2) in \'Gas-Phase Combustion Chemistry\' (ISBN: 978-1-4612-7088-1), chapter 2, \'Combustion Chemistry of Nitrogen\', Anthony M. Dean, Joseph W. Bozzelli",\n\nConverted to training reaction from rate rule: NH2_rad;N3s/H2_s_Nbirad',
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
)

entry(
    index = 90,
    label = "HO2-2 + H2N2 <=> H2O2 + HN2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (58000, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (-6.6944, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Added by Beat Buesser, value for reaction: H2NN + HO2 = NNH + H2O2 (B&D #30h2) in \'Gas-Phase Combustion Chemistry\' (ISBN: 978-1-4612-7088-1), chapter 2, \'Combustion Chemistry of Nitrogen\', Anthony M. Dean, Joseph W. Bozzelli",\n\nConverted to training reaction from rate rule: O_rad/NonDeO;N3s/H2_s_Nbirad',
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
)

entry(
    index = 91,
    label = "H + H3N2 <=> H2 + H2N2-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (4.8e+08, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Added by Beat Buesser, value for reaction: N2H3 + H = N2H2 + H2 (B&D #31b) in \'Gas-Phase Combustion Chemistry\' (ISBN: 978-1-4612-7088-1), chapter 2, \'Combustion Chemistry of Nitrogen\', Anthony M. Dean, Joseph W. Bozzelli",\n\nConverted to training reaction from rate rule: H_rad;N3s/H2_s_Nrad',
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
)

entry(
    index = 92,
    label = "H3N2 + O <=> HO-2 + H2N2-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (3.4e+08, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (-2.7196, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Added by Beat Buesser, value for reaction: N2H3 + O = N2H2 + OH (B&D #31c3) in \'Gas-Phase Combustion Chemistry\' (ISBN: 978-1-4612-7088-1), chapter 2, \'Combustion Chemistry of Nitrogen\', Anthony M. Dean, Joseph W. Bozzelli",\n\nConverted to training reaction from rate rule: O_atom_triplet;N3s/H2_s_Nrad',
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
)

entry(
    index = 93,
    label = "HO + H3N2 <=> H2O + H2N2-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (2.4e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-4.97896, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Added by Beat Buesser, value for reaction: N2H3 + OH = N2H2 + H2O (B&D #31d1) in \'Gas-Phase Combustion Chemistry\' (ISBN: 978-1-4612-7088-1), chapter 2, \'Combustion Chemistry of Nitrogen\', Anthony M. Dean, Joseph W. Bozzelli",\n\nConverted to training reaction from rate rule: O_pri_rad;N3s/H2_s_Nrad',
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
)

entry(
    index = 94,
    label = "H3N2 + CH3 <=> CH4 + H2N2-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.64e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (7.61488, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Added by Beat Buesser, value for reaction: N2H3 + CH3 = N2H2 + CH4 (B&D #31e1) in \'Gas-Phase Combustion Chemistry\' (ISBN: 978-1-4612-7088-1), chapter 2, \'Combustion Chemistry of Nitrogen\', Anthony M. Dean, Joseph W. Bozzelli",\n\nConverted to training reaction from rate rule: C_methyl;N3s/H2_s_Nrad',
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
)

entry(
    index = 95,
    label = "H2N + H3N2 <=> H3N + H2N2-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.84e+06, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (-4.8116, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Added by Beat Buesser, value for reaction: N2H3 + NH2 = N2H2 + NH3 (B&D #31f1) in \'Gas-Phase Combustion Chemistry\' (ISBN: 978-1-4612-7088-1), chapter 2, \'Combustion Chemistry of Nitrogen\', Anthony M. Dean, Joseph W. Bozzelli",\n\nConverted to training reaction from rate rule: NH2_rad;N3s/H2_s_Nrad',
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
)

entry(
    index = 96,
    label = "HO2-2 + H3N2 <=> H2O2 + H2N2-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (58000, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (-6.6944, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Added by Beat Buesser, value for reaction: N2H3 + HO2 = N2H2 + H2O2 (B&D #31g2) in \'Gas-Phase Combustion Chemistry\' (ISBN: 978-1-4612-7088-1), chapter 2, \'Combustion Chemistry of Nitrogen\', Anthony M. Dean, Joseph W. Bozzelli",\n\nConverted to training reaction from rate rule: O_rad/NonDeO;N3s/H2_s_Nrad',
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
)

entry(
    index = 97,
    label = "HO2-3 + H3N2-2 <=> H4N2 + O2-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (920000, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (8.91192, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Added by Beat Buesser, value for reaction: N2H3 + HO2 = N2H4 + O2 (B&D #31g3) in \'Gas-Phase Combustion Chemistry\' (ISBN: 978-1-4612-7088-1), chapter 2, \'Combustion Chemistry of Nitrogen\', Anthony M. Dean, Joseph W. Bozzelli",\n\nDegeneracy not recalculated\n\nConverted to training reaction from rate rule: N3s_rad/H/NonDeN;O_Orad',
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
)

entry(
    index = 98,
    label = "H + H2NO <=> H2 + HNO-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (9.6e+08, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (6.52704, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Added by Beat Buesser, value for reaction: NH2O + H = HNO + H2 (B&D #37c2) in \'Gas-Phase Combustion Chemistry\' (ISBN: 978-1-4612-7088-1), chapter 2, \'Combustion Chemistry of Nitrogen\', Anthony M. Dean, Joseph W. Bozzelli",\n\nConverted to training reaction from rate rule: H_rad;N3s/H2_s_Orad',
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
)

entry(
    index = 99,
    label = "H2NO + O <=> HO-2 + HNO-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (6.6e+08, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (2.05016, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Added by Beat Buesser, value for reaction: NH2O + O = HNO + OH (B&D #37d) in \'Gas-Phase Combustion Chemistry\' (ISBN: 978-1-4612-7088-1), chapter 2, \'Combustion Chemistry of Nitrogen\', Anthony M. Dean, Joseph W. Bozzelli",\n\nConverted to training reaction from rate rule: O_atom_triplet;N3s/H2_s_Orad',
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
)

entry(
    index = 100,
    label = "HO + H2NO <=> H2O + HNO-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (4.8e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-4.97896, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Added by Beat Buesser, value for reaction: NH2O + OH = HNO + H2O (B&D #37e) in \'Gas-Phase Combustion Chemistry\' (ISBN: 978-1-4612-7088-1), chapter 2, \'Combustion Chemistry of Nitrogen\', Anthony M. Dean, Joseph W. Bozzelli",\n\nConverted to training reaction from rate rule: O_pri_rad;N3s/H2_s_Orad',
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
)

entry(
    index = 101,
    label = "CH3 + H2NO <=> CH4 + HNO-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (3.2e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (12.3846, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Added by Beat Buesser, value for reaction: NH2O + CH3 = CH4 + HNO (B&D #37f2) in \'Gas-Phase Combustion Chemistry\' (ISBN: 978-1-4612-7088-1), chapter 2, \'Combustion Chemistry of Nitrogen\', Anthony M. Dean, Joseph W. Bozzelli",\n\nConverted to training reaction from rate rule: C_methyl;N3s/H2_s_Orad',
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
)

entry(
    index = 102,
    label = "H2N + H2NO <=> H3N + HNO-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (3.6e+06, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (-4.8116, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Added by Beat Buesser, value for reaction: NH2O + NH2 = HNO + NH3 (B&D #37g) in \'Gas-Phase Combustion Chemistry\' (ISBN: 978-1-4612-7088-1), chapter 2, \'Combustion Chemistry of Nitrogen\', Anthony M. Dean, Joseph W. Bozzelli",\n\nConverted to training reaction from rate rule: NH2_rad;N3s/H2_s_Orad',
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
)

entry(
    index = 103,
    label = "HO2-2 + H2NO <=> H2O2 + HNO-2",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (58000, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (-6.6944, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Added by Beat Buesser, value for reaction: NH2O + HO2 = HNO + H2O2 (B&D #37h1) in \'Gas-Phase Combustion Chemistry\' (ISBN: 978-1-4612-7088-1), chapter 2, \'Combustion Chemistry of Nitrogen\', Anthony M. Dean, Joseph W. Bozzelli",\n\nConverted to training reaction from rate rule: O_rad/NonDeO;N3s/H2_s_Orad',
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
)

entry(
    index = 104,
    label = "HO2-3 + H2NO-2 <=> H3NO + O2-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (29000, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (-6.6944, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Added by Beat Buesser, value for reaction: NH2O + HO2 = NH2OH + O2 (B&D #37h2) in \'Gas-Phase Combustion Chemistry\' (ISBN: 978-1-4612-7088-1), chapter 2, \'Combustion Chemistry of Nitrogen\', Anthony M. Dean, Joseph W. Bozzelli",\n\nDegeneracy not recalculated\n\nConverted to training reaction from rate rule: O_rad/NonDeN;O_Orad',
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
)

entry(
    index = 105,
    label = "H + H2NO-3 <=> H2 + HNO-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (4.8e+08, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (1.58992, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Added by Beat Buesser, value for reaction: HNOH + H = HNO + H2 (B&D #38b2) in \'Gas-Phase Combustion Chemistry\' (ISBN: 978-1-4612-7088-1), chapter 2, \'Combustion Chemistry of Nitrogen\', Anthony M. Dean, Joseph W. Bozzelli",\n\nConverted to training reaction from rate rule: H_rad;O_Nrad',
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
)

entry(
    index = 106,
    label = "H2NO-3 + O <=> HO-2 + HNO-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (3.3e+08, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (-1.50624, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Added by Beat Buesser, value for reaction: HNOH + O = HNO + OH (B&D #38c2) in \'Gas-Phase Combustion Chemistry\' (ISBN: 978-1-4612-7088-1), chapter 2, \'Combustion Chemistry of Nitrogen\', Anthony M. Dean, Joseph W. Bozzelli",\n\nConverted to training reaction from rate rule: O_atom_triplet;O_Nrad',
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
)

entry(
    index = 107,
    label = "HO + H2NO-3 <=> H2O + HNO-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.4e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-4.97896, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Added by Beat Buesser, value for reaction: HNOH + OH = HNO + H2O (B&D #38d) in \'Gas-Phase Combustion Chemistry\' (ISBN: 978-1-4612-7088-1), chapter 2, \'Combustion Chemistry of Nitrogen\', Anthony M. Dean, Joseph W. Bozzelli",\n\nConverted to training reaction from rate rule: O_pri_rad;O_Nrad',
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
)

entry(
    index = 108,
    label = "H2NO-3 + CH3 <=> CH4 + HNO-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.6e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (8.7864, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Added by Beat Buesser, value for reaction: HNOH + CH3 = CH4 + HNO (B&D #38e2) in \'Gas-Phase Combustion Chemistry\' (ISBN: 978-1-4612-7088-1), chapter 2, \'Combustion Chemistry of Nitrogen\', Anthony M. Dean, Joseph W. Bozzelli",\n\nConverted to training reaction from rate rule: C_methyl;O_Nrad',
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
)

entry(
    index = 109,
    label = "H2N + H2NO-3 <=> H3N + HNO-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.8e+06, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (-4.8116, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Added by Beat Buesser, value for reaction: HNOH + NH2 = HNO + NH3 (B&D #38f3)  in \'Gas-Phase Combustion Chemistry\' (ISBN: 978-1-4612-7088-1), chapter 2, \'Combustion Chemistry of Nitrogen\', Anthony M. Dean, Joseph W. Bozzelli",\n\nConverted to training reaction from rate rule: NH2_rad;O_Nrad',
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
)

entry(
    index = 110,
    label = "HO2-2 + H2NO-3 <=> H2O2 + HNO-3",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (29400, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (-6.6944, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Added by Beat Buesser, value for reaction: HNOH + HO2 = HNO + H2O2 (B&D #38g2) in \'Gas-Phase Combustion Chemistry\' (ISBN: 978-1-4612-7088-1), chapter 2, \'Combustion Chemistry of Nitrogen\', Anthony M. Dean, Joseph W. Bozzelli",\n\nConverted to training reaction from rate rule: O_rad/NonDeO;O_Nrad',
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
)

entry(
    index = 111,
    label = "HO2-3 + H2NO-4 <=> H3NO-2 + O2-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (29000, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (-6.6944, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Added by Beat Buesser, value for reaction: HNOH + HO2 = NH2OH + O2 (B&D #38g3) in \'Gas-Phase Combustion Chemistry\' (ISBN: 978-1-4612-7088-1), chapter 2, \'Combustion Chemistry of Nitrogen\', Anthony M. Dean, Joseph W. Bozzelli",\n\nDegeneracy not recalculated\n\nConverted to training reaction from rate rule: N3s_rad/H/NonDeO;O_Orad',
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
)

entry(
    index = 112,
    label = "HO2-2 + CH2N <=> H2O2 + CHN",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (28000, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (-6.73624, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Added by Beat Buesser, value for reaction: H2CN + HO2 = HCN + H2O2 (B&D #45b1) in \'Gas-Phase Combustion Chemistry\' (ISBN: 978-1-4612-7088-1), chapter 2, \'Combustion Chemistry of Nitrogen\', Anthony M. Dean, Joseph W. Bozzelli",\n\nConverted to training reaction from rate rule: O_rad/NonDeO;Cds/H2_d_N3rad',
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
)

entry(
    index = 113,
    label = "HO2-3 + CH2N-2 <=> CH3N + O2-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (14000, 'cm^3/(mol*s)'),
        n = 2.69,
        Ea = (-6.73624, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Added by Beat Buesser, value for reaction: H2CN + HO2 = H2CNH + O2 (B&D #45b2) in \'Gas-Phase Combustion Chemistry\' (ISBN: 978-1-4612-7088-1), chapter 2, \'Combustion Chemistry of Nitrogen\', Anthony M. Dean, Joseph W. Bozzelli",\n\nDegeneracy not recalculated\n\nConverted to training reaction from rate rule: N3d_rad/C;O_Orad',
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
)

entry(
    index = 114,
    label = "CH2N + CH3 <=> CH4 + CHN",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.62e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-4.64424, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Added by Beat Buesser, value for reaction: H2CN + CH3 = HCN + CH4 (B&D #45d) in \'Gas-Phase Combustion Chemistry\' (ISBN: 978-1-4612-7088-1), chapter 2, \'Combustion Chemistry of Nitrogen\', Anthony M. Dean, Joseph W. Bozzelli",\n\nConverted to training reaction from rate rule: C_methyl;Cds/H2_d_N3rad',
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
)

entry(
    index = 115,
    label = "HO + CH2N <=> H2O + CHN",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (2.4e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-4.97896, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Added by Beat Buesser, value for reaction: H2CN + OH = HCN + H2O (B&D #45e2) in \'Gas-Phase Combustion Chemistry\' (ISBN: 978-1-4612-7088-1), chapter 2, \'Combustion Chemistry of Nitrogen\', Anthony M. Dean, Joseph W. Bozzelli",\n\nConverted to training reaction from rate rule: O_pri_rad;Cds/H2_d_N3rad',
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
)

entry(
    index = 116,
    label = "H + CH2N <=> H2 + CHN",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (4.8e+08, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (-3.72376, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Added by Beat Buesser, value for reaction: H2CN + H = HCN + H2 (B&D #45g) in \'Gas-Phase Combustion Chemistry\' (ISBN: 978-1-4612-7088-1), chapter 2, \'Combustion Chemistry of Nitrogen\', Anthony M. Dean, Joseph W. Bozzelli",\n\nConverted to training reaction from rate rule: H_rad;Cds/H2_d_N3rad',
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
)

entry(
    index = 117,
    label = "H2N + CH2N <=> H3N + CHN",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (1.84e+06, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (-4.8116, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Added by Beat Buesser, value for reaction: H2CN + NH2 = HCN + NH3 (B&D #45h) in \'Gas-Phase Combustion Chemistry\' (ISBN: 978-1-4612-7088-1), chapter 2, \'Combustion Chemistry of Nitrogen\', Anthony M. Dean, Joseph W. Bozzelli",\n\nConverted to training reaction from rate rule: NH2_rad;Cds/H2_d_N3rad',
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
)

entry(
    index = 118,
    label = "CH2N + O <=> HO-2 + CHN",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (3.4e+08, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (-3.72376, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Added by Beat Buesser, value for reaction: H2CN + O = HCN + OH (B&D #45i1) in \'Gas-Phase Combustion Chemistry\' (ISBN: 978-1-4612-7088-1), chapter 2, \'Combustion Chemistry of Nitrogen\', Anthony M. Dean, Joseph W. Bozzelli",\n\nConverted to training reaction from rate rule: O_atom_triplet;Cds/H2_d_N3rad',
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
)

entry(
    index = 119,
    label = "H + CH2N-3 <=> H2 + CHN-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (2.4e+08, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (-3.72376, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Added by Beat Buesser, value for reaction: HCNH + H = HCN + H2 (B&D #46a2) in \'Gas-Phase Combustion Chemistry\' (ISBN: 978-1-4612-7088-1), chapter 2, \'Combustion Chemistry of Nitrogen\', Anthony M. Dean, Joseph W. Bozzelli",\n\nConverted to training reaction from rate rule: H_rad;N3d/H_d_Crad',
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
)

entry(
    index = 120,
    label = "CH2N-3 + O <=> HO-2 + CHN-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.7e+08, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (-3.72376, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Added by Beat Buesser, value for reaction: HCNH + O = HCN + OH (B&D #46b2) in \'Gas-Phase Combustion Chemistry\' (ISBN: 978-1-4612-7088-1), chapter 2, \'Combustion Chemistry of Nitrogen\', Anthony M. Dean, Joseph W. Bozzelli",\n\nConverted to training reaction from rate rule: O_atom_triplet;N3d/H_d_Crad',
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
)

entry(
    index = 121,
    label = "HO + CH2N-3 <=> H2O + CHN-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (1.2e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-4.97896, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Added by Beat Buesser, value for reaction: HCNH + OH = HCN + H2O (B&D #46c) in \'Gas-Phase Combustion Chemistry\' (ISBN: 978-1-4612-7088-1), chapter 2, \'Combustion Chemistry of Nitrogen\', Anthony M. Dean, Joseph W. Bozzelli",\n\nConverted to training reaction from rate rule: O_pri_rad;N3d/H_d_Crad',
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
)

entry(
    index = 122,
    label = "CH2N-3 + CH3 <=> CH4 + CHN-2",
    degeneracy = 1.0,
    kinetics = Arrhenius(
        A = (820000, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-4.64424, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Added by Beat Buesser, value for reaction: HCNH + CH3 = HCN + CH4 (B&D #46d) in \'Gas-Phase Combustion Chemistry\' (ISBN: 978-1-4612-7088-1), chapter 2, \'Combustion Chemistry of Nitrogen\', Anthony M. Dean, Joseph W. Bozzelli",\n\nConverted to training reaction from rate rule: C_methyl;N3d/H_d_Crad',
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
)

entry(
    index = 123,
    label = "H + CH4N <=> H2 + CH3N-2",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (2.16e+09, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (-3.72376, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Added by Beat Buesser, value for reaction: CH3NH + H = H2CNH + H2 (B&D #49b) in \'Gas-Phase Combustion Chemistry\' (ISBN: 978-1-4612-7088-1), chapter 2, \'Combustion Chemistry of Nitrogen\', Anthony M. Dean, Joseph W. Bozzelli",\n\nConverted to training reaction from rate rule: H_rad;Cmethyl_Nrad',
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
)

entry(
    index = 124,
    label = "CH4N + O <=> HO-2 + CH3N-2",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (1.5e+09, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (-3.72376, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Added by Beat Buesser, value for reaction: CH3NH + O = H2CNH + OH (B&D #49c) in \'Gas-Phase Combustion Chemistry\' (ISBN: 978-1-4612-7088-1), chapter 2, \'Combustion Chemistry of Nitrogen\', Anthony M. Dean, Joseph W. Bozzelli",\n\nConverted to training reaction from rate rule: O_atom_triplet;Cmethyl_Nrad',
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
)

entry(
    index = 125,
    label = "HO + CH4N <=> H2O + CH3N-2",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (1.08e+07, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-4.97896, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Added by Beat Buesser, value for reaction: CH3NH + OH = H2CNH + H2O (B&D #49d) in \'Gas-Phase Combustion Chemistry\' (ISBN: 978-1-4612-7088-1), chapter 2, \'Combustion Chemistry of Nitrogen\', Anthony M. Dean, Joseph W. Bozzelli",\n\nConverted to training reaction from rate rule: O_pri_rad;Cmethyl_Nrad',
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
)

entry(
    index = 126,
    label = "CH4N + CH3 <=> CH4 + CH3N-2",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (7.2e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-4.64424, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Added by Beat Buesser, value for reaction: CH3NH + CH3 = H2CNH + CH4 (B&D #49e) in \'Gas-Phase Combustion Chemistry\' (ISBN: 978-1-4612-7088-1), chapter 2, \'Combustion Chemistry of Nitrogen\', Anthony M. Dean, Joseph W. Bozzelli",\n\nConverted to training reaction from rate rule: C_methyl;Cmethyl_Nrad',
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
)

entry(
    index = 127,
    label = "H + CH4N-2 <=> H2 + CH3N-3",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (8e+08, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (-3.72376, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Added by Beat Buesser, value for reaction: CH2NH2 + H = H2CNH + H2 (B&D #50b) in \'Gas-Phase Combustion Chemistry\' (ISBN: 978-1-4612-7088-1), chapter 2, \'Combustion Chemistry of Nitrogen\', Anthony M. Dean, Joseph W. Bozzelli",\n\nConverted to training reaction from rate rule: H_rad;N3s/H2_s_Cssrad',
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
)

entry(
    index = 128,
    label = "CH4N-2 + O <=> HO-2 + CH3N-3",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (6.6e+08, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (-3.72376, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Added by Beat Buesser, value for reaction: CH2NH2 + O = H2CNH + OH (B&D #50c2) in \'Gas-Phase Combustion Chemistry\' (ISBN: 978-1-4612-7088-1), chapter 2, \'Combustion Chemistry of Nitrogen\', Anthony M. Dean, Joseph W. Bozzelli",\n\nConverted to training reaction from rate rule: O_atom_triplet;N3s/H2_s_Cssrad',
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
)

entry(
    index = 129,
    label = "HO + CH4N-2 <=> H2O + CH3N-3",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (4.8e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-4.97896, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Added by Beat Buesser, value for reaction: CH2NH2 + OH = H2CNH + H2O (B&D #50d2) in \'Gas-Phase Combustion Chemistry\' (ISBN: 978-1-4612-7088-1), chapter 2, \'Combustion Chemistry of Nitrogen\', Anthony M. Dean, Joseph W. Bozzelli",\n\nConverted to training reaction from rate rule: O_pri_rad;N3s/H2_s_Cssrad',
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
)

entry(
    index = 130,
    label = "CH3 + CH4N-2 <=> CH4 + CH3N-3",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (3.2e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-2.63592, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Added by Beat Buesser, value for reaction: CH2NH2 + CH3 = H2CNH + CH4 (B&D #50e2) in \'Gas-Phase Combustion Chemistry\' (ISBN: 978-1-4612-7088-1), chapter 2, \'Combustion Chemistry of Nitrogen\', Anthony M. Dean, Joseph W. Bozzelli",\n\nConverted to training reaction from rate rule: C_methyl;N3s/H2_s_Cssrad',
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
)

entry(
    index = 131,
    label = "H + CH2NO <=> H2 + CHNO",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (9.6e+08, 'cm^3/(mol*s)'),
        n = 1.5,
        Ea = (-3.72376, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Added by Beat Buesser, value for reaction: CH2NO + H = HCNO + H2\nThe reacting structures are CH2=[N.+][O-] + R = [CH]#[N+][O-] + RH\n(D&B #57c2) in \'Gas-Phase Combustion Chemistry\' (ISBN: 978-1-4612-7088-1), chapter 2, \'Combustion Chemistry of Nitrogen\', Anthony M. Dean, Joseph W. Bozzelli",\n\nConverted to training reaction from rate rule: H_rad;Cds/H2_d_N5dcrad/O',
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
)

entry(
    index = 132,
    label = "HO + CH2NO <=> H2O + CHNO",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (4.8e+06, 'cm^3/(mol*s)'),
        n = 2,
        Ea = (-4.97896, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Added by Beat Buesser, value for reaction: CH2NO + OH = HCNO + H2O\n(D&B #57e2) in \'Gas-Phase Combustion Chemistry\' (ISBN: 978-1-4612-7088-1), chapter 2, \'Combustion Chemistry of Nitrogen\', Anthony M. Dean, Joseph W. Bozzelli",\n\nConverted to training reaction from rate rule: O_pri_rad;Cds/H2_d_N5dcrad/O',
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
)

entry(
    index = 133,
    label = "CH3 + CH2NO <=> CH4 + CHNO",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (3.2e+06, 'cm^3/(mol*s)'),
        n = 1.87,
        Ea = (-4.64424, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Added by Beat Buesser, value for reaction: CH2NO + CH3 = HCNO + CH4\n(D&B #57f2) in \'Gas-Phase Combustion Chemistry\' (ISBN: 978-1-4612-7088-1), chapter 2, \'Combustion Chemistry of Nitrogen\', Anthony M. Dean, Joseph W. Bozzelli",\n\nConverted to training reaction from rate rule: C_methyl;Cds/H2_d_N5dcrad/O',
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
)

entry(
    index = 134,
    label = "H2N + CH2NO <=> H3N + CHNO",
    degeneracy = 2.0,
    kinetics = Arrhenius(
        A = (3.6e+06, 'cm^3/(mol*s)'),
        n = 1.94,
        Ea = (-4.8116, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Added by Beat Buesser, value for reaction: CH2NO + NH2 = HCNO + NH3\n(D&B #57g2) in \'Gas-Phase Combustion Chemistry\' (ISBN: 978-1-4612-7088-1), chapter 2, \'Combustion Chemistry of Nitrogen\', Anthony M. Dean, Joseph W. Bozzelli",\n\nConverted to training reaction from rate rule: NH2_rad;Cds/H2_d_N5dcrad/O',
    ),
    rank = 2,
    shortDesc = u"""Added by Beat Buesser""",
)

entry(
    index = 135,
    label = "C5H7 + C4H7-2 <=> C5H8 + C4H6",
    degeneracy = 3.0,
    kinetics = Arrhenius(
        A = (1.5e+11, 'cm^3/(mol*s)'),
        n = 0,
        Ea = (0, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (300, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Estimating rate coefficient for cyclopentadienyl radical + butadieneyl radical\nNIST estimate for allyl + iso-butyl is 8E+11 at 1000 K, however in our system the butadieneyl radical is also resonance stabilized\nand it will be harder to break the bond to give butadiene + cyclopentadiene. Currently estimate it to be a factor of 5 slower.\n\nConverted to training reaction from rate rule: C_rad/H/TwoDe;Cmethyl_Csrad/H/Cd',
    ),
    rank = 11,
    shortDesc = u"""Estimated by S.S. Merchant""",
)

