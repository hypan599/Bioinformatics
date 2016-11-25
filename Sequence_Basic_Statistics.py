# -*- coding:utf-8 -*-
from collections import defaultdict
from sys import argv

try:
    seq = argv[1].upper()
except IndexError:
    print "please give a sequence"
    exit()
result = defaultdict(int)

for base in seq:
    result[base] += 1
for k, v in result.items():
    print "{0}:{1}".format(k, v)
