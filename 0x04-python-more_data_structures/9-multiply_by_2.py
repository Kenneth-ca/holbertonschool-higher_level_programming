#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = {}
    elem = a_dictionary.items()
    for keys, val in elem:
        new[keys] = val * 2
    return new
