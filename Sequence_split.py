# -*- coding:utf-8 -*-
from sys import argv
try:
    script, input_file_name, length, overlap, result_file_name = argv
except IndexError:
    print """how to use:
    python Sequence_split.py in.fasta length overlap out.fasta
    please give enough parameter to run this program"""
    exit()


def read_fasta(file_item):
    lines = file_item.readlines()
    file_item.close()
    raw_result = ""
    for j in lines:
        if j[0] == ">":
            continue
        line = j.strip("\n")
        raw_result += line
    return raw_result


def split(dna, length, overlap, result_file):
    start = 1
    end = length
    result = ""
    while start < len(dna):
        if end > len(dna):
            end = len(dna)
        result += ">sequence:*** start:{0} end:{1}\n".format(start, end)
        result += dna[start-1:end-1]
        result += "\n"
        start += length - overlap
        end += length - overlap
    f = open(result_file, "w")
    f.truncate()
    f.write(result)
    f.close()

split(read_fasta(open(input_file_name)), int(length), int(overlap), result_file_name)
