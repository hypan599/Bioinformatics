# -*- coding : utf-8 -*-
"""
calculate dna molecular weight
"""

from collections import defaultdict

A_weight = 312
T_weight = 303
G_weight = 328
C_weight = 288
phosphory_group = 61


def calculate_mw(dna):
    bases = defaultdict(int)
    for i in dna:
        bases[i] += 1
    weight = bases["A"] * A_weight \
             + bases["G"] * G_weight \
             + bases["T"] * T_weight \
             + bases["C"] * C_weight
    weight -= phosphory_group
    print "weight = ", weight

calculate_mw("AAAATTTTCCCCGGGG")