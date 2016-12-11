# -*- coding:utf-8 -*-
"""
Bioinfo homework: RNA structure predictor
"""

from sys import argv

help_information = """Help on RNA_structure.py

NAME
    RNA_structure

SYNOPSIS
    python RNA_structure.py SEQUENCE >output

DESCRIPTION
    Predict RNA structure by calculating max hydrogen bonds and dynamic programming.
    Base pair:
        GC score = 3; AU score = 2; GU score = 2.
    Minimun internal loop: 3.

AUTHOR
    Hanying Pan @ Tsinghua University

SEE ALSO
    recursion, trace back and VW tables.pdf
"""

try:
    rna = argv[1].upper()
except IndexError:
    print help_information
    exit()


def main():
    length = len(rna)
    keylist = ['CG', 'GC', 'AU', 'UA', 'GU', 'UG']
    valuelist = [3, 3, 2, 2, 2, 2]
    pair = dict(zip(keylist, valuelist))
    v_table =  [[0 for i in range(length)] for j in range(length)]
    w_table =  [[0 for i in range(length)] for j in range(length)]
    vs_table = [[0 for i in range(length)] for j in range(length)]
    ws_table = [[0 for i in range(length)] for j in range(length)]

    def fill(i, j):
        bases = rna[i] + rna[j]
        hbs = pair.get(bases, 0)
        #  v i,j
        if hbs and j - i > 3:
            hsb = [0, 0, 0]
            list = [0, 0, 0]
            if j - i > 3:
                hsb[0] = hbs
            dict = {}
            for k1 in range(i + 1, j):
                for k2 in range(k1 + 1, j):
                    dict[k1 * 10000 + k2] = v_table[k1][k2] + hbs
            if dict:
                list[1], hsb[1] = max(dict.items(), key=lambda x: x[1])
            dict = {}
            for k in range(i + 2, j - 2):
                list.append(w_table[i + 1][k] + w_table[k + 1][j - 1])
                dict[k] = w_table[i + 1][k] + w_table[k + 1][j - 1]
            if dict:
                list[2], hsb[2] = max(dict.items(), key=lambda x: x[1])
            v_value = max(hsb)
            v_table[i][j] = v_value
            vs_table[i][j] = list[hsb.index(v_value)] * 10 + hsb.index(v_value) + 1
        # w i,j
        if j > i:
            w_list = [v_table[i][j], w_table[i + 1][j], w_table[i][j - 1], 0]
            dict = {}
            for k in range(i + 1, j - 1):
                dict[k] = w_table[i][k] + w_table[k + 1][j]
            if dict:
                kk, w_list[3] = max(dict.items(), key=lambda x: x[1])
            else:
                kk = 0
            w_value = max(w_list)
            w_table[i][j] = w_value
            ws_table[i][j] = kk * 10 + w_list.index(w_value) + 1

    def print_table(name):
        for i in range(len(rna)):
            for j in range(len(rna)):
                print name[i][j],
            print

    def traceback():
        stack = [(0, length - 1)]
        pair_list = list('.' * length)
        while stack:
            i, j = stack.pop()
            if ws_table[i][j] % 10 == 1:
                pair_list[i] = "("
                pair_list[j] = ")"
                if vs_table[i][j] % 10 == 1:
                    continue
                elif vs_table[i][j] % 10 == 2:
                    k1 = vs_table[i][j] / 100000
                    k2 = (vs_table[i][j] / 10) % 10000
                    stack.append((k1, k2))
                else:
                    k = vs_table[i][j] / 10
                    stack.append((i + 1, k))
                    stack.append((k + 1, j - 1))
            elif ws_table[i][j] % 10 == 2:
                stack.append((i + 1, j))
            elif ws_table[i][j] % 10 == 3:
                stack.append((i, j - 1))
            else:
                k = ws_table[i][j] / 10
                stack.append((i, k))
                stack.append((k + 1, j))
        return "".join(pair_list)

    for i in range(len(rna) - 1, -1, -1):
        for j in range(i, len(rna)):
            fill(i, j)
    print rna + "\n" + traceback()


if __name__ == "__main__":
    main()
