# -*- coding:utf-8 -*-
from sys import argv  # todo: argv

file_names = []
i = 1
if len(argv) < 3:
    argv.pop(-1)
    while argv:
        file_names.append(argv[i])
        i += 1
else:
    print "please give at least 2 fasta file"
    exit()


def export_seq(head="> ", seq="", filename="result.fasta"):  # todo: check how they did this on the internet
    line_len = 80
    result = ""
    for i in range(len(seq)):
        if i % line_len == 0 and i:
            result += "\n"
        result += seq[i]
    result = "{0}\n{1}".format(head, result)
    f = open(filename, 'w')
    f.truncate()
    f.write(result)
    f.close()


def read_fasta(filename):
    f = open(filename)
    lines = f.readlines()
    f.close()
    raw_result = ""
    for j in lines:
        if j[0] == ">":
            head = j[2:]
            continue
        line = j.strip("\n")
        raw_result += line
    return head, raw_result


def combine_fasta(filenames):
    raw_result = ""
    heads = []
    for i in filenames:
        head, seq = read_fasta(i)
        raw_result += seq
        heads.append(head)
    return heads, raw_result


head, result = combine_fasta(file_names)
export_seq("combined result", result)
