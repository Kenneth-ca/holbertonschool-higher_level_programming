#!/usr/bin/python3
def no_c(my_string):
    if my_string is not None:
        new = ""
        for m in range(len(my_string)):
            if my_string[m] == 'C':
                pass
            elif my_string[m] == 'c':
                pass
            else:
                new = new + my_string[m]
        return new
