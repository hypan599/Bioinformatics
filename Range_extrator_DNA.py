# -*- coding: utf-8 -*-
from sys import argv

seq = "ATAGACATAGAC"
seq_range = "1, center ,5..7"


def range_extract(seq, seq_range):
    length = len(seq)
    seq_range = seq_range.replace("start", "1")
    seq_range = seq_range.replace("center", str(length / 2))
    seq_range = seq_range.replace("end", str(length))
    seq_range = seq_range.split(",")
    print length, seq_range
    print
    result = ""
    for piece in seq_range:
        try:
            num = int(piece)
            num = [num]
        except ValueError:
            num = range(int(piece.split(".")[0]), int(piece.split(".")[-1]) + 1)
        print num
        for i in num:
            result += seq[i-1]
    print result


range_extract(seq, seq_range)
