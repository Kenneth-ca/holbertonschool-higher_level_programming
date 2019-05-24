#!/usr/bin/python3
"""
    Module to indent text
"""


def text_indentation(text):
    """ A function that indent text"""
    if isinstance(text, str) is not True or text is None:
        raise TypeError("text must be a string")
    flag = 0
    for t in text:
        if t == "." or t == "?" or t == ":":
            print("{}\n".format(t))
            flag = 1
            continue
        if flag == 0:
            print("{}".format(t), end="")
        flag = 0
