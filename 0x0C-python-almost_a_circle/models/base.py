#!/usr/bin/python3
"""Module base"""


class Base:
    """Base and everything"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Init for base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
