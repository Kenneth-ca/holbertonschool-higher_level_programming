#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if len(argv) == 1:
        print("0")
    else:
        total = 0
        for a in range(1, len(argv)):
            total += int(argv[a])
        print("{:d}".format(total))
