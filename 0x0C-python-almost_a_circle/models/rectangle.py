#!/usr/bin/python3
"""Import base"""
from models.base import Base


class Rectangle(Base):
    """Module for Rectangle"""

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

    @property
    def width(self):
        """Width and all"""
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
        """Height very high"""
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
        """X not just x"""
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
        """Y why"""
        return self.__y

    @y.setter
    def y(self, value):
        """Y setter"""
        if isinstance(value, int) is not True:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Area of the rectangle"""
        return self.__width * self. __height

    def display(self):
        """Display it all"""
        for j in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x + "#" * self.__width)

    def __str__(self):
        """Str is for string"""
        id = str(self.id)
        x = str(self.x)
        y = str(self.y)
        w = str(self.width)
        h = str(self.height)
        return "[Rectangle] (" + id + ") " + x + "/" + y + " - " + w + "/" + h

    def update(self, *args, **kwargs):
        """Update it please"""
        new_list = ["id", "width", "height", "x", "y"]
        if args and args != "":
            for i in range(len(args)):
                setattr(self, new_list[i], args[i])
        else:
            for key, value in kwargs.items():
                for i in range(len(new_list)):
                    setattr(self, key, value)
