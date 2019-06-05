#!/usr/bin/python3
def append_write(filename="", text=""):
    count = 0
    with open(filename, "a+") as f:
        count = f.write(text)
    return count
