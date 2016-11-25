# -*- coding: utf-8 -*-
from sys import argv

peptide = "ADADAHHA"
one_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
               "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "*"]
three_letters = ["Ala", "Asx", "Cys", "Asp", "Glu", "Phe", "Gly", "His", "Ile", "Lys", "Leu", "Met",
                 "Asn", "Pro", "Gln", "Arg", "Ser", "Thr", "Val", "Trp", "Xaa", "Tyr", "Glx", "*"]
one2three_dict = dict(zip(one_letters, three_letters))
three_letter_peptide = ""
for aa in peptide:
    three_letter_peptide += one2three_dict[aa]
print three_letter_peptide
