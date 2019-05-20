#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if my_list is None:
        return 0
    cont = 0
    try:
        for ele in range(x):
            print("{}".format(my_list[ele]), end="")
            cont += 1
        print()
    except IndexError:
        print()
        pass
    return cont
