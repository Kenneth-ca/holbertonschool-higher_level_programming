def uniq_add(my_list=[]):
    uniq = set(my_list)
    result = 0
    for u in uniq:
        result = result + u
    return result
