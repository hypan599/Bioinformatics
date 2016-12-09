# -*- coding: utf-8 -*-

dna_complement_dict = {
    "a": "t",
    "g": "c",
    "r": "y",
    "k": "m",
    "b": "v",
    "d": "h",
    "c": "g",
    "t": "a",
    "y": "r",
    "m": "k",
    "v": "b",
    "h": "d",
    "u": "a",
}


def sequence_reverse_complement(seq, type):
    if type == "reverse":
        return seq[::-1]
    elif type == "complement":
        result = ""
        for i in seq:
            result += dna_complement_dict[i]
        return result
    elif type == "reverse_complement":
        result = ""
        for i in range(len(seq)-1, -1, -1):
            result += dna_complement_dict[seq[i]]
        return result

print sequence_reverse_complement("AAAATTTTAAAATTTT".lower(), "reverse_complement")
