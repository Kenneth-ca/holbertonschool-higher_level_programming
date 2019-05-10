#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if value in a_dictionary.values():
        where = []
        for keys, val in a_dictionary.items():
            if val == value:
                where.append(keys)
        for w in where:
            a_dictionary.pop(w)
    return a_dictionary
