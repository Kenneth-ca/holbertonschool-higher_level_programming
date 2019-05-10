#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if (a_dictionary is not None) and (len(a_dictionary) is not 0):
        where = []
        for keys, val in a_dictionary.items():
            if val == value:
                where.append(keys)
        for w in where:
            a_dictionary.pop(w)
        return a_dictionary
