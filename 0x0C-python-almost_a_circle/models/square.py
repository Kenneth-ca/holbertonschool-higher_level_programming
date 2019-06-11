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
