#!/usr/bin/python3
from models.base import Base
"""Import base"""


class Rectangle(Base):
    """Module for Rectangle"""
    @property
    def width(self):
        """Width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Width setter"""
        if isinstance(value, int) is not True:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Height setter"""
        if isinstance(value, int) is not True:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """X"""
        return self.__x

    @x.setter
    def x(self, value):
        """X setter"""
        if isinstance(value, int) is not True:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Y setter"""
        if isinstance(value, int) is not True:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def __init__(self, width, height, x=0, y=0, id=None):
        """Init of the rectangle"""
        super().__init__(id)
        if isinstance(width, int) is not True:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if isinstance(height, int) is not True:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        if isinstance(x, int) is not True:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        if isinstance(y, int) is not True:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """Area of the rectangle"""
        return self.__width * self. __height

    def display(self):
        """Display"""
        for j in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x + "#" * self.__width)

    def __str__(self):
        """Str"""
        id = str(self.id)
        x = str(self.x)
        y = str(self.y)
        w = str(self.width)
        h = str(self.height)
        return "[Rectangle] (" + id + ") " + x + "/" + y + " - " + w + "/" + h

    def update(self, *args, **kwargs):
        """Update"""
        if args:
            for i in range(len(args)):
                if i == 0:
                    super().__init__(args[i])
                elif i == 1:
                    self.width = args[i]
                elif i == 2:
                    self.height = args[i]
                elif i == 3:
                    self.x = args[i]
                elif i == 4:
                    self.y = args[i]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value
