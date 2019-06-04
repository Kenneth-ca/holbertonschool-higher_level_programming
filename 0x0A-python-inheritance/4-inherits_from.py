#!/usr/bin/python3
def inherits_from(obj, a_class):
    if isinstance(obj, a_class) is True and type(obj) is a_class:
        return False
    else:
        return True
