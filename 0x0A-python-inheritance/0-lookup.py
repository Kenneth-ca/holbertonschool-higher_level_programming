#!/usr/bin/python3
def lookup(obj):
    """A function that returns the list of available attributes
    and methods of an object"""
    if obj is None:
        return None
    return dir(obj)
