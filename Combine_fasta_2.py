# -*- coding:utf-8 -*-


# for tool 1: combine fasta:
# below are copied from internet, haven't understood yet todo: try to understand this
# from itertools import groupby
#
# if __name__ == '__main__':
#
# ishead = lambda x: x.startswith('>')
# all_seqs = set()
# with open(inname) as handle:
# with open(oname, 'w') as outhandle:
# head = None
# for h, lines in groupby(handle, ishead):
# if h:
# head = lines.next()
# else:
# seq = ''.join(lines)
# if seq not in all_seqs:
# all_seqs.add(seq)
# outhandle.write('%s\n%s\n' % (head, seq))


# file_names = ["test.embl"]
# embl_to_fasta(file_names)
