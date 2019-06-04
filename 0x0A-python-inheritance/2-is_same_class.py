#!/usr/bin/python3
def is_same_class(obj, a_class):
    if a_class == object:
        return False
    if isinstance(obj, a_class) is not True:
        return False
    else:
        return True
