# -*- coding:utf-8 -*-
from sys import argv

try:
    seq = argv[1].upper()
except IndexError:
    print "please give a sequence"
    exit()
dna_characters = list("ATGC")
result = ""

for character in seq:
    if character in dna_characters:
        result += character

print result