# -*- coding:utf-8 -*-
from sys import argv

try:
    seq = argv[1].upper()
except IndexError:
    print "please give a sequence"
    exit()
protein_characters = list("ACDEFGHIKLMNPQRSTVWY")
result = ""

for character in seq:
    if character in protein_characters:
        result += character

print result