# -*- coding: utf-8 -*-
from sys import argv

peptide = "AlaAlaAlaAlaAlaAlaAlaAsp"
one_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
               "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "*"]
three_letters = ["Ala", "Asx", "Cys", "Asp", "Glu", "Phe", "Gly", "His", "Ile", "Lys", "Leu", "Met",
                 "Asn", "Pro", "Gln", "Arg", "Ser", "Thr", "Val", "Trp", "Xaa", "Tyr", "Glx", "*"]
three2one_dict = dict(zip(three_letters, one_letters))
i = 0
one_letter_peptide = ""
while i < len(peptide):
    one_letter_peptide += three2one_dict[peptide[i:i+3]]
    i += 3
print one_letter_peptide
