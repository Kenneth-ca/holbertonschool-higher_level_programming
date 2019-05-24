#!/usr/bin/python3
"""
    Module to add two integers
"""


def add_integer(a, b=98):
    """ A function that adds two integers"""
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    if isinstance(a, int) is not True:
        raise TypeError("a must be an integer")
    if isinstance(b, int) is not True:
        raise TypeError("b must be an integer")
    if a is None:
        raise TypeError("a must be an integer")
    if b is None:
        raise TypeError("b must be an integer")
    return a + b
