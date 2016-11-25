# -*- coding:utf-8 -*-
from sys import argv   # todo: argv
file_names = ["test.embl"]
# if len(argv) < 2:
#     argv.pop(-1)
#     while argv:
#         file_names.append(argv.pop())
# else:
#     print "please give at least 1 embl file"
#     exit()


def export_seq(head="> ", seq="", filename="result.fasta"):
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


def get_fasta_head(head):  # todo: define header for each source
    return head["ID"]


def embl_to_fasta(filenames):
    for idx, f_name in enumerate(filenames):
        f = open(f_name)
        lines = f.readlines()
        f.close()
        head = {}
        result = ""
        for line in lines:
            label = line[0:2]
            line = line[5:].strip("\n")
            if label == "XX":
                continue
            elif label == "  ":
                result += "{0}{1}{2}{3}{4}{5}".format(line[0:10], line[11:21], line[22:32],
                                                      line[33:43], line[44:54], line[55:65])
            else:
                head[label] = line
        head = get_fasta_head(head)
        r_name = "result" + str(idx) + ".fasta"
        export_seq(head, result, r_name)

embl_to_fasta(file_names)


