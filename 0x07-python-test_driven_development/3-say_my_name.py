#!/usr/bin/python3
"""
    Module to say a name
"""
import pdb

def say_my_name(first_name, last_name=""):
    """ A function that says a name"""
    pdb.set_trace()
    if first_name is None or type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if last_name is None or type(first_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
