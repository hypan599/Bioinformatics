# -*- coding:utf-8 -*-


def read_seq(filename):   # todo: deal with fasta file containing multi sequences
    f = open(filename)
    lines = f.readlines()
    f.close()
    raw_result = ""
    for j in lines:
        if j[0] == ">":
            continue
        line = j.strip("\n")
        raw_result += line
    return raw_result


def get_substitution(filename):
    f = open(filename)
    substitution = {}
    for line in f.readlines():
        bases, value = line.strip("\n").split(":")
        substitution[bases] = int(value)
    f.close()
    return substitution


def align(seq1, seq2, substitution, d):
    dpmatrix = [[[0, 0] for i in range(len(seq1)+1)] for j in range(len(seq2)+1)]
    for col in range(len(seq2)+1):
        for row in range(len(seq1)+1):
            if col == 0 and row == 0:
                continue
            if row == 0:
                dpmatrix[col][row][0] = dpmatrix[col-1][row][0] + d
                dpmatrix[col][row][1] = "U"
                continue
            if col == 0:
                dpmatrix[col][row][0] = dpmatrix[col][row-1][0] + d
                dpmatrix[col][row][1] = "L"
                continue
            left = dpmatrix[col][row-1][0] + d
            up = dpmatrix[col-1][row][0] + d
            bases = [seq2[col-1].upper(), seq1[row-1].upper()]
            base_str = "{0}-{1}".format(min(bases), max(bases))
            diagnose = dpmatrix[col-1][row-1][0] + substitution[base_str]
            maxvalue = max([left, up, diagnose])
            if maxvalue == left:
                source = "L"
            elif maxvalue == up:
                source = "U"
            else:
                source = "D"
            dpmatrix[col][row][0] = maxvalue
            dpmatrix[col][row][1] = source
    # print_map(dpmatrix, i, j)
    return align_result(dpmatrix, i, j)


def align_result(dpmatrix, i, j):
    result =["", "", ""]
    r_path = ""
    col = j
    row = i
    while True:
        if dpmatrix[col][row][1]:
            r_path += dpmatrix[col][row][1]
        else:
            break
        if r_path[-1] == "U":
            col -= 1
        elif r_path[-1] == "L":
            row -= 1
        else:
            col -= 1
            row -= 1
    path = r_path[::-1]
    m = 0
    n = 0
    for i in path:
        if i == "U":
            result[0] += "-"
            result[1] += " "
            result[2] += seq2[n]
            n += 1
        elif i == "L":
            result[0] += seq1[m]
            result[1] += " "
            result[2] += "-"
            m += 1
        else:
            result[0] += seq1[m]
            result[1] += "|"
            result[2] += seq2[n]
            m += 1
            n += 1
    return result


def print_align_result(result):
    line_len = 80
    i = 0
    result_str = ""
    while i <= len(result[1]):
        result_str += result[0][i:line_len + i] + "\n"
        result_str += result[1][i:line_len + i] + "\n"
        result_str += result[2][i:line_len + i] + "\n"
        i += line_len
    print result_str


def print_map(result, m, n):
    for i in range(m + 1):
        for j in range(n + 1):
            print result[i][j],
        print

substitution = get_substitution("Substitution_matrix")
# seq1 = "AAAATTTTGGGG"
# seq2 = "AAAACCCCTTTT"
try:
    ali_res = align(seq1, seq2, substitution, -5)
except NameError:
    seq1 = read_seq("sequence_small.fasta")
    seq2 = read_seq("sequence_small2.fasta")
    ali_res = align(seq1, seq2, substitution, -5)
    print_align_result(ali_res)