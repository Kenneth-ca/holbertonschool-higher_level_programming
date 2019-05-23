#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        try:
            if isinstance(value, int) is False:
                raise TypeError
            if value < 0:
                raise ValueError
        except TypeError:
            print("size must be an integer", end="")
            raise Exception
        except ValueError:
            print("size must be >= 0", end="")
            raise Exception
        self.__size = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print()
            return
        for j in range(self.__position[1]):
            print()
        for i in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)

    def __str__(self):
        self.my_list = []
        if self.__size == 0:
            return ""
        for j in range(self.__position[1]):
            self.my_list.append("\n")
        for i in range(self.__size):
            self.my_list.append(" " * self.__position[0])
            self.my_list.append("#" * self.__size)
            if (i < self.__size - 1):
                self.my_list.append("\n")
        return "".join(self.my_list)

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif isinstance(value[0], int) is False:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif isinstance(value[1], int) is False:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
