#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        return (fct(*args))
    except Exception as store:
        print("Exception: {}".format(store), file=sys.stderr)
        return None
