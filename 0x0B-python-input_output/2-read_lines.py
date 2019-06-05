#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    counter = 0
    with open(filename, "r") as f:
        for line in f:
            if counter >= nb_lines and nb_lines > 0:
                break
            counter += 1
            print(line, end="")
