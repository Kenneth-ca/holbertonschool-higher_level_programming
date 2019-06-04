#!/usr/bin/python3

class MyList(list):
    """A class MyList that inherits from list"""
    def __init__(self):
        self.lista = list()

    def print_sorted(self):
        """print sorted"""
        print(sorted(self))
