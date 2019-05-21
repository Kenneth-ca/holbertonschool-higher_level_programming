#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        try:
            if isinstance(size, int) is False:
                raise TypeError
            if size < 0:
                raise ValueError
        except TypeError:
            print("size must be an integer", end="")
            raise Exception
        except ValueError:
            print("size must be >= 0", end="")
            raise Exception
        self.__size = size

    def area(self):
        return self.__size * self.__size
