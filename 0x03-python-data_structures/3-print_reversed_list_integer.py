#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    rev = reversed(my_list)
    for m in rev:
        print("{:d}".format(m))
