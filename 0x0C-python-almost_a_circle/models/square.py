#!/usr/bin/python3
"""Import rectangle to be inherited"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A square that inherits a rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Init for the Square"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Property for size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size"""
        self.width = value

    def __str__(self):
        """Str for square"""
        return ("[Square] ({}) {}/{} - {}".
                format(self.id, self.x, self.y, self.width))

    def update(self, *args, **kwargs):
        """A function that updates"""
        new_list = ["id", "size", "x", "y"]
        if args and args != "":
            for i in range(len(args)):
                setattr(self, new_list[i], args[i])
        else:
            for key, value in kwargs.items():
                for i in range(len(new_list)):
                    setattr(self, key, value)

    def to_dictionary(self):
        """Square instance to dictionary"""
        new_dict = {'id': self.id, 'x': self.x, 'size': self.width,
                    'y': self.y}
        return new_dict
