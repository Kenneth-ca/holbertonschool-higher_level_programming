#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    if my_list is None:
        return 0
    cont = 0
    for m in range(x):
        try:
            print("{:d}".format(my_list[m]), end="")
            cont += 1
        except (ValueError, TypeError):
            continue
    print()
    return cont
