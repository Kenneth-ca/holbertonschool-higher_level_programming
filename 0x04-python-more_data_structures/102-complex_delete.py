#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if (a_dictionary is not None) and (len(a_dictionary) is not 0):
        new = {}
        elem = a_dictionary.items()
        for keys, val in elem:
            if val == value:
                pass
            else:
                new[keys] = val
        return new
