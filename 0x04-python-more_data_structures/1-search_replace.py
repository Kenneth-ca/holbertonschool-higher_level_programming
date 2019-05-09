#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list is not None:
        new = []
        new = my_list.copy()
        idx = new.index(search)
        new.remove(search)
        new.insert(idx, replace)
        return new
