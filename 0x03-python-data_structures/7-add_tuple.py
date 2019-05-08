#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    list1 = list(tuple_a)
    list2 = list(tuple_b)
    new = []
    modify(list1)
    modify(list2)
    new.append(list1[0] + list2[0])
    new.append(list1[1] + list2[1])
    return (tuple(new))


def modify(l):
    if len(l) == 0:
        l.append(0)
        l.append(0)
    elif len(l) == 1:
        l.append(0)
